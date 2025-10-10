# Substring Finding Algorithms

This directory contains implementations of various substring finding algorithms in both Java and Python, with comprehensive examples and performance comparisons.

## Files Overview

### Documentation
- `description.MD` - Comprehensive guide to all substring finding algorithms with complexity analysis

### Java Implementations
- `NaiveSearch.java` - Brute force algorithm implementation
- `KMPSearch.java` - Knuth-Morris-Pratt algorithm with LPS array
- `RabinKarpSearch.java` - Rolling hash-based search algorithm  
- `BuiltInSearch.java` - Java built-in string methods and regex

### Python Implementations
- `naive_search.py` - Naive algorithm with detailed examples
- `kmp_search.py` - KMP algorithm with LPS visualization
- `rabin_karp_search.py` - Rabin-Karp with hash collision handling
- `builtin_search.py` - Python built-in methods and regex patterns
- `run_all_tests.py` - Comprehensive testing and performance comparison

## How to Run

### Java Examples
```bash
# Compile and run individual algorithms
javac NaiveSearch.java && java NaiveSearch
javac KMPSearch.java && java KMPSearch
javac RabinKarpSearch.java && java RabinKarpSearch
javac BuiltInSearch.java && java BuiltInSearch
```

### Python Examples
```bash
# Run individual algorithms
python naive_search.py
python kmp_search.py
python rabin_karp_search.py
python builtin_search.py

# Run comprehensive comparison
python run_all_tests.py
```

## Algorithm Summary

| Algorithm | Time Complexity | Space Complexity | Best Use Case |
|-----------|----------------|------------------|---------------|
| **Naive** | O(n×m) | O(1) | Simple cases, educational |
| **KMP** | O(n+m) | O(m) | Multiple searches, patterns with repetition |
| **Rabin-Karp** | O(n+m) avg, O(n×m) worst | O(1) | Multiple patterns, rolling hash applications |
| **Built-in** | Varies (optimized) | O(1) | General use, production code |

Where:
- `n` = text length
- `m` = pattern length

## Features Included

### Java Features
- ✅ Complete implementations of all major algorithms
- ✅ Performance timing measurements
- ✅ Multiple test cases with edge cases
- ✅ Find first occurrence and all occurrences
- ✅ Built-in methods showcase (indexOf, contains, regex)

### Python Features  
- ✅ Detailed algorithm implementations with comments
- ✅ LPS array visualization for KMP
- ✅ Hash collision demonstration for Rabin-Karp
- ✅ Performance comparison across algorithms
- ✅ Edge case handling
- ✅ Advanced regex pattern examples
- ✅ Comprehensive test suite

## Key Learning Points

1. **Naive Algorithm**: Simple but inefficient for large texts
2. **KMP Algorithm**: Optimal for patterns with repeating prefixes
3. **Rabin-Karp**: Great for multiple pattern searches using rolling hash
4. **Built-in Methods**: Highly optimized, best for production use

## Example Output

When you run the Python comparison (`python run_all_tests.py`), you'll see:
- Correctness verification across all algorithms
- Performance benchmarks on different text sizes
- Detailed timing analysis
- Algorithm behavior on edge cases

## Advanced Features

- **Hash collision handling** in Rabin-Karp
- **LPS array computation** visualization in KMP  
- **Rolling hash mechanics** demonstration
- **Performance profiling** tools
- **Edge case testing** (empty strings, single characters, etc.)

## Educational Value

These implementations are designed for:
- 📚 Computer Science students learning string algorithms
- 🎯 Interview preparation and coding practice
- 🔍 Performance analysis and algorithm comparison
- 🛠️ Understanding real-world string processing

Run the examples to see each algorithm in action with detailed output showing how they work step-by-step!