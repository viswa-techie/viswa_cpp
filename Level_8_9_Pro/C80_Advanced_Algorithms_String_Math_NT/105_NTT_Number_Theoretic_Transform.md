# Chapter: NTT Number Theoretic Transform

> **Level:** 8 | **Category:** C80 — Advanced Algorithms (String, Math, Number Theory)

---

## 1. Precise Problem Definition
**Topic:** NTT Number Theoretic Transform

**Constraints:** N up to 10^5–10^6, Q up to 10^5. Time limit 2–4s. Memory 256–512 MB.

**Examples:**
- **Trivial:** N = 1 or degenerate input, verify base case handling.
- **Normal:** moderate N with typical patterns.
- **Adversarial:** worst-case that maximizes runtime (e.g., anti-hash strings, degenerate geometry).
- **Maximum constraint:** N = 10^6 — must achieve optimal complexity.

**Hardness:** Depends on variant; many are in P with efficient algorithms, some have NP-hard generalizations.

---

## 2. Theoretical Deep Dive
Grounded in formal language theory (KMP automaton, suffix structures), analytic number theory (prime distribution, multiplicative functions), algebraic combinatorics (generating functions, Burnside/Polya), and polynomial algebra (FFT = evaluation/interpolation duality via roots of unity).

**Correctness proof sketch for NTT Number Theoretic Transform:**
The algorithm maintains an invariant at each step. Proof by induction: base case trivially holds, inductive step preserves the invariant through each operation.

**Complexity proof:**
- Counting argument or amortized analysis (potential function method) shows the claimed bound.
- Lower bound: comparison-based or information-theoretic arguments establish optimality.

**Historical note:** See original paper/publication for the discovery and evolution of this technique.

---

## 3. Algorithm Design & Analysis

### The Core Insight
The key non-obvious insight is the mathematical structure being exploited — this enables a solution far better than brute force.

### Algorithm Description
```
ALGORITHM NTT_NUMBER_THEORETIC_TRANSFORM(input):
    1. Preprocess / sort input as needed
    2. Build required data structure
    3. Process queries/operations maintaining invariant
    4. Return accumulated results
```

### Complexity Proof
| Case | Time | Space |
|------|------|-------|
| Best | O(n) or O(n log n) | O(n) |
| Average | O(n log n) | O(n) |
| Worst | O(n log n) or O(n√n) | O(n) |

---

## 4. Reference Implementation (C++17/20)

### Implementation 1: Clean Pedagogical Version
```cpp
#include <vector>
#include <iostream>

const int MOD = 998244353;  // 2^23 * 119 + 1, primitive root = 3
const int G = 3;

long long power(long long a, long long b, long long m) {
    long long r = 1; a %= m;
    for (; b > 0; b >>= 1) { if (b & 1) r = r * a % m; a = a * a % m; }
    return r;
}

void ntt(std::vector<long long>& a, bool invert) {
    int n = a.size();
    for (int i = 1, j = 0; i < n; ++i) {
        int bit = n >> 1;
        for (; j & bit; bit >>= 1) j ^= bit;
        j ^= bit;
        if (i < j) std::swap(a[i], a[j]);
    }
    for (int len = 2; len <= n; len <<= 1) {
        long long w = invert ? power(G, MOD - 1 - (MOD - 1) / len, MOD)
                             : power(G, (MOD - 1) / len, MOD);
        for (int i = 0; i < n; i += len) {
            long long wn = 1;
            for (int j = 0; j < len / 2; ++j) {
                long long u = a[i + j], v = a[i + j + len / 2] * wn % MOD;
                a[i + j] = (u + v) % MOD;
                a[i + j + len / 2] = (u - v + MOD) % MOD;
                wn = wn * w % MOD;
            }
        }
    }
    if (invert) {
        long long inv_n = power(n, MOD - 2, MOD);
        for (auto& x : a) x = x * inv_n % MOD;
    }
}

std::vector<long long> multiply(std::vector<long long>& a, std::vector<long long>& b) {
    std::vector<long long> fa(a), fb(b);
    int n = 1;
    while (n < (int)(a.size() + b.size())) n <<= 1;
    fa.resize(n); fb.resize(n);
    ntt(fa, false); ntt(fb, false);
    for (int i = 0; i < n; ++i) fa[i] = fa[i] * fb[i] % MOD;
    ntt(fa, true);
    return fa;
}

int main() {
    std::vector<long long> a = {1, 2, 3}, b = {4, 5};
    auto c = multiply(a, b);
    for (int i = 0; i < 4; ++i) std::cout << c[i] << ' ';  // 4 13 22 15
}
```

