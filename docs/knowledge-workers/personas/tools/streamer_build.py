#!/usr/bin/env python3
"""KiKi breadth prototype: streamer scenario builder (illustrative analytics for one 3-hour stream).

Deterministic (seeded). Builds scenario.json for the streamer persona (Meera, placeholder) and
checks that the drop near minute 40 lines up with the segment change, that chat falls before
CCV, and that viewers recover once the next segment starts.

Run:  py -3 -I streamer_build.py
Writes: <personas>/streamer/scenario.json  and  ./streamer_scenes.json (for the tutor-flow builder)
"""
import json
import math
import os
import random
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = (r"C:\Users\Arpan Vihan\Downloads\Google AI Builder\Design-Thinking"
           r"\docs\knowledge-workers\personas\streamer")
SEED = 4040
N = 180  # minutes 0..179
rng = random.Random(SEED)

LT = lambda en, hl: {"en": en, "hi-Latn": hl}

SEGMENTS = [
    # id, from, to, en label, hinglish label, what happened
    ("seg-pre", 0, 5, "Starting soon", "Starting soon",
     "Countdown screen, music; Meera greets early chatters"),
    ("seg-intro", 5, 12, "Intro + today's plan", "Intro + aaj ka plan",
     "Says today's goals out loud; pins them in chat"),
    ("seg-mission", 12, 38, "Story mission: first heist", "Story mission: pehla heist",
     "High stakes, constant commentary, reacts to chat"),
    ("seg-grind", 38, 60, "Silent grind: cash farming", "Silent grind: cash farming",
     "Repetitive driving for cash; mic mostly off, music only; no goal said, chat not read"),
    ("seg-vote", 60, 92, "Free roam: chat votes the heist plan", "Free roam: chat vote se heist plan",
     "Gameplay without a mission, but two chat polls, reads chat, talks through the plan"),
    ("seg-collab", 92, 150, "Collab: duo heist with agency partner", "Collab: agency partner ke saath duo heist",
     "Duo heist with another agency creator; incoming raid at 95:00"),
    ("seg-wind", 150, 180, "Wind-down: Q&A + raid out", "Wind-down: Q&A + raid out",
     "Q&A, recap of tomorrow's plan, raids out to an agency partner at 179:00"),
]

GRIND_END_VALUE = 333 + (555 - 333) * math.exp(-(61 - 40) / 7.5)


def collab_base(m):
    return 484 + 95 * (1 - math.exp(-(m - 92) / 15)) - max(0, m - 128) * 1.4


def raid_in(m):
    return 140 * (0.62 + 0.38 * math.exp(-(m - 95) / 6)) if m >= 95 else 0.0


WIND_START = collab_base(150) + raid_in(150)


def ccv_model(m):
    if m < 5:
        return 40 + 150 * (m / 5)
    if m < 12:
        return 190 + 140 * ((m - 5) / 7)
    if m < 38:
        x = (m - 12) / 26
        base = 330 + 230 * (1 - math.exp(-3.0 * x)) / (1 - math.exp(-3.0))
        bump = 14 * math.exp(-((m - 25) / 2.5) ** 2) + 10 * math.exp(-((m - 34) / 2.0) ** 2)
        return base + bump
    if m < 61:
        if m <= 40:
            return 560 - (m - 38) * 2.5          # viewers hold for ~2 minutes after the switch
        return 333 + (555 - 333) * math.exp(-(m - 40) / 7.5)
    if m < 92:
        return GRIND_END_VALUE + (485 - GRIND_END_VALUE) * (1 - math.exp(-(m - 61) / 9))
    if m < 150:
        return collab_base(m) + raid_in(m)
    d = m - 150
    return WIND_START - d * 5.5 - d * d * 0.05


