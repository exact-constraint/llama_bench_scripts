# Llama.cpp Ngram-Mod Analysis Session

## Goal
Analyze llama-server ngram-mod speculative decoding performance from log files and provide data-driven flag tuning recommendations for Qwen3.6-27B on AMD Radeon AI PRO R9700.

## Workspace Files
- `analyze_ngram.py` — Original script for b9009 log format (task-prefixed timing lines)
- `analyze_ngram_v2.py` — Updated script for b8967+ log format (bare timing lines), includes baseline comparison
- `parse_perf_histo.py` — Updated to parse raw_total.txt, outputs ASCII histograms with token-weighted harmonic mean
- `raw_log_b9009.txt` — Build b9009 log, 45 request cycles (smaller sample, newer build)
- `raw_total.txt` — Build b8967 log, 797 request cycles (larger sample, older build)
- `ngram_analysis.csv` — CSV export from b9009 log (45 rows)
- `ngram_total.csv` — CSV export from b8967 log (797 rows)

## Baseline (No Speculation)
- Generation: **21 tok/s**
- Prompt processing: **~350 pps**
- Model: Qwen3.6-27B-UD-Q4_K_XL on AMD Radeon AI PRO R9700 (Vulkan RADV GFX1201)

## Key Findings

### raw_total.txt (b8967, 797 requests)
| Metric | Value |
|--------|-------|
| Overall draft acceptance | 46.5% (7.27M acc / 15.65M gen) |
| Gen throughput | 26.9 t/s mean, 24.9 t/s median |
| Token-weighted harmonic mean | 26.0 t/s |
| Gen gain vs baseline | **+28.3%** |
| Draft overhead | 2.5x (gen/acc ratio) |
| Verification cost | 2.4% of ngram duration |
| Cache occupancy | 0.45% → 4.46% (16MB table, vastly underutilized) |
| Acceptance ↔ throughput correlation | +0.140 (weak) |
| Distribution skew | 5.86 (burst-heavy, CV 37%) |
| P50 / P90 throughput | 24.9 / 33.6 t/s |

### raw_log_b9009.txt (b9009, 45 requests)
| Metric | Value |
|--------|-------|
| Overall draft acceptance | 24.6% (40K acc / 164K gen) |
| Gen throughput | 25.6 t/s mean |
| Gen gain vs baseline | **+21.8%** |
| Draft overhead | 4.4x (nearly 2x worse than b8967) |
| Verification cost | 2.6% |
| Cache occupancy | 0.53% → 2.99% |
| Acceptance ↔ throughput correlation | -0.216 (weak/negative) |

### Cross-Build Observations
- b8967 has nearly 2x higher acceptance rate (46.5% vs 24.6%) but similar gen throughput
- b9009 base engine is faster, compensating for worse speculation quality
- Acceptance rate has weak correlation with throughput in both builds — GPU compute is the dominant factor
- 40-50% acceptance bucket is largest (349 of 797 requests) with flat ~26 t/s throughput
- 70%+ acceptance bucket averages 32.5 t/s but only 41 samples

## Current Config (After Tuning)
```
--spec-type ngram-mod
--spec-ngram-size-n 24
--draft-min 48
--draft-max 64
--threads 10  (maxed, though benefit is limited — GPU is the bottleneck)
--batch-size 2048
```

## Verified Facts
- Batch verification is **GPU memory-bandwidth bound**, NOT CPU-bound (confirmed via llama.cpp docs, DeepWiki)
- `--threads` affects CPU-side work (tokenization, preprocessing, HTTP overhead) — limited impact when model is fully on GPU
- `--draft-min 48` and `--draft-max 64` are the meaningful tuning knobs: they reduce wasted GPU verification passes
- Ngram-mod is providing real ~25% gain on this hardware/model combo

## Recommendations from Session
1. **`--draft-min 48`** — Applied. Eliminates wasteful short draft attempts.
2. **`--draft-max 64`** — Applied. Allows longer chains for responses up to 18K tokens.
3. **`--threads 10`** — Applied, but expect marginal benefit (GPU-bound workload).
4. **`--spec-ngram-size-n 24`** — Kept. Appropriate for 27B model.

## Next Steps (When More Data Available)
- Compare new logs with tuned flags vs current baselines
- Track whether `--draft-min 48` improved acceptance rate distribution (reduced 0-30% bucket)
- Monitor whether `--draft-max 64` improved throughput on long responses (800+ tokens)
- Look for shift in acceptance distribution toward higher buckets
- Re-run `analyze_ngram_v2.py <new_log.txt> --baseline-tps 21.0 --baseline-pps 350.0`
- Re-run `parse_perf_histo.py` (update filename if needed)
- Target: push mean throughput from ~27 t/s toward 30+ t/s

## Script Usage
```bash
# Full analysis with baseline comparison
python3 analyze_ngram_v2.py <logfile.txt> --baseline-tps 21.0 --baseline-pps 350.0 --csv output.csv

# Histogram analysis (update filename in script if needed)
python3 parse_perf_histo.py

# Flags-only summary
python3 analyze_ngram_v2.py <logfile.txt> --flags-only --baseline-tps 21.0
```

## Session Date
May 2, 2026
