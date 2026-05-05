# Level 8 — Pro: Advanced Algorithms (Strings, Math & Number Theory)

> **Directory:** `Level_8_9_Pro/`  
> **Category:** `C80_Advanced_Algorithms_String_Math_NT`  
> **Total Files:** **130 files**  
> **Prerequisite:** Level 7 (Templates, Concurrency)  
> **Leads to:** Level 9 (System Design, Low-Level C++)

---

## Overview

Level 8 covers the advanced algorithmic techniques used in competitive programming, computational geometry, and cryptographic systems. String algorithms power search engines and compilers. Number theory underlies cryptography. Polynomial operations accelerate signal processing and combinatorics. Mastery here puts you in the top 1% of algorithm engineers.

---

## C80 — Advanced Algorithms: Strings, Math & Number Theory (130 files)

### What is Covered

#### String Algorithms (001–040)

| Range | Topics |
|-------|--------|
| 001–010 | KMP: prefix function construction (full derivation), KMP search, Z-function, Z-algorithm for pattern matching |
| 011–020 | Rabin-Karp (single + multi-pattern), Boyer-Moore (bad-character + good-suffix heuristics) |
| 021–030 | Aho-Corasick (advanced: stream matching, dictionary links, counting matches per pattern) |
| 031–040 | Suffix array (prefix-doubling O(n log² n), SA-IS O(n)), LCP array (Kasai's algorithm), suffix automaton (DAWGs) |

#### Number Theory (041–080)

| Range | Topics |
|-------|--------|
| 041–050 | Sieve of Eratosthenes (segmented), linear sieve, Euler's totient (φ), Möbius function (μ), prime factorisation |
| 051–060 | GCD/LCM (extended), Bezout's identity, modular inverse (Fermat's little theorem, extended Euclidean) |
| 061–070 | Fast exponentiation (binary), modular exponentiation; Chinese Remainder Theorem (CRT); Lucas' theorem |
| 071–080 | Primality: Miller-Rabin probabilistic, deterministic (BPSW), Pollard's rho factorisation |

#### Polynomial & FFT (081–110)

| Range | Topics |
|-------|--------|
| 081–090 | Polynomial basics, polynomial multiplication (naïve O(n²)), FFT (Cooley-Tukey O(n log n)), IFFT |
| 091–100 | Number Theoretic Transform (NTT) — FFT over modular arithmetic; NTT-friendly primes |
| 101–110 | Polynomial division, polynomial inversion, polynomial log/exp (Newton's method), polynomial GCD |

#### Advanced Topics (111–130)

| Range | Topics |
|-------|--------|
| 111–120 | Integer FFT with modular arithmetic, convolution with multiple moduli (Garner's algorithm) |
| 121–130 | Sparse polynomial multiplication, polynomial composition, polynomial power, truncated exp, formal Laurent series, Dirichlet series convolution |

### Key Concepts Learned
- **KMP prefix function**: `π[i]` = length of longest proper prefix of `s[0..i]` that is also a suffix
- **Z-function**: `Z[i]` = length of longest string starting at `s[i]` matching a prefix of `s`
- **Suffix array**: stores sorted order of all suffixes; combined with LCP enables O(1) LCP queries
- **Miller-Rabin**: probabilistic primality test; use witnesses {2,3,5,7,11,13,17,19,23,29,31,37} for deterministic up to 3.3×10²⁴
- **FFT**: multiply polynomials in O(n log n) by converting to point-value form in frequency domain
- **NTT**: FFT over Z/pZ — avoids floating-point errors; useful for counting problems with modular arithmetic
- **Extended Euclidean**: `ax + by = gcd(a,b)` — find modular inverse when gcd = 1
- **CRT**: reconstruct unique `x mod (m₁·m₂·...·mₖ)` from x mod mᵢ values (pairwise coprime moduli)

### Algorithm Complexity Reference

| Algorithm | Time | Space | Use Case |
|-----------|------|-------|---------|
| KMP | O(n + m) | O(m) | Single pattern search |
| Rabin-Karp | O(n + m) avg | O(1) | Multi-pattern, rolling hash |
| Aho-Corasick | O(n + m + z) | O(m·σ) | Multiple patterns simultaneously |
| Suffix Array | O(n log n) | O(n) | All substring operations |
| FFT/NTT | O(n log n) | O(n) | Polynomial multiplication |
| Miller-Rabin | O(k log² n) | O(1) | Primality (k rounds) |
| Pollard's Rho | O(n^¼) | O(1) | Integer factorisation |
| Extended GCD | O(log min(a,b)) | O(1) | Modular inverse |

### Patterns Introduced
- **Polynomial hashing** — collision-resistant string fingerprinting
- **Convolution via FFT** — count of pairs summing to each value
- **Inclusion-exclusion + Möbius** — count integers with specific prime properties
- **CRT reconstruction** — combine residues to unique solution

### Cross-Links
- Rolling hash (C80) ↔ Hashing (Level 3, C32)
- KMP failure function (C80) ↔ Aho-Corasick (Level 6, C60)
- Bitmask DP for TSP (C80 context) ↔ Bitmask DP (Level 5, C50)
- NTT primes (C80) ↔ Modular arithmetic patterns in competitive (Level 9, C90)

---

## Level 8 — Revision Checklist

### String Algorithms
- [ ] Implement KMP failure function and KMP search from memory
- [ ] Implement Z-function and use it to find all occurrences of pattern in text
- [ ] Build suffix array with prefix-doubling and compute LCP with Kasai's
- [ ] Implement Rabin-Karp for multi-pattern search

### Number Theory
- [ ] Implement linear sieve (produces primes + smallest prime factor for all n ≤ N)
- [ ] Compute modular inverse using Fermat's little theorem AND extended GCD
- [ ] Implement CRT for two congruences
- [ ] Write Miller-Rabin with deterministic witnesses for n < 3.3×10²⁴

### Polynomials & FFT
- [ ] Implement Cooley-Tukey FFT (iterative, bit-reversal permutation)
- [ ] Use FFT to multiply two polynomials and verify result
- [ ] Implement NTT with prime 998244353
- [ ] Explain why NTT avoids FFT's floating-point precision issues

## Common Mistakes at Level 8

| Mistake | Correct Approach |
|---------|-----------------|
| KMP: computing `π` with O(n²) naïve | Use the two-pointer KMP definition directly |
| FFT: forgetting IFFT normalisation | Divide by n after IFFT |
| Suffix array: off-by-one in LCP array | Kasai's algorithm handles this carefully |
| Miller-Rabin: too few witnesses | Use ≥7 specific witnesses for deterministic results |
| Modular inverse: calling when `gcd(a,m) ≠ 1` | Verify gcd = 1 first; no inverse exists otherwise |
| CRT: multiplying large moduli causing overflow | Use `__int128` or multiply-then-mod carefully |

## Interview / Competitive Focus (Level 8 Topics)

| Problem | Algorithm | Complexity |
|---------|-----------|------------|
| String matching | KMP / Z-function | O(n + m) |
| Multiple pattern search | Aho-Corasick | O(n + m + z) |
| Polynomial multiplication | NTT | O(n log n) |
| Count distinct substrings | Suffix Array + LCP | O(n log n) |
| Modular inverse | Extended GCD | O(log n) |
| Is n prime? (large n) | Miller-Rabin | O(k log² n) |
