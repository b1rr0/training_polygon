import time

def compute_lps(pattern):
    """
    Compute the Longest Proper Prefix which is also Suffix (LPS) array
    """
    m = len(pattern)
    lps = [0] * m
    length = 0
    i = 1
    
    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    
    return lps

def kmp_search(text, pattern):
    """
    KMP (Knuth-Morris-Pratt) string search algorithm
    Time Complexity: O(n + m)
    Space Complexity: O(m)
    """
    n = len(text)
    m = len(pattern)
    
    if m == 0:
        return 0
    if m > n:
        return -1
    
    lps = compute_lps(pattern)
    
    i = 0  # index for text
    j = 0  # index for pattern
    
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
        
        if j == m:
            return i - j  # Found at index i-j
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    
    return -1


def print_lps_table(pattern, lps):
    """Print a visual representation of the LPS array"""
    print("LPS Array computation:")
    print("Pattern: " + " ".join(pattern))
    print("Index:   " + " ".join(str(i) for i in range(len(pattern))))
    print("LPS:     " + " ".join(str(x) for x in lps))

def main():
    test_cases = [
        ("ABABDABACDABABCABCABCABCABC", "ABABCAB"),
        ("Hello World Hello", "Hello"),
        ("AAAAAAA", "AAA"),
        ("ABABABAB", "ABAB"),
        ("The quick brown fox jumps over the lazy dog", "fox")
    ]
    
    print("=== KMP String Search Algorithm ===\n")
    
    for i, (text, pattern) in enumerate(test_cases, 1):
        print(f"Test {i}:")
        print(f"Text: \"{text}\"")
        print(f"Pattern: \"{pattern}\"")
        
        # Compute and display LPS array
        lps = compute_lps(pattern)
        print_lps_table(pattern, lps)
        
        # Measure time for first occurrence
        start_time = time.perf_counter()
        first_occurrence = kmp_search(text, pattern)
        end_time = time.perf_counter()
        
        if first_occurrence != -1:
            print(f"First occurrence at index: {first_occurrence}")
            
            # Show the found substring
            found_substring = text[first_occurrence:first_occurrence + len(pattern)]
            print(f"Found substring: \"{found_substring}\"")
        else:
            print("Pattern not found")
        
        print(f"Time taken: {(end_time - start_time) * 1000000:.3f} microseconds")
        print("-" * 50)
        print()

def demonstrate_kmp_advantage():
    """Demonstrate where KMP shows its advantage over naive approach"""
    print("=== KMP Advantage Demonstration ===\n")
    
    # Case where KMP performs better than naive
    text = "ABABCABABABCABABABCAB" * 100  # Long text with repetitive pattern
    pattern = "ABABCAB"
    
    print(f"Text length: {len(text)}")
    print(f"Pattern: \"{pattern}\"")
    print(f"Text preview: \"{text[:50]}...\"")
    
    # Time naive approach
    from naive_search import naive_search
    start_time = time.perf_counter()
    naive_result = naive_search(text, pattern)
    naive_time = time.perf_counter() - start_time
    
    # Time KMP approach
    start_time = time.perf_counter()
    kmp_result = kmp_search(text, pattern)
    kmp_time = time.perf_counter() - start_time
    
    print(f"Naive result: {naive_result}, Time: {naive_time * 1000000:.3f} μs")
    print(f"KMP result: {kmp_result}, Time: {kmp_time * 1000000:.3f} μs")
    
    if naive_time > 0:
        speedup = naive_time / kmp_time
        print(f"KMP speedup: {speedup:.2f}x faster")

if __name__ == "__main__":
    main()
    try:
        demonstrate_kmp_advantage()
    except ImportError:
        print("Note: naive_search.py not found, skipping performance comparison")