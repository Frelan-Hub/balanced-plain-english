# Balanced Plain English — Token Efficiency Evidence v2

## Sweet-spot benchmark

20 complex scenarios × 2 conditions = 40 model executions.

- OFF: Balanced Plain English disabled
- ON: Balanced Plain English enabled
- Keep model, model version, settings, tools, context, and execution environment constant.
- The only intended variable is the Balanced Plain English condition.

## Scenario mix

20 complex scenarios across:
software architecture, AI architecture, BIM/design operations, interior design, AI evaluation, security, code analysis, requirements engineering, decision analysis, orchestration, knowledge management, document intelligence, governance, workflow automation, QA, local AI, cost/efficiency, incident response, system design, and strategic planning.

## Required telemetry

Capture actual model telemetry, not estimates:

- input_tokens
- output_tokens
- total_tokens
- latency_ms (if available)
- model/model version
- timestamp
- complete raw response

## Quality

Score each response /10 using:
- correctness
- requirement coverage
- technical depth
- completeness
- useful specificity
- constraint adherence

Do not reward an answer merely for being shorter.

## Calculations

Input reduction % = `(OFF input - ON input) / OFF input * 100`

Output reduction % = `(OFF output - ON output) / OFF output * 100`

Total reduction % = `(OFF total - ON total) / OFF total * 100`

Quality delta = `ON quality - OFF quality`

Report both mean and median reduction, plus range and quality delta.

## Evidence claim

This is an initial empirical benchmark, not a universal proof. Do not generalize beyond the tested model, task set, and conditions.

## Raw evidence structure

evidence/
  BPE-001/
    OFF/
      prompt.txt
      output.txt
      telemetry.json
    ON/
      prompt.txt
      output.txt
      telemetry.json
  ...
  BPE-020/

The JSONL and CSV are intentionally ready for execution and contain blank measurements until real telemetry is captured.
