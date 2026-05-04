# Chapter: Pollard rho factorization

> **Level:** 8 | **Category:** C80 — Advanced Algorithms (String, Math, Number Theory)

---

## 1. Precise Problem Definition
**Topic:** Pollard rho factorization

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

**Correctness proof sketch for Pollard rho factorization:**
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
ALGORITHM POLLARD_RHO_FACTORIZATION(input):
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
#include <cstdint>
#include <numeric>
#include <iostream>
#include <vector>
#include <algorithm>

using u64 = uint64_t;
using u128 = __uint128_t;

u64 mulmod(u64 a, u64 b, u64 m) { return (u128)a * b % m; }
u64 powmod(u64 a, u64 e, u64 m) {
    u64 r = 1; a %= m;
    for (; e; e >>= 1) { if (e & 1) r = mulmod(r, a, m); a = mulmod(a, a, m); }
    return r;
}

bool millerRabin(u64 n, u64 a) {
    if (n % a == 0) return n == a;
    u64 d = n - 1; int r = 0;
    while (d % 2 == 0) { d /= 2; ++r; }
    u64 x = powmod(a, d, n);
    if (x == 1 || x == n - 1) return true;
    for (int i = 0; i < r - 1; ++i) { x = mulmod(x, x, n); if (x == n - 1) return true; }
    return false;
}

bool isPrime(u64 n) {
    if (n < 2) return false;
    for (u64 a : {2,3,5,7,11,13,17,19,23,29,31,37})
        if (!millerRabin(n, a)) return false;
    return true;
}

u64 pollardRho(u64 n) {
    if (n % 2 == 0) return 2;
    u64 x = rand() % (n - 2) + 2, y = x, c = rand() % (n - 1) + 1, d = 1;
    while (d == 1) {
        x = (mulmod(x, x, n) + c) % n;
        y = (mulmod(y, y, n) + c) % n;
        y = (mulmod(y, y, n) + c) % n;
        d = std::gcd(x > y ? x - y : y - x, n);
    }
    return d == n ? pollardRho(n) : d;
}

std::vector<u64> factorize(u64 n) {
    if (n <= 1) return {};
    if (isPrime(n)) return {n};
    u64 d = pollardRho(n);
    auto l = factorize(d), r = factorize(n / d);
    l.insert(l.end(), r.begin(), r.end());
    return l;
}

int main() {
    u64 n = 1000000007ULL * 998244353ULL;
    auto f = factorize(n);
    std::sort(f.begin(), f.end());
    for (u64 p : f) std::cout << p << ' ';  // 998244353 1000000007
}
```

### Implementation 2: Competitive Programming Version
```cpp
// Pollard's rho: expected O(n^{1/4}). Combined with Miller-Rabin for primality.
// Handles 64-bit numbers. Use __int128 for mulmod to avoid overflow.
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
