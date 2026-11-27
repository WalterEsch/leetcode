"use strict";

const $ = (id) => document.getElementById(id);
const state = {
  problems: [],
  current: null,     // full problem payload
  hintsShown: 0,
  dirty: false,      // editor has changes not yet saved
  saveTimer: null,
  lastSaved: "",
};

// ---------------------------------------------------------------- helpers

async function api(path, options = {}) {
  const res = await fetch(path, {
    ...options,
    headers: { "Content-Type": "application/json", "X-Local-App": "1" },
  });
  if (!res.ok) throw new Error(`${res.status} ${res.statusText}`);
  return res.json();
}

function escapeHtml(s) {
  return s.replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
}

// Tiny Markdown subset: paragraphs, ``` code blocks, - lists, `code`, **bold**.
function inlineMd(text) {
  return escapeHtml(text)
    .replace(/`([^`]+)`/g, "<code>$1</code>")
    .replace(/\*\*([^*]+)\*\*/g, "<strong>$1</strong>");
}

function renderMarkdown(md) {
  const out = [];
  const blocks = md.replace(/\r\n/g, "\n").split(/\n{2,}/);
  for (const block of blocks) {
    if (block.startsWith("```")) {
      const code = block.replace(/^```\w*\n?/, "").replace(/\n?```$/, "");
      out.push(`<pre><code>${escapeHtml(code)}</code></pre>`);
    } else if (/^- /.test(block)) {
      const items = block.split(/\n(?=- )/).map((l) => `<li>${inlineMd(l.replace(/^- /, ""))}</li>`);
      out.push(`<ul>${items.join("")}</ul>`);
    } else {
      out.push(`<p>${inlineMd(block).replace(/\n/g, "<br>")}</p>`);
    }
  }
  return out.join("");
}

// Show values the way Python prints them (True, None, 'a') so they match your code.
function py(value) {
  if (value === null) return "None";
  if (value === true) return "True";
  if (value === false) return "False";
  if (typeof value === "string") return JSON.stringify(value);
  if (Array.isArray(value)) return "[" + value.map(py).join(", ") + "]";
  if (typeof value === "object") {
    if ("__repr__" in value) return value.__repr__;
    return "{" + Object.entries(value).map(([k, v]) => `${JSON.stringify(k)}: ${py(v)}`).join(", ") + "}";
  }
  return String(value);
}

// Like py(), but puts each row of a grid on its own line so boards and matrices are readable.
function pretty(value) {
  const flat = py(value);
  if (Array.isArray(value) && value.length > 1 && value.every(Array.isArray) && flat.length > 50) {
    return "[\n" + value.map((row) => "  " + py(row)).join(",\n") + "\n]";
  }
  return flat;
}

function formatInput(input) {
  return Object.entries(input).map(([k, v]) => `${k} = ${short(pretty(v))}`).join("\n");
}

function indent(text) {
  return text.split("\n").map((l) => "  " + l).join("\n");
}

// Very large test inputs would flood the screen, so cut them down for display.
function short(text, limit = 600) {
  return text.length <= limit ? text : `${text.slice(0, limit)} ... (${text.length - limit} more characters)`;
}

// ---------------------------------------------------------------- sidebar

function renderList() {
  const query = $("search").value.trim().toLowerCase();
  const nav = $("problem-list");
  nav.innerHTML = "";
  let lastCategory = null;
  for (const p of state.problems) {
    if (query && !p.title.toLowerCase().includes(query) && !p.category.toLowerCase().includes(query)) continue;
    if (p.category !== lastCategory) {
      const h = document.createElement("div");
      h.className = "category";
      h.textContent = p.category;
      nav.appendChild(h);
      lastCategory = p.category;
    }
    const a = document.createElement("a");
    a.className = "problem-link" + (state.current && state.current.id === p.id ? " active" : "");
    a.href = `#${p.id}`;
    a.innerHTML = `<span class="dot ${p.difficulty}" title="${p.difficulty}"></span><span class="name"></span>`;
    a.querySelector(".name").textContent = p.title;
    nav.appendChild(a);
  }
}

// ---------------------------------------------------------------- problem view

async function openProblem(id) {
  await flushSave();
  let problem;
  try {
    problem = await api(`/api/problems/${id}`);
  } catch {
    return;
  }
  state.current = problem;
  state.hintsShown = 0;
  try { localStorage.setItem("lastProblem", id); } catch {}

  $("empty").hidden = true;
  $("workspace").hidden = false;
  $("title").textContent = problem.title;
  $("difficulty").textContent = problem.difficulty;
  $("difficulty").className = `badge ${problem.difficulty}`;
  $("category").textContent = problem.category;
  $("description").innerHTML = renderMarkdown(problem.description);

  $("examples").innerHTML = problem.examples.map((t, i) => `
    <div class="example">
      <strong>Example ${i + 1}</strong>
      <pre>Input:\n${escapeHtml(indent(formatInput(t.input)))}\nOutput:\n${escapeHtml(indent(short(pretty(t.expected))))}</pre>
    </div>`).join("");

  renderHints();
  setEditor(problem.code);
  state.lastSaved = problem.code;
  state.dirty = false;
  $("save-status").textContent = `Saved to ${problem.solution_file}`;
  $("results").innerHTML = `<div class="muted">${problem.test_count} tests. Press Run tests (Ctrl+Enter) to check your solution.</div>`;
  $("left-pane").scrollTop = 0;
  renderList();
}

