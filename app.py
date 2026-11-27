"""Local NeetCode 150 practice app.

Run with:  python app.py   (or double-click start.bat on Windows)

Starts a small web server on your own machine (no internet needed) and opens
the app in your browser. Uses only the Python standard library.
"""

import json
import re
import subprocess
import sys
import threading
import webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PROBLEMS_DIR = ROOT / "problems"
SOLUTIONS_DIR = ROOT / "solutions"
STATIC_DIR = ROOT / "static"
RUNNER = ROOT / "runner.py"

HOST = "127.0.0.1"
DEFAULT_PORT = 8150
RUN_TIMEOUT_SECONDS = 10
MAX_BODY_BYTES = 1_000_000

ID_PATTERN = re.compile(r"^[a-z0-9-]+$")
STATIC_FILES = {
    "/": ("index.html", "text/html; charset=utf-8"),
    "/app.js": ("app.js", "text/javascript; charset=utf-8"),
    "/style.css": ("style.css", "text/css; charset=utf-8"),
}


def load_problem(problem_id):
    if not ID_PATTERN.match(problem_id):
        return None
    path = PROBLEMS_DIR / f"{problem_id}.json"
    if not path.is_file():
        return None
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def list_problems():
    problems = []
    for path in PROBLEMS_DIR.glob("*.json"):
        with open(path, encoding="utf-8") as f:
            p = json.load(f)
        problems.append({
            "id": p["id"],
            "order": p["order"],
            "title": p["title"],
            "category": p["category"],
            "difficulty": p["difficulty"],
            "started": (SOLUTIONS_DIR / f"{p['id']}.py").is_file(),
        })
    problems.sort(key=lambda p: p["order"])
    return problems


def solution_path(problem_id):
    return SOLUTIONS_DIR / f"{problem_id}.py"


def read_solution(problem):
    path = solution_path(problem["id"])
    if path.is_file():
        return path.read_text(encoding="utf-8")
    return problem["starter"]


def save_solution(problem_id, code):
    SOLUTIONS_DIR.mkdir(exist_ok=True)
    # newline="\n" keeps line endings consistent on Windows.
    with open(solution_path(problem_id), "w", encoding="utf-8", newline="\n") as f:
        f.write(code)


def run_tests(problem_id):
    try:
        proc = subprocess.run(
            [sys.executable, str(RUNNER), str(PROBLEMS_DIR / f"{problem_id}.json"), str(solution_path(problem_id))],
            capture_output=True,
            text=True,
            encoding="utf-8",
            timeout=RUN_TIMEOUT_SECONDS,
            cwd=str(ROOT),
        )
    except subprocess.TimeoutExpired:
        return {"ok": False, "error": f"Time limit exceeded: your code ran longer than {RUN_TIMEOUT_SECONDS} seconds. "
                                      "Check for an infinite loop."}
    try:
        return json.loads(proc.stdout)
    except json.JSONDecodeError:
        detail = (proc.stderr or proc.stdout).strip()[-3000:]
        return {"ok": False, "error": "The test runner crashed.\n" + detail}


class Handler(BaseHTTPRequestHandler):
    server_version = "LocalLeetCode/1.0"

    def log_message(self, fmt, *args):  # keep the console quiet
        pass

    # -- safety checks -----------------------------------------------------
    # The server runs code, so only accept requests from this app's own page.
    def _host_ok(self):
        host = self.headers.get("Host", "")
        port = self.server.server_address[1]
        return host in (f"127.0.0.1:{port}", f"localhost:{port}")

    def _api_ok(self):
        return self._host_ok() and self.headers.get("X-Local-App") == "1"

    # -- responses -----------------------------------------------------------
    def _send(self, status, body, content_type):
        data = body if isinstance(body, bytes) else body.encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(data)

    def _json(self, status, obj):
        self._send(status, json.dumps(obj), "application/json; charset=utf-8")

    def _read_json(self):
        length = int(self.headers.get("Content-Length") or 0)
        if length > MAX_BODY_BYTES:
            return None
        try:
            return json.loads(self.rfile.read(length) or b"{}")
        except json.JSONDecodeError:
            return None

    # -- routes --------------------------------------------------------------
    def do_GET(self):
        if not self._host_ok():
            return self._send(403, "Forbidden", "text/plain")
        path = self.path.split("?", 1)[0]

        if path in STATIC_FILES:
            name, ctype = STATIC_FILES[path]
            return self._send(200, (STATIC_DIR / name).read_bytes(), ctype)

        if not self._api_ok():
            return self._send(404, "Not found", "text/plain")

        if path == "/api/problems":
            return self._json(200, list_problems())

        m = re.fullmatch(r"/api/problems/([a-z0-9-]+)", path)
        if m:
            problem = load_problem(m.group(1))
            if problem is None:
                return self._json(404, {"error": "No such problem"})
            payload = {k: v for k, v in problem.items() if k != "tests"}
            payload["code"] = read_solution(problem)
            payload["examples"] = [t for t in problem["tests"] if t.get("example")]
            payload["test_count"] = len(problem["tests"])
            payload["solution_file"] = str(solution_path(problem["id"]).relative_to(ROOT))
            return self._json(200, payload)

        self._send(404, "Not found", "text/plain")

    def do_POST(self):
        if not self._api_ok():
            return self._send(403, "Forbidden", "text/plain")
        m = re.fullmatch(r"/api/problems/([a-z0-9-]+)/(save|run|reset)", self.path)
        if not m:
            return self._send(404, "Not found", "text/plain")
        problem = load_problem(m.group(1))
        if problem is None:
            return self._json(404, {"error": "No such problem"})
        action = m.group(2)

        if action == "reset":
            path = solution_path(problem["id"])
            if path.is_file():
                path.unlink()
            return self._json(200, {"code": problem["starter"]})

        body = self._read_json()
        if body is None or not isinstance(body.get("code"), str):
            return self._json(400, {"error": "Bad request"})
        save_solution(problem["id"], body["code"])
        if action == "save":
            return self._json(200, {"saved": True})
        return self._json(200, run_tests(problem["id"]))


def make_server():
    for port in range(DEFAULT_PORT, DEFAULT_PORT + 20):
        try:
            return ThreadingHTTPServer((HOST, port), Handler)
        except OSError:
            continue
    raise SystemExit("Could not find a free port to run on.")


def main():
    server = make_server()
    url = f"http://127.0.0.1:{server.server_address[1]}/"
    print(f"NeetCode practice app running at {url}")
    print("Your solutions are saved in the 'solutions' folder.")
    print("Keep this window open while you practice. Press Ctrl+C to stop.")
    if "--no-browser" not in sys.argv:
        threading.Timer(0.5, lambda: webbrowser.open(url)).start()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped.")


if __name__ == "__main__":
    main()
