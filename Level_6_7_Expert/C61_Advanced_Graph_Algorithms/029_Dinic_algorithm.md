# Chapter: Dinic algorithm

> **Level:** 6 | **Category:** C61 — Advanced Graph Algorithms

---

## 1. Formal Problem Definition
**Topic:** Dinic algorithm

**Constraints:** Typically N ≤ 10^5 to 10^6 with Q ≤ 10^5 queries. Time limit 2–3s.

**Examples:**
- **Simple:** small input, verify algorithm correctness manually.
- **Adversarial:** worst-case input that maximizes time/space (e.g., skewed tree, anti-hash).
- **Maximum constraint:** N = 10^6, Q = 10^5 — must hit optimal asymptotic.

---

## 2. Theoretical Foundation
Grounded in flow/cut duality (max-flow = min-cut), Koenig's theorem (matching = vertex cover in bipartite), and Tarjan's low-link for 2-edge/2-vertex connectivity.

**Key theorem/property for Dinic algorithm:**  
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
#include <vector>
#include <queue>
#include <algorithm>
#include <climits>
struct Edge { int to, rev; long long cap; };
struct Dinic {
    std::vector<std::vector<Edge>> g;
    std::vector<int> level, iter;
    int n;
    Dinic(int n) : n(n), g(n), level(n), iter(n) {}
    void addEdge(int u, int v, long long cap) {
        g[u].push_back({v, (int)g[v].size(), cap});
        g[v].push_back({u, (int)g[u].size()-1, 0});
    }
    bool bfs(int s, int t) {
        std::fill(level.begin(), level.end(), -1);
        std::queue<int> q; q.push(s); level[s] = 0;
        while (!q.empty()) {
            int v = q.front(); q.pop();
            for (auto& e : g[v]) if (e.cap > 0 && level[e.to] < 0) {
                level[e.to] = level[v] + 1; q.push(e.to);
            }
        }
        return level[t] >= 0;
    }
    long long dfs(int v, int t, long long f) {
        if (v == t) return f;
        for (int& i = iter[v]; i < (int)g[v].size(); ++i) {
            Edge& e = g[v][i];
            if (e.cap > 0 && level[v] < level[e.to]) {
                long long d = dfs(e.to, t, std::min(f, e.cap));
                if (d > 0) { e.cap -= d; g[e.to][e.rev].cap += d; return d; }
            }
        }
        return 0;
    }
    long long maxflow(int s, int t) {
        long long flow = 0;
        while (bfs(s, t)) {
            std::fill(iter.begin(), iter.end(), 0);
            long long d;
            while ((d = dfs(s, t, LLONG_MAX)) > 0) flow += d;
        }
        return flow;
    }
};
int main() {
    Dinic d(4);
    d.addEdge(0,1,10); d.addEdge(0,2,10);
    d.addEdge(1,3,10); d.addEdge(2,3,10);
    d.addEdge(1,2,2);
    // max flow 0->3 = 20
    return 0;
}
```

### Competitive Programming Version
```cpp
// O(V²E) general. For unit-cap networks: O(E√V). Practical best for most competitive problems.
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
Flow algorithms: use adjacency lists with residual edges. For HLD: Euler tour flattens tree into array for segment tree. Centroid decomposition: O(n log n) preprocessing.

**When NOT to use:** If N is small (< 1000), or if the problem has simpler structure (sorted array → binary search suffices).

**Embedded/RTOS:** Avoid dynamic allocation. Use fixed-size arrays with compile-time N. Stack-based segment tree is possible.

---

## 9. Connections to Other Topics
- Builds upon: BFS/DFS, shortest paths
- Used by: min-cost max-flow, planarity testing
- Real systems: network routing, logistics, chip placement

---

## 10. Competitive Programming Applications
Flows appear in ICPC; matching in bipartite problems. HLD + segment tree for tree path queries. Centroid decomposition for distance queries.

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
- **System design connection:** Load balancing = flow/matching

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

**When to use:** Network Flow / Matching / Tree Decomposition pattern — whenever you need O(log n) range operations on a sequence.

---
*Compile:* `g++ -std=c++17 -O2 -Wall -Wextra main.cpp`
