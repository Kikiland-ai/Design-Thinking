#!/usr/bin/env python3
"""Merge computed scenes into the hand-written tutor graphs, validate, and write tutor-flow.json.

Run: py -3 -I tutor_build.py
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = (r"C:\Users\Arpan Vihan\Downloads\Google AI Builder\Design-Thinking"
        r"\docs\knowledge-workers\personas")

DIMS = {"concept", "words", "english", "lab"}
LEVELS = {"ok", "partial", "not_yet", "n/a"}
KINDS = {"circle", "box", "arrow", "underline", "label"}

PERSONAS = {
    "trader": {
        "draft": "trader_graph_draft.json", "scenes": "trader_scenes.json", "learner": "hi",
        "shots": {1: ("TR-01", False, "Thesis appears on the intro case card; the map starts with n1 lit."),
                  2: ("TR-04", True, None), 3: ("TR-04", True, None), 4: ("TR-05", True, None),
                  5: ("TR-06", True, None), 6: ("TR-06", True, None), 7: ("TR-06", True, None),
                  8: ("TR-07", True, None), 9: ("TR-07", True, None)},
        "mustQuote": ["90.25", "59.55", "9,210", "₹40", "₹48", "₹23", "304", "+110", "27,075", "10,000",
                      "7,785", "442.50", "17.5%", "11%", "2.7"],
    },
    "streamer": {
        "draft": "streamer_graph_draft.json", "scenes": "streamer_scenes.json", "learner": "hi-Latn",
        "shots": {1: ("ST-05", True, None), 2: ("ST-06", True, None), 3: ("ST-07", True, None),
                  4: ("ST-07", True, None), 5: ("ST-08", True, None), 6: ("ST-09", True, None),
                  7: ("ST-09", True, None)},
        "mustQuote": None,  # filled from streamer numbers below
    },
}

errors = []


def err(p, msg):
    errors.append(f"[{p}] {msg}")


def ltext_ok(p, where, lt, learner):
    if not isinstance(lt, dict) or "en" not in lt or learner not in lt or not lt["en"] or not lt[learner]:
        err(p, f"LText at {where} must have non-empty 'en' and '{learner}'")


def scene_ids(scene):
    pr = scene["params"]
    t = scene["template"]
    if t == "candles":
        return {e["id"] for e in pr.get("events", [])} | {l["id"] for l in pr.get("levels", [])}
    if t == "payoff":
        return {l["id"] for l in pr["legs"]}
    if t == "line":
        return ({s["id"] for s in pr["series"]} | {b["id"] for b in pr.get("bands", [])}
                | {m["id"] for m in pr.get("markers", [])})
    return set()


def build(p, cfg):
    with open(os.path.join(HERE, cfg["draft"]), encoding="utf-8") as f:
        g = json.load(f)
    with open(os.path.join(HERE, cfg["scenes"]), encoding="utf-8") as f:
        sc = json.load(f)
    learner = cfg["learner"]

    # ---- scenes
    scenes = []
    for sid, spec in g.pop("sceneStates").items():
        scenes.append({"id": sid, "template": spec["template"], "params": sc[spec["from"]], "states": spec["states"]})
    S = {s["id"]: s for s in scenes}
    for s in scenes:
        ids = scene_ids(s)
        for st_name, st in s["states"].items():
            for key in ("show", "hide", "highlight"):
                for i in st.get(key, []):
                    if i not in ids:
                        err(p, f"scene {s['id']} state {st_name}: unknown id '{i}' in {key}")
        for lv in s["params"].get("levels", []) + s["params"].get("events", []):
            ltext_ok(p, f"scene {s['id']} {lv['id']}.label", lv["label"], learner)

    # ---- graph basics
    if g.get("schema") != "kiki-tutor-graph/v0":
        err(p, "schema must be kiki-tutor-graph/v0")
    for k in ("title", "problem"):
        ltext_ok(p, k, g[k], learner)
    metrics = {m["id"]: m for m in g["metrics"]}
    for m in g["metrics"]:
        ltext_ok(p, f"metric {m['id']}", m["label"], learner)
        if m["dim"] not in DIMS:
            err(p, f"metric {m['id']} bad dim")
    nodes = g["nodes"]
    if g["start"] not in nodes:
        err(p, "start node missing")
    n_nodes = len(nodes)
    n_misc = sum(len(n.get("misconceptions", [])) for n in nodes.values())
    if not 6 <= n_nodes <= 8:
        err(p, f"brief asks for 6-8 nodes, found {n_nodes}")
    if not 1 <= n_misc <= 2:
        err(p, f"brief asks for 1-2 misconceptions, found {n_misc}")

    def check_canvas(where, cv):
        if cv is None:
            return
        if cv["sceneId"] not in S:
            err(p, f"{where}: unknown scene {cv['sceneId']}")
            return
        sc_ = S[cv["sceneId"]]
        if cv.get("state") and cv["state"] not in sc_["states"]:
            err(p, f"{where}: unknown state {cv['state']} for {cv['sceneId']}")
        ids = scene_ids(sc_)
        for a in cv.get("annotate", []):
            if a["kind"] not in KINDS:
                err(p, f"{where}: bad annotation kind {a['kind']}")
            if a.get("dim") and a["dim"] not in DIMS:
                err(p, f"{where}: bad annotation dim")
            if a.get("target") and a["target"] not in ids:
                err(p, f"{where}: unknown annotation target {a['target']}")
            if not a.get("target") and not a.get("at"):
                err(p, f"{where}: annotation {a['id']} needs target or at")
            if a.get("text"):
                ltext_ok(p, f"{where} annotation {a['id']}", a["text"], learner)

    edges = {}
    for nid, n in nodes.items():
        ltext_ok(p, f"{nid}.say", n["say"], learner)
        check_canvas(nid, n.get("canvas"))
        out = []
        for b in n.get("expect", []) + n.get("misconceptions", []):
            if b["next"] not in nodes:
                err(p, f"{nid}: branch {b['id']} -> missing node {b['next']}")
            if b["metric"] not in metrics:
                err(p, f"{nid}: branch {b['id']} unknown metric {b['metric']}")
            if b.get("level") and b["level"] not in LEVELS:
                err(p, f"{nid}: branch {b['id']} bad level")
            out.append(b["next"])
        if n["kind"] == "show":
            if n.get("expect") or n.get("misconceptions") or not n.get("next"):
                err(p, f"{nid}: show nodes need next and no branches")
            out.append(n["next"])
        elif n["kind"] == "probe":
            if not n.get("expect"):
                err(p, f"{nid}: probe needs expect branches")
            if len(n.get("hints", [])) > 4:
                err(p, f"{nid}: at most 4 hint rungs")
        elif n["kind"] == "conclusion":
            ltext_ok(p, f"{nid}.summary", n.get("summary"), learner)
            if out:
                err(p, f"{nid}: conclusion must not have outgoing edges")
        for i, h in enumerate(n.get("hints", [])):
            ltext_ok(p, f"{nid}.hints[{i}]", h["say"], learner)
            check_canvas(f"{nid}.hints[{i}]", h.get("canvas"))
        for i, c in enumerate(n.get("chips", [])):
            ltext_ok(p, f"{nid}.chips[{i}]", c["label"], learner)
        edges[nid] = sorted(set(out))

    # reachability, acyclic, every path ends at a conclusion
    seen, stack = set(), [g["start"]]
    while stack:
        x = stack.pop()
        if x in seen:
            continue
        seen.add(x)
        stack.extend(edges.get(x, []))
    if seen != set(nodes):
        err(p, f"unreachable nodes: {sorted(set(nodes) - seen)}")
    color = {}

    def dfs(x):
        color[x] = 1
        for y in edges[x]:
            if color.get(y) == 1:
                err(p, f"cycle via {x}->{y}")
            elif color.get(y) is None:
                dfs(y)
        color[x] = 2

    dfs(g["start"])
    for nid in nodes:
        if nodes[nid]["kind"] != "conclusion" and not edges[nid]:
            err(p, f"dead end at {nid}")
    paths = []

    def walk(x, path):
        if nodes[x]["kind"] == "conclusion":
            paths.append(path + [x])
            return
        for y in edges[x]:
            walk(y, path + [x])

    walk(g["start"], [])

    # ---- scripted path
    sp = g["scriptedPath"]
    for i, t in enumerate(sp):
        nid = t["node"]
        n = nodes.get(nid)
        if n is None:
            err(p, f"turn {t['turn']}: unknown node {nid}")
            continue
        shot = cfg["shots"].get(t["turn"])
        if shot:
            t["video"] = {"show": shot[1], "shot": shot[0]}
            if shot[2]:
                t["video"]["note"] = shot[2]
        if t.get("kiki") is not None:
            ltext_ok(p, f"turn {t['turn']}.kiki", t["kiki"], learner)
            if t["hintLevel"] == 0 and t["kiki"] != n["say"]:
                err(p, f"turn {t['turn']}: kiki line differs from node say")
        if t.get("kikiAfter"):
            if t["kikiAfter"] != n["hints"][t.get("hintUsed", 1) - 1]["say"]:
                err(p, f"turn {t['turn']}: kikiAfter differs from hint rung")
        lbl = (t.get("route") or {}).get("label")
        branches = {b["id"]: b for b in n.get("expect", []) + n.get("misconceptions", [])}
        if n["kind"] == "show":
            if t.get("user") is not None or t.get("next") != n["next"]:
                err(p, f"turn {t['turn']}: show turn must have no user input and follow node.next")
        elif n["kind"] == "conclusion":
            if not t.get("done") or i != len(sp) - 1:
                err(p, f"turn {t['turn']}: conclusion must be the last turn and done")
        elif lbl == "unclear":
            if t.get("next") != nid or not t.get("hintUsed"):
                err(p, f"turn {t['turn']}: unclear must stay on the node with a hint")
        elif lbl in branches:
            if t.get("next") != branches[lbl]["next"]:
                err(p, f"turn {t['turn']}: next {t.get('next')} != branch next {branches[lbl]['next']}")
            mc = t["route"].get("misconception")
            if (lbl.startswith("m-")) != (mc == lbl):
                err(p, f"turn {t['turn']}: misconception field inconsistent")
        else:
            err(p, f"turn {t['turn']}: route label {lbl} not valid at {nid}")
        if i + 1 < len(sp) and sp[i + 1]["node"] != t.get("next"):
            err(p, f"turn {t['turn']}: next {t.get('next')} but following turn is at {sp[i + 1]['node']}")
        for e in t.get("evidence", []):
            if e["dim"] not in DIMS or e["level"] not in LEVELS:
                err(p, f"turn {t['turn']}: bad evidence dim/level")
            if e.get("metric"):
                if e["metric"] not in metrics:
                    err(p, f"turn {t['turn']}: unknown metric {e['metric']}")
                elif metrics[e["metric"]]["dim"] != e["dim"]:
                    err(p, f"turn {t['turn']}: evidence dim != metric dim")
    for m in g["scriptedScorecard"]["metrics"]:
        if m["id"] not in metrics or m["level"] not in LEVELS:
            err(p, f"scorecard metric {m['id']} invalid")
    if {m["id"] for m in g["scriptedScorecard"]["metrics"]} != set(metrics):
        err(p, "scorecard must cover every metric")

    # ---- the text quotes the scenario's numbers
    blob = json.dumps({k: g[k] for k in ("problem", "caseData", "nodes", "scriptedPath")}, ensure_ascii=False)
    for s in cfg["mustQuote"]:
        if s not in blob:
            err(p, f"expected scenario number '{s}' not quoted anywhere in the graph text")

    out = {
        "schema": g["schema"], "id": g["id"], "packId": g["packId"], "title": g["title"], "problem": g["problem"],
        "caseData": g["caseData"], "metrics": g["metrics"], "scenes": scenes, "start": g["start"],
        "nodes": g["nodes"], "scriptedPath": g["scriptedPath"], "scriptedScorecard": g["scriptedScorecard"],
        "videoScorecard": g["videoScorecard"], "meta": g["meta"],
    }
    out["meta"]["validation"] = {
        "nodes": n_nodes, "misconceptions": n_misc, "reachable": len(seen) == n_nodes,
        "pathsToConclusion": len(paths), "acyclic": not any("cycle" in e for e in errors),
        "scriptedTurns": len(sp), "scriptedTurnsInVideo": sum(1 for t in sp if t.get("video", {}).get("show")),
        "checkedBy": os.path.join(HERE, "tutor_build.py"),
        "note": "Local structural check only. S3's validator is the acceptance gate.",
    }
    print(f"{p}: {n_nodes} nodes, {n_misc} misconceptions, {len(paths)} paths, {len(sp)} scripted turns")
    for path in paths:
        print("   ", " > ".join(path))
    return out


# streamer numbers to quote
with open(os.path.join(HERE, "streamer_scenes.json"), encoding="utf-8") as f:
    sn = json.load(f)["numbers"]
PERSONAS["streamer"]["mustQuote"] = [str(sn["preDrop"]), str(sn["trough"]), f"{abs(sn['dropPct'])}%",
                                     str(sn["chat37"]), str(sn["chat41"]), str(sn["ccv91"]), str(sn["peak"]),
                                     str(sn["grindRet"]), str(sn["voteRet"]), str(sn["ccvAt"]["60"]),
                                     f"{round(sn['missionChat'])}/min", f"{round(sn['grindChat'])}/min"]
print("streamer numbers quoted:", PERSONAS["streamer"]["mustQuote"])

built = {p: build(p, cfg) for p, cfg in PERSONAS.items()}
if errors:
    print("\nVALIDATION ERRORS")
    for e in errors:
        print(" -", e)
    sys.exit(1)
for p, g in built.items():
    path = os.path.join(BASE, p, "tutor-flow.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(g, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print("wrote", path)
