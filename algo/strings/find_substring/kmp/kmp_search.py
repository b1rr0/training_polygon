def compute_lps(pattern):
    """Build failure function for pattern"""
    lps = [0] * len(pattern)
    length = 0
    i = 1
    
    while i < len(pattern):
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
    """KMP search: use failure function to skip comparisons"""
    lps = compute_lps(pattern)
    i = j = 0
    
    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1
        
        if j == len(pattern):
            return i - j
        elif i < len(text) and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return -1

def test():
    text = "ABABDABACDABABCAB"
    pattern = "ABABCAB"
    result = kmp_search(text, pattern)
    print(f"Text: {text}")
    print(f"Pattern: {pattern}")
    print(f"Found at: {result}")

if __name__ == "__main__":
    test()