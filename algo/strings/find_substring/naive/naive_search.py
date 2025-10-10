import time

def naive_search(text, pattern):
    """
    Naive string search algorithm
    Time Complexity: O(n*m)
    Space Complexity: O(1)
    """
    n = len(text)
    m = len(pattern)
    
    for i in range(n - m + 1):
        j = 0
        while j < m and text[i + j] == pattern[j]:
            j += 1
        if j == m:
            return i
    return -1


def main():
    test_cases = [
        ("ABABDABACDABABCABCABCABCABC", "ABABCAB"),
        ("Hello World", "World"),
        ("AAAAAAA", "AAA"),
        ("ABCDEFGHIJKLMNOP", "XYZ"),
        ("The quick brown fox jumps over the lazy dog", "fox")
    ]
    
    print("=== Naive String Search Algorithm ===\n")
    
    for i, (text, pattern) in enumerate(test_cases, 1):
        print(f"Test {i}:")
        print(f"Text: \"{text}\"")
        print(f"Pattern: \"{pattern}\"")
        
        # Measure time for first occurrence
        start_time = time.perf_counter()
        first_occurrence = naive_search(text, pattern)
        end_time = time.perf_counter()
        
        if first_occurrence != -1:
            print(f"First occurrence at index: {first_occurrence}")
            
            # Show the found substring
            found_substring = text[first_occurrence:first_occurrence + len(pattern)]
            print(f"Found substring: \"{found_substring}\"")
        else:
            print("Pattern not found")
        
        print(f"Time taken: {(end_time - start_time) * 1000000:.3f} microseconds")
        print()

def demonstrate_edge_cases():
    print("=== Edge Cases ===\n")
    
    edge_cases = [
        ("", "abc"),           # Empty text
        ("abc", ""),           # Empty pattern
        ("", ""),              # Both empty
        ("a", "a"),            # Single character match
        ("a", "b"),            # Single character no match
        ("abc", "abcd"),       # Pattern longer than text
        ("aaaa", "aa"),        # Overlapping matches
    ]
    
    for i, (text, pattern) in enumerate(edge_cases, 1):
        print(f"Edge Case {i}:")
        print(f"Text: \"{text}\"")
        print(f"Pattern: \"{pattern}\"")
        
        try:
            result = naive_search(text, pattern)
            print(f"First occurrence: {result}")
        except Exception as e:
            print(f"Error: {e}")
        print()

if __name__ == "__main__":
    main()
    demonstrate_edge_cases()