def chat_model(m):
    if m < 5:
        return 6 + 2.4 * m
    if m < 12:
        return 32 + 2.2 * (m - 5)
    if m < 38:
        base = 60 + 20 * min(1.0, (m - 12) / 10)
        spike = 45 * math.exp(-((m - 25) / 1.5) ** 2) + 60 * math.exp(-((m - 34) / 1.3) ** 2)
        return base + spike
    if m < 60:
        if m == 38:
            return 64
        if m == 39:
            return 37
        if m == 40:
            return 22
        return 14 + 4 * math.exp(-((m - 50) / 1.5) ** 2)
    if m < 92:
        base = 85
        poll1 = 75 * math.exp(-((m - 64) / 1.8) ** 2)
        poll2 = 45 * math.exp(-((m - 77) / 1.5) ** 2)
        ramp = -45 * math.exp(-(m - 60) / 1.5)
        return base + poll1 + poll2 + ramp
    if m < 150:
        base = 100 + 10 * math.sin((m - 92) / 7)
        burst = 140 * math.exp(-(m - 95) / 1.6) if m >= 95 else 0.0
        return base + burst
    if m < 170:
        return 76
    if m < 179:
        return 52
    return 110


def follow_rate(m):
    if m < 5:
        r = 0.04
    elif m < 12:
        r = 0.30
    elif m < 38:
        r = 0.75
    elif m < 60:
        r = 0.06
    elif m < 92:
        r = 0.60
    elif m < 150:
        r = 0.45 + (3.5 if 95 <= m <= 98 else 0.0)
    else:
        r = 0.22
    return r


ccv, chat, follows = [], [], []
noise = 0.0
acc = 0.0
for m in range(N):
    noise = 0.6 * noise + rng.gauss(0, 4 + 0.006 * ccv_model(m))
    ccv.append(max(0, int(round(ccv_model(m) + noise))))
    chat.append(max(0, int(round(chat_model(m) * (1 + rng.gauss(0, 0.07))))))
    acc += follow_rate(m) * (0.5 + rng.random())
    n = int(acc)
    acc -= n
    follows.append(n)

# ----------------------------------------------------------------------------- stats
checks = []


def check(name, ok, detail=""):
    checks.append({"name": name, "pass": bool(ok), "detail": detail})
    print(("PASS " if ok else "FAIL ") + name + (" :: " + detail if detail else ""))


def mean(xs):
    return sum(xs) / len(xs)


seg_stats = []
for sid, a, b, en, hl, what in SEGMENTS:
    c = ccv[a:b]
    seg_stats.append({
        "id": sid, "from": a, "to": b, "minutes": b - a,
        "ccvStart": ccv[a], "ccvEnd": ccv[b - 1], "ccvAvg": round(mean(c)),
        "ccvMin": min(c), "ccvMax": max(c),
        "retention": round(ccv[b - 1] / ccv[a], 2),
        "chatPerMinAvg": round(mean(chat[a:b]), 1),
        "follows": sum(follows[a:b]),
    })
S = {s["id"]: s for s in seg_stats}

peak = max(ccv)
peak_min = ccv.index(peak)
pre_drop = ccv[38]          # CCV at the segment change
pre_drop_min = 38
trough = min(ccv[40:66])
trough_min = 40 + ccv[40:66].index(trough)
drop_pct = (trough - pre_drop) / pre_drop * 100
mission_chat_avg = S["seg-mission"]["chatPerMinAvg"]
chat_37, chat_41 = chat[37], chat[41]
chat_drop_3min_pct = (chat_41 - chat_37) / chat_37 * 100
chat_half_min = next(m for m in range(38, 60) if chat[m] < 0.5 * mission_chat_avg)
ccv_90_min = next(m for m in range(38, 60) if ccv[m] < 0.9 * pre_drop)
lead = ccv_90_min - chat_half_min
ccv_40 = ccv[40]
ccv_60 = ccv[60]
ccv_91 = ccv[91]
recovery_pct = (ccv_91 - trough) / trough * 100
raid_peak = max(ccv[95:100])
hours_watched = sum(ccv) / 60

check("CCV holds through 40:00 (within 3% of 38:00) then falls > 5% by 42:00",
      all(abs(ccv[m] - ccv[38]) <= 0.03 * ccv[38] for m in (39, 40)) and ccv[42] < 0.95 * ccv[38],
      f"ccv 38-42: {ccv[38:43]}")
