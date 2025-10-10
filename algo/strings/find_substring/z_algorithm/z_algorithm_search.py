import time

def compute_z_array(s):
    """
    Compute Z array for string s
    Z[i] = length of the longest substring starting from s[i] which is also a prefix of s
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    n = len(s)
    z = [0] * n
    l, r = 0, 0
    
    for i in range(1, n):
        if i <= r:
            z[i] = min(r - i + 1, z[i - l])
        
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        
        if i + z[i] - 1 > r:
            l, r = i, i + z[i] - 1
    
    return z

def z_algorithm_search(text, pattern):
    """
    Z Algorithm string search
    Time Complexity: O(n + m)
    Space Complexity: O(n + m)
    """
    if not pattern:
        return 0
    if not text or len(pattern) > len(text):
        return -1
    
    # Create combined string: pattern + $ + text
    combined = pattern + "$" + text
    z_array = compute_z_array(combined)
    pattern_length = len(pattern)
    
    # Look for Z values equal to pattern length
    for i in range(pattern_length + 1, len(combined)):
        if z_array[i] == pattern_length:
            return i - pattern_length - 1  # Convert to text index
    
    return -1


def print_z_array(s, z_array):
    """Print a visual representation of the Z array"""
    print(f"String: {s}")
    print("Index:  " + " ".join(f"{i:2}" for i in range(len(s))))
    print("Char:   " + " ".join(f"{c:2}" for c in s))
    print("Z[i]:   " + " ".join(f"{z:2}" for z in z_array))

def visualize_z_computation(s):
    """Show step-by-step Z array computation"""
    n = len(s)
    z = [0] * n
    l, r = 0, 0
    
    print(f"Computing Z array for: '{s}'")
    print("=" * 50)
    
    for i in range(1, n):
        print(f"\nStep {i}: Processing position {i} (character '{s[i]}')")
        print(f"Current l={l}, r={r}")
        
        old_z_i = z[i]
        
        if i <= r:
            z[i] = min(r - i + 1, z[i - l])
            print(f"i <= r, so Z[{i}] = min({r - i + 1}, Z[{i - l}]) = min({r - i + 1}, {z[i - l]}) = {z[i]}")
        else:
            print(f"i > r, so Z[{i}] starts at 0")
        
        # Extend Z[i]
        extensions = 0
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            print(f"  Extending: s[{z[i]}]='{s[z[i]]}' == s[{i + z[i]}]='{s[i + z[i]]}'")
            z[i] += 1
            extensions += 1
        
        if extensions == 0:
            print(f"  No extension possible")
        
        # Update l and r if necessary
        if i + z[i] - 1 > r:
            old_l, old_r = l, r
            l, r = i, i + z[i] - 1
            print(f"  Updated l={l}, r={r} (was l={old_l}, r={old_r})")
        
        print(f"Final Z[{i}] = {z[i]}")
        print("Current Z array:", z[:i+1])
    
    return z

def main():
    test_cases = [
        ("ABABDABACDABABCABCABCABCABC", "ABABCAB"),
        ("Hello World Hello", "Hello"),
        ("AAAAAAA", "AAA"),
        ("ABABABAB", "ABAB"),
        ("The quick brown fox jumps over the lazy dog", "fox")
    ]
    
    print("=== Z Algorithm String Search ===\n")
    
    for i, (text, pattern) in enumerate(test_cases, 1):
        print(f"Test {i}:")
        print(f"Text: \"{text}\"")
        print(f"Pattern: \"{pattern}\"")
        
        # Create combined string and compute Z array
        combined = pattern + "$" + text
        z_array = compute_z_array(combined)
        
        print(f"\nZ Array for combined string \"{combined}\":")
        print_z_array(combined, z_array)
        
        # Measure time for first occurrence
        start_time = time.perf_counter()
        first_occurrence = z_algorithm_search(text, pattern)
        end_time = time.perf_counter()
        
        if first_occurrence != -1:
            print(f"First occurrence at index: {first_occurrence}")
            
            # Show the found substring
            found_substring = text[first_occurrence:first_occurrence + len(pattern)]
            print(f"Found substring: \"{found_substring}\"")
        else:
            print("Pattern not found")
        
        print(f"Time taken: {(end_time - start_time) * 1000000:.3f} microseconds")
        print("-" * 60)
        print()

def demonstrate_z_array_analysis():
    """Demonstrate Z array computation for different patterns"""
    print("=== Z Array Analysis for Different Patterns ===\n")
    
    patterns = [
        "ABABAB",
        "AABAAAB", 
        "ABCABCAB",
        "AAAA"
    ]
    
    for pattern in patterns:
        print(f"Pattern analysis for: \"{pattern}\"")
        z_array = compute_z_array(pattern)
        print_z_array(pattern, z_array)
        
        # Show interpretation
        print("Interpretation:")
        for i in range(1, len(z_array)):
            if z_array[i] > 0:
                prefix = pattern[:z_array[i]]
                suffix = pattern[i:i + z_array[i]]
                print(f"  Z[{i}] = {z_array[i]} means prefix \"{prefix}\" matches suffix \"{suffix}\"")
        print()

def demonstrate_step_by_step():
    """Show detailed step-by-step Z array computation"""
    print("=== Step-by-Step Z Array Computation ===\n")
    
    example = "AABAAAB"
    print(f"Detailed computation for pattern: '{example}'")
    z_array = visualize_z_computation(example)
    
    print(f"\nFinal Z array: {z_array}")
    print_z_array(example, z_array)

def performance_comparison():
    """Compare Z algorithm with other methods"""
    print("=== Performance Comparison ===\n")
    
    # Create test case
    text = "ABCABCABCABC" * 1000
    pattern = "ABCABC"
    
    print(f"Text length: {len(text):,} characters")
    print(f"Pattern: '{pattern}'")
    print()
    
    # Z Algorithm
    start_time = time.perf_counter()
    for _ in range(100):
        result_z = z_algorithm_search(text, pattern)
    z_time = time.perf_counter() - start_time
    
    # Built-in find
    start_time = time.perf_counter()
    for _ in range(100):
        result_builtin = text.find(pattern)
    builtin_time = time.perf_counter() - start_time
    
    print(f"Z Algorithm: Found at {result_z}, Time: {z_time * 10:.3f} μs per search")
    print(f"Built-in find(): Found at {result_builtin}, Time: {builtin_time * 10:.3f} μs per search")
    
    if builtin_time > 0:
        speedup = z_time / builtin_time
        if speedup > 1:
            print(f"Built-in is {speedup:.2f}x faster")
        else:
            print(f"Z Algorithm is {1/speedup:.2f}x faster")

if __name__ == "__main__":
    main()
    demonstrate_z_array_analysis()
    demonstrate_step_by_step()
    performance_comparison()