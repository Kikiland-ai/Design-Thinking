#!/usr/bin/env python3
"""KiKi breadth prototype: trader scenario builder and Black-Scholes check.

Illustrative only. Builds scenario.json for the F&O trader persona (Ravi, placeholder)
and checks that the long call really loses value although spot moves the right way.

Run:  py -3 -I trader_build.py
Writes: <personas>/trader/scenario.json  and  ./trader_scenes.json (for the tutor-flow builder)
"""
import itertools
import json
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = (r"C:\Users\Arpan Vihan\Downloads\Google AI Builder\Design-Thinking"
           r"\docs\knowledge-workers\personas\trader")

# ----------------------------------------------------------------------------- Black-Scholes

def ncdf(x):
    return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))


def npdf(x):
    return math.exp(-0.5 * x * x) / math.sqrt(2.0 * math.pi)


def d1d2(S, K, T, sig, r, q=0.0):
    v = sig * math.sqrt(T)
    d1 = (math.log(S / K) + (r - q + 0.5 * sig * sig) * T) / v
    return d1, d1 - v


def bs(S, K, T, sig, r, q=0.0, kind="call"):
    """European Black-Scholes(-Merton) price."""
    if T <= 0:
        return max(0.0, S - K) if kind == "call" else max(0.0, K - S)
    d1, d2 = d1d2(S, K, T, sig, r, q)
    if kind == "call":
        return S * math.exp(-q * T) * ncdf(d1) - K * math.exp(-r * T) * ncdf(d2)
    return K * math.exp(-r * T) * ncdf(-d2) - S * math.exp(-q * T) * ncdf(-d1)


def greeks_call(S, K, T, sig, r, q=0.0):
    d1, d2 = d1d2(S, K, T, sig, r, q)
    delta = math.exp(-q * T) * ncdf(d1)
    gamma = math.exp(-q * T) * npdf(d1) / (S * sig * math.sqrt(T))
    vega_pt = S * math.exp(-q * T) * npdf(d1) * math.sqrt(T) / 100.0      # per 1 vol point
    theta_y = (-S * math.exp(-q * T) * npdf(d1) * sig / (2.0 * math.sqrt(T))
               - r * K * math.exp(-r * T) * ncdf(d2)
               + q * S * math.exp(-q * T) * ncdf(d1))
    return {"delta": delta, "gamma": gamma, "vegaPerVolPoint": vega_pt,
            "thetaPerCalendarDay": theta_y / 365.0}


def tick(x, size=0.05):
    return round(round(x / size) * size, 2)


def r2(x):
    return round(x, 2)


# ----------------------------------------------------------------------------- self-tests
checks = []


def check(name, ok, detail=""):
    checks.append({"name": name, "pass": bool(ok), "detail": detail})
    print(("PASS " if ok else "FAIL ") + name + (" :: " + detail if detail else ""))


# Hull, Options Futures and Other Derivatives, worked example: S=42 K=40 r=10% sigma=20% T=0.5
hc = bs(42, 40, 0.5, 0.20, 0.10)
hp = bs(42, 40, 0.5, 0.20, 0.10, kind="put")
check("self-test: textbook call 4.76", abs(hc - 4.76) < 0.005, f"{hc:.4f}")
check("self-test: textbook put 0.81", abs(hp - 0.81) < 0.005, f"{hp:.4f}")
par = hc - hp - (42 - 40 * math.exp(-0.10 * 0.5))
check("self-test: put-call parity", abs(par) < 1e-9, f"residual {par:.2e}")

