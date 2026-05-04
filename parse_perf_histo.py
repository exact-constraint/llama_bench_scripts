import re
import statistics
import math

def calculate_percentile(data, p):
    if not data: return 0
    sorted_data = sorted(data)
    idx = (len(sorted_data) - 1) * p
    return sorted_data[int(math.floor(idx))] + (sorted_data[int(math.ceil(idx))] - sorted_data[int(math.floor(idx))]) * (idx % 1)

def parse_llama_logs(file_path):
    prompt_pattern = re.compile(
        r"prompt eval time\s+=\s+([\d.]+)\s+ms\s+/\s+(\d+)\s+tokens\s+\(\s+[\d.]+\s+ms per token,\s+([\d.]+)\s+tokens per second\)"
    )
    eval_pattern = re.compile(
        r"(?<!\w)eval time\s+=\s+([\d.]+)\s+ms\s+/\s+(\d+)\s+tokens\s+\(\s+[\d.]+\s+ms per token,\s+([\d.]+)\s+tokens per second\)"
    )
    data = []
    try:
        with open(file_path, 'r') as f:
            lines = f.readlines()

        pending_prompt = None
        for line in lines:
            stripped = re.sub(r'\x1b\[[0-9;]*m', '', line.strip())

            pm = prompt_pattern.search(stripped)
            if pm:
                pending_prompt = {
                    "p_ms": float(pm.group(1)),
                    "prompt_tokens": int(pm.group(2)),
                    "pps": float(pm.group(3))
                }
                continue

            if 'eval time' in stripped and 'prompt eval time' not in stripped:
                em = eval_pattern.search(stripped)
                if em and pending_prompt:
                    data.append({
                        "pps": pending_prompt["pps"],
                        "tok_s": float(em.group(3)),
                        "tokens": int(em.group(2)),
                        "g_ms": float(em.group(1)),
                        "prompt_tokens": pending_prompt["prompt_tokens"],
                        "p_ms": pending_prompt["p_ms"]
                    })
                    pending_prompt = None
            else:
                pending_prompt = None
    except FileNotFoundError: return []
    return data

def print_terminal_histogram(data, custom_edges=None, bins=None, step_size=None, min_bound=None, max_width=40):
    """Draws an ASCII histogram. Uses custom_edges if provided, otherwise auto-bins."""
    if not data: return
    
    # === CUSTOM BIN EDGES LOGIC ===
    if custom_edges:
        counts = [0] * (len(custom_edges) - 1)
        
        for v in data:
            if v < custom_edges[0]:
                counts[0] += 1
            elif v >= custom_edges[-1]:
                counts[-1] += 1
            else:
                for i in range(len(custom_edges) - 1):
                    if custom_edges[i] <= v < custom_edges[i+1]:
                        counts[i] += 1
                        break
                        
        max_count = max(counts) if counts else 0
        
        print("\n  Distribution:")
        for i in range(len(custom_edges) - 1):
            bin_start = custom_edges[i]
            bin_end = custom_edges[i+1]
            count = counts[i]
            bar_len = int((count / max_count) * max_width) if max_count > 0 else 0
            bar = '█' * bar_len
            print(f"  {bin_start:>8.2f} - {bin_end:>8.2f} | {bar} ({count})")
        return

    # === STANDARD AUTO-BIN LOGIC (Used for PPS) ===
    actual_min, max_val = min(data), max(data)
    min_val = min_bound if min_bound is not None else actual_min
    
    if min_val == max_val:
        print(f"  {min_val:>8.2f} | {'█' * max_width} ({len(data)})")
        return

    if step_size:
        bin_width = float(step_size)
        bins = max(1, math.ceil((max_val - min_val) / bin_width))
    else:
        bins = bins if bins else 10
        bin_width = (max_val - min_val) / bins
        
    counts = [0] * bins
    
    for v in data:
        if v < min_val:
            idx = 0
        else:
            idx = int((v - min_val) / bin_width)
        if idx >= bins: 
            idx = bins - 1
        counts[idx] += 1
        
    max_count = max(counts)
    
    print("\n  Distribution:")
    for i in range(bins):
        bin_start = min_val + i * bin_width
        bin_end = min_val + (i + 1) * bin_width
        bar_len = int((counts[i] / max_count) * max_width) if max_count > 0 else 0
        bar = '█' * bar_len
        print(f"  {bin_start:>8.2f} - {bin_end:>8.2f} | {bar} ({counts[i]})")


def analyze(label, values, weights=None, custom_edges=None, step_size=None, min_bound=None):
    if not values: return
    mean = statistics.mean(values)
    std_dev = statistics.stdev(values) if len(values) > 1 else 0
    cv = (std_dev / mean) * 100 if mean > 0 else 0
    p99 = calculate_percentile(values, 0.99)
    
    skew = sum((x - mean)**3 for x in values) / (len(values) * std_dev**3) if len(values) > 2 and std_dev > 0 else 0
    skew_type = "Symmetric" if abs(skew) < 0.5 else ("Slow-End Heavy" if skew < 0 else "Burst Heavy")

    # --- THE FIX IS HERE ---
    if weights:
        # Calculate Weighted Harmonic Mean (Total Tokens / Total Time)
        # w = tokens, v = tokens/sec. Time = w/v.
        total_tokens = sum(weights)
        total_time_seconds = sum(w / v for v, w in zip(values, weights) if v > 0)
        effective_avg = total_tokens / total_time_seconds if total_time_seconds > 0 else 0
        avg_label = "(Token-Weighted Harmonic Mean)"
    else:
        effective_avg = mean
        avg_label = "(Simple Mean)"
    # -----------------------

    print(f"\n== {label} Analysis ==")
    print(f"Effective Avg: {effective_avg:>10.2f} t/s {avg_label}")
    print(f"Median (P50):  {statistics.median(values):>10.2f} t/s")
    print(f"Tail (P99):    {p99:>10.2f} t/s")
    print(f"Stability(CV): {cv:>10.1f}% {'(STABLE)' if cv < 10 else '(JITTERY)'}")
    print(f"Skewness:      {skew:>10.2f} ({skew_type})")
    
    # Print the histogram
    print_terminal_histogram(values, custom_edges=custom_edges, step_size=step_size, min_bound=min_bound)


results = parse_llama_logs("raw_total.txt")
if results:
    # 1. Analyze PPS with auto-binning
    analyze("Prompt Processing (PPS)", [r['pps'] for r in results])
    
    # 2. Build the custom edges for Token Generation
    tok_edges = [15.0, 18.0]
    
    # 0.5 resolution between 18 and 42
    curr = 18.0
    while curr < 42.0:
        curr = round(curr + 0.5, 2)
        tok_edges.append(curr)
        
    # 5 point resolution from 42 to 130
    curr = 42.0
    while curr < 130.0:
        curr = round(curr + 5.0, 2)
        tok_edges.append(curr)
        
    # 3. Analyze Token Generation with custom binning
    analyze("Token Generation (Tok/s)", [r['tok_s'] for r in results], [r['tokens'] for r in results], custom_edges=tok_edges)
else:
    print("No logs found. Please check if 'raw_total.txt' exists in the directory.")
