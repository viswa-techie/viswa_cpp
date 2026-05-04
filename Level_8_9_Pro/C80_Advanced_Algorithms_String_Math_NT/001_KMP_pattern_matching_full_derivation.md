# Chapter: KMP pattern matching full derivation

> **Level:** 8 | **Category:** C80 — Advanced Algorithms (String, Math, Number Theory)

---

## 1. Precise Problem Definition
**Topic:** KMP pattern matching full derivation

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

**Correctness proof sketch for KMP pattern matching full derivation:**
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
ALGORITHM KMP_PATTERN_MATCHING_FULL_DERIVATION(input):
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
#include <string>
#include <iostream>

// Compute KMP failure function (longest proper prefix-suffix)
std::vector<int> computeFailure(const std::string& pat) {
    int m = pat.size();
    std::vector<int> fail(m, 0);
    for (int i = 1, j = 0; i < m; ++i) {
        while (j > 0 && pat[i] != pat[j]) j = fail[j - 1];
        if (pat[i] == pat[j]) ++j;
        fail[i] = j;
    }
    return fail;
}

// KMP search: returns all match starting positions
std::vector<int> kmpSearch(const std::string& text, const std::string& pat) {
    std::vector<int> fail = computeFailure(pat);
    std::vector<int> matches;
    int n = text.size(), m = pat.size();
    for (int i = 0, j = 0; i < n; ++i) {
        while (j > 0 && text[i] != pat[j]) j = fail[j - 1];
        if (text[i] == pat[j]) ++j;
        if (j == m) {
            matches.push_back(i - m + 1);
            j = fail[j - 1];  // continue searching for overlapping matches
        }
    }
    return matches;
}

int main() {
    std::string text = "ababcababcabc";
    std::string pat = "abc";
    auto res = kmpSearch(text, pat);
    for (int pos : res) std::cout << pos << ' ';  // 2 7 10
    std::cout << '\n';
}
```

### Implementation 2: Competitive Programming Version
```cpp
// Competitive version — compact
#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(0); cin.tie(0);
    string t,p; cin>>t>>p;
    int n=t.size(),m=p.size();
    vector<int> f(m,0);
    for(int i=1,j=0;i<m;++i){
        while(j&&p[i]!=p[j])j=f[j-1];
        if(p[i]==p[j])++j;
        f[i]=j;
    }
    for(int i=0,j=0;i<n;++i){
        while(j&&t[i]!=p[j])j=f[j-1];
        if(t[i]==p[j])++j;
        if(j==m){cout<<i-m+1<<'\n';j=f[j-1];}
    }
}
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
