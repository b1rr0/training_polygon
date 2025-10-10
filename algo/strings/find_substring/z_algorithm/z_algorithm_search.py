def compute_z_array(s):
    """Build Z array: length of longest prefix at each position"""
    z = [0] * len(s)
    l = r = 0
    
    for i in range(1, len(s)):
        if i <= r:
            z[i] = min(r - i + 1, z[i - l])
        
        while i + z[i] < len(s) and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        
        if i + z[i] - 1 > r:
            l, r = i, i + z[i] - 1
    
    return z

def z_algorithm_search(text, pattern):
    """Z algorithm search: find pattern using Z array"""
    if not pattern or len(pattern) > len(text):
        return -1
    
    combined = pattern + "$" + text
    z_array = compute_z_array(combined)
    
    for i in range(len(pattern) + 1, len(combined)):
        if z_array[i] == len(pattern):
            return i - len(pattern) - 1
    
    return -1

def test():
    text = "ABABDABACDABABCAB"
    pattern = "ABABCAB"
    result = z_algorithm_search(text, pattern)
    print(f"Text: {text}")
    print(f"Pattern: {pattern}")
    print(f"Found at: {result}")

if __name__ == "__main__":
    test()