# ----------------------------------------------------------------------------- scenario inputs
R = 0.065            # illustrative risk-free rate, continuous
Q = 0.0              # index dividend yield ignored (teaching simplification)
LOT = 75             # illustrative lot size
LOTS = 4
QTY = LOT * LOTS
S0 = 24040.0         # spot at entry: D-1 close
S1 = 24150.0         # spot at exit:  D0 close (+110)
K = 24200.0          # Ravi's strike (CE)
K_SHORT = 24400.0    # short leg of the playbook counterfactual spread
K_ATM = 24050.0      # nearest strike to spot at entry (strike step 50)
IV0 = 0.175          # IV of the 24200 CE at entry (flat across strikes: teaching simplification)
IV1 = 0.110          # IV after the event
DTE0 = 3.0           # calendar days to expiry at entry (D-1 15:30 -> D+2 15:30)
DTE1 = 2.0           # calendar days to expiry at exit  (D0 15:30 -> D+2 15:30)
T0 = DTE0 / 365.0
T1 = DTE1 / 365.0
BOOK = 1_000_000     # trainee paper book, notional INR
EVENT_BUDGET = 0.01 * BOOK

# ----------------------------------------------------------------------------- headline trade
c0 = bs(S0, K, T0, IV0, R, Q)
c1 = bs(S1, K, T1, IV1, R, Q)
paid = tick(c0)
exit_px = tick(c1)
pnl_unit = r2(exit_px - paid)
pnl = r2(pnl_unit * QTY)
premium_at_risk = r2(paid * QTY)

check("direction was right (spot rose)", S1 > S0, f"{S0:.0f} -> {S1:.0f} ({(S1 / S0 - 1) * 100:+.2f}%)")
check("option lost value despite the favourable move", c1 < c0, f"{c0:.2f} -> {c1:.2f}")
check("loss is material (> 25% of premium)", (c0 - c1) / c0 > 0.25, f"{(c1 / c0 - 1) * 100:.1f}%")

g0 = greeks_call(S0, K, T0, IV0, R, Q)

# Shapley decomposition of the price change over {spot, iv, time}
factors = ["spot", "iv", "time"]
start = {"spot": S0, "iv": IV0, "time": T0}
end = {"spot": S1, "iv": IV1, "time": T1}


def val(st):
    return bs(st["spot"], K, st["time"], st["iv"], R, Q)


contrib = {f: 0.0 for f in factors}
perms = list(itertools.permutations(factors))
for p in perms:
    st = dict(start)
    prev = val(st)
    for f in p:
        st[f] = end[f]
        cur = val(st)
        contrib[f] += cur - prev
        prev = cur
for f in factors:
    contrib[f] /= len(perms)
total_model = c1 - c0
check("decomposition sums to the model change", abs(sum(contrib.values()) - total_model) < 1e-9,
      f"{sum(contrib.values()):.4f} vs {total_model:.4f}")

# sequential (spot -> iv -> time), for reference
seq_a = bs(S1, K, T0, IV0, R, Q)
seq_b = bs(S1, K, T0, IV1, R, Q)
seq = {"spot": seq_a - c0, "iv": seq_b - seq_a, "time": c1 - seq_b}

# rounded rupee decomposition that adds up exactly to the fill-based P&L per unit
dec_round = {f: round(contrib[f]) for f in factors}
diff = round(pnl_unit) - sum(dec_round.values())
if diff:
    # put any rounding residue on the largest component
    big = max(factors, key=lambda f: abs(contrib[f]))
    dec_round[big] += diff
check("IV fall is the largest single drag", abs(contrib["iv"]) > abs(contrib["time"]) and contrib["iv"] < 0,
      f"iv {contrib['iv']:.2f}, time {contrib['time']:.2f}, spot {contrib['spot']:+.2f}")

# counterfactual: same move, same day passes, IV does not fall
c_nocrush = bs(S1, K, T1, IV0, R, Q)
check("without the IV fall the same move would have gained", c_nocrush > c0, f"{c_nocrush:.2f} vs {c0:.2f}")


# spot needed at D0 close (IV 11%, 2 DTE) to get the premium back
def solve_spot(target, lo, hi):
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if bs(mid, K, T1, IV1, R, Q) < target:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


s_be_after = solve_spot(paid, S0, S0 + 2000)
be_expiry = K + paid

