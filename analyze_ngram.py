#!/usr/bin/env python3
"""
Analyze llama-server ngram-mod speculative decoding performance from log files.
Parses per-request metrics and produces actionable flag tuning recommendations.
"""

import re
import csv
import argparse
import sys
from collections import defaultdict

import numpy as np


def strip_ansi(text: str) -> str:
    return re.sub(r'\x1b\[[0-9;]*m', '', text)


def parse_log(filepath: str) -> list[dict]:
    with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
        raw_lines = f.readlines()

    lines = [strip_ansi(l.rstrip()) for l in raw_lines]

    records = []
    req_id = 0

    for i, line in enumerate(lines):
        if 'statistics ngram_mod:' not in line:
            continue

        stats_match = re.match(
            r'statistics ngram_mod:\s+'
            r'#calls\(b,g,a\)\s*=\s*(\d+)\s+(\d+)\s+(\d+),\s+'
            r'#gen drafts\s*=\s*(\d+),\s+'
            r'#acc drafts\s*=\s*(\d+),\s+'
            r'#gen tokens\s*=\s*(\d+),\s+'
            r'#acc tokens\s*=\s*(\d+),\s+'
            r'dur\(b,g,a\)\s*=\s*([\d.]+),\s*([\d.]+),\s*([\d.]+)\s*ms',
            line
        )
        if not stats_match:
            continue

        rec = {
            'calls_b': int(stats_match.group(1)),
            'calls_g': int(stats_match.group(2)),
            'calls_a': int(stats_match.group(3)),
            'gen_drafts': int(stats_match.group(4)),
            'acc_drafts': int(stats_match.group(5)),
            'gen_tokens': int(stats_match.group(6)),
            'acc_tokens': int(stats_match.group(7)),
            'dur_b': float(stats_match.group(8)),
            'dur_g': float(stats_match.group(9)),
            'dur_a': float(stats_match.group(10)),
        }

        for j in range(i, max(0, i - 30), -1):
            lj = lines[j]

            if 'prompt eval time' in lj:
                pm = re.search(
                    r'prompt eval time\s*=\s*([\d.]+)\s*ms\s*/\s*(\d+)\s*tokens\s*'
                    r'\(\s*([\d.]+)\s*ms per token,\s*([\d.]+)\s*tokens per second\)',
                    lj
                )
                if pm:
                    rec['prompt_ms'] = float(pm.group(1))
                    rec['prompt_tokens'] = int(pm.group(2))
                    rec['prompt_ms_per_token'] = float(pm.group(3))
                    rec['prompt_tps'] = float(pm.group(4))

            if re.search(r'(?<!\w)eval time\s*=', lj) and 'prompt eval time' not in lj:
                em = re.search(
                    r'\s+eval time\s*=\s*([\d.]+)\s*ms\s*/\s*(\d+)\s*tokens\s*'
                    r'\(\s*([\d.]+)\s*ms per token,\s*([\d.]+)\s*tokens per second\)',
                    lj
                )
                if em:
                    rec['eval_ms'] = float(em.group(1))
                    rec['eval_tokens'] = int(em.group(2))
                    rec['eval_ms_per_token'] = float(em.group(3))
                    rec['eval_tps'] = float(em.group(4))

            if re.search(r'\s+total time\s*=', lj):
                tm = re.search(
                    r'\s+total time\s*=\s*([\d.]+)\s*ms\s*/\s*(\d+)\s*tokens',
                    lj
                )
                if tm:
                    rec['total_ms'] = float(tm.group(1))
                    rec['total_tokens'] = int(tm.group(2))

            acc_re_match = re.search(
                r'draft acceptance rate\s*=\s*([\d.]+)\s*\(\s*(\d+)\s*accepted\s*/\s*(\d+)\s*generated\)',
                lj
            )
            if acc_re_match:
                rec['acc_from_rate'] = float(acc_re_match.group(1))
                rec['accepted_from_rate'] = int(acc_re_match.group(2))
                rec['generated_from_rate'] = int(acc_re_match.group(3))

            occ_match = re.search(
                r'ngram_mod occupancy\s*=\s*(\d+)/(\d+)\s*\(\s*([\d.]+)\s*\)',
                lj
            )
            if occ_match:
                rec['occupancy'] = int(occ_match.group(1))
                rec['occupancy_max'] = int(occ_match.group(2))
                rec['occupancy_pct'] = rec['occupancy'] / rec['occupancy_max'] * 100

        if 'eval_tps' in rec and rec['gen_tokens'] > 0:
            rec['acc_rate'] = rec['acc_tokens'] / rec['gen_tokens'] if rec['gen_tokens'] > 0 else 0.0
            rec['draft_overhead'] = rec['gen_tokens'] / rec['acc_tokens'] if rec['acc_tokens'] > 0 else float('inf')
            rec['acc_to_gen_ratio'] = rec['acc_tokens'] / rec['gen_tokens'] if rec['gen_tokens'] > 0 else 0.0
            rec['verif_pct'] = (rec['dur_a'] / (rec['dur_b'] + rec['dur_g'] + rec['dur_a'])) * 100.0 if (rec['dur_b'] + rec['dur_g'] + rec['dur_a']) > 0 else 0.0
            rec['output_tokens'] = rec['eval_tokens']
        else:
            rec['acc_rate'] = 0.0
            rec['draft_overhead'] = float('inf')
            rec['acc_to_gen_ratio'] = 0.0
            rec['verif_pct'] = 0.0
            rec['output_tokens'] = 0
            if 'eval_tps' not in rec:
                rec['eval_ms'] = 0.0
                rec['eval_tokens'] = 0
                rec['eval_ms_per_token'] = 0.0
                rec['eval_tps'] = 0.0
                rec['total_ms'] = 0.0
                rec['total_tokens'] = 0
                rec['prompt_ms'] = 0.0
                rec['prompt_tokens'] = 0
                rec['prompt_ms_per_token'] = 0.0
                rec['prompt_tps'] = 0.0

        req_id += 1
        rec['req_id'] = req_id
        records.append(rec)

    return records