check("drop is clear: 30-45% from the pre-drop level to the trough", -45 <= drop_pct <= -30,
      f"{drop_pct:.1f}% ({pre_drop} -> {trough} at {trough_min})")
check("trough sits at the end of the grind / start of the next segment", 56 <= trough_min <= 63, f"{trough_min}")
check("chat falls before CCV (lead >= 2 min)", lead >= 2,
      f"chat < 50% of mission avg at {chat_half_min}, CCV < 90% of pre-drop at {ccv_90_min}")
check("chat collapses after the switch (> 70% down 37->41)", chat_drop_3min_pct < -70, f"{chat_drop_3min_pct:.0f}%")
check("recovery once the vote segment starts (CCV at 91 >= 1.25 x trough)", ccv_91 >= 1.25 * trough,
      f"{trough} -> {ccv_91} (+{recovery_pct:.0f}%)")
check("grind retention < 0.8, vote retention > 1.2",
      S["seg-grind"]["retention"] < 0.8 and S["seg-vote"]["retention"] > 1.2,
      f"{S['seg-grind']['retention']} / {S['seg-vote']['retention']}")
check("peak comes after the incoming raid", peak_min >= 95, f"peak {peak} at {peak_min}")
check("follows total plausible (70-120) and near zero in the grind",
      70 <= sum(follows) <= 120 and S["seg-grind"]["follows"] <= 3,
      f"total {sum(follows)}, grind {S['seg-grind']['follows']}")
check("segments tile 0-180 without gaps", all(SEGMENTS[i][2] == SEGMENTS[i + 1][1] for i in range(len(SEGMENTS) - 1))
      and SEGMENTS[0][1] == 0 and SEGMENTS[-1][2] == N, "")
check("all series are non-negative integers of length 180",
      all(isinstance(v, int) and v >= 0 for v in ccv + chat + follows) and len(ccv) == len(chat) == len(follows) == N, "")

per5 = {"bucketStartMin": list(range(0, N, 5)),
        "ccvAvg": [round(mean(ccv[i:i + 5])) for i in range(0, N, 5)],
        "chatTotal": [sum(chat[i:i + 5]) for i in range(0, N, 5)],
        "follows": [sum(follows[i:i + 5]) for i in range(0, N, 5)]}

print()
for s in seg_stats:
    print(s)
print(f"peak {peak} @ {peak_min}; avg {mean(ccv):.0f}; pre-drop {pre_drop} @ {pre_drop_min}; "
      f"trough {trough} @ {trough_min}; drop {drop_pct:.1f}%")
print(f"ccv[38] {ccv[38]} ccv[40] {ccv_40} ccv[45] {ccv[45]} ccv[50] {ccv[50]} ccv[60] {ccv_60} ccv[91] {ccv_91}"
      f" raid peak {raid_peak}")
print(f"chat 37 {chat_37} -> 41 {chat_41} ({chat_drop_3min_pct:.0f}%), lead {lead} min "
      f"(chat {chat_half_min}, ccv {ccv_90_min})")
print(f"follows {sum(follows)}; chat total {sum(chat)}; hours watched {hours_watched:.0f}")
print("ccv:", ccv)
print("chat:", chat)

if any(not c["pass"] for c in checks):
    print("CHECK FAILED")
    sys.exit(1)

# ----------------------------------------------------------------------------- scenario.json
segments_out = [{"id": sid, "from": a, "to": b, "label": LT(en, hl), "whatHappened": what}
                for sid, a, b, en, hl, what in SEGMENTS]
events = [
    {"id": "ev-mission-start", "atMin": 12, "label": LT("Mission starts", "Mission shuru")},
    {"id": "ev-segment-change", "atMin": 38,
     "label": LT("Segment change: mission ends, silent grind starts", "Segment change: mission khatam, silent grind shuru")},
    {"id": "ev-poll-1", "atMin": 62, "label": LT("Chat poll 1: heist approach", "Chat poll 1: heist ka approach")},
    {"id": "ev-poll-2", "atMin": 75, "label": LT("Chat poll 2: getaway car", "Chat poll 2: getaway car")},
    {"id": "ev-raid-in", "atMin": 95, "label": LT("Raid in · 140 viewers", "Raid in · 140 viewers"), "viewers": 140},
    {"id": "ev-raid-out", "atMin": 179, "label": LT("Raid out to agency partner", "Agency partner ko raid out")},
]

