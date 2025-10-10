import time

class RabinKarpSearch:
    def __init__(self, base=256, prime=101):
        self.base = base
        self.prime = prime
    
    def search(self, text, pattern):
        """
        Rabin-Karp string search algorithm
        Time Complexity: O(n + m) average case, O(n*m) worst case
        Space Complexity: O(1)
        """
        n = len(text)
        m = len(pattern)
        
        if m == 0:
            return 0
        if m > n:
            return -1
        
        pattern_hash = 0
        text_hash = 0
        h = 1
        
        # Calculate h = pow(base, m-1) % prime
        for i in range(m - 1):
            h = (h * self.base) % self.prime
        
        # Calculate hash of pattern and first window of text
        for i in range(m):
            pattern_hash = (self.base * pattern_hash + ord(pattern[i])) % self.prime
            text_hash = (self.base * text_hash + ord(text[i])) % self.prime
        
        # Slide pattern over text
        for i in range(n - m + 1):
            # Check if hash values match
            if pattern_hash == text_hash:
                # Check characters one by one (spurious hit verification)
                j = 0
                while j < m and text[i + j] == pattern[j]:
                    j += 1
                if j == m:
                    return i  # Found at index i
            
            # Calculate hash for next window
            if i < n - m:
                text_hash = (self.base * (text_hash - ord(text[i]) * h) + ord(text[i + m])) % self.prime
                # Handle negative hash
                if text_hash < 0:
                    text_hash += self.prime
        
        return -1
    
    
    def calculate_hash(self, s):
        """Calculate hash value of a string"""
        hash_value = 0
        for char in s:
            hash_value = (self.base * hash_value + ord(char)) % self.prime
        return hash_value

def main():
    test_cases = [
        ("ABABDABACDABABCABCABCABCABC", "ABABCAB"),
        ("Hello World Hello", "Hello"),
        ("AAAAAAA", "AAA"),
        ("The quick brown fox jumps over the lazy dog", "fox"),
        ("Programming is fun and challenging", "and")
    ]
    
    rk = RabinKarpSearch()
    
    print("=== Rabin-Karp String Search Algorithm ===")
    print(f"Using BASE={rk.base} and PRIME={rk.prime}\n")
    
    for i, (text, pattern) in enumerate(test_cases, 1):
        print(f"Test {i}:")
        print(f"Text: \"{text}\"")
        print(f"Pattern: \"{pattern}\"")
        
        # Calculate pattern hash
        pattern_hash = rk.calculate_hash(pattern)
        print(f"Pattern hash: {pattern_hash}")
        
        # Measure time for first occurrence
        start_time = time.perf_counter()
        first_occurrence = rk.search(text, pattern)
        end_time = time.perf_counter()
        
        if first_occurrence != -1:
            print(f"First occurrence at index: {first_occurrence}")
            
            # Show the found substring and its hash
            found_substring = text[first_occurrence:first_occurrence + len(pattern)]
            found_hash = rk.calculate_hash(found_substring)
            print(f"Found substring: \"{found_substring}\" (hash: {found_hash})")
        else:
            print("Pattern not found")
        
        print(f"Time taken: {(end_time - start_time) * 1000000:.3f} microseconds")
        print("-" * 50)
        print()

def demonstrate_hash_collisions():
    """Demonstrate hash collisions and their handling"""
    print("=== Hash Collision Demonstration ===\n")
    
    rk = RabinKarpSearch(base=3, prime=7)  # Small values to force collisions
    
    # Strings that might have same hash
    strings = ["ab", "ba", "ca", "bc"]
    
    print(f"Using BASE={rk.base} and PRIME={rk.prime}")
    print("Hash values for different strings:")
    
    for s in strings:
        hash_val = rk.calculate_hash(s)
        print(f"'{s}' -> {hash_val}")
    
    print()
    
    # Test with a text that contains potential hash collisions
    text = "abcabacaba"
    pattern = "ba"
    
    print(f"Searching for '{pattern}' in '{text}'")
    
    result = rk.search(text, pattern)
    
    print(f"First occurrence: {result}")
    
    # Show how the algorithm handles spurious hits
    print("\nNote: Rabin-Karp handles hash collisions by verifying character-by-character")

def performance_comparison():
    """Compare different prime numbers and their effect on performance"""
    print("=== Performance with Different Parameters ===\n")
    
    text = "ABCABCABCABC" * 1000
    pattern = "ABCABC"
    
    primes = [101, 1009, 10007, 100003]
    
    print(f"Text length: {len(text)}")
    print(f"Pattern: '{pattern}'")
    print()
    
    for prime in primes:
        rk = RabinKarpSearch(prime=prime)
        
        start_time = time.perf_counter()
        result = rk.search(text, pattern)
        end_time = time.perf_counter()
        
        print(f"Prime {prime}: Found at {result}, Time: {(end_time - start_time) * 1000000:.3f} μs")

if __name__ == "__main__":
    main()
    demonstrate_hash_collisions()
    performance_comparison()