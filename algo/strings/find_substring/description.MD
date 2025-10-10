# Substring Finding Algorithms

This document describes various methods to find a substring within a string, along with their time complexities and use cases.

## 1. Naive/Brute Force Algorithm

**Description**: Compare the pattern with all possible positions in the text.

**Time Complexity**: O(n*m) where n is text length, m is pattern length
**Space Complexity**: O(1)

**When to use**: Simple cases, very short patterns, or when implementation simplicity is prioritized.

**Implementation**: [📁 naive/](./naive/) - Contains Java and Python implementations

## 2. KMP (Knuth-Morris-Pratt) Algorithm

**Description**: Uses a failure function to avoid redundant comparisons by preprocessing the pattern.

**Time Complexity**: O(n+m)
**Space Complexity**: O(m)

**When to use**: When you need to find multiple occurrences efficiently, or when the pattern has repeating prefixes.

**Implementation**: [📁 kmp/](./kmp/) - Contains Java and Python implementations

## 3. Boyer-Moore Algorithm

**Description**: Searches from right to left and uses bad character and good suffix heuristics to skip characters.

**Time Complexity**: O(n*m) worst case, O(n/m) best case
**Space Complexity**: O(�) where � is alphabet size

**When to use**: Large texts with large patterns, especially when alphabet is large.

## 4. Rabin-Karp Algorithm

**Description**: Uses rolling hash to compare hash values of pattern and text substrings.

**Time Complexity**: O(n+m) average case, O(n*m) worst case
**Space Complexity**: O(1)

**When to use**: When searching for multiple patterns simultaneously, or when hash comparisons are faster than character comparisons.

**Implementation**: [📁 rabin_karp/](./rabin_karp/) - Contains Java and Python implementations

## 5. Z Algorithm

**Description**: Constructs a Z array that stores the length of the longest substring starting from each position that matches a prefix.

**Time Complexity**: O(n+m)
**Space Complexity**: O(n+m)

**When to use**: When you need to find all occurrences and the preprocessing overhead is acceptable.

## 6. Built-in String Functions

**Description**: Most programming languages provide optimized built-in functions.

**Time Complexity**: Usually O(n*m) but highly optimized
**Space Complexity**: O(1)

**When to use**: For most practical applications unless specific performance requirements exist.

**Implementation**: [📁 builtin/](./builtin/) - Contains Java and Python implementations

---

## Code Examples

All algorithms have been implemented in both Java and Python with comprehensive examples and test cases. Each algorithm is organized in its own directory:

- [📁 naive/](./naive/) - Naive/Brute Force Algorithm
- [📁 kmp/](./kmp/) - KMP (Knuth-Morris-Pratt) Algorithm  
- [📁 rabin_karp/](./rabin_karp/) - Rabin-Karp Algorithm
- [📁 builtin/](./builtin/) - Built-in String Functions

## How to Run the Examples

### Java
```bash
# Navigate to algorithm directory and run
cd naive/ && javac NaiveSearch.java && java NaiveSearch
cd kmp/ && javac KMPSearch.java && java KMPSearch
cd rabin_karp/ && javac RabinKarpSearch.java && java RabinKarpSearch
cd builtin/ && javac BuiltInSearch.java && java BuiltInSearch
```

### Python
```bash
# Navigate to algorithm directory and run
cd naive/ && python naive_search.py
cd kmp/ && python kmp_search.py
cd rabin_karp/ && python rabin_karp_search.py
cd builtin/ && python builtin_search.py

# Or run comprehensive comparison
python run_all_tests.py
```

---

## Java Examples (Legacy - see individual directories for updated code)

### 1. Naive Algorithm
```java
public class NaiveSearch {
    public static int findSubstring(String text, String pattern) {
        int n = text.length();
        int m = pattern.length();
        
        for (int i = 0; i <= n - m; i++) {
            int j = 0;
            while (j < m && text.charAt(i + j) == pattern.charAt(j)) {
                j++;
            }
            if (j == m) {
                return i; // Found at index i
            }
        }
        return -1; // Not found
    }
    
    public static void main(String[] args) {
        String text = "ABABDABACDABABCABCABCABCABC";
        String pattern = "ABABCAB";
        int result = findSubstring(text, pattern);
        System.out.println("Pattern found at index: " + result);
    }
}
```

