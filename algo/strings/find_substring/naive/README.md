# Naive/Brute Force String Search

This directory contains implementations of the naive (brute force) substring search algorithm in both Java and Python.

## Algorithm Overview

The naive algorithm compares the pattern with all possible positions in the text by checking character by character.

**Time Complexity**: O(n×m) where n = text length, m = pattern length  
**Space Complexity**: O(1)

## Files

- `NaiveSearch.java` - Java implementation with performance timing
- `naive_search.py` - Python implementation with edge case handling

## How to Run

### Java
```bash
javac NaiveSearch.java
java NaiveSearch
```

### Python
```bash
python naive_search.py
```

## Features

- ✅ Find first occurrence
- ✅ Find all occurrences  
- ✅ Performance timing
- ✅ Multiple test cases
- ✅ Edge case handling (empty strings, etc.)

## When to Use

- Simple implementation needed
- Small texts and patterns
- Educational purposes
- When memory is extremely limited

## Algorithm Steps

1. Start from the first character of the text
2. Compare pattern with text starting at current position
3. If all characters match, return the position
4. If mismatch found, move to next position in text
5. Repeat until pattern found or end of text reached

The naive approach is straightforward but can be inefficient for large texts with repetitive patterns, as it doesn't utilize any information from previous comparisons.