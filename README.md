# llama.cpp Ngram-Mod Speculative Decoding Analysis

> Data-driven flag tuning and performance analysis for ngram-mod speculative decoding on Qwen3.6-27B (AMD Radeon AI PRO R9700).

## Overview

This repository contains analysis scripts and log data for evaluating **ngram-mod speculative decoding** performance in [llama.cpp](https://github.com/ggerganov/llama.cpp). It parses `llama-server` logs, computes throughput/acceptance statistics, and produces flag tuning recommendations.

### Hardware & Model

| | |
|---|---|
| **GPU** | AMD Radeon AI PRO R9700 (Vulkan RADV GFX1201) |
| **Model** | Qwen3.6-27B-UD-Q4_K_XL |
| **Spec type** | `ngram-mod` |

### Baseline (No Speculation)

| Metric | Value |
|---|---|
| Generation throughput | **21 tok/s** |
| Prompt processing | ~350 pps |

---

## Scripts

### `analyze_ngram_v2.py` — Main analysis (recommended)

Parses llama-server logs (b8967+ bare timing format), computes per-request and aggregate statistics, and outputs flag tuning recommendations.

```bash
python3 analyze_ngram_v2.py <logfile.txt> --baseline-tps 21.0 --baseline-pps 350.0
```

**Output sections:**
- **Global Summary** — Overall acceptance rate, throughput (mean/median/std/min/P10/P90), draft overhead, verification cost, cache occupancy
- **Baseline Comparison** — Delta vs no-speculation baseline
- **Acceptance Rate Distribution** — Throughput per 10% acceptance bucket
- **Correlation** — Pearson correlation between acceptance rate and throughput (with ASCII scatter plot)
- **Cache Occupancy Timeline** — Sampled ngram hash table fill rate over requests
- **Request Size Analysis** — Throughput by output token size bucket
- **Flag Tuning Recommendations** — Inferred current config and suggested changes

**Options:**

| Flag | Description |
|---|---|
| `--csv <path>` | Export per-request data to CSV |
| `--table` | Show per-request detail table |
| `--flags-only` | Only display flag recommendations |
| `--baseline-tps <float>` | Baseline gen throughput without spec (default: 21.0) |
| `--baseline-pps <float>` | Baseline prompt throughput without spec (default: 350.0) |

**Example — CSV export:**

```bash
python3 analyze_ngram_v2.py raw_total.txt --baseline-tps 21.0 --baseline-pps 350.0 --csv output.csv
```

**Example — Flags-only:**

```bash
python3 analyze_ngram_v2.py raw_total.txt --flags-only --baseline-tps 21.0
```

---

### `analyze_ngram.py` — Legacy script (b9009 task-prefixed format)

Same functionality as `analyze_ngram_v2.py` but parses the older b9009 log format (task-prefixed timing lines). Use this for older llama-server builds.

```bash
python3 analyze_ngram.py <logfile.txt> --csv output.csv --table
```

---

### `parse_perf_histo.py` — ASCII Histogram Generator

Parses raw log files and produces ASCII histograms for prompt processing speed (PPS) and token generation throughput (Tok/s), with **token-weighted harmonic mean** for a more accurate effective average.

```bash
python3 parse_perf_histo.py
```

Reads `raw_total.txt` by default. Update the filename in the script to analyze a different log.

**Key metrics:**
- **Token-weighted harmonic mean** — `total_tokens / total_time_seconds`, preferred over simple mean for throughput
- **Median (P50)** — 50th percentile
- **Tail (P99)** — 99th percentile
- **Stability (CV)** — Coefficient of variation; <10% = stable, >10% = jittery
- **Skewness** — Distribution shape (symmetric / slow-end heavy / burst heavy)

**Histogram binning:**
- PPS — Auto-binned (10 bins)
- Tok/s — Custom multi-resolution bins (0.5 res from 18-42, 5 res from 42-130)

---

## CSV Output Schema

Both analyzers export the same CSV columns:

| Column | Description |
|---|---|
| `req_id` | Request sequence number |
| `occupancy` / `occupancy_max` / `occupancy_pct` | Ngram hash table entries / capacity / fill % |
| `acc_rate` | Draft acceptance rate (acc_tokens / gen_tokens) |
| `accepted_from_rate` / `generated_from_rate` | Acceptance from `draft acceptance rate` log line |
| `gen_tokens` / `acc_tokens` | Draft tokens generated / accepted |
| `gen_drafts` / `acc_drafts` | Draft attempts generated / accepted |
| `calls_b` / `calls_g` / `calls_a` | Pre-fill / gen / verification call counts |
| `dur_b` / `dur_g` / `dur_a` | Pre-fill / gen / verification duration (ms) |
| `prompt_tokens` / `prompt_tps` / `prompt_ms_per_token` | Prompt processing stats |
| `eval_tokens` / `eval_tps` / `eval_ms_per_token` | Generation (eval) stats |
| `total_ms` / `total_tokens` | Total request time and token count |
| `draft_overhead` | gen_tokens / acc_tokens (lower is better) |
| `acc_to_gen_ratio` | Same as `acc_rate` |
| `verif_pct` | Verification cost as % of total duration |
| `output_tokens` | Generation output tokens (= eval_tokens) |

---

## Sample Data

| Dataset | Build | Requests | Acceptance | Gen Throughput |
|---|---|---|---|---|
| `raw_total.txt` | b8967 | 797 | 46.5% | 26.9 t/s (+28.3%) |
| `raw_log_b9009.txt` | b9009 | 45 | 24.6% | 25.6 t/s (+21.8%) |

CSV exports: `ngram_total.csv` (797 rows), `ngram_analysis.csv` (45 rows).

---

## Current Tuned Config

```bash
llama-server \
  -m your-model.gguf \
  --spec-type ngram-mod \
  --spec-ngram-size-n 24 \
  --draft-min 48 \
  --draft-max 64 \
  --threads 10 \
  --batch-size 2048 \
  ...other flags...
```

### Flag Rationale

| Flag | Value | Why |
|---|---|---|
| `--spec-ngram-size-n` | 24 | Appropriate for 27B model; smaller = more false matches, larger = fewer hits |
| `--draft-min` | 48 | Eliminates wasteful short draft attempts with low confidence |
| `--draft-max` | 64 | Allows longer chains for responses up to 18K tokens |
| `--threads` | 10 | Maxed out (CPU-side work only; GPU is the bottleneck) |
| `--batch-size` | 2048 | Good default for batch verification |

---

## How It Works

1. **Parse** — Scans log for `statistics ngram_mod:` lines and associated timing lines (within 30 lines prior)
2. **Compute** — Derives acceptance rate, draft overhead, verification cost, and per-request throughput
3. **Analyze** — Groups by acceptance bucket and size bucket; computes Pearson correlation
4. **Recommend** — Suggests flag changes based on overall acceptance rate and current distribution

Verification cost is GPU memory-bandwidth bound, not CPU-bound. The `--draft-min` and `--draft-max` flags are the primary tuning knobs for reducing wasted verification passes.

---

## Requirements

- Python 3.11+
- `numpy` (for `analyze_ngram*.py`)

```bash
pip install numpy
```
