"""Checks every problem file: required fields, starter code loads, and the
reference solution in dev/reference/ (if present) passes every test.

Usage: python dev/check_problems.py
"""
import json, pathlib, subprocess, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
REQUIRED = ["id", "order", "title", "category", "difficulty", "description",
            "starter", "tests", "hints"]

def run(problem_path, solution_path):
    out = subprocess.run([sys.executable, str(ROOT / "runner.py"), str(problem_path), str(solution_path)],
                         capture_output=True, text=True, encoding="utf-8", timeout=60)
    return json.loads(out.stdout)

failures = 0
for path in sorted((ROOT / "problems").glob("*.json")):
    p = json.loads(path.read_text(encoding="utf-8"))
    problems = [f for f in REQUIRED if f not in p]
    if p.get("kind") == "design":
        problems += [f for f in ("class",) if f not in p]
    else:
        problems += [f for f in ("function", "params") if f not in p]
    if p.get("id") != path.stem:
        problems.append("id does not match file name")
    for t in p.get("tests", []):
        if p.get("kind") != "design" and not p.get("harness") and set(t["input"]) != set(p["params"]):
            problems.append(f"test input keys {sorted(t['input'])} != params")
    starter = ROOT / "dev" / ".starter_tmp.py"
    starter.write_text(p["starter"], encoding="utf-8")
    r = run(path, starter)
    if not r.get("ok"):
        problems.append("starter code does not load: " + r.get("error", ""))
    ref = ROOT / "dev" / "reference" / f"{path.stem}.py"
    if ref.is_file():
        r = run(path, ref)
        if not r.get("ok") or r["passed"] != r["total"]:
            problems.append(f"reference failed: {json.dumps(r)[:500]}")
        status = f"reference {r.get('passed')}/{r.get('total')}"
    else:
        status = "no reference"
    starter.unlink()
    if problems:
        failures += 1
        print(f"FAIL {path.stem}: " + "; ".join(problems))
    else:
        print(f"ok   {path.stem} ({status})")
sys.exit(1 if failures else 0)