### 2. KMP Algorithm
```java
public class KMPSearch {
    public static int[] computeLPS(String pattern) {
        int m = pattern.length();
        int[] lps = new int[m];
        int len = 0;
        int i = 1;
        
        while (i < m) {
            if (pattern.charAt(i) == pattern.charAt(len)) {
                len++;
                lps[i] = len;
                i++;
            } else {
                if (len != 0) {
                    len = lps[len - 1];
                } else {
                    lps[i] = 0;
                    i++;
                }
            }
        }
        return lps;
    }
    
    public static int findSubstring(String text, String pattern) {
        int n = text.length();
        int m = pattern.length();
        int[] lps = computeLPS(pattern);
        
        int i = 0; // index for text
        int j = 0; // index for pattern
        
        while (i < n) {
            if (pattern.charAt(j) == text.charAt(i)) {
                i++;
                j++;
            }
            
            if (j == m) {
                return i - j; // Found at index i-j
            } else if (i < n && pattern.charAt(j) != text.charAt(i)) {
                if (j != 0) {
                    j = lps[j - 1];
                } else {
                    i++;
                }
            }
        }
        return -1; // Not found
    }
    
    public static void main(String[] args) {
        String text = "ABABDABACDABABCABCABCABCABC";
        String pattern = "ABABCAB";
        int result = findSubstring(text, pattern);
        System.out.println("Pattern found at index: " + result);
    }
}
```

### 3. Rabin-Karp Algorithm
```java
public class RabinKarpSearch {
    private static final int PRIME = 101;
    
    public static int findSubstring(String text, String pattern) {
        int n = text.length();
        int m = pattern.length();
        int patternHash = 0;
        int textHash = 0;
        int h = 1;
        
        // Calculate h = pow(256, m-1) % PRIME
        for (int i = 0; i < m - 1; i++) {
            h = (h * 256) % PRIME;
        }
        
        // Calculate hash of pattern and first window of text
        for (int i = 0; i < m; i++) {
            patternHash = (256 * patternHash + pattern.charAt(i)) % PRIME;
            textHash = (256 * textHash + text.charAt(i)) % PRIME;
        }
        
        // Slide pattern over text
        for (int i = 0; i <= n - m; i++) {
            if (patternHash == textHash) {
                // Check characters one by one
                int j = 0;
                while (j < m && text.charAt(i + j) == pattern.charAt(j)) {
                    j++;
                }
                if (j == m) {
                    return i; // Found at index i
                }
            }
            
            // Calculate hash for next window
            if (i < n - m) {
                textHash = (256 * (textHash - text.charAt(i) * h) + text.charAt(i + m)) % PRIME;
                if (textHash < 0) {
                    textHash += PRIME;
                }
            }
        }
        return -1; // Not found
    }
    
    public static void main(String[] args) {
        String text = "ABABDABACDABABCABCABCABCABC";
        String pattern = "ABABCAB";
        int result = findSubstring(text, pattern);
        System.out.println("Pattern found at index: " + result);
    }
}
```

### 4. Built-in Java Methods
```java
public class BuiltInSearch {
    public static void main(String[] args) {
        String text = "ABABDABACDABABCABCABCABCABC";
        String pattern = "ABABCAB";
        
        // Using indexOf
        int index = text.indexOf(pattern);
        System.out.println("Pattern found at index: " + index);
        
        // Using contains
        boolean found = text.contains(pattern);
        System.out.println("Pattern found: " + found);
        
        // Find all occurrences
        int currentIndex = 0;
        while ((currentIndex = text.indexOf(pattern, currentIndex)) != -1) {
            System.out.println("Pattern found at index: " + currentIndex);
            currentIndex++;
        }
    }
}
```

---

## Python Examples

