"""Self-check for personas/ece-phase-error (graph.json + routing-set.json).

Usage: py -3 -I validate_ece_graph.py <folder>
Exits 1 on any error. Warnings do not fail the run.
"""
import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

folder = Path(sys.argv[1])
errors, warnings = [], []


def err(msg):
    errors.append(msg)


def warn(msg):
    warnings.append(msg)


def no_dupes(pairs):
    keys = [k for k, _ in pairs]
    dupes = {k for k in keys if keys.count(k) > 1}
    if dupes:
        err(f"duplicate JSON keys: {sorted(dupes)}")
    return dict(pairs)


def load(name):
    try:
        return json.loads((folder / name).read_text(encoding="utf-8"), object_pairs_hook=no_dupes)
    except Exception as e:  # noqa: BLE001
        err(f"{name} does not parse: {e}")
        return None


g = load("graph.json")
rs = load("routing-set.json")
if g is None or rs is None:
    print("\n".join(errors))
    sys.exit(1)

LANGS = ("en", "or")
DIMS = {"concept", "words", "english", "lab"}
LEVELS = {"ok", "partial", "not_yet", "n/a"}
KINDS = {"probe", "show", "conclusion"}
ANN_KINDS = {"circle", "box", "arrow", "underline", "label"}
ID_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$|^[A-Z0-9]+(-[A-Z0-9]+)*$")
ODIA = re.compile(r"[଀-୿]")
EMOJI = re.compile("[\U0001F000-\U0001FAFF☀-➿️]")
# Odia-script spellings of course terms (ledger pronunciations): Odia lines must keep these in Latin script.
TRANSLITERATED_TERMS = ["ଫେଜ୍", "କ୍ୟାରିଅର୍", "ଫିଲ୍ଟର୍", "ଲୋପାସ୍", "ଫ୍ରିକ୍ୱେନ୍ସି", "ଆମ୍ପ୍ଲିଟ୍ୟୁଡ୍", "ମେସେଜ୍", "ଅସିଲେଟର୍", "ରିସିଭର୍", "ଗେନ୍"]
# Targets that exist in PhaseRecoveryScene (data-testid) or in the C-AM-08 walkthrough, plus one proposed id.
TARGETS_EXISTING = {"aligned-trace", "recovered-trace", "recovery-fraction",
                    "Carrier mismatch", "relative phase error", "frequency mismatch"}
TARGETS_PROPOSED = {"comparison-presets"}
TARGETS = TARGETS_EXISTING | TARGETS_PROPOSED


def check_ltext(lt, where, max_sentences=None):
    if not isinstance(lt, dict):
        err(f"{where}: not an LText object")
        return
    for lang in LANGS:
        s = lt.get(lang)
        if not isinstance(s, str) or not s.strip():
            err(f"{where}: missing '{lang}'")
            continue
        if EMOJI.search(s):
            err(f"{where}.{lang}: contains emoji")
        if re.search(r"\bwrong\b", s, re.I):
            err(f"{where}.{lang}: uses 'wrong' (copy rule: say 'not yet')")
        if max_sentences is not None:
            n = count_sentences(s)
            if n > max_sentences:
                err(f"{where}.{lang}: {n} sentences (max {max_sentences}): {s}")
    if isinstance(lt.get("or"), str):
        o = lt["or"]
        has_latin_letters = re.search(r"[A-Za-z]", o) is not None
        if not ODIA.search(o) and has_latin_letters and o != lt.get("en"):
            warn(f"{where}.or: no Odia script and differs from en: {o}")
        for t in TRANSLITERATED_TERMS:
            if t in o:
                err(f"{where}.or: technical term written in Odia script ({t}); keep it in English")


def count_sentences(s):
    # Remove quoted model sentences (counted as one unit) and decimals/abbreviations, then count terminators.
    s2 = re.sub(r"“[^”]*”", "Q", s)
    s2 = re.sub(r"\d\.\d", "0", s2)
    terms = re.findall(r"[.?!।](?=\s|$)", s2)
    return max(1, len(terms))


# ---- top level ----
if g.get("schema") != "kiki-tutor-graph/v0":
    err("schema must be kiki-tutor-graph/v0")
if g.get("id") != "ece-phase-error":
    err("id must be ece-phase-error")
if g.get("packId") != "ece-analog-modulation":
    err("packId must be ece-analog-modulation")
