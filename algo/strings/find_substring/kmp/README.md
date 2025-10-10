# KMP (Knuth-Morris-Pratt) String Search

This directory contains implementations of the KMP substring search algorithm in both Java and Python.

## Algorithm Overview

KMP uses a failure function (LPS array) to avoid redundant comparisons by preprocessing the pattern to determine how much to skip when a mismatch occurs.

**Time Complexity**: O(n+m) where n = text length, m = pattern length  
**Space Complexity**: O(m) for the LPS array

## Files

- `KMPSearch.java` - Java implementation with LPS array computation
- `kmp_search.py` - Python implementation with LPS visualization

## How to Run

### Java
```bash
javac KMPSearch.java
java KMPSearch
```

### Python
```bash
python kmp_search.py
```

## Features

- ✅ Optimal O(n+m) time complexity
- ✅ LPS (Longest Proper Prefix which is also Suffix) array computation
- ✅ Visual representation of LPS array
- ✅ Find first and all occurrences
- ✅ Performance comparison with naive approach
- ✅ Detailed step-by-step execution

## Key Concepts

### LPS Array
The LPS array stores the length of the longest proper prefix of the pattern which is also a suffix for each position. This information helps determine how many characters to skip when a mismatch occurs.

Example for pattern "ABABCAB":
```
Pattern: A B A B C A B
Index:   0 1 2 3 4 5 6
LPS:     0 0 1 2 0 1 2
```

## When to Use

- Large texts with repetitive patterns
- Multiple searches with the same pattern
- When optimal time complexity is required
- Patterns with repeating prefixes

## Algorithm Steps

1. **Preprocessing**: Compute LPS array for the pattern
2. **Search**: Use LPS array to skip characters efficiently during mismatch
3. When characters match, advance both text and pattern pointers
4. When mismatch occurs, use LPS array to determine next comparison position
5. Continue until pattern found or end of text reached

The KMP algorithm never re-examines previously matched characters in the text, making it optimal for large inputs.