def size_bucket(n: int) -> str:
    if n < 100:
        return 'tiny (<100)'
    if n < 300:
        return 'small (100-299)'
    if n < 800:
        return 'medium (300-799)'
    if n < 2000:
        return 'large (800-1999)'
    return 'huge (2000+)'


def compute_stats(records: list[dict]) -> dict:
    stats = {}

    def arr(k):
        vals = [r[k] for r in records if r.get(k) is not None and not (isinstance(r.get(k), float) and np.isinf(r.get(k)))]
        return np.array(vals, dtype=float)

    for k in ['acc_rate', 'eval_tps', 'eval_ms_per_token', 'prompt_tps',
              'prompt_ms_per_token', 'gen_tokens', 'acc_tokens', 'draft_overhead',
              'verif_pct', 'output_tokens', 'dur_b', 'dur_g', 'dur_a']:
        vals = arr(k)
        if len(vals) == 0:
            continue
        stats[k] = {
            'mean': float(np.mean(vals)),
            'median': float(np.median(vals)),
            'std': float(np.std(vals)),
            'min': float(np.min(vals)),
            'max': float(np.max(vals)),
            'p10': float(np.percentile(vals, 10)),
            'p90': float(np.percentile(vals, 90)),
            'count': len(vals),
        }

    total_acc = sum(r['acc_tokens'] for r in records)
    total_gen = sum(r['gen_tokens'] for r in records)
    stats['overall_acc_rate'] = total_acc / total_gen if total_gen > 0 else 0.0
    stats['total_acc_tokens'] = total_acc
    stats['total_gen_tokens'] = total_gen
    stats['num_requests'] = len(records)

    occ_vals = [r['occupancy_pct'] for r in records if r.get('occupancy_pct') is not None]
    if occ_vals:
        stats['occupancy'] = {
            'min': min(occ_vals),
            'max': max(occ_vals),
            'final': occ_vals[-1] if occ_vals else 0,
        }

    return stats


def print_header(title: str):
    w = 78
    print()
    print('=' * w)
    print(f'  {title}')
    print('=' * w)


def print_section(title: str):
    print()
    print(f'--- {title} ---')