check_ltext(g.get("title"), "title", 1)
check_ltext(g.get("problem"), "problem", 2)

metrics = {m["id"]: m for m in g.get("metrics", [])}
if len(metrics) != len(g.get("metrics", [])):
    err("duplicate metric ids")
for m in g.get("metrics", []):
    if m.get("dim") not in DIMS:
        err(f"metric {m['id']}: bad dim")
    if not ID_RE.match(m["id"]):
        err(f"metric id not kebab: {m['id']}")
    check_ltext(m.get("label"), f"metric {m['id']}.label", 1)
want_metrics = {"conceptual-understanding": "concept", "calculation-accuracy": "concept", "terms": "words", "articulation": "english"}
for mid, dim in want_metrics.items():
    if metrics.get(mid, {}).get("dim") != dim:
        err(f"metric {mid} should exist with dim {dim}")

# ---- scenes ----
scenes = {s["id"]: s for s in g.get("scenes", [])}
if len(scenes) != len(g.get("scenes", [])):
    err("duplicate scene ids")
for sid, s in scenes.items():
    if s.get("template") != "ece":
        err(f"scene {sid}: template must be ece")
    p = s.get("params", {})
    if p.get("renderer") != "coherent-phase-recovery/v1" or p.get("conceptId") != "C-AM-08":
        err(f"scene {sid}: params must be coherent-phase-recovery/v1 + C-AM-08")
    for name, patch in s.get("states", {}).items():
        if not ID_RE.match(name):
            err(f"scene {sid} state name not kebab: {name}")
        vals = patch.get("values", {})
        if set(vals) != {"phi"}:
            err(f"scene {sid} state {name}: values must set exactly 'phi' (the real control name)")
        phi = vals.get("phi")
        if not isinstance(phi, (int, float)) or not (0 <= phi <= 180) or phi % 15:
            err(f"scene {sid} state {name}: phi {phi} off the 0-180 step-15 grid")
        for key in ("show", "hide", "highlight"):
            for t in patch.get(key, []):
                if t not in TARGETS:
                    err(f"scene {sid} state {name}.{key}: unknown target {t!r}")
        for k in patch:
            if k not in {"show", "hide", "highlight", "focus", "values"}:
                err(f"scene {sid} state {name}: field {k} is not in StatePatch")


def check_canvas(c, where):
    if c is None:
        return
    if c.get("sceneId") not in scenes:
        err(f"{where}: unknown sceneId {c.get('sceneId')}")
        return
    st = c.get("state")
    if st is not None and st not in scenes[c["sceneId"]].get("states", {}):
        err(f"{where}: unknown state {st}")
    ids = [a["id"] for a in c.get("annotate", [])]
    if len(set(ids)) != len(ids):
        err(f"{where}: duplicate annotation ids")
    for a in c.get("annotate", []):
        if a.get("kind") not in ANN_KINDS:
            err(f"{where}: annotation {a.get('id')} bad kind")
        if a.get("target") not in TARGETS:
            err(f"{where}: annotation {a.get('id')} unknown target {a.get('target')!r}")
        if a.get("dim") not in DIMS:
            err(f"{where}: annotation {a.get('id')} bad dim")
        if "text" in a:
            check_ltext(a["text"], f"{where}.annotate[{a.get('id')}].text", 1)
    for k in c:
        if k not in {"sceneId", "state", "annotate"}:
            err(f"{where}: canvas field {k} not in the contract")


# ---- nodes ----
nodes = g.get("nodes", {})
start = g.get("start")
if start not in nodes:
    err(f"start {start} is not a node")
if not (8 <= len(nodes) <= 12):
    err(f"{len(nodes)} nodes; contract wants 8-12")