# implied move: ATM straddle at entry, and the event-variance view
atm_call = bs(S0, K_ATM, T0, IV0, R, Q)
atm_put = bs(S0, K_ATM, T0, IV0, R, Q, kind="put")
straddle = tick(atm_call) + tick(atm_put)
var_event = (IV0 ** 2 - IV1 ** 2) * T0            # variance attributed to the event (IV1 = base)
event_sd_pts = S0 * math.sqrt(var_event)
realised = S1 - S0
check("realised move smaller than the priced move", realised < straddle,
      f"+{realised:.0f} vs straddle {straddle:.2f}")

# playbook counterfactual: 24200/24400 call spread sized inside the event budget
short0 = tick(bs(S0, K_SHORT, T0, IV0, R, Q))
short1 = tick(bs(S1, K_SHORT, T1, IV1, R, Q))
debit = r2(paid - short0)
spread_after = r2(exit_px - short1)
spread_lots = int(EVENT_BUDGET // (debit * LOT))
spread_qty = spread_lots * LOT
spread_max_loss = r2(debit * spread_qty)
spread_pnl = r2((spread_after - debit) * spread_qty)
spread_pnl_4lots = r2((spread_after - debit) * QTY)
check("spread max loss inside the event budget", spread_max_loss <= EVENT_BUDGET,
      f"{spread_max_loss:.2f} <= {EVENT_BUDGET:.0f}")
check("spread loses far less than the long call", abs(spread_pnl) < abs(pnl) / 5,
      f"{spread_pnl:.2f} vs {pnl:.2f}")

# ----------------------------------------------------------------------------- candles (30-min bars)
# t, open, high, low, close ; bar close times are listed separately
D1 = [
    ("D-1 09:15", 23985, 24012, 23958, 23996),
    ("D-1 09:45", 23996, 24021, 23977, 24008),
    ("D-1 10:15", 24008, 24030, 23990, 23998),
    ("D-1 10:45", 23998, 24015, 23972, 23981),
    ("D-1 11:15", 23981, 24004, 23962, 23993),
    ("D-1 11:45", 23993, 24019, 23985, 24011),
    ("D-1 12:15", 24011, 24026, 23999, 24004),
    ("D-1 12:45", 24004, 24017, 23988, 24009),
    ("D-1 13:15", 24009, 24038, 24002, 24027),
    ("D-1 13:45", 24027, 24049, 24016, 24036),
    ("D-1 14:15", 24036, 24058, 24020, 24025),
    ("D-1 14:45", 24025, 24068, 24019, 24051),
    ("D-1 15:15", 24051, 24064, 24031, 24040),
]
D0 = [
    ("D0 09:15", 24032, 24055, 24011, 24038),
    ("D0 09:45", 24038, 24194, 23986, 24168),   # policy announcement at 10:00 falls in this bar
    ("D0 10:15", 24168, 24181, 24109, 24126),
    ("D0 10:45", 24126, 24152, 24098, 24141),
    ("D0 11:15", 24141, 24166, 24122, 24158),
    ("D0 11:45", 24158, 24171, 24130, 24137),
    ("D0 12:15", 24137, 24150, 24112, 24124),
    ("D0 12:45", 24124, 24146, 24109, 24140),
    ("D0 13:15", 24140, 24168, 24131, 24161),
    ("D0 13:45", 24161, 24178, 24139, 24147),
    ("D0 14:15", 24147, 24163, 24128, 24135),
    ("D0 14:45", 24135, 24159, 24126, 24154),
    ("D0 15:15", 24154, 24166, 24141, 24150),
]
CLOSE_H = [9.75, 10.25, 10.75, 11.25, 11.75, 12.25, 12.75, 13.25, 13.75, 14.25, 14.75, 15.25, 15.5]
EXPIRY_DAY = 3.0 + 15.5 / 24.0        # D+2 15:30, with D-1 = day 0
EVENT_TIME = 1.0 + 10.0 / 24.0        # D0 10:00
POST_SPAN_H = 5.5                     # 10:00 -> 15:30


def iv_at(day_time):
    T = (EXPIRY_DAY - day_time) / 365.0
    if day_time <= EVENT_TIME:
        return math.sqrt(IV1 ** 2 + var_event / T)       # event variance spread over remaining time
    h = (day_time - EVENT_TIME) * 24.0
    return IV1 + 0.016 * max(0.0, 1.0 - h / POST_SPAN_H) ** 1.5   # residual uncertainty bleeds out


bars, iv_series, prem_series, t_labels = [], [], [], []
for day, rows in ((0, D1), (1, D0)):
    for (t, o, h, l, c), ch in zip(rows, CLOSE_H):
        assert h >= max(o, c) and l <= min(o, c), t
        bars.append({"t": t, "o": o, "h": h, "l": l, "c": c})
        dt = day + ch / 24.0
        sig = iv_at(dt)
        T = (EXPIRY_DAY - dt) / 365.0
        iv_series.append(round(sig * 100, 2))
        prem_series.append(r2(bs(c, K, T, sig, R, Q)))
        t_labels.append(t)
for i in range(1, len(bars)):
    if i != 13:
        assert bars[i]["o"] == bars[i - 1]["c"], bars[i]["t"]
check("candles consistent (H/L bound O/C, opens follow closes intraday)", True, f"{len(bars)} bars")
check("per-bar premium at entry bar equals headline model price", abs(prem_series[12] - r2(c0)) < 0.01,
      f"{prem_series[12]} vs {c0:.2f}")
check("per-bar premium at exit bar equals headline model price", abs(prem_series[25] - r2(c1)) < 0.01,
      f"{prem_series[25]} vs {c1:.2f}")
check("per-bar IV at entry/exit equals headline IV", abs(iv_series[12] - IV0 * 100) < 0.01 and
      abs(iv_series[25] - IV1 * 100) < 0.01, f"{iv_series[12]} / {iv_series[25]}")

d0_open, d0_high = D0[0][1], max(b[2] for b in D0)
d0_low, d0_close = min(b[3] for b in D0), D0[-1][4]
check("spot never reached the strike on event day", d0_high < K, f"D0 high {d0_high} < {K:.0f}")

# ----------------------------------------------------------------------------- option chain snapshot (D-1 15:25)
OI_CALL = {23900: 21400, 23950: 18900, 24000: 52300, 24050: 38700, 24100: 61200, 24150: 44800,
           24200: 112600, 24250: 58100, 24300: 89400, 24350: 41200, 24400: 76500}
OI_PUT = {23900: 68300, 23950: 47900, 24000: 104800, 24050: 51600, 24100: 42700, 24150: 22300,
          24200: 18900, 24250: 9800, 24300: 7600, 24350: 4100, 24400: 3900}
chain = []
for k in sorted(OI_CALL):
    chain.append({"strike": k,
                  "callLtp": tick(bs(S0, k, T0, IV0, R, Q)), "callIvPct": IV0 * 100, "callOi": OI_CALL[k],
                  "putLtp": tick(bs(S0, k, T0, IV0, R, Q, kind="put")), "putIvPct": IV0 * 100,
                  "putOi": OI_PUT[k]})
pcr = sum(OI_PUT.values()) / sum(OI_CALL.values())
check("chain: 24200 CE LTP equals Ravi's fill", [c for c in chain if c["strike"] == 24200][0]["callLtp"] == paid,
      f"{paid}")

# payoff-at-expiry sanity
check("breakeven at expiry = strike + premium", abs(be_expiry - (K + paid)) < 1e-9, f"{be_expiry:.2f}")

# ----------------------------------------------------------------------------- report
print()
print(f"premium paid  {paid:.2f}   (model {c0:.4f})")
print(f"exit price    {exit_px:.2f}   (model {c1:.4f})")
print(f"P&L per unit  {pnl_unit:+.2f}   P&L total {pnl:+.2f} on {QTY} units")
print(f"Shapley: spot {contrib['spot']:+.2f}  iv {contrib['iv']:+.2f}  time {contrib['time']:+.2f}"
      f"   rounded {dec_round}")
print(f"sequential: {', '.join(f'{k} {v:+.2f}' for k, v in seq.items())}")
print(f"greeks at entry: {', '.join(f'{k} {v:.5f}' for k, v in g0.items())}")
print(f"no IV fall: {c_nocrush:.2f}  -> P&L/unit {c_nocrush - paid:+.2f}")
print(f"spot needed at D0 close to recover premium: {s_be_after:.1f}")
print(f"ATM straddle {K_ATM:.0f}: call {tick(atm_call)} + put {tick(atm_put)} = {straddle:.2f}"
      f"  ({straddle / S0 * 100:.2f}%)")
print(f"event 1-sd move {event_sd_pts:.1f} pts  ({event_sd_pts / S0 * 100:.2f}%)")
print(f"spread {K:.0f}/{K_SHORT:.0f}: short {short0}->{short1}, debit {debit}, after {spread_after},"
      f" lots {spread_lots}, max loss {spread_max_loss}, P&L {spread_pnl}  (4 lots: {spread_pnl_4lots})")
print(f"premium at risk {premium_at_risk:.2f} = {premium_at_risk / EVENT_BUDGET:.2f}x budget"
      f" = {premium_at_risk / BOOK * 100:.2f}% of book")
print(f"PCR {pcr:.2f}")
print("IV per bar:", iv_series)
print("premium per bar:", prem_series)
print(f"D0 O {d0_open} H {d0_high} L {d0_low} C {d0_close}")

failed = [c for c in checks if not c["pass"]]
if failed:
    print("\nCHECK FAILED:", failed)
    sys.exit(1)

# ----------------------------------------------------------------------------- scenario.json
LT = lambda en, hi: {"en": en, "hi": hi}

scenario = {
    "schema": "kiki-scenario/v0-draft",
    "id": "trader-event-day-iv-crush",
    "packId": "trading-fno",
    "illustrative": True,
    "labels": {
        "prototype": "Prototype · illustrative",
        "disclaimer": LT("Education on a past, illustrative trade. Not investment advice.",
                         "एक पुराने, illustrative trade पर शिक्षा। यह investment advice नहीं है।"),
        "machineDraft": LT("Machine draft · native review pending", "Machine draft · native review बाकी"),
    },
    "languageReview": {"en": "draft", "hi": "draft (machine draft: needs a native Hindi reviewer and a trader)"},
    "persona": {"name": "Ravi (placeholder)", "role": "Trainee index-options trader, onboarding week 2",
                "org": "Illustrative proprietary trading desk (paper book during onboarding)"},
    "context": {
        "book": "Trainee paper book (simulated); no real money",
        "bookNotionalInr": BOOK,
        "eventBudgetPct": 1.0,
        "eventBudgetInr": EVENT_BUDGET,
        "playbookRefs": ["EV-2.1 implied move before premium", "EV-4.1 event budget 1% of book",
                         "EV-4.3 defined risk on event days", "EV-6.1 journal: process over P&L"],
    },
    "underlying": {
        "name": "INDEX (illustrative)",
        "note": "A generic index. Levels, lot size and strike step are illustrative, not any exchange's specification.",
        "lotSize": LOT, "strikeStep": 50, "tickSize": 0.05, "currency": "INR",
    },
    "event": {
        "id": "ev-policy",
        "label": LT("Scheduled policy announcement", "Scheduled policy announcement"),
        "kind": "Scheduled monetary-policy announcement (generic; no real date)",
        "at": "D0 10:00",
        "outcome": "As widely expected; no surprise",
        "timeline": {"D-1": "day before the event (entry at the close)", "D0": "event day (exit at the close)",
                     "D+2": "weekly expiry, 15:30"},
    },
    "trade": {
        "legs": [{"id": "leg-24200ce", "instrument": "24200 CE (weekly)", "type": "call", "side": "long",
                  "strike": K, "lots": LOTS, "qty": QTY,
                  "entry": {"at": "D-1 15:25", "price": paid},
                  "exit": {"at": "D0 15:25", "price": exit_px}}],
        "thesisAsWritten": LT("Policy will be positive, index will go up. Bought calls.",
                              "Policy positive आएगी, index ऊपर जाएगा। Call खरीदे।"),
        "preTradeNote": "Direction only; no implied move, no max-loss line, no exit plan",
    },
    "marketBefore": {"at": "D-1 15:30", "spot": S0, "ivPct": IV0 * 100, "daysToExpiry": DTE0,
                     "premiumModel": r2(c0)},
    "marketAfter": {"at": "D0 15:30", "spot": S1, "ivPct": IV1 * 100, "daysToExpiry": DTE1,
                    "premiumModel": r2(c1)},
    "move": {"points": S1 - S0, "pct": r2((S1 / S0 - 1) * 100), "direction": "up (Ravi's direction was right)"},
    "pnl": {
        "perUnit": pnl_unit, "total": pnl, "pctOfPremium": r2(pnl_unit / paid * 100),
        "pctOfBook": r2(pnl / BOOK * 100),
        "note": "Before brokerage, taxes and charges. Notional (paper book).",
    },
    "decomposition": {
        "method": "Shapley average over the 6 orders of changing spot, IV and time (order-independent)",
        "perUnitModel": {k: r2(v) for k, v in contrib.items()},
        "perUnitRoundedForScreen": dec_round,
        "totalForLotsModel": {k: round(v * QTY) for k, v in contrib.items()},
        "totalsNote": (f"Model components x {QTY} units sum to about −₹{abs(round(sum(contrib.values()) * QTY)):,}; "
                       f"the fills-based P&L is −₹{abs(pnl):,.0f} because entry and exit prices are rounded to ₹0.05 ticks. "
                       f"The screen line uses per-unit rupees, which sum to −₹{abs(sum(dec_round.values()))} "
                       f"(P&L per unit −₹{abs(pnl_unit):.2f})."),
        "sequentialSpotThenIvThenTime": {k: r2(v) for k, v in seq.items()},
        "screenLine": LT(f"Move +₹{dec_round['spot']} · IV −₹{abs(dec_round['iv'])} · time −₹{abs(dec_round['time'])}",
                         f"Move +₹{dec_round['spot']} · IV −₹{abs(dec_round['iv'])} · time −₹{abs(dec_round['time'])}"),
    },
    "greeksAtEntry": {k: round(v, 5) for k, v in g0.items()},
    "impliedMove": {
        "atmStrike": K_ATM, "atmCall": tick(atm_call), "atmPut": tick(atm_put), "straddle": r2(straddle),
        "straddlePctOfSpot": r2(straddle / S0 * 100),
        "eventOneSdPoints": round(event_sd_pts, 1),
        "eventModel": "IV(t)^2 = IV_base^2 + V_event / T(t), with IV_base = 11% (post-event IV); V_event = (17.5%^2 - 11%^2) * 3/365",
        "realisedPoints": S1 - S0,
        "realisedVsStraddle": r2((S1 - S0) / straddle),
        "screenLine": LT(f"Priced move ≈ ±{round(straddle)} · actual +{round(S1 - S0)}",
                         f"Priced move ≈ ±{round(straddle)} · असल move +{round(S1 - S0)}"),
        "rule": "Desk rule of thumb: the ATM straddle price approximates the move the market expects by expiry",
    },
    "sizing": {
        "premiumAtRisk": premium_at_risk,
        "eventBudget": EVENT_BUDGET,
        "multipleOfBudget": r2(premium_at_risk / EVENT_BUDGET),
        "pctOfBook": r2(premium_at_risk / BOOK * 100),
        "note": "The realised loss stayed under the budget, but the risk taken (max loss = full premium) was 2.7x the budget: process breach, not outcome.",
    },
    "breakevens": {
        "atExpiry": r2(be_expiry),
        "spotNeededAtD0CloseToRecoverPremium": round(s_be_after, 0),
        "note": f"With IV at 11% and 2 days left, spot had to close near this level (above the strike) just to get ₹{paid:.2f} back.",
    },
    "counterfactuals": {
        "noIvFall": {"desc": "Same spot move and same day passed, IV stays 17.5%",
                     "value": r2(c_nocrush), "pnlPerUnit": r2(c_nocrush - paid),
                     "pnlTotal": r2((c_nocrush - paid) * QTY)},
        "playbookSpread": {
            "desc": "Playbook event-day setup applied to the same past view: 24200/24400 call spread, sized inside the event budget",
            "legs": [{"strike": K, "type": "call", "side": "long", "entry": paid, "exit": exit_px},
                     {"strike": K_SHORT, "type": "call", "side": "short", "entry": short0, "exit": short1}],
            "netDebit": debit, "valueAfter": spread_after, "lots": spread_lots, "qty": spread_qty,
            "maxLoss": spread_max_loss, "pnl": spread_pnl, "pnlIfFourLots": spread_pnl_4lots,
            "framing": "Shown only as a review of a past trade against the desk's process. Not a recommendation.",
        },
    },
    "candles": {
        "interval": "30m", "session": "09:15-15:30", "barCloseNote": "Last bar of each day is 15:15-15:30",
        "bars": bars,
        "entryBarIndex": 12, "eventBarIndex": 14, "exitBarIndex": 25,
        "eventDay": {"open": d0_open, "high": d0_high, "low": d0_low, "close": d0_close,
                     "changePoints": d0_close - S0, "note": "High stayed below the 24200 strike"},
    },
    "ivSeries": {"unit": "%", "of": "24200 CE", "byBar": iv_series,
                 "note": "Rises into the event (event variance over shrinking time), collapses at 10:00 on D0, bleeds to 11% by the close"},
    "premiumSeries": {"unit": "INR", "of": "24200 CE (model value at each bar close)", "byBar": prem_series},
    "optionChainSnapshot": {
        "at": "D-1 15:25", "spot": S0, "daysToExpiry": DTE0,
        "note": "LTPs are Black-Scholes values at a flat 17.5% IV (teaching simplification); OI figures are invented for the prototype.",
        "rows": chain, "pcrOi": round(pcr, 2),
    },
    "doTask": {
        "id": "pre-event-checklist",
        "tool": LT("Trading terminal: chart and option chain (paper mode, historical replay of D-1)",
                   "Trading terminal: chart और option chain (paper mode, D-1 का historical replay)"),
        "userAsk": LT("Is my pre-event note complete?", "क्या मेरा pre-event note पूरा है?"),
        "lookFor": [
            {"id": "iv-read", "desc": "IV of the chosen strike is noted (17.5%)"},
            {"id": "implied-move", "desc": f"Implied move from the {K_ATM:.0f} straddle is written (about ±{round(straddle)})"},
            {"id": "max-loss", "desc": "Max loss written and inside the event budget (≤ ₹10,000)"},
            {"id": "exit-plan", "desc": "Exit plan (time and price) is written"},
        ],
        "askAfter": LT("Your exit plan is missing. When would you get out?",
                       "Exit plan अभी नहीं लिखा। आप कब निकलेंगे?"),
        "graphId": "trading-fno/bad-call-iv-crush",
        "note": "KiKi points and checks visible work. It never places, modifies or suggests an order.",
    },
    "bsCheck": {
        "result": "PASS",
        "script": os.path.join(HERE, "trader_build.py"),
        "rerun": "py -3 -I trader_build.py",
        "model": {"formula": "Black-Scholes-Merton, European", "riskFreeRate": R, "dividendYield": Q,
                  "dayCount": "calendar days / 365", "ivUnitInParams": "fraction (0.175 = 17.5%)",
                  "smile": "flat IV across strikes (simplification)"},
        "inputs": {"before": {"S": S0, "K": K, "T_days": DTE0, "iv": IV0},
                   "after": {"S": S1, "K": K, "T_days": DTE1, "iv": IV1}},
        "outputs": {"callBefore": round(c0, 4), "callAfter": round(c1, 4), "changePerUnit": round(c1 - c0, 4)},
        "checks": checks,
        "selfTestReference": "Textbook example S=42, K=40, r=10%, sigma=20%, T=0.5: call 4.76, put 0.81",
    },
    "notes": [
        "Everything here is illustrative: a generic index, invented levels and OI, a placeholder trainee and a paper book.",
        "Numbers are internally consistent: the per-bar series, the chain and the payoff scenes all come from the same Black-Scholes function as the headline premiums.",
        "Process, not picks: the scenario reviews a past decision against the desk's process. No recommendation for any live trade.",
    ],
}

os.makedirs(OUT_DIR, exist_ok=True)
with open(os.path.join(OUT_DIR, "scenario.json"), "w", encoding="utf-8") as f:
    json.dump(scenario, f, ensure_ascii=False, indent=2)
    f.write("\n")

# scenes for the tutor-flow builder (contract 05 section 3 shapes)
scenes = {
    "candles": {
        "bars": bars,
        "events": [{"id": "ev-policy", "at": "D0 09:45",
                    "label": LT("Policy announcement · 10:00", "Policy announcement · 10:00")}],
        "levels": [
            {"id": "lv-entry", "price": S0, "label": LT(f"Entry spot {S0:,.0f}", f"Entry spot {S0:,.0f}")},
            {"id": "lv-strike", "price": K, "label": LT("Strike 24200", "Strike 24200")},
            {"id": "lv-breakeven", "price": r2(be_expiry),
             "label": LT(f"Breakeven at expiry {be_expiry:,.2f}", f"Expiry पर breakeven {be_expiry:,.2f}")},
            {"id": "lv-implied-up", "price": round(S0 + straddle),
             "label": LT(f"+{round(straddle)} priced", f"+{round(straddle)} priced")},
            {"id": "lv-implied-down", "price": round(S0 - straddle),
             "label": LT(f"−{round(straddle)} priced", f"−{round(straddle)} priced")},
        ],
    },
    "payoff": {"legs": [{"id": "leg-24200ce", "type": "call", "side": "long", "strike": K,
                         "premium": paid, "lots": LOTS}],
               "lotSize": LOT, "spot": S0, "range": [23600, 24700],
               "iv": {"before": IV0, "after": IV1}, "daysToExpiry": {"before": DTE0, "after": DTE1}},
    "payoffSpread": {"legs": [{"id": "leg-24200ce", "type": "call", "side": "long", "strike": K,
                               "premium": paid, "lots": spread_lots},
                              {"id": "leg-24400ce", "type": "call", "side": "short", "strike": K_SHORT,
                               "premium": short0, "lots": spread_lots}],
                     "lotSize": LOT, "spot": S0, "range": [23600, 24700],
                     "iv": {"before": IV0, "after": IV1}, "daysToExpiry": {"before": DTE0, "after": DTE1}},
    "ivLine": {"x": {"label": LT("30-min bars, D-1 and D0", "30-min bars, D-1 और D0"), "unit": "bar",
                     "values": list(range(len(bars)))},
               "series": [{"id": "iv", "label": LT("IV of 24200 CE (%)", "24200 CE का IV (%)"),
                           "values": iv_series},
                          {"id": "premium", "label": LT("24200 CE premium (₹)", "24200 CE premium (₹)"),
                           "values": prem_series}],
               "markers": [{"id": "mk-entry", "x": 12, "label": LT("Entry", "Entry")},
                           {"id": "mk-event", "x": 14, "label": LT("Policy · 10:00", "Policy · 10:00")},
                           {"id": "mk-exit", "x": 25, "label": LT("Exit", "Exit")}]},
    "numbers": {"paid": paid, "exit": exit_px, "pnl": pnl, "pnlUnit": pnl_unit, "dec": dec_round,
                "straddle": straddle, "premiumAtRisk": premium_at_risk,
                "multiple": r2(premium_at_risk / EVENT_BUDGET), "spreadLots": spread_lots,
                "spreadMaxLoss": spread_max_loss, "spreadPnl": spread_pnl, "debit": debit,
                "short0": short0, "short1": short1, "noCrushPnlUnit": r2(c_nocrush - paid),
                "sBeAfter": round(s_be_after), "beExpiry": r2(be_expiry)},
}
with open(os.path.join(HERE, "trader_scenes.json"), "w", encoding="utf-8") as f:
    json.dump(scenes, f, ensure_ascii=False, indent=2)

print("\nwrote", os.path.join(OUT_DIR, "scenario.json"))
print("wrote", os.path.join(HERE, "trader_scenes.json"))
