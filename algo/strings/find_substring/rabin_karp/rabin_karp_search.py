def rabin_karp_search(text, pattern):
    """Rolling hash search: compare hash values"""
    if len(pattern) > len(text):
        return -1
    
    base = 256
    prime = 101
    
    # Compute hash values
    pattern_hash = 0
    text_hash = 0
    h = pow(base, len(pattern) - 1) % prime
    
    for i in range(len(pattern)):
        pattern_hash = (base * pattern_hash + ord(pattern[i])) % prime
        text_hash = (base * text_hash + ord(text[i])) % prime
    
    # Slide window and compare
    for i in range(len(text) - len(pattern) + 1):
        if pattern_hash == text_hash:
            if text[i:i + len(pattern)] == pattern:
                return i
        
        if i < len(text) - len(pattern):
            text_hash = (base * (text_hash - ord(text[i]) * h) + ord(text[i + len(pattern)])) % prime
            if text_hash < 0:
                text_hash += prime
    
    return -1

def test():
    text = "Programming is fun"
    pattern = "is"
    result = rabin_karp_search(text, pattern)
    print(f"Text: {text}")
    print(f"Pattern: {pattern}")
    print(f"Found at: {result}")

if __name__ == "__main__":
    test()