edges = {}
labels_by_node = {}
misc_ids = set()
for nid, n in nodes.items():
    w = f"node {nid}"
    if not ID_RE.match(nid):
        err(f"{w}: id not kebab")
    k = n.get("kind")
    if k not in KINDS:
        err(f"{w}: bad kind {k}")
    if not isinstance(n.get("goal"), str) or not n["goal"].strip():
        err(f"{w}: missing goal")
    check_ltext(n.get("say"), f"{w}.say", 2)
    check_canvas(n.get("canvas"), f"{w}.canvas")
    out = []
    if k == "probe":
        exp, mis = n.get("expect") or [], n.get("misconceptions") or []
        if not exp:
            err(f"{w}: probe without expect")
        bids = [b["id"] for b in exp + mis]
        if len(set(bids)) != len(bids):
            err(f"{w}: duplicate branch ids")
        for b in exp + mis:
            if not ID_RE.match(b["id"]):
                err(f"{w}: branch id not kebab: {b['id']}")
            if b.get("metric") not in metrics:
                err(f"{w}: branch {b['id']} unknown metric {b.get('metric')}")
            if b.get("level", "ok") not in LEVELS:
                err(f"{w}: branch {b['id']} bad level")
            if not b.get("desc"):
                err(f"{w}: branch {b['id']} missing desc")
            out.append(b.get("next"))
        for b in mis:
            misc_ids.add(b["id"])
            if b.get("level") != "not_yet":
                warn(f"{w}: misconception {b['id']} level is {b.get('level')}")
        for b in exp:
            if b["id"] in {"unclear", "off_topic"}:
                err(f"{w}: branch id collides with a reserved label")
        labels_by_node[nid] = set(bids) | {"unclear", "off_topic"}
        hints = n.get("hints") or []
        if len(hints) != 4:
            err(f"{w}: {len(hints)} hint rungs; want 4 (question, nudge, worked step, answer)")
        for i, h in enumerate(hints):
            check_ltext(h.get("say"), f"{w}.hints[{i}].say", 2)
            check_canvas(h.get("canvas"), f"{w}.hints[{i}].canvas")
        chips = n.get("chips") or []
        if not (2 <= len(chips) <= 4):
            err(f"{w}: {len(chips)} chips; want 2-4")
        for i, c in enumerate(chips):
            check_ltext(c.get("label"), f"{w}.chips[{i}].label", 1)
            if not isinstance(c.get("text"), str) or not c["text"].strip():
                err(f"{w}.chips[{i}]: missing text")
            r = c.get("route")
            if r is not None and r not in labels_by_node[nid]:
                err(f"{w}.chips[{i}]: route {r} is not a label of this node")
        if n.get("next"):
            err(f"{w}: probe has next (transitions come from branches)")
    elif k == "show":
        if not n.get("canvas"):
            err(f"{w}: show node without canvas")
        out.append(n.get("next"))
        for f in ("expect", "misconceptions", "hints", "chips"):
            if n.get(f):
                err(f"{w}: show node has {f}")
    elif k == "conclusion":
        check_ltext(n.get("summary"), f"{w}.summary", 4)
        for f in ("expect", "misconceptions", "next"):
            if n.get(f):
                err(f"{w}: conclusion has {f}")
    for t in out:
        if t not in nodes:
            err(f"{w}: next {t!r} does not exist")
    edges[nid] = [t for t in out if t in nodes]

if not (2 <= len(misc_ids) <= 3):
    err(f"{len(misc_ids)} distinct misconceptions; contract wants 2-3")

# reachability
seen, stack = set(), [start]
while stack:
    x = stack.pop()
    if x in seen or x not in nodes:
        continue
    seen.add(x)
    stack.extend(edges.get(x, []))
for nid in nodes:
    if nid not in seen:
        err(f"node {nid} unreachable from start")

# acyclic + every sink is a conclusion => every path ends at a conclusion
color = {}
order = []


def dfs(u, trail):
    color[u] = 1
    for v in edges.get(u, []):
        if color.get(v) == 1:
            err(f"cycle: {' -> '.join(trail + [v])}")
        elif color.get(v) is None:
            dfs(v, trail + [v])
    color[u] = 2
    order.append(u)


dfs(start, [start])
for nid, n in nodes.items():
    if not edges.get(nid) and n.get("kind") != "conclusion":
        err(f"node {nid} is a dead end (not a conclusion)")

# enumerate paths and learner turns
paths = []


def walk(u, trail):
    if nodes[u]["kind"] == "conclusion":
        paths.append(trail)
        return
    for v in sorted(set(edges[u])):
        walk(v, trail + [v])


if not errors:
    walk(start, [start])

# each misconception reaches at least one show node with a canvas
for mid in sorted(misc_ids):
    targets = {b["next"] for n in nodes.values() for b in (n.get("misconceptions") or []) if b["id"] == mid}
    if not any(nodes[t]["kind"] == "show" and nodes[t].get("canvas") for t in targets):
        err(f"misconception {mid} never routes to a show node with a canvas")

# forced advance (after the 4th rung) follows the first expect: it must be the 'ok' one
for nid, n in nodes.items():
    if n.get("kind") == "probe" and n.get("expect"):
        if n["expect"][0].get("level", "ok") != "ok":
            warn(f"node {nid}: first expect is not level ok (forced advance would follow it)")

# ---- caseData ----
cd = g.get("caseData", {})
for key in ("setup", "question"):
    check_ltext(cd.get(key), f"caseData.{key}", 2)
for i, lt in enumerate(cd.get("given", [])):
    check_ltext(lt, f"caseData.given[{i}]", 1)

# ---- routing set ----
if not isinstance(rs, list) or len(rs) != 20:
    err(f"routing set must have 20 entries, has {len(rs) if isinstance(rs, list) else 'n/a'}")
label_hits, lang_hits, node_hits = {}, {}, {}
for i, r in enumerate(rs):
    if set(r) != {"node", "reply", "lang", "expected_label"}:
        err(f"routing[{i}]: fields {sorted(r)}")
    if r.get("node") not in labels_by_node:
        err(f"routing[{i}]: node {r.get('node')} is not a probe")
        continue
    if r.get("lang") not in {"en", "or", "mixed"}:
        err(f"routing[{i}]: bad lang {r.get('lang')}")
    if r.get("expected_label") not in labels_by_node[r["node"]]:
        err(f"routing[{i}]: {r.get('expected_label')} is not a label of {r['node']}")
    if EMOJI.search(r.get("reply", "")):
        err(f"routing[{i}]: emoji")
    label_hits[r["expected_label"]] = label_hits.get(r["expected_label"], 0) + 1
    lang_hits[r["lang"]] = lang_hits.get(r["lang"], 0) + 1
    node_hits[r["node"]] = node_hits.get(r["node"], 0) + 1
if len(node_hits) < 4:
    err("routing set covers fewer than 4 nodes")
for need in sorted(misc_ids | {"unclear", "off_topic"}):
    if need not in label_hits:
        err(f"routing set has no {need}")
expect_ids = {b["id"] for n in nodes.values() for b in (n.get("expect") or [])}
if not (expect_ids & set(label_hits)):
    err("routing set has no correct answers")
for lang in ("en", "or", "mixed"):
    if lang not in lang_hits:
        err(f"routing set has no lang={lang}")
odia_script = sum(1 for r in rs if ODIA.search(r["reply"]))
romanised = sum(1 for r in rs if r["lang"] in {"or", "mixed"} and not ODIA.search(r["reply"]))
if not odia_script or not romanised:
    err("routing set needs both Odia-script and romanised Odia replies")

# ---- report ----
print("graph:", g["id"], "|", len(nodes), "nodes |", len(misc_ids), "misconceptions:", ", ".join(sorted(misc_ids)))
print("node order:", " ".join(f"{k}({v['kind']})" for k, v in nodes.items()))
print("labels per probe:")
for nid, labs in labels_by_node.items():
    print(f"  {nid}: {', '.join(sorted(labs))}")
if paths:
    turns = [sum(1 for x in p if nodes[x]["kind"] == "probe") for p in paths]
    print(f"paths start->conclusion: {len(paths)}; learner turns per path: min {min(turns)}, max {max(turns)}")
    print("happy path:", " -> ".join(min(paths, key=len)))
print("routing set:", len(rs), "replies | nodes", node_hits, "| langs", lang_hits)
print("  labels", dict(sorted(label_hits.items())), "| Odia script", odia_script, "| romanised", romanised)
targets_used = set()
for n in nodes.values():
    for c in [n.get("canvas")] + [h.get("canvas") for h in n.get("hints") or []]:
        for a in (c or {}).get("annotate", []):
            targets_used.add(a["target"])
for s in scenes.values():
    for patch in s.get("states", {}).values():
        for key in ("show", "hide", "highlight"):
            targets_used.update(patch.get(key, []))
print("targets used:", sorted(targets_used), "| proposed (not in the scene yet):", sorted(targets_used & TARGETS_PROPOSED))
for w in warnings:
    print("WARN:", w)
if errors:
    print(f"\n{len(errors)} ERROR(S):")
    for e in errors:
        print("  -", e)
    sys.exit(1)
print("\nOK: all checks passed")
