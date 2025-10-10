# Z Algorithm String Search

This directory contains implementations of the Z Algorithm for substring search in both Java and Python.

## Algorithm Overview

The Z Algorithm constructs a Z array where Z[i] represents the length of the longest substring starting from position i that matches a prefix of the string. This preprocessing enables efficient pattern matching.

**Time Complexity**: O(n+m) where n = text length, m = pattern length  
**Space Complexity**: O(n+m) for the combined string and Z array

## Files

- `ZAlgorithmSearch.java` - Java implementation with Z array visualization
- `z_algorithm_search.py` - Python implementation with step-by-step computation

## How to Run

### Java
```bash
javac ZAlgorithmSearch.java
java ZAlgorithmSearch
```

### Python
```bash
python z_algorithm_search.py
```

## Features

- ✅ Linear time O(n+m) complexity
- ✅ Z array computation and visualization
- ✅ Step-by-step algorithm demonstration
- ✅ Find first and all occurrences
- ✅ Pattern analysis capabilities
- ✅ Performance comparison with built-in methods

## Key Concepts

### Z Array
For a string S, the Z array Z[i] stores the length of the longest substring starting from S[i] which is also a prefix of S.

Example for string "AABAAAB":
```
String: A A B A A A B
Index:  0 1 2 3 4 5 6
Z[i]:   0 1 0 2 3 1 0
```

Interpretation:
- Z[1] = 1: substring "A" at position 1 matches prefix "A"
- Z[3] = 2: substring "AA" at position 3 matches prefix "AA"
- Z[4] = 3: substring "AAB" at position 4 matches prefix "AAB"

### Pattern Matching Process
1. **Combine**: Create string `pattern + "$" + text` ($ is a separator)
2. **Compute**: Build Z array for the combined string
3. **Search**: Find positions where Z[i] equals pattern length
4. **Extract**: Convert positions to original text indices

## Algorithm Mechanics

The Z algorithm uses two pointers (l, r) to maintain a "Z-box" - the rightmost segment that matches a prefix. This allows optimal reuse of previously computed information.

### Key Variables
- **l, r**: Left and right boundaries of the current Z-box
- **Z[i]**: Length of longest prefix match starting at position i

### Optimization Strategy
- If position i is within current Z-box, use symmetry to avoid redundant comparisons
- Extend matches character by character only when necessary
- Update Z-box boundaries when a longer match is found

## When to Use

- **Multiple pattern searches** on the same text
- **Pattern analysis** requiring prefix-suffix relationships
- **Preprocessing patterns** for complex string algorithms
- **Educational purposes** to understand linear-time string algorithms

## Advantages

1. **Linear Time**: Guaranteed O(n+m) performance
2. **No Backtracking**: Each character examined at most twice
3. **Versatile**: Can solve various string problems beyond search
4. **Intuitive**: Z array provides clear insight into string structure

## Applications Beyond Search

- Finding all periods of a string
- String compression algorithms
- Palindrome detection variants
- Text processing and analysis

## Python-Specific Features

The Python implementation includes:
- **Step-by-step visualization** of Z array computation
- **Detailed explanations** of each algorithmic step
- **Performance benchmarking** against built-in methods
- **Pattern structure analysis** showing prefix-suffix relationships

## Java-Specific Features

The Java implementation provides:
- **Formatted Z array display** with aligned columns
- **Pattern matching demonstrations** with multiple test cases
- **Performance timing** measurements
- **Comprehensive edge case handling**

The Z Algorithm is particularly valuable when you need to understand the internal structure of strings or when performing multiple searches that can benefit from the preprocessing step.