function renderHints() {
  const hints = state.current.hints || [];
  $("hint-list").innerHTML = hints.slice(0, state.hintsShown)
    .map((h) => `<li class="hint">${inlineMd(h)}</li>`).join("");
  const btn = $("hint-btn");
  if (state.hintsShown < hints.length) {
    btn.hidden = false;
    btn.textContent = state.hintsShown === 0 ? `Show a hint (${hints.length} available)` : `Show next hint (${state.hintsShown + 1} of ${hints.length})`;
  } else {
    btn.hidden = true;
  }
  $("hints").hidden = hints.length === 0;
}

// ---------------------------------------------------------------- editor

const editor = $("editor");
const INDENT = "    ";

function setEditor(code) {
  editor.value = code;
  updateGutter();
  editor.scrollTop = 0;
}

function updateGutter() {
  const lines = editor.value.split("\n").length;
  let nums = "";
  for (let i = 1; i <= lines; i++) nums += i + "\n";
  $("gutter").textContent = nums;
  $("gutter").scrollTop = editor.scrollTop;
}

function replaceSelection(text, selStart, selEnd) {
  // execCommand keeps the browser's undo history working.
  editor.focus();
  if (!document.execCommand("insertText", false, text)) {
    editor.setRangeText(text, editor.selectionStart, editor.selectionEnd, "end");
  }
  if (selStart !== undefined) editor.setSelectionRange(selStart, selEnd);
  onEdit();
}

editor.addEventListener("keydown", (e) => {
  const { selectionStart: start, selectionEnd: end, value } = editor;

  if (e.key === "Enter" && (e.ctrlKey || e.metaKey)) {
    e.preventDefault();
    runTests();
    return;
  }
  if (e.key === "s" && (e.ctrlKey || e.metaKey)) {
    e.preventDefault();
    flushSave();
    return;
  }

  if (e.key === "Tab") {
    e.preventDefault();
    const lineStart = value.lastIndexOf("\n", start - 1) + 1;
    if (start === end && !e.shiftKey) {
      replaceSelection(INDENT);
      return;
    }
    // Indent or dedent every selected line.
    const block = value.slice(lineStart, end);
    const lines = block.split("\n");
    const changed = lines.map((l) => e.shiftKey ? l.replace(/^ {1,4}/, "") : INDENT + l).join("\n");
    editor.setSelectionRange(lineStart, end);
    replaceSelection(changed, lineStart, lineStart + changed.length);
    return;
  }

  if (e.key === "Enter" && !e.shiftKey && !e.altKey) {
    e.preventDefault();
    const lineStart = value.lastIndexOf("\n", start - 1) + 1;
    const line = value.slice(lineStart, start);
    let indent = line.match(/^\s*/)[0];
    if (/:\s*(#.*)?$/.test(line)) indent += INDENT;
    replaceSelection("\n" + indent);
    return;
  }

  if (e.key === "Backspace" && start === end) {
    const lineStart = value.lastIndexOf("\n", start - 1) + 1;
    const before = value.slice(lineStart, start);
    if (before.length > 0 && /^ +$/.test(before)) {
      e.preventDefault();
      const remove = before.length % 4 || 4;
      editor.setSelectionRange(start - remove, start);
      replaceSelection("");
    }
  }
});

editor.addEventListener("input", onEdit);
editor.addEventListener("scroll", () => { $("gutter").scrollTop = editor.scrollTop; });

function onEdit() {
  updateGutter();
  state.dirty = true;
  $("save-status").textContent = "Unsaved changes";
  clearTimeout(state.saveTimer);
  state.saveTimer = setTimeout(flushSave, 800);
}

async function flushSave() {
  clearTimeout(state.saveTimer);
  if (!state.current || !state.dirty) return;
  const code = editor.value;
  try {
    await api(`/api/problems/${state.current.id}/save`, { method: "POST", body: JSON.stringify({ code }) });
    state.lastSaved = code;
    state.dirty = editor.value !== code;
    if (!state.dirty) $("save-status").textContent = `Saved to ${state.current.solution_file}`;
    markStarted();
  } catch {
    $("save-status").textContent = "Could not save. Is the app still running?";
  }
}

function markStarted() {
  const p = state.problems.find((x) => x.id === state.current.id);
  if (p) p.started = true;
}

// If you edited the file in VS Code, pick up those changes when you come back.
window.addEventListener("focus", async () => {
  if (!state.current || state.dirty) return;
  try {
    const fresh = await api(`/api/problems/${state.current.id}`);
    if (!state.dirty && fresh.code !== state.lastSaved) {
      const pos = editor.selectionStart;
      setEditor(fresh.code);
      editor.setSelectionRange(pos, pos);
      state.lastSaved = fresh.code;
      $("save-status").textContent = "Reloaded changes from file";
    }
  } catch {}
});

window.addEventListener("beforeunload", () => {
  if (state.dirty && state.current) {
    fetch(`/api/problems/${state.current.id}/save`, {
      method: "POST",
      keepalive: true,
      headers: { "Content-Type": "application/json", "X-Local-App": "1" },
      body: JSON.stringify({ code: editor.value }),
    });
  }
});

// ---------------------------------------------------------------- running tests

async function runTests() {
  if (!state.current) return;
  const btn = $("run-btn");
  btn.disabled = true;
  btn.textContent = "Running...";
  $("results").innerHTML = `<div class="muted">Running tests...</div>`;
  clearTimeout(state.saveTimer);
  const code = editor.value;
  try {
    const report = await api(`/api/problems/${state.current.id}/run`, { method: "POST", body: JSON.stringify({ code }) });
    state.lastSaved = code;
    state.dirty = editor.value !== code;
    if (!state.dirty) $("save-status").textContent = `Saved to ${state.current.solution_file}`;
    markStarted();
    renderResults(report);
  } catch {
    $("results").innerHTML = `<pre class="error-box">Could not reach the app. Is the start.bat window still open?</pre>`;
  } finally {
    btn.disabled = false;
    btn.textContent = "Run tests";
  }
}

function renderResults(report) {
  const box = $("results");
  if (!report.ok) {
    box.innerHTML = `<div class="summary fail">Error</div><pre class="error-box">${escapeHtml(report.error)}</pre>`;
    return;
  }
  const allPassed = report.passed === report.total;
  const parts = [`<div class="summary ${allPassed ? "pass" : "fail"}">${allPassed ? "All tests passed" : "Some tests failed"}: ${report.passed} / ${report.total}</div>`];
  let openedFirstFailure = false;
  for (const r of report.results) {
    const open = !r.passed && !openedFirstFailure;
    if (open) openedFirstFailure = true;
    const rows = [
      `<div class="label">Input</div><pre>${escapeHtml(formatInput(r.input))}</pre>`,
      `<div class="label">Expected</div><pre>${escapeHtml(short(pretty(r.expected)))}</pre>`,
    ];
    if (r.error) rows.push(`<div class="label">Error</div><pre class="error-box">${escapeHtml(r.error)}</pre>`);
    else rows.push(`<div class="label">Your output</div><pre>${escapeHtml(short(pretty(r.actual)))}</pre>`);
    if (r.stdout) rows.push(`<div class="label">Printed</div><pre>${escapeHtml(r.stdout)}</pre>`);
    parts.push(`
      <details class="test"${open ? " open" : ""}>
        <summary><span class="mark ${r.passed ? "pass" : "fail"}">${r.passed ? "✓" : "✗"}</span>
          Test ${r.index + 1}<span class="spacer"></span><span class="muted">${r.ms} ms</span></summary>
        <div class="body">${rows.join("")}</div>
      </details>`);
  }
  box.innerHTML = parts.join("");
}

// ---------------------------------------------------------------- wiring

$("run-btn").addEventListener("click", runTests);
$("reset-btn").addEventListener("click", async () => {
  if (!state.current) return;
  if (!window.confirm("Replace your code with the starter code? This cannot be undone.")) return;
  const { code } = await api(`/api/problems/${state.current.id}/reset`, { method: "POST", body: "{}" });
  clearTimeout(state.saveTimer);
  setEditor(code);
  state.lastSaved = code;
  state.dirty = false;
  $("save-status").textContent = "Reset to starter code";
});
$("hint-btn").addEventListener("click", () => { state.hintsShown++; renderHints(); });
$("search").addEventListener("input", renderList);
window.addEventListener("hashchange", () => {
  const id = location.hash.slice(1);
  if (id && (!state.current || state.current.id !== id)) openProblem(id);
});

(async function init() {
  state.problems = await api("/api/problems");
  renderList();
  let start = location.hash.slice(1);
  if (!start) { try { start = localStorage.getItem("lastProblem") || ""; } catch {} }
  if (start && state.problems.some((p) => p.id === start)) {
    if (location.hash.slice(1) !== start) history.replaceState(null, "", `#${start}`);
    openProblem(start);
  }
})();