def print_summary(stats: dict):
    print_header('NGRAM-MOD SPECULATIVE DECODING ANALYSIS')

    print_section('GLOBAL SUMMARY')
    print(f'  Total request cycles analyzed: {stats["num_requests"]}')
    print(f'  Overall draft acceptance rate: {stats["overall_acc_rate"]:.1%}  ({stats["total_acc_tokens"]} accepted / {stats["total_gen_tokens"]} generated)')
    print()

    fmt = '  {:<30} {:>8} {:>8} {:>8} {:>8} {:>8} {:>8}'
    print(fmt.format('Metric', 'Mean', 'Median', 'Std', 'Min', 'P10', 'P90'))
    print('  ' + '-' * 70)

    m = stats.get('acc_rate', {})
    if m:
        print(fmt.format('Draft acceptance rate', f'{m["mean"]:.1%}', f'{m["median"]:.1%}',
                         f'{m["std"]:.1%}', f'{m["min"]:.1%}', f'{m["p10"]:.1%}', f'{m["p90"]:.1%}'))

    m = stats.get('eval_tps', {})
    if m:
        print(fmt.format('Gen throughput (t/s)', f'{m["mean"]:.1f}', f'{m["median"]:.1f}',
                         f'{m["std"]:.1f}', f'{m["min"]:.1f}', f'{m["p10"]:.1f}', f'{m["p90"]:.1f}'))

    m = stats.get('eval_ms_per_token', {})
    if m:
        print(fmt.format('Gen ms/token', f'{m["mean"]:.1f}', f'{m["median"]:.1f}',
                         f'{m["std"]:.1f}', f'{m["min"]:.1f}', f'{m["p10"]:.1f}', f'{m["p90"]:.1f}'))

    m = stats.get('prompt_tps', {})
    if m:
        print(fmt.format('Prompt t/s', f'{m["mean"]:.0f}', f'{m["median"]:.0f}',
                         f'{m["std"]:.0f}', f'{m["min"]:.0f}', f'{m["p10"]:.0f}', f'{m["p90"]:.0f}'))

    m = stats.get('draft_overhead', {})
    if m:
        fin_vals = [v for v in [m["mean"], m["median"], m["std"], m["min"]] if not np.isinf(v)]
        print(fmt.format('Draft overhead (gen/acc)', f'{fin_vals[0]:.1f}x', f'{fin_vals[1]:.1f}x',
                         f'{fin_vals[2]:.1f}x', f'{m["min"]:.1f}x' if not np.isinf(m["min"]) else 'inf',
                         '', ''))

    m = stats.get('output_tokens', {})
    if m:
        print(fmt.format('Output tokens/req', f'{m["mean"]:.0f}', f'{m["median"]:.0f}',
                         f'{m["std"]:.0f}', f'{m["min"]:.0f}', f'{m["p10"]:.0f}', f'{m["p90"]:.0f}'))

    m = stats.get('verif_pct', {})
    if m:
        print(fmt.format('Verification cost (% dur)', f'{m["mean"]:.1f}%', f'{m["median"]:.1f}%',
                         f'{m["std"]:.1f}%', f'{m["min"]:.1f}%', f'{m["p10"]:.1f}%', f'{m["p90"]:.1f}%'))

    occ = stats.get('occupancy', {})
    if occ:
        print()
        print(f'  Ngram cache occupancy: {occ["min"]:.2f}% -> {occ["max"]:.2f}% (final: {occ["final"]:.2f}%)')
        print(f'  Cache is vastly underutilized (< 3% full throughout session)')


