# Rabin-Karp String Search

This directory contains implementations of the Rabin-Karp substring search algorithm in both Java and Python.

## Algorithm Overview

Rabin-Karp uses rolling hash to efficiently compare pattern and text substrings. Instead of comparing characters directly, it compares hash values first, only checking characters when hashes match.

**Time Complexity**: O(n+m) average case, O(n×m) worst case  
**Space Complexity**: O(1)

## Files

- `RabinKarpSearch.java` - Java implementation with hash computation
- `rabin_karp_search.py` - Python implementation with collision handling demo

## How to Run

### Java
```bash
javac RabinKarpSearch.java
java RabinKarpSearch
```

### Python
```bash
python rabin_karp_search.py
```

## Features

- ✅ Rolling hash implementation
- ✅ Hash collision detection and handling
- ✅ Configurable base and prime parameters
- ✅ Performance analysis with different parameters
- ✅ Spurious hit verification
- ✅ Multiple pattern search capability

## Key Concepts

### Rolling Hash
The algorithm uses a rolling hash function that can efficiently compute the hash of the next substring by:
1. Removing the contribution of the first character
2. Adding the contribution of the new character

Formula: `hash = (base * (hash - char[i] * h) + char[i+m]) % prime`

### Hash Parameters
- **Base**: Usually 256 (number of characters in extended ASCII)
- **Prime**: A large prime number to reduce collisions (e.g., 101, 1009)

## When to Use

- Searching for multiple patterns simultaneously
- When hash computation is faster than character comparison
- Large alphabets where character comparison is expensive
- Applications requiring average O(n+m) performance

## Algorithm Steps

1. **Preprocessing**: Compute hash of pattern and first window of text
2. **Rolling**: Slide window through text, updating hash in O(1) time
3. **Hash Comparison**: Compare pattern hash with current window hash
4. **Verification**: If hashes match, verify character by character (handles collisions)
5. **Continue**: Move to next position and repeat

## Hash Collision Handling

When two different strings have the same hash value (collision), the algorithm performs character-by-character verification to ensure correctness. The choice of prime number affects collision probability.