### 1. Naive Algorithm
```python
def naive_search(text, pattern):
    n = len(text)
    m = len(pattern)
    
    for i in range(n - m + 1):
        j = 0
        while j < m and text[i + j] == pattern[j]:
            j += 1
        if j == m:
            return i  # Found at index i
    return -1  # Not found

# Example usage
text = "ABABDABACDABABCABCABCABCABC"
pattern = "ABABCAB"
result = naive_search(text, pattern)
print(f"Pattern found at index: {result}")
```

### 2. KMP Algorithm
```python
def compute_lps(pattern):
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
    n = len(text)
    m = len(pattern)
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
    return -1  # Not found

# Example usage
text = "ABABDABACDABABCABCABCABCABC"
pattern = "ABABCAB"
result = kmp_search(text, pattern)
print(f"Pattern found at index: {result}")
```

### 3. Rabin-Karp Algorithm
```python
def rabin_karp_search(text, pattern):
    n = len(text)
    m = len(pattern)
    prime = 101
    pattern_hash = 0
    text_hash = 0
    h = 1
    
    # Calculate h = pow(256, m-1) % prime
    for i in range(m - 1):
        h = (h * 256) % prime
    
    # Calculate hash of pattern and first window of text
    for i in range(m):
        pattern_hash = (256 * pattern_hash + ord(pattern[i])) % prime
        text_hash = (256 * text_hash + ord(text[i])) % prime
    
    # Slide pattern over text
    for i in range(n - m + 1):
        if pattern_hash == text_hash:
            # Check characters one by one
            j = 0
            while j < m and text[i + j] == pattern[j]:
                j += 1
            if j == m:
                return i  # Found at index i
        
        # Calculate hash for next window
        if i < n - m:
            text_hash = (256 * (text_hash - ord(text[i]) * h) + ord(text[i + m])) % prime
            if text_hash < 0:
                text_hash += prime
    
    return -1  # Not found

# Example usage
text = "ABABDABACDABABCABCABCABCABC"
pattern = "ABABCAB"
result = rabin_karp_search(text, pattern)
print(f"Pattern found at index: {result}")
```

### 4. Built-in Python Methods
```python
def builtin_search():
    text = "ABABDABACDABABCABCABCABCABC"
    pattern = "ABABCAB"
    
    # Using find()
    index = text.find(pattern)
    print(f"Pattern found at index: {index}")
    
    # Using in operator
    found = pattern in text
    print(f"Pattern found: {found}")
    
    # Find all occurrences
    start = 0
    while True:
        index = text.find(pattern, start)
        if index == -1:
            break
        print(f"Pattern found at index: {index}")
        start = index + 1

# Example usage
builtin_search()
```

### 5. Using Regular Expressions
```python
import re

def regex_search():
    text = "ABABDABACDABABCABCABCABCABC"
    pattern = "ABABCAB"
    
    # Find first occurrence
    match = re.search(pattern, text)
    if match:
        print(f"Pattern found at index: {match.start()}")
    
    # Find all occurrences
    matches = re.finditer(pattern, text)
    for match in matches:
        print(f"Pattern found at index: {match.start()}")

# Example usage
regex_search()
```

---

## Performance Comparison

| Algorithm | Best Case | Average Case | Worst Case | Space | Best For |
|-----------|-----------|--------------|------------|-------|----------|
| Naive | O(n) | O(n*m) | O(n*m) | O(1) | Simple cases |
| KMP | O(n) | O(n) | O(n) | O(m) | Multiple searches |
| Boyer-Moore | O(n/m) | O(n) | O(n*m) | O(�) | Large alphabets |
| Rabin-Karp | O(n) | O(n+m) | O(n*m) | O(1) | Multiple patterns |
| Built-in | Varies | Usually O(n*m) | Varies | O(1) | General use |

## Conclusion

For most practical applications, built-in string functions are recommended due to their optimization and simplicity. However, understanding these algorithms is crucial for:

- Interview preparation
- Performance-critical applications
- Educational purposes
- Situations requiring custom implementations

Choose the algorithm based on your specific requirements: text size, pattern characteristics, memory constraints, and performance needs.