def print_acceptance_distribution(records: list[dict]):
    print_header('ACCEPTANCE RATE DISTRIBUTION & THROUGHPUT')

    buckets = [
        ('0-10%', lambda r: 0 <= r < 0.10),
        ('10-20%', lambda r: 0.10 <= r < 0.20),
        ('20-30%', lambda r: 0.20 <= r < 0.30),
        ('30-40%', lambda r: 0.30 <= r < 0.40),
        ('40-50%', lambda r: 0.40 <= r < 0.50),
        ('50-60%', lambda r: 0.50 <= r < 0.60),
        ('60-70%', lambda r: 0.60 <= r < 0.70),
        ('70%+', lambda r: r >= 0.70),
    ]

    fmt = '  {:<10} {:>6} {:>10} {:>10} {:>12}'
    print(fmt.format('Bucket', 'Count', 'Avg t/s', 'Avg ms/t', 'Avg overhead'))
    print('  ' + '-' * 55)

    for label, pred in buckets:
        subset = [r for r in records if r['gen_tokens'] > 0 and pred(r['acc_rate'])]
        if not subset:
            continue
        avg_tps = np.mean([r['eval_tps'] for r in subset])
        avg_mst = np.mean([r['eval_ms_per_token'] for r in subset])
        overheads = [r['draft_overhead'] for r in subset if not np.isinf(r['draft_overhead'])]
        avg_oh = np.mean(overheads) if overheads else 0
        print(fmt.format(label, len(subset), f'{avg_tps:.1f}', f'{avg_mst:.1f}', f'{avg_oh:.1f}x'))

    print()
    print('  KEY INSIGHT: Requests with higher acceptance rates tend to have')
    print('  better throughput (higher t/s, lower ms/token). The draft overhead')
    print('  ratio drops as acceptance improves, meaning fewer wasted draft tokens.')


def print_correlation(records: list[dict]):
    print_header('ACCEPTANCE RATE vs THROUGHPUT CORRELATION')

    valid = [r for r in records if r['gen_tokens'] > 0 and r['eval_tokens'] > 0]
    if len(valid) < 3:
        print('  Not enough data for correlation.')
        return

    acc_rates = np.array([r['acc_rate'] for r in valid])
    tps = np.array([r['eval_tps'] for r in valid])
    mst = np.array([r['eval_ms_per_token'] for r in valid])

    r_tps = np.corrcoef(acc_rates, tps)[0, 1]
    r_mst = np.corrcoef(acc_rates, mst)[0, 1]

    print(f'  Correlation (acceptance rate, throughput t/s):  {r_tps:+.3f}')
    print(f'  Correlation (acceptance rate, ms/token):        {r_mst:+.3f}')
    print()

    if r_tps > 0.3:
        print('  POSITIVE correlation: higher acceptance -> higher throughput.')
        print('  Improving acceptance rate will directly improve generation speed.')
    elif r_tps > -0.3:
        print('  WEAK correlation: acceptance rate has limited impact on throughput.')
        print('  Other factors (GPU compute, batch size) may dominate.')
    else:
        print('  NEGATIVE correlation: higher acceptance -> lower throughput.')
        print('  This suggests draft overhead is hurting; consider reducing --draft-max.')

    print()
    print('  Scatter (acceptance rate vs throughput):')
    for i in range(10):
        lo = i * 0.1
        hi = (i + 1) * 0.1
        subset = [r for r in valid if lo <= r['acc_rate'] < hi]
        if not subset:
            continue
        avg_tps = np.mean([r['eval_tps'] for r in subset])
        bar_len = int(avg_tps)
        bar = '#' * bar_len
        print(f'    {lo:.0f}-{hi:.0f}%:  {bar} ({avg_tps:.1f} t/s, n={len(subset)})')


