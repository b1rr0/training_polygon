import time
import re

def find_substring(text, pattern):
    """Using built-in find() method"""
    return text.find(pattern)


def find_with_index(text, pattern):
    """Using built-in index() method (raises exception if not found)"""
    try:
        return text.index(pattern)
    except ValueError:
        return -1

def contains_substring(text, pattern):
    """Using 'in' operator"""
    return pattern in text

def find_with_regex(text, pattern):
    """Using regular expressions"""
    match = re.search(re.escape(pattern), text)
    return match.start() if match else -1


def case_insensitive_search(text, pattern):
    """Case insensitive search"""
    return text.lower().find(pattern.lower())

def find_last_occurrence(text, pattern):
    """Find last occurrence using rfind()"""
    return text.rfind(pattern)

def starts_ends_with(text, pattern):
    """Check if text starts or ends with pattern"""
    return {
        'starts_with': text.startswith(pattern),
        'ends_with': text.endswith(pattern)
    }

def main():
    test_cases = [
        ("ABABDABACDABABCABCABCABCABC", "ABABCAB"),
        ("Hello World Hello World", "World"),
        ("AAAAAAA", "AAA"),
        ("Java is great, Java is powerful, Java is everywhere", "Java"),
        ("The Quick Brown Fox Jumps Over The Lazy Dog", "the")
    ]
    
    print("=== Built-in String Search Methods ===\n")
    
    for i, (text, pattern) in enumerate(test_cases, 1):
        print(f"Test {i}:")
        print(f"Text: \"{text}\"")
        print(f"Pattern: \"{pattern}\"")
        
        # Test contains (in operator)
        start_time = time.perf_counter()
        contains = contains_substring(text, pattern)
        contains_time = time.perf_counter() - start_time
        print(f"Contains (in operator): {contains} (Time: {contains_time * 1000000:.3f} μs)")
        
        # Test find() method
        start_time = time.perf_counter()
        first_occurrence = find_substring(text, pattern)
        find_time = time.perf_counter() - start_time
        
        if first_occurrence != -1:
            print(f"First occurrence (find): {first_occurrence} (Time: {find_time * 1000000:.3f} μs)")
            
            # Test index() method
            index_result = find_with_index(text, pattern)
            print(f"First occurrence (index): {index_result}")
            
            # Test regex approach
            start_time = time.perf_counter()
            regex_result = find_with_regex(text, pattern)
            regex_time = time.perf_counter() - start_time
            print(f"First occurrence (regex): {regex_result} (Time: {regex_time * 1000000:.3f} μs)")
            
            # Last occurrence
            last_occurrence = find_last_occurrence(text, pattern)
            print(f"Last occurrence (rfind): {last_occurrence}")
            
            # Case insensitive search
            case_insensitive = case_insensitive_search(text, pattern)
            print(f"Case insensitive search: {case_insensitive}")
            
            # Show the found substring
            found_substring = text[first_occurrence:first_occurrence + len(pattern)]
            print(f"Found substring: \"{found_substring}\"")
            
        else:
            print("Pattern not found")
        
        # Starts/ends with
        starts_ends = starts_ends_with(text, pattern)
        print(f"Starts with pattern: {starts_ends['starts_with']}")
        print(f"Ends with pattern: {starts_ends['ends_with']}")
        
        print("-" * 60)
        print()

def demonstrate_string_methods():
    """Demonstrate various string methods"""
    print("=== Additional String Methods Demo ===\n")
    
    text = "The quick brown fox jumps over the lazy dog"
    
    print(f"Text: \"{text}\"")
    print()
    
    # Split and count
    words = text.split()
    print(f"Words: {words}")
    print(f"Word count: {len(words)}")
    
    # Count occurrences
    print(f"Count of 'the': {text.count('the')}")
    print(f"Count of 'the' (case insensitive): {text.lower().count('the')}")
    
    # Replace
    replaced = text.replace('the', 'a')
    print(f"Replace 'the' with 'a': \"{replaced}\"")
    
    # Partition
    before, sep, after = text.partition('fox')
    print(f"Partition by 'fox': before=\"{before}\", sep=\"{sep}\", after=\"{after}\"")
    
    # String formatting
    pattern = "fox"
    index = text.find(pattern)
    print(f"Using f-string: Pattern '{pattern}' found at position {index}")

def performance_comparison():
    """Compare performance of different search methods"""
    print("=== Performance Comparison ===\n")
    
    # Create a large text for meaningful performance comparison
    text = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" * 10000
    pattern = "XYZ"
    
    print(f"Text length: {len(text):,} characters")
    print(f"Pattern: '{pattern}'")
    print()
    
    methods = [
        ("in operator", lambda: pattern in text),
        ("find()", lambda: text.find(pattern)),
        ("index()", lambda: text.index(pattern)),
        ("regex", lambda: re.search(re.escape(pattern), text).start())
    ]
    
    for name, method in methods:
        start_time = time.perf_counter()
        for _ in range(1000):  # Run multiple times for accurate measurement
            result = method()
        end_time = time.perf_counter()
        
        avg_time = (end_time - start_time) / 1000
        print(f"{name:12}: {avg_time * 1000000:.3f} μs per search")

def regex_patterns_demo():
    """Demonstrate advanced regex patterns"""
    print("=== Advanced Regex Patterns ===\n")
    
    text = "Contact: john.doe@email.com or call 123-456-7890"
    
    patterns = [
        (r'\b\w+@\w+\.\w+\b', "Email addresses"),
        (r'\b\d{3}-\d{3}-\d{4}\b', "Phone numbers"),
        (r'\b[A-Z][a-z]+\b', "Capitalized words"),
        (r'\b\w{4,}\b', "Words with 4+ characters")
    ]
    
    print(f"Text: \"{text}\"")
    print()
    
    for pattern, description in patterns:
        matches = re.findall(pattern, text)
        print(f"{description}: {matches}")

if __name__ == "__main__":
    main()
    demonstrate_string_methods()
    performance_comparison()
    regex_patterns_demo()