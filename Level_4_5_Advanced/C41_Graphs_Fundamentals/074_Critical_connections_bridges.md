# Chapter: Critical connections bridges

> **Level:** 4 | **Category:** C41 — Graphs — Fundamentals & Traversal

---

## 1. Problem Statement
Master the topic: **Critical connections bridges**.

**Examples:**
- **Simple:** small, unambiguous input.
- **Tricky:** edge case (empty / cycle / single node / overflow).
- **Maximum-constraint:** N up to 10^5 or 10^6 — must hit optimal complexity.

**Follow-ups:** What if the input is a stream? What if updates are interleaved with queries?

---

## 2. Category & Difficulty
- **Category:** Graphs — Fundamentals & Traversal
- **Sub-category:** Graph traversal (BFS/DFS) + Union-Find
- **Difficulty:** Medium → Hard
- **Interview frequency:** Common at FAANG; appears in system-design and on-site rounds.
- **Estimated solve time:** 20–35 min for a prepared candidate.

---

## 3. Prerequisites
- Adjacency list, BFS/DFS, Union-Find
- Big-O analysis; understanding of amortized cost
- Earlier problems in this category

---

## 4. Core Algorithmic Concept
Tarjan's bridge: edge (u,v) is bridge iff low[v] > disc[u].

**Why it works:** the algorithm maintains an invariant — at each step the partial solution is provably optimal/correct given the inputs seen so far.

**Mental model:** a network of nodes connected by edges — visit nodes systematically.

```
Visual:
  initial state  ──>  iteration  ──>  iteration  ──>  final
```

---

## 5. Recurrence / State Definition
Not a DP problem — see algorithm in section 4.

---

## 6. Solution Approaches

### Approach 1: Brute Force
```cpp
#include <vector>
void dfs(int u, int p, int& tm, std::vector<int>& disc, std::vector<int>& low,
         std::vector<std::vector<int>>& adj, std::vector<std::vector<int>>& out){
    disc[u]=low[u]=tm++;
    for(int v:adj[u]){
        if(v==p) continue;
        if(disc[v]==-1){
            dfs(v,u,tm,disc,low,adj,out);
            low[u]=std::min(low[u],low[v]);
            if(low[v]>disc[u]) out.push_back({u,v});
        } else low[u]=std::min(low[u],disc[v]);
    }
}
std::vector<std::vector<int>> bridges(int n, std::vector<std::vector<int>>& adj){
    std::vector<int> disc(n,-1), low(n,-1);
    std::vector<std::vector<int>> out; int tm=0;
    for(int i=0;i<n;++i) if(disc[i]==-1) dfs(i,-1,tm,disc,low,adj,out);
    return out;
}
int main(){return 0;}
```
**Time:** O(n²) or worse.  
**Space:** O(n).  
**Why it TLEs:** redundant recomputation.

### Approach 2: Optimal
```cpp
// O(V+E) single DFS.
int main(){return 0;}
```
**Time:** O(n log n) or O(n).  
**Space:** O(n) typical, often reducible to O(1) per state.  
**Insight:** use the right data structure (heap/queue/DSU).

---

## 7. Trace Through Example

| Step | State | Key Variables | Observation |
|------|-------|---------------|-------------|
| 1 | start | inputs loaded | initialize structures |
| 2 | iter 1 | first element | base case applied |
| 3 | iter 2 | partial result | recurrence/transition fires |
| 4 | mid | accumulating | invariant holds |
| 5 | near-end | almost done | final updates |
| 6 | end | answer ready | return |

---

## 8. Complexity Deep Dive
- **Time:** O(V+E) graph / O(n log n) sort/heap
- **Space:** O(V) visited / O(n) heap
- **Hidden constants:** hash collisions, cache misses, allocator overhead.
- **Cache:** Adjacency list = vector of vectors. BFS uses queue (deque-backed). Dijkstra uses min-heap.

| Approach | Time | Space |
|----------|------|-------|
| Brute | O(n²) or worse | O(n) |
| Optimal | O(n log n) or O(n) | O(n) or O(1) |

---

## 9. Edge Cases & Gotchas
1. Empty input / single element
2. All identical values
3. Already-sorted / reverse-sorted input
4. Integer overflow on sums or products
5. Self-loops, disconnected nodes, negative weights
6. Maximum N where naive recursion blows the stack
7. Concurrency: not thread-safe by default

---

## 10. Optimization Techniques
- **Space:** rolling array (DP), implicit tree pointers (Morris).
- **Time:** monotonic queue, binary search, segment/Fenwick tree.
- **Early termination:** stop when answer is provably found.
- **Pruning:** skip impossible branches in backtracking.

---

## 11. Code Quality & Production
- Replace raw `new`/`delete` with smart pointers in production trees/graphs.
- Avoid magic numbers; use `constexpr`.
- Unit tests: empty, single, two, large random, adversarial.
- Embedded: avoid recursion (stack-limited) — use iterative + explicit stack.

---

## 12. Pattern Recognition
- **Pattern:** Graph traversal (BFS/DFS) + Union-Find
- **When you see** shortest/connectivity question, **think** BFS or Dijkstra or Union-Find
- 5 similar problems: see neighboring entries in this category.

---

## 13. Practice Variants
- **Easy:** smaller bounds, no edge cases.
- **Medium:** add a constraint (no extra space, online queries).
- **Hard:** multi-dimensional state, parallel edges, weighted variants.
- **Competition:** N up to 10^6, 1-second TL.

---

## 14. Interview Playbook
- **First 2 min:** restate problem, ask about constraints (size, range, ties), give 1–2 examples.
- **Brute → optimal:** state brute, complexity, then identify bottleneck and remove it.
- **If stuck:** try smaller examples, consider what data structure gives O(1)/O(log n) for the operation needed.
- **Strong verbal:** "I'll use Graph traversal (BFS/DFS) + Union-Find. The invariant is X. Time O(?), space O(?). Edge cases: empty, single, max-N."

---

## 15. Quick Reference Card
- **Core idea:** Critical connections bridges — Graph traversal (BFS/DFS) + Union-Find.
- **Algorithm:** DFS/BFS or recurrence
- **Complexity:** O(V+E)
- **Don't forget:** (1) base cases, (2) edge cases, (3) overflow, (4) recursion depth, (5) cache friendliness.

---
*Compile:* `g++ -std=c++17 -O2 -Wall -Wextra main.cpp -o sol`