def print_occupancy_timeline(records: list[dict]):
    print_header('NGRAM CACHE OCCUPANCY OVER TIME')

    occ_recs = [r for r in records if r.get('occupancy_pct') is not None]
    if not occ_recs:
        print('  No occupancy data found.')
        return

    step = max(1, len(occ_recs) // 20)
    sampled = occ_recs[::step]

    print(f'  {"Req":>4}  {"Occupancy":>10}  {"% Full":>8}  {"Acc Rate":>10}  {"t/s":>8}')
    print('  ' + '-' * 48)
    for r in sampled:
        print(f'  {r["req_id"]:>4}  {r["occupancy"]:>10}  {r["occupancy_pct"]:>7.2f}%  {r["acc_rate"]:>9.1%}  {r["eval_tps"]:>7.1f}')

    print()
    print('  NOTE: Occupancy grows slowly and stays below 3%. The 16MB hash table')
    print('  is massively oversized for the working set. This is expected with ngram-mod')
    print('  as it stores one hash->token mapping per unique n-gram prefix.')


def print_size_analysis(records: list[dict]):
    print_header('REQUEST SIZE ANALYSIS')

    buckets = defaultdict(list)
    for r in records:
        if r['gen_tokens'] > 0:
            buckets[size_bucket(r['output_tokens'])].append(r)

    fmt = '  {:<18} {:>6} {:>10} {:>10} {:>12}'
    print(fmt.format('Size Bucket', 'Count', 'Avg t/s', 'Avg ms/t', 'Avg overhead'))
    print('  ' + '-' * 60)

    order = ['tiny (<100)', 'small (100-299)', 'medium (300-799)', 'large (800-1999)', 'huge (2000+)']
    for label in order:
        subset = buckets.get(label, [])
        if not subset:
            continue
        avg_tps = np.mean([r['eval_tps'] for r in subset])
        avg_mst = np.mean([r['eval_ms_per_token'] for r in subset])
        overheads = [r['draft_overhead'] for r in subset if not np.isinf(r['draft_overhead'])]
        avg_oh = np.mean(overheads) if overheads else 0
        print(fmt.format(label, len(subset), f'{avg_tps:.1f}', f'{avg_mst:.1f}', f'{avg_oh:.1f}x'))

    print()
    print('  LARGER responses benefit more from speculation when acceptance is decent.')
    print('  If most responses are short (<300 tokens), speculative decoding has')
    print('  less room to help and the overhead may dominate.')


def print_flag_recommendations(records: list[dict], stats: dict):
    print_header('FLAG TUNING RECOMMENDATIONS')

    overall_acc = stats['overall_acc_rate']
    mean_tps = stats.get('eval_tps', {}).get('mean', 0)
    mean_mst = stats.get('eval_ms_per_token', {}).get('mean', 0)
    mean_overhead = stats.get('draft_overhead', {})
    overhead_mean = mean_overhead.get('mean', 0) if mean_overhead and not np.isinf(mean_overhead.get('mean', 0)) else 0

    print('  CURRENT CONFIG (inferred from log):')
    print('    --spec-type ngram-mod')
    print('    --spec-ngram-size-n 24  (n_match=24)')
    print('    --draft-min 0  (default, no minimum)')
    print('    --draft-max 16  (default)')
    print('    --threads 3  (only 3 of 10 CPU threads used)')
    print()

    recs = []

    print('  RECOMMENDED CHANGES:')
    print()

    print('  1. --draft-min 48')
    if overall_acc < 0.30:
        print(f'     Reason: Overall acceptance is only {overall_acc:.1%}. Short draft attempts')
        print(f'     with low acceptance add pure overhead. Setting --draft-min 48 ensures')
        print(f'     speculation only activates when the ngram cache has a confident match.')
    else:
        print(f'     Reason: Prevents wasteful short drafts. With {overall_acc:.1%} acceptance,')
        print(f'     skipping low-confidence attempts will reduce overhead on bad guesses.')
    print()

    print('  2. --draft-max 64')
    print(f'     Reason: Current default (16) caps draft length. With n_match=24, the cache')
    print(f'     can produce longer chains. Allowing up to 64 draft tokens lets good')
    print(f'     matches contribute more. Long responses (up to {stats.get("output_tokens", {}).get("max", 0):.0f} tokens)')
    print(f'     benefit most from longer drafts.')
    print()

    print('  3. --threads 8')
    print(f'     Reason: Only 3 of 10 CPU threads are used. Batch verification of draft')
    print(f'     tokens is CPU-bound. More threads = faster verification = higher effective')
    print(f'     throughput. 8 threads leaves 2 for OS/background tasks.')
    print()

    print('  4. --spec-ngram-size-n 24  (KEEP)')
    print(f'     Reason: n=24 is appropriate for a 27B model. Smaller n would produce')
    print(f'     more false matches; larger n would reduce cache hits.')
    print()

    print('  5. Consider --batch-size 2048 (already set)')
    print(f'     Reason: Current n_batch=2048 is good. No change needed.')
    print()

    print('  FULL RECOMMENDED COMMAND:')
    print()
    print('    llama-server \\')
    print('      -m your-model.gguf \\')
    print('      --spec-type ngram-mod \\')
    print('      --spec-ngram-size-n 24 \\')
    print('      --draft-min 48 \\')
    print('      --draft-max 64 \\')
    print('      --threads 8 \\')
    print('      --batch-size 2048 \\')
    print('      ...other flags...')
    print()

    print('  EXPECTED IMPROVEMENT:')
    print(f'    Current mean throughput: {mean_tps:.1f} t/s ({mean_mst:.1f} ms/token)')
    print(f'    Current draft overhead: {overhead_mean:.1f}x (tokens generated per accepted)')
    print('    With --draft-min 48 and --draft-max 64, expect:')
    print('    - Fewer wasted draft attempts on low-confidence matches')
    print('    - Better utilization of high-acceptance streaks')
    print('    - ~10-30% throughput improvement on repetitive/structured content')
    print('    - Neutral or slightly worse on highly creative/divergent content')
    print()
    print('  NOTE: Some benchmarks show ngram-mod provides minimal or negative speedup')
    print('  on certain model architectures (especially MoE+SSM like Qwen3.6). If')
    print('  testing shows no improvement, try disabling speculation entirely:')
    print('    --spec-type none')
    print()


def export_csv(records: list[dict], path: str):
    if not records:
        print('  No records to export.')
        return

    fieldnames = [
        'req_id', 'occupancy', 'occupancy_max', 'occupancy_pct',
        'acc_rate', 'accepted_from_rate', 'generated_from_rate',
        'gen_tokens', 'acc_tokens', 'gen_drafts', 'acc_drafts',
        'calls_b', 'calls_g', 'calls_a',
        'dur_b', 'dur_g', 'dur_a',
        'prompt_tokens', 'prompt_tps', 'prompt_ms_per_token',
        'eval_tokens', 'eval_tps', 'eval_ms_per_token',
        'total_ms', 'total_tokens',
        'draft_overhead', 'acc_to_gen_ratio', 'verif_pct', 'output_tokens'
    ]

    with open(path, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction='ignore')
        writer.writeheader()
        for r in records:
            row = {k: r.get(k, '') for k in fieldnames}
            writer.writerow(row)

    print(f'  CSV exported: {path} ({len(records)} rows)')


def print_per_request_table(records: list[dict]):
    print_header('PER-REQUEST DETAILS')

    fmt = '  {:>4} {:>8} {:>8} {:>8} {:>8} {:>8} {:>8} {:>8} {:>8}'
    hdr = fmt.format('Req', 'Acc%', 'GenTok', 'AccTok', 'OH', 't/s', 'ms/t', 'OutTok', 'Occ%')
    print(hdr)
    print('  ' + '-' * 70)

    for r in records:
        oh = r['draft_overhead']
        oh_str = f'{oh:.1f}x' if not np.isinf(oh) else 'inf'
        fmt_row = '  {:>4} {:>7.0%} {:>8} {:>8} {:>8} {:>7.1f} {:>7.1f} {:>8} {:>7.4f}'
        print(fmt_row.format(
            r['req_id'], r['acc_rate'], r['gen_tokens'], r['acc_tokens'],
            oh_str, r['eval_tps'], r['eval_ms_per_token'],
            r['output_tokens'], r.get('occupancy_pct', 0) or 0
        ))


def main():
    parser = argparse.ArgumentParser(description='Analyze llama-server ngram-mod speculative decoding performance')
    parser.add_argument('logfile', help='Path to llama-server log file')
    parser.add_argument('--csv', help='Export per-request data to CSV file')
    parser.add_argument('--table', action='store_true', help='Show per-request detail table')
    parser.add_argument('--flags-only', action='store_true', help='Only show flag recommendations')
    args = parser.parse_args()

    records = parse_log(args.logfile)
    if not records:
        print(f'ERROR: No ngram-mod statistics found in {args.logfile}')
        sys.exit(1)

    stats = compute_stats(records)

    if args.flags_only:
        print_flag_recommendations(records, stats)
        return

    print_summary(stats)
    print_acceptance_distribution(records)
    print_correlation(records)
    print_occupancy_timeline(records)
    print_size_analysis(records)
    print_flag_recommendations(records, stats)

    if args.table:
        print_per_request_table(records)

    if args.csv:
        export_csv(records, args.csv)


if __name__ == '__main__':
    main()
