# Substring Finding Algorithms

## 1. Naive Algorithm
**How it works**: Checks the pattern at every position in the text, comparing character by character.

**Principle**: For each position i in the text, checks if substring text[i:i+m] matches the pattern.

**Complexity**: 
- Time: O(n*m) - worst case checks all pattern characters at each position
- Space: O(1) - uses only a few variables

## 2. KMP (Knuth-Morris-Pratt)
**How it works**: Preprocesses the pattern to create a shift table (LPS) to avoid redundant comparisons.

**Principle**: When a mismatch occurs, uses information about already checked characters to skip ahead instead of moving just one position.

**Complexity**:
- Time: O(n+m) - linear, as each text character is examined at most once
- Space: O(m) - for storing the LPS array

## 3. Rabin-Karp Algorithm  
**How it works**: Uses hash function for fast comparison. Computes pattern hash and rolling hash for text window.

**Principle**: Compares hash values instead of characters. When hashes match, additionally checks characters to handle hash collisions.

**Complexity**:
- Time: O(n+m) average case, O(n*m) worst case (many hash collisions)
- Space: O(1) - only for storing hash values

## 4. Z Algorithm
**How it works**: Builds Z-array where Z[i] = length of longest prefix that matches substring starting at position i.

**Principle**: Combines pattern and text with separator (pattern$text), then searches Z-array for values equal to pattern length.

**Complexity**:
- Time: O(n+m) - linear due to smart reuse of previously computed values
- Space: O(n+m) - for storing Z-array of combined string

## Implementations

- [📁 naive/](./naive/) - Naive/Brute Force Algorithm
- [📁 kmp/](./kmp/) - KMP (Knuth-Morris-Pratt) Algorithm  
- [📁 rabin_karp/](./rabin_karp/) - Rabin-Karp Algorithm
- [📁 z_algorithm/](./z_algorithm/) - Z Algorithm
- [📁 builtin/](./builtin/) - Built-in String Functions

https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/
LINK https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/solutions/6617473/optimal-kmp-rabin-karp-z-algorithm-solutions-with-detailed-inline-comments-and-break-down/