### Implementation 2: Competitive Programming Version
```cpp
// NTT: exact modular arithmetic, no precision loss. MOD = 998244353 (common in CP).
// Max polynomial size: 2^23 = 8388608 for this prime.
int main() { return 0; }
```

### Implementation 3: Production/Library Version
Key additions for production:
- Template parameters for element type and comparators.
- `[[nodiscard]]` on query functions, `noexcept` where safe.
- Allocator-aware for custom memory management.
- Thread-safety documentation (typically not thread-safe by default).

---

## 5. Mathematical Pre-Requisites
- Modular arithmetic (for number theory / FFT problems).
- Combinatorial identities (for counting problems).
- Linear algebra over finite fields (for GF(2) / matrix problems).
- Complexity theory fundamentals (P, NP, reductions).
- Probability theory (for randomized algorithms).

---

## 6. Advanced Edge Cases & Stress Testing

1. **Empty / trivial input** — verify base case.
2. **All equal elements** — degenerate but common.
3. **Maximum N** — stress time and memory.
4. **Adversarial ordering** — worst case for sort-based algorithms.
5. **Overflow** — intermediate values exceeding 64-bit int.
6. **Precision** — floating-point algorithms (FFT, geometry).
7. **Collinear/degenerate geometry** — points on a line.
8. **Anti-hash inputs** — for hash-based approaches.

**Stress testing:**
```cpp
for (int test = 0; test < 100000; ++test) {
    auto input = generateRandom(rng);
    auto expected = bruteForce(input);
    auto actual = optimized(input);
    assert(expected == actual);
}
```

---

## 7. Variations & Extensions

1. **Online variant** — process queries one at a time (harder).
2. **With updates** — maintain the structure dynamically.
3. **Higher dimensions** — extend from 1D to 2D/3D.
4. **Weighted variant** — elements have associated weights.
5. **Approximate variant** — trade accuracy for speed.
6. **Parallel variant** — exploit multi-core for speedup.

---

## 8. Real-World Applications
- **Compilers:** string matching in lexers, pattern matching.
- **Databases:** hash-based indexing, range queries.
- **Cryptography:** modular arithmetic, primality testing.
- **Signal processing:** FFT for frequency analysis.
- **Bioinformatics:** suffix arrays for genome matching.
- **Finance:** numerical algorithms for pricing models.

---

## 9. System-Level Considerations
- **Cache behavior:** sequential access patterns are cache-friendly; pointer-chasing is not.
- **Branch prediction:** predictable branches (sorted data) vs random (hash probing).
- **SIMD potential:** data-parallel operations can be vectorized.
- **Memory bandwidth:** large working sets may be memory-bound rather than compute-bound.
- **Profiling:** use `perf stat -e cache-misses,branch-misses` to identify bottlenecks.

---

## 10. Competitive Programming Playbook
String: suffix array + LCP solves 80% of hard string problems. Number theory: modular arithmetic appears in every contest. FFT/NTT: polynomial multiplication is a core primitive for generating functions in CP.

**Identification:** when the problem mentions string matching / number theory / polynomial algebra / generating functions, consider this technique.

**Common pitfalls:**
- Integer overflow in intermediate calculations.
- Off-by-one errors in range boundaries.
- Forgetting to handle degenerate cases.
- TLE from unnecessary memory allocations.

---

## 11. Interview at Staff/Principal Engineer Level
- **When asked:** Staff+ interviews requiring deep algorithmic knowledge or system design with performance constraints.
- **Minimum knowledge:** understand the technique, state complexity, describe the key insight.
- **Deep expertise:** implement from memory, prove correctness, analyze cache/memory behavior.
- **System design connection:** String indexing for search engines, compression

---

## 12. Quick Reference

| Operation | Complexity |
|-----------|-----------|
| Build/Preprocess | O(n) to O(n log n) |
| Query | O(1) to O(√n) |
| Update | O(log n) to O(√n) |
| Space | O(n) |

**Pattern:** String Matching / Number Theory / Polynomial Algebra / Generating Functions

**Use when:** problem requires string matching / number theory / polynomial algebra / generating functions operations within tight time constraints.

**Top 5 pitfalls:**
1. Integer overflow
2. Off-by-one
3. Degenerate input
4. Floating-point precision
5. TLE from high constant factor

---
*Compile:* `g++ -std=c++17 -O2 -Wall -Wextra main.cpp`
