def naive_search(text, pattern):
    """Naive search: check pattern at each position"""
    for i in range(len(text) - len(pattern) + 1):
        if text[i:i + len(pattern)] == pattern:
            return i
    return -1

def test():
    text = "Hello World"
    pattern = "World"
    result = naive_search(text, pattern)
    print(f"Text: {text}")
    print(f"Pattern: {pattern}")
    print(f"Found at: {result}")

if __name__ == "__main__":
    test()