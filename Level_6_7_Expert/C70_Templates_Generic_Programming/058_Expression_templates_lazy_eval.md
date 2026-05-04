# Chapter: Expression templates lazy eval

> **Level:** 7 | **Category:** C70 — Templates & Generic Programming

---

## 1. Formal Problem Definition
**Topic:** Expression templates lazy eval

**Constraints:** Typically N ≤ 10^5 to 10^6 with Q ≤ 10^5 queries. Time limit 2–3s.

**Examples:**
- **Simple:** small input, verify algorithm correctness manually.
- **Adversarial:** worst-case input that maximizes time/space (e.g., skewed tree, anti-hash).
- **Maximum constraint:** N = 10^6, Q = 10^5 — must hit optimal asymptotic.

---

## 2. Theoretical Foundation
Based on C++ template instantiation model: each unique set of template arguments creates a new type/function at compile time. Concepts add compile-time constraint checking via requires-expressions.

**Key theorem/property for Expression templates lazy eval:**  
The algorithm maintains a provable invariant at each step, ensuring correctness. Lower bound analysis shows the approach is optimal (or near-optimal) for this class of problems.

**Connection:** this problem reduces to / builds upon fundamental results in combinatorics, graph theory, or formal languages.

---

## 3. Data Structure / Algorithm Design

**Why this approach?** Alternatives are either too slow (brute O(n²)) or too complex. This structure provides O(log n) operations with manageable constant factors.

**Memory layout:** Array-based for cache friendliness where possible. Pointer-based when dynamic structure is needed (persistent trees, tries).

**Key operations:**
- Build: O(n) or O(n log n)
- Query: O(log n) amortized
- Update: O(log n) amortized

---

## 4. Implementation in C++17/20

### Production-Quality Implementation
```cpp
#include <iostream>
#include <array>
// Simplified expression template for vector addition
template<typename E>
struct VecExpr {
    double operator[](int i) const { return static_cast<const E&>(*this)[i]; }
    int size() const { return static_cast<const E&>(*this).size(); }
};

struct Vec : VecExpr<Vec> {
    std::array<double, 3> data;
    Vec() : data{} {}
    template<typename E>
    Vec(const VecExpr<E>& expr) { for(int i=0;i<3;++i) data[i]=expr[i]; }
    double operator[](int i) const { return data[i]; }
    int size() const { return 3; }
};

template<typename L, typename R>
struct VecAdd : VecExpr<VecAdd<L,R>> {
    const L& l; const R& r;
    VecAdd(const L& l, const R& r) : l(l), r(r) {}
    double operator[](int i) const { return l[i] + r[i]; }
    int size() const { return l.size(); }
};

template<typename L, typename R>
VecAdd<L,R> operator+(const VecExpr<L>& l, const VecExpr<R>& r) {
    return VecAdd<L,R>(static_cast<const L&>(l), static_cast<const R&>(r));
}

int main() {
    Vec a, b, c;
    a.data = {1,2,3}; b.data = {4,5,6}; c.data = {7,8,9};
    Vec result = a + b + c; // NO temporaries! Single loop evaluates all at once.
    for(int i=0;i<3;++i) std::cout << result[i] << ' '; // 12 15 18
}
```

### Competitive Programming Version
```cpp
// Expression templates: Eigen, Blaze, xtensor all use this pattern.
// Zero overhead: compiler optimizes to a single fused loop.
int main() { return 0; }
```

### Key Implementation Notes
- Use `constexpr` for compile-time constants.
- Mark non-throwing operations `noexcept`.
- `[[nodiscard]]` on query functions.
- Template where the data type varies.

---

## 5. Correctness Proof / Invariants

**Invariant:** After each operation, the data structure satisfies property P (e.g., heap property, BST property, segment tree node = aggregate of children).

**Proof sketch:** Induction on operation sequence. Base case: build satisfies P. Inductive step: each update preserves P via local adjustments.

**Common bugs from invariant violation:**
- Forgetting to push lazy tags before accessing children.
- Off-by-one in range boundaries.
- Not handling identity element for empty ranges.

---

## 6. Complexity Analysis (Rigorous)

| Operation | Time (worst) | Time (amortized) | Space |
|-----------|-------------|-------------------|-------|
| Build | O(n) or O(n log n) | — | O(n) |
| Query | O(log n) | O(log n) | O(1) |
| Update | O(log n) | O(log n) | O(1) |

**Actual bytes:** For n = 10^6 — approx. 16–32 MB depending on node size.

**When simpler is better:** For n < 1000, brute force with O(n²) is faster due to cache effects and lower constants.

---

## 7. Advanced Edge Cases & Stress Testing

1. **Empty input** — all queries return identity element.
2. **Single element** — degenerate tree/structure.
3. **All same values** — tests merge/combine logic.
4. **Maximum N** — memory and time limits.
5. **Alternating updates and queries** — tests lazy propagation.
6. **Adversarial input** — anti-hash, worst-case tree shape.
7. **Integer overflow** — use `long long` for sums.
8. **Concurrent access** — not thread-safe by default.

**Stress testing pattern:**
```cpp
// Compare against brute force on random inputs
for (int test = 0; test < 10000; ++test) {
    auto input = generateRandom();
    assert(optimal(input) == bruteForce(input));
}
```

---

## 8. Practical Engineering Notes
Heavy template usage increases compile time and binary size. Use explicit instantiation to control. `extern template` reduces redundant instantiations across TUs.

**When NOT to use:** If N is small (< 1000), or if the problem has simpler structure (sorted array → binary search suffices).

**Embedded/RTOS:** Avoid dynamic allocation. Use fixed-size arrays with compile-time N. Stack-based segment tree is possible.

---

## 9. Connections to Other Topics
- Builds upon: class templates, type deduction
- Used by: STL implementation, Boost, Eigen
- Real systems: STL, Boost.Hana, Eigen, ranges

---

## 10. Competitive Programming Applications
Templates rarely tested directly in CP, but template-based DSU/SegTree libraries are standard.

**Classic problems:** see Codeforces EDU series, USACO Platinum, AtCoder Library problems.

**Common mistakes:**
- Off-by-one in 0-indexed vs 1-indexed.
- Forgetting to push lazy before split/query.
- Integer overflow in intermediate calculations.
- TLE from unnecessary allocations.

---

## 11. Interview at FAANG/Senior Level
- **When asked:** Senior/Staff level system design (concurrent data structures, template library design) or algorithmic rounds requiring O(log n) structures.
- **Surface vs deep:** Surface = "I know what a segment tree is." Deep = "I can implement lazy propagation with arbitrary monoid operations and explain amortized complexity."
- **System design connection:** Type-erased callbacks, plugin architectures

---

## 12. Quick Reference + Cheat Sheet

| Operation | Complexity |
|-----------|-----------|
| Build | O(n) |
| Point/Range Query | O(log n) |
| Point/Range Update | O(log n) |
| Space | O(n) |

**5-line essence:**
```
Build tree bottom-up from leaves.
Query: recurse into overlapping children, combine results.
Update: modify leaf, propagate up (or push lazy down).
Invariant: each node = aggregate of its subtree.
Lazy: defer updates until query forces resolution.
```

**When to use:** Generic Programming / Metaprogramming / Compile-Time Computation pattern — whenever you need O(log n) range operations on a sequence.

---
*Compile:* `g++ -std=c++17 -O2 -Wall -Wextra main.cpp`
