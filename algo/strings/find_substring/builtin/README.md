# Built-in String Search Methods

This directory contains implementations showcasing built-in string search methods available in Java and Python.

## Overview

Most programming languages provide highly optimized built-in string search functions. While their internal implementations may vary, they are typically the best choice for production code.

**Time Complexity**: Usually O(n×m) but highly optimized  
**Space Complexity**: O(1)

## Files

- `BuiltInSearch.java` - Java built-in methods (`indexOf`, `contains`, regex)
- `builtin_search.py` - Python built-in methods (`find`, `in`, regex)

## How to Run

### Java
```bash
javac BuiltInSearch.java
java BuiltInSearch
```

### Python
```bash
python builtin_search.py
```

## Java Methods Demonstrated

### String Methods
- `indexOf(String)` - Find first occurrence
- `lastIndexOf(String)` - Find last occurrence
- `contains(String)` - Check if substring exists
- `startsWith(String)` - Check if string starts with substring
- `endsWith(String)` - Check if string ends with substring

### Regular Expressions
- `Pattern.compile()` and `Matcher` for complex pattern matching
- `Pattern.quote()` for literal string matching

## Python Methods Demonstrated

### String Methods
- `find(substring)` - Find first occurrence (returns -1 if not found)
- `index(substring)` - Find first occurrence (raises exception if not found)
- `rfind(substring)` - Find last occurrence
- `count(substring)` - Count all occurrences
- `in` operator - Check if substring exists
- `startswith()` / `endswith()` - Check string boundaries

### Regular Expressions
- `re.search()` - Find first match
- `re.findall()` - Find all matches
- `re.finditer()` - Iterator for all matches
- Advanced regex patterns for complex searches

## Performance Features

- ✅ Highly optimized implementations
- ✅ Performance comparison between different methods
- ✅ Case-sensitive and case-insensitive searches
- ✅ Multiple occurrence finding
- ✅ Regular expression pattern matching
- ✅ Boundary checking methods

## When to Use

- **Production code** - Built-in methods are usually the best choice
- **General-purpose searching** - When you don't need specialized algorithms
- **Quick prototyping** - Fast development with reliable functions
- **Complex patterns** - Regular expressions for advanced pattern matching

## Advanced Features Shown

### Python Advanced Examples
- Email and phone number extraction using regex
- Case-insensitive searching
- Word boundary matching
- Performance benchmarking across methods

### Java Advanced Examples
- Stream API integration
- Regex with groups and capturing
- Performance measurement and comparison
- Error handling best practices

Built-in methods are recommended for most real-world applications unless you have specific performance requirements that necessitate custom implementations.