scenario = {
    "schema": "kiki-scenario/v0-draft",
    "id": "streamer-launch-week-day2",
    "packId": "streaming-gta",
    "illustrative": True,
    "labels": {
        "prototype": "Prototype · illustrative",
        "ip": "GTA 6 is referred to by name only. No publisher logos, artwork, characters or footage. All charts are our own.",
        "machineDraft": LT("Machine draft · native review pending", "Machine draft · native review pending"),
    },
    "languageReview": {"en": "draft",
                       "hi-Latn": "draft (machine draft: needs a native Hinglish reviewer and a practising streamer)"},
    "persona": {"name": "Meera (placeholder)", "role": "Newly signed streamer, GTA 6 launch-week cohort",
                "org": "Illustrative creator agency"},
    "stream": {
        "title": LT("Launch week Day 2: first heist", "Launch week Day 2: pehla heist"),
        "game": "GTA 6 (named only)",
        "platform": "Twitch. The prototype dashboard is our own generic design, not the platform's UI.",
        "day": "Launch week · Day 2",
        "startLocal": "20:00 IST",
        "durationMin": N,
        "language": "Hinglish",
        "agencyTargetAvgCcv": 550,
    },
    "segments": segments_out,
    "events": events,
    "series": {"resolution": "1 min", "minute": list(range(N)), "ccv": ccv, "chatPerMin": chat,
               "followsPerMin": follows},
    "per5min": per5,
    "summary": {
        "peakCcv": peak, "peakAtMin": peak_min, "avgCcv": round(mean(ccv)),
        "hoursWatched": round(hours_watched), "chatMessages": sum(chat), "follows": sum(follows),
        "note": "Scenario numbers only. Not statistics about any real platform or creator.",
    },
    "segmentStats": seg_stats,
    "drop": {
        "segmentChangeAtMin": 38, "dropStartsAtMin": 40,
        "preDropCcv": pre_drop, "preDropAtMin": pre_drop_min,
        "troughCcv": trough, "troughAtMin": trough_min, "dropPct": round(drop_pct, 1),
        "ccvAt40": ccv_40, "ccvAt60": ccv_60,
        "chatAt37": chat_37, "chatAt41": chat_41, "chatDropPct37to41": round(chat_drop_3min_pct),
        "chatLeadMin": lead,
        "leadDefinition": "chat below 50% of the mission average vs CCV below 90% of the pre-drop level",
        "cause": "Segment change at 38:00 from a high-stakes mission to a silent grind: no stated goal, mic mostly off, chat not read, no chat mechanic. Chat went quiet first; CCV followed.",
        "notTheCause": ["A bigger streamer going live (the recovery at 60:00 lines up with her own segment change)",
                        "Viewer fatigue (CCV recovered and peaked after 95:00)",
                        "Grinding as such (the 60-92 segment was also mission-free gameplay, but with polls and talk, and recovered)"],
    },
    "recovery": {
        "startsAtMin": 61, "ccvAt91": ccv_91, "recoveryPctFromTrough": round(recovery_pct),
        "why": "Free-roam segment run with chat polls, reading chat and a plan said out loud",
        "raidPeak": raid_peak,
    },
    "doTask": {
        "id": "find-the-drop",
        "tool": LT("Stream analytics dashboard (generic, unbranded)", "Stream analytics dashboard (generic, unbranded)"),
        "userAsk": LT("KiKi, why did viewers drop here?", "KiKi, yahan viewers kyun gire?"),
        "lookFor": [
            {"id": "ccv-drop-40", "desc": "The CCV drop starting at 40:00 on the viewers chart"},
            {"id": "chat-lull-38", "desc": "The chat-rate lull starting at 38:00"},
            {"id": "segment-change-38", "desc": "The segment marker at 38:00 (mission -> grind)"},
            {"id": "recovery-60", "desc": "The recovery after 60:00"},
            {"id": "raid-in-95", "desc": "The incoming raid at 95:00"},
        ],
        "askAfter": LT("What changed on stream just before the drop?", "Drop se just pehle stream pe kya badla tha?"),
        "graphId": "streaming-gta/engagement-drop-40",
        "note": "KiKi marks what it can see on the dashboard and asks one question. It never edits her stream, scenes or settings.",
    },
    "generator": {"script": os.path.join(HERE, "streamer_build.py"), "rerun": "py -3 -I streamer_build.py",
                  "seed": SEED, "method": "Piecewise model per segment + seeded AR(1) noise; follows from per-segment rates"},
    "checks": checks,
    "notes": [
        "Everything here is illustrative: a placeholder creator, an invented agency, a generated stream.",
        "Segment retention = CCV at the segment's last minute / CCV at its first minute (agency playbook definition).",
        "The tutor graph, the storyboard and the Do task all quote numbers from this file.",
    ],
}

os.makedirs(OUT_DIR, exist_ok=True)
with open(os.path.join(OUT_DIR, "scenario.json"), "w", encoding="utf-8") as f:
    json.dump(scenario, f, ensure_ascii=False, indent=2)
    f.write("\n")

line = {
    "x": {"label": LT("Stream time", "Stream time"), "unit": "min", "values": list(range(N))},
    "series": [{"id": "ccv", "label": LT("CCV (concurrent viewers)", "CCV (concurrent viewers)"), "values": ccv},
               {"id": "chat", "label": LT("Chat messages per minute", "Chat messages per minute"), "values": chat}],
    "bands": [{"id": sid, "from": a, "to": b, "label": LT(en, hl)} for sid, a, b, en, hl, _ in SEGMENTS],
    "markers": [{"id": "mk-switch", "x": 38, "label": LT("38:00 segment change", "38:00 segment change")},
                {"id": "mk-drop", "x": 40, "label": LT("40:00 drop starts", "40:00 drop shuru")},
                {"id": "mk-trough", "x": trough_min, "label": LT(f"Low {trough}", f"Low {trough}")},
                {"id": "mk-raid-in", "x": 95, "label": LT("Raid in · 140", "Raid in · 140")},
                {"id": "mk-raid-out", "x": 179, "label": LT("Raid out", "Raid out")}],
}
nums = {"peak": peak, "peakMin": peak_min, "preDrop": pre_drop, "preDropMin": pre_drop_min, "trough": trough,
        "troughMin": trough_min, "dropPct": round(drop_pct), "chat37": chat_37, "chat41": chat_41,
        "chatDropPct": round(chat_drop_3min_pct), "lead": lead, "ccv40": ccv_40, "ccv60": ccv_60, "ccv91": ccv_91,
        "recoveryPct": round(recovery_pct), "grindRet": S["seg-grind"]["retention"],
        "voteRet": S["seg-vote"]["retention"], "grindChat": S["seg-grind"]["chatPerMinAvg"],
        "missionChat": mission_chat_avg, "voteChat": S["seg-vote"]["chatPerMinAvg"], "follows": sum(follows),
        "avg": round(mean(ccv)), "chatTotal": sum(chat), "hoursWatched": round(hours_watched),
        "grindFollows": S["seg-grind"]["follows"], "missionFollows": S["seg-mission"]["follows"],
        "ccvAt": {str(m): ccv[m] for m in (12, 38, 40, 45, 50, 55, 59, 60, 61, 70, 80, 91, 95, 96, 150, 179)},
        "chatAt": {str(m): chat[m] for m in (36, 37, 38, 39, 40, 41, 45, 50, 59, 60, 62, 64, 75, 77, 95)}}
with open(os.path.join(HERE, "streamer_scenes.json"), "w", encoding="utf-8") as f:
    json.dump({"line": line, "numbers": nums}, f, ensure_ascii=False, indent=2)

print("\nwrote", os.path.join(OUT_DIR, "scenario.json"))
print("wrote", os.path.join(HERE, "streamer_scenes.json"))
