#!/usr/bin/env python3
"""Recompute every published figure in Balanced Plain English Token Efficiency Benchmark v2.

Reads the raw paired telemetry and recomputes the aggregates from scratch, then
asserts them against the figures published in README.md. Nothing is trusted as
typed in.

    python verify.py            # verify only
    python verify.py --emit     # verify, then regenerate data/ from raw/

Standard library only. Exit code 0 on success, 1 on any mismatch.
"""

from __future__ import annotations

import csv
import json
import statistics as st
import sys
from pathlib import Path

HERE = Path(__file__).parent
RAW = HERE / "raw" / "BPE_PAIRED_results.csv"
DATA = HERE / "data"

# Scenario domains, from the benchmark design file (raw/BENCHMARK_DESIGN_V2.md).
DOMAINS = {
    "BPE-001": "software architecture",
    "BPE-002": "AI system architecture",
    "BPE-003": "architecture and BIM operations",
    "BPE-004": "interior design operations",
    "BPE-005": "AI evaluation",
    "BPE-006": "security architecture",
    "BPE-007": "complex code analysis",
    "BPE-008": "requirements engineering",
    "BPE-009": "decision analysis",
    "BPE-010": "multi-agent orchestration",
    "BPE-011": "knowledge management",
    "BPE-012": "document intelligence",
    "BPE-013": "AI governance",
    "BPE-014": "workflow automation",
    "BPE-015": "technical QA",
    "BPE-016": "privacy and local AI",
    "BPE-017": "cost and efficiency",
    "BPE-018": "incident response",
    "BPE-019": "system design tradeoffs",
    "BPE-020": "complex strategic planning",
}

# Figures published in README.md. Recomputed values must match these.
PUBLISHED = {
    "runs": 20,
    "executions": 40,
    "total_off": 285757,
    "total_on": 141604,
    "tokens_saved": 144153,
    "aggregate_reduction_pct": 50.45,
    "mean_reduction_pct": 47.81,
    "median_reduction_pct": 54.83,
    "positive_reductions": 19,
}


def load():
    with RAW.open(encoding="utf-8-sig") as fh:
        rows = list(csv.DictReader(fh))
    out = []
    for r in rows:
        off = int(r["OFF_OutputTokens"])
        on = int(r["ON_OutputTokens"])
        out.append(
            {
                "run_id": r["RunID"],
                "domain": DOMAINS[r["RunID"]],
                "model": r["Model"],
                "off_output_tokens": off,
                "on_output_tokens": on,
                "tokens_saved": off - on,
                "reduction_pct": round((off - on) / off * 100, 2),
                "off_session": r["OFF_Session"],
                "on_session": r["ON_Session"],
            }
        )
    return out


def compute(rows):
    off = sum(r["off_output_tokens"] for r in rows)
    on = sum(r["on_output_tokens"] for r in rows)
    red = [(r["off_output_tokens"] - r["on_output_tokens"]) / r["off_output_tokens"] * 100 for r in rows]
    return {
        "runs": len(rows),
        "executions": len(rows) * 2,
        "total_off": off,
        "total_on": on,
        "tokens_saved": off - on,
        "aggregate_reduction_pct": round((off - on) / off * 100, 2),
        "mean_reduction_pct": round(st.mean(red), 2),
        "median_reduction_pct": round(st.median(red), 2),
        "positive_reductions": sum(1 for r in red if r > 0),
        "min_reduction_pct": round(min(red), 2),
        "max_reduction_pct": round(max(red), 2),
    }


def main() -> int:
    rows = load()
    got = compute(rows)
    failures = []

    print(f"Loaded {len(rows)} paired runs from {RAW.name}\n")

    # Per-run internal consistency: the CSV's own ReductionPercent column.
    with RAW.open(encoding="utf-8-sig") as fh:
        for r in csv.DictReader(fh):
            off, on = int(r["OFF_OutputTokens"]), int(r["ON_OutputTokens"])
            recomputed = round((off - on) / off * 100, 2)
            stated = round(float(r["ReductionPercent"]), 2)
            if recomputed != stated:
                failures.append(f"{r['RunID']}: reduction {recomputed} != stated {stated}")
            saved = int(r["TokensSaved"])
            if off - on != saved:
                failures.append(f"{r['RunID']}: saved {off - on} != stated {saved}")
    print("per-run reduction and tokens-saved columns: "
          f"{'OK' if not failures else str(len(failures)) + ' MISMATCH'}")

    print("\naggregate figures (recomputed vs published):")
    for key, expected in PUBLISHED.items():
        actual = got[key]
        ok = actual == expected
        if not ok:
            failures.append(f"{key}: recomputed {actual} != published {expected}")
        print(f"  {key:<24} {str(actual):>10}  {'OK' if ok else 'MISMATCH -> published ' + str(expected)}")

    print(f"\n  {'min_reduction_pct':<24} {got['min_reduction_pct']:>10}")
    print(f"  {'max_reduction_pct':<24} {got['max_reduction_pct']:>10}")

    if "--emit" in sys.argv and not failures:
        DATA.mkdir(exist_ok=True)
        with (DATA / "paired-results.csv").open("w", newline="", encoding="utf-8") as fh:
            w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
            w.writeheader()
            w.writerows(rows)
        payload = {
            "benchmark": "Balanced Plain English Token Efficiency Benchmark v2",
            "standard_version": "1.1.0",
            "model": "claude-opus-5",
            "measurement": "output tokens only, from Claude Code JSONL session telemetry",
            "summary": got,
            "runs": rows,
        }
        (DATA / "paired-results.json").write_text(
            json.dumps(payload, indent=2) + "\n", encoding="utf-8"
        )
        print(f"\nwrote {DATA/'paired-results.csv'}")
        print(f"wrote {DATA/'paired-results.json'}")

    if failures:
        print("\nFAILED:")
        for f in failures:
            print("  -", f)
        return 1
    print("\nAll figures verified.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
