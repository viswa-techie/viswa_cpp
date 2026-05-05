# MASTER INDEX — viswa_cpp C++ Learning Curriculum

> **Repository:** `viswa-techie/viswa_cpp`  
> **Total Files:** ~2,400+ problem files across 23 categories  
> **Language:** C++17/20/23  
> **Scope:** Zero to Research-Level C++

---

## Curriculum at a Glance

```
Level 0-1  │ Beginner       │ Syntax → Arrays & Strings
Level 2-3  │ Intermediate   │ Pointers → STL → Data Structures
Level 4-5  │ Advanced       │ Trees/Graphs → DP → Heaps
Level 6-7  │ Expert         │ Advanced DS → Templates → Concurrency
Level 8-9  │ Pro            │ Algorithms → Systems → Competitive
Level 10   │ Master         │ C++ Future → Real-Time → Kernel
```

---

## Quick Navigation

| Level | File | Core Topics | Files | Difficulty |
|-------|------|-------------|-------|------------|
| 0 | [LEVEL_00](LEVEL_00_Syntax_DataTypes.md) | Syntax, Build, Data Types, Const/Constexpr | 246 | ★☆☆☆☆ |
| 1 | [LEVEL_01](LEVEL_01_ControlFlow_Functions_Arrays.md) | Control Flow, Recursion, Arrays, Strings | 366 | ★★☆☆☆ |
| 2 | [LEVEL_02](LEVEL_02_Pointers_OOP.md) | Pointers, Smart Ptrs, OOP, RAII | 245 | ★★★☆☆ |
| 3 | [LEVEL_03](LEVEL_03_STL_DataStructures.md) | STL, Linked Lists, Stacks, Hashing | 475 | ★★★☆☆ |
| 4 | [LEVEL_04](LEVEL_04_Trees_Graphs.md) | Trees, BST, Graph Fundamentals | 265 | ★★★★☆ |
| 5 | [LEVEL_05](LEVEL_05_DP_Heaps_Sorting.md) | Dynamic Programming, Heaps, Sorting | 260 | ★★★★☆ |
| 6 | [LEVEL_06](LEVEL_06_AdvancedTrees_AdvancedGraphs.md) | SegTree, Trie, DSU, Max-Flow, SCC | 250 | ★★★★★ |
| 7 | [LEVEL_07](LEVEL_07_Templates_Concurrency.md) | Templates, Concepts, Threads, Atomics | 240 | ★★★★★ |
| 8 | [LEVEL_08](LEVEL_08_AdvAlgorithms_Strings_Math.md) | KMP, FFT, NTT, Number Theory | 130 | ★★★★★ |
| 9 | [LEVEL_09](LEVEL_09_SystemDesign_Competitive.md) | Systems, SIMD, io_uring, Mo's, Geometry | 265 | ★★★★★ |
| 10 | [LEVEL_10](LEVEL_10_Master_Research.md) | C++26, Reflection, Contracts, eBPF | 120 | ★★★★★ |

**Total: ~2,862 files**

---

## Detailed Level Map

### Level 0 — Beginner: Syntax & Data Types
**→ [Full Level 0 Guide](LEVEL_00_Syntax_DataTypes.md)**

| Category | Dir | Files | Topics |
|----------|-----|-------|--------|
| C00 | `C00_Syntax_Program_Structure` | 130 | main(), headers, operators, preprocessor, scope, storage class, const/constexpr, build tools |
| C01 | `C01_Data_Types_Variables` | 116 | int/float/bool, fixed-width types, casts, string, optional, variant, bitfields, alignment, initialisation, type traits |

**Gateway skills:** Write + compile multi-file C++ · Use sanitisers · Understand UB · `std::optional` over -1 sentinels

---

### Level 1 — Beginner: Control Flow, Functions & Arrays
**→ [Full Level 1 Guide](LEVEL_01_ControlFlow_Functions_Arrays.md)**

| Category | Dir | Files | Topics |
|----------|-----|-------|--------|
| C10 | `C10_Control_Flow_Loops` | 120 | if/switch/ternary, while/for/range-for, break/continue, FizzBuzz, primes, sieve, digit ops, patterns |
| C11 | `C11_Functions_Recursion` | 122 | parameters, overloading, inline, constexpr, function ptrs, lambdas (captures/generic), backtracking, merge/quick sort, memoisation |
| C12 | `C12_Arrays_Strings_Core` | 124 | C-array/std::array/vector, binary search, Two Sum, Kadane's, Dutch flag, sliding window, prefix sum, rain water, sorting |

**Gateway skills:** Two pointers · Sliding window · Prefix sum · Backtracking template · Binary search

---

### Level 2 — Intermediate: Pointers & OOP
**→ [Full Level 2 Guide](LEVEL_02_Pointers_OOP.md)**

| Category | Dir | Files | Topics |
|----------|-----|-------|--------|
| C20 | `C20_Pointers_Memory` | 125 | pointer arithmetic, smart pointers (unique/shared/weak), RAII, Pimpl, memory model, ASan/Valgrind, false sharing, SoA |
| C21 | `C21_OOP_Classes` | 120 | constructors, Rule of 5, operator overloading, inheritance, virtual/vtable, CRTP, concepts in class, spaceship operator |

**Gateway skills:** RAII · Smart pointer ownership model · Virtual dispatch · Rule of 0/3/5 · Copy-and-swap

---

### Level 3 — Intermediate: STL, Linked Lists, Stacks & Hashing
**→ [Full Level 3 Guide](LEVEL_03_STL_DataStructures.md)**

| Category | Dir | Files | Topics |
|----------|-----|-------|--------|
| C22 | `C22_STL_Containers_Iterators` | 130 | vector/deque/list/set/map/unordered_*, iterators, algorithms, parallel STL, std::ranges, views |
| C30 | `C30_Linked_Lists` | 120 | singly/doubly/circular, Floyd's cycle, LRU cache, merge K sorted, skip list |
| C31 | `C31_Stacks_Queues` | 115 | monotonic stack, BFS queue, min-stack, histogram rectangle, circular buffer |
| C32 | `C32_Hashing` | 110 | hash functions, chaining, open addressing, rolling hash, bloom filter, consistent hash |

**Gateway skills:** LRU cache O(1) · Monotonic stack · Floyd cycle detection · Frequency map patterns

---

### Level 4 — Advanced: Trees & Graph Fundamentals
**→ [Full Level 4 Guide](LEVEL_04_Trees_Graphs.md)**

| Category | Dir | Files | Topics |
|----------|-----|-------|--------|
| C40 | `C40_Trees_BST` | 140 | all traversals, BST ops, LCA, AVL rotations, Fenwick tree, Trie, HLD intro, tree DP |
| C41 | `C41_Graphs_Fundamentals` | 125 | DFS/BFS, cycle detection, topological sort, Dijkstra, Bellman-Ford, DSU, Kruskal, Prim, Tarjan SCC |

**Gateway skills:** Topological sort · Dijkstra from memory · DSU with path compression · Fenwick tree · Trie

---

### Level 5 — Advanced: Dynamic Programming & Heaps/Sorting
**→ [Full Level 5 Guide](LEVEL_05_DP_Heaps_Sorting.md)**

| Category | Dir | Files | Topics |
|----------|-----|-------|--------|
| C50 | `C50_Dynamic_Programming` | 150 | linear DP, knapsack, interval DP, string DP, tree DP, bitmask DP, state machine DP, game theory DP |
| C51 | `C51_Heaps_PQ_Sorting` | 110 | binary heap, heapify, heap sort, priority_queue, K-way merge, median stream, all sorting algorithms |

**Gateway skills:** Identify DP archetype · Coin change · LIS O(n log n) · State machine (stocks) · Two-heap median

---

### Level 6 — Expert: Advanced Trees & Advanced Graphs
**→ [Full Level 6 Guide](LEVEL_06_AdvancedTrees_AdvancedGraphs.md)**

| Category | Dir | Files | Topics |
|----------|-----|-------|--------|
| C60 | `C60_Advanced_Trees_SegTree_Trie_DSU` | 130 | lazy seg tree, persistent seg tree, Aho-Corasick, suffix array, DSU rollback, HLD, centroid decomp, LCT, Treap |
| C61 | `C61_Advanced_Graph_Algorithms` | 120 | Dinic max-flow, MCMF, bipartite matching, Eulerian path, Hamiltonian, 2-SAT, bridges/AP, Floyd-Warshall |

**Gateway skills:** Lazy propagation · Dinic's max-flow · 2-SAT · HLD path queries · Suffix array + LCP

---

### Level 7 — Expert: Templates & Concurrency
**→ [Full Level 7 Guide](LEVEL_07_Templates_Concurrency.md)**

| Category | Dir | Files | Topics |
|----------|-----|-------|--------|
| C70 | `C70_Templates_Generic_Programming` | 120 | variadic templates, fold expressions, SFINAE, Concepts, type traits, TMP, policy design, CRTP, expression templates, type erasure, coroutines |
| C71 | `C71_Concurrency_Multithreading` | 120 | std::thread, mutex/condition_variable, atomics + memory orders, lock-free (CAS, ABA), futures, thread pool, parallel STL, coroutines |

**Gateway skills:** Write Concepts constraints · CAS loop · Thread pool · Memory order semantics · Coroutine generator

---

### Level 8 — Pro: Advanced Algorithms (Strings, Math, NT)
**→ [Full Level 8 Guide](LEVEL_08_AdvAlgorithms_Strings_Math.md)**

| Category | Dir | Files | Topics |
|----------|-----|-------|--------|
| C80 | `C80_Advanced_Algorithms_String_Math_NT` | 130 | KMP, Z-function, Rabin-Karp, Aho-Corasick, suffix array/automaton, linear sieve, Euler φ, Möbius, Miller-Rabin, Pollard's rho, FFT, NTT, polynomial ops |

**Gateway skills:** KMP from memory · NTT polynomial multiply · Miller-Rabin primality · Extended GCD · CRT

---

### Level 9 — Pro: System Design & Competitive Mastery
**→ [Full Level 9 Guide](LEVEL_09_SystemDesign_Competitive.md)**

| Category | Dir | Files | Topics |
|----------|-----|-------|--------|
| C81 | `C81_System_Design_Low_Level_CPP` | 120 | virtual memory, cache hierarchy, MESI, lock-free (hazard pointers, RCU, EBR), epoll, io_uring, SIMD (AVX2/NEON), branchless, bit tricks |
| C90 | `C90_Competitive_Programming_Mastery` | 145 | Mo's algorithm, sqrt decomp, HLD/centroid advanced, convex hull, game theory (Sprague-Grundy), randomised algorithms, matrix exponentiation, combinatorics |

**Gateway skills:** epoll event loop · SIMD vectorisation · Mo's offline queries · Matrix exponentiation · Convex hull

---

### Level 10 — Master: Research & Frontier C++
**→ [Full Level 10 Guide](LEVEL_10_Master_Research.md)**

| Category | Dir | Files | Topics |
|----------|-----|-------|--------|
| C100 | `C100_Expert_Research_Level` | 120 | C++23/26 (deducing this, expected, reflection, contracts, executors), real-time RT scheduling, WCET, seccomp, eBPF, NUMA mbind |

**Gateway skills:** std::expected chaining · Static reflection · Sender/receiver model · RT scheduling · eBPF programs

---

## Learning Paths

### Path A — Interview Preparation (FAANG)
```
Level 0 → Level 1 → Level 2 (C21 OOP) → Level 3 → Level 4 → Level 5 → stop
Estimated time: 3–6 months daily practice
Focus files: C12 arrays, C30-32 DS, C40-41 graphs/trees, C50 DP
```

### Path B — Competitive Programming
```
Level 0 → Level 1 → Level 3 (STL) → Level 4 → Level 5 → Level 6 → Level 8 → Level 9 (C90)
Estimated time: 6–12 months
Focus files: C50 DP, C60 seg tree/DSU, C61 max-flow, C80 strings/math, C90 Mo/matrix-exp
```

### Path C — Systems / Embedded Engineering
```
Level 0 → Level 1 → Level 2 (C20 memory) → Level 7 (C71 concurrency) → Level 9 (C81) → Level 10
Estimated time: 4–8 months
Focus files: C20 memory/sanitisers, C71 atomics/lock-free, C81 SIMD/io_uring, C100 real-time
```

### Path D — Full Mastery (Research)
```
All levels in order: 0 → 1 → 2 → 3 → 4 → 5 → 6 → 7 → 8 → 9 → 10
Estimated time: 18–24 months
```

---

## Algorithm Complexity Quick Reference

### Sorting
| Algorithm | Time | Space | Stable |
|-----------|------|-------|--------|
| `std::sort` | O(n log n) | O(log n) | No |
| Merge sort | O(n log n) | O(n) | Yes |
| Heap sort | O(n log n) | O(1) | No |
| Counting sort | O(n+k) | O(k) | Yes |
| Radix sort | O(d·n) | O(n) | Yes |

### Graph Algorithms
| Algorithm | Time | When to Use |
|-----------|------|-------------|
| BFS | O(V+E) | Shortest path (unweighted) |
| Dijkstra | O((V+E) log V) | Shortest path (non-negative weights) |
| Bellman-Ford | O(VE) | Negative weights, cycle detection |
| Floyd-Warshall | O(V³) | All-pairs shortest path |
| Kruskal MST | O(E log E) | Minimum spanning tree |
| Dinic max-flow | O(V²E) | Network flow |
| Tarjan SCC | O(V+E) | Strongly connected components |

### Data Structure Operations
| Structure | Access | Search | Insert | Delete |
|-----------|--------|--------|--------|--------|
| Array | O(1) | O(n) | O(n) | O(n) |
| Hash Map | O(1) avg | O(1) avg | O(1) avg | O(1) avg |
| Binary Search Tree | O(log n) | O(log n) | O(log n) | O(log n) |
| Heap | O(1) top | O(n) | O(log n) | O(log n) |
| Segment Tree | — | O(log n) | O(log n) | — |
| Trie | — | O(L) | O(L) | O(L) |

### DP Archetypes
| Pattern | State | Example |
|---------|-------|---------|
| Linear | `dp[i]` | Fibonacci, coin change |
| 2D Grid | `dp[i][j]` | Unique paths, min path sum |
| Knapsack | `dp[i][w]` | 0-1 knapsack, subset sum |
| Interval | `dp[l][r]` | Matrix chain, burst balloons |
| Bitmask | `dp[mask][i]` | TSP, assignment |
| Tree | `dp[node][state]` | Max independent set on tree |
| State machine | `dp[i][s]` | Stock with cooldown |

---

## Common Pitfalls Across All Levels

| Level | Biggest Trap | Fix |
|-------|-------------|-----|
| 0 | `using namespace std` in headers | Never; qualify with `std::` |
| 1 | Binary search with `(l+r)/2` overflow | Use `l + (r-l)/2` |
| 2 | Forgetting virtual destructor | Always `virtual ~Base() = default` |
| 3 | `map` when `unordered_map` needed | Choose based on order requirement |
| 4 | Dijkstra with negative edges | Use Bellman-Ford instead |
| 5 | 1D knapsack iterating forward | Iterate weight **reverse** for 0-1 |
| 6 | Lazy seg tree — no push_down | Always push before recursing |
| 7 | `volatile` for thread sync | Use `std::atomic<T>` |
| 8 | FFT without IFFT normalisation | Divide by n after IFFT |
| 9 | `epoll` ET without drain loop | Loop until `EAGAIN` |
| 10 | Heap alloc in real-time code | Static pools, stack allocation |

---

## Revision Strategy

### Daily (30 min)
1. Pick one file from your current level
2. Read the problem + approach
3. Write the solution from memory
4. Check edge cases + complexity

### Weekly (2 hours)
1. Complete one sub-category (10–15 files)
2. Use the level's Revision Checklist
3. Time yourself on 2–3 "Interview Focus" problems
4. Note any "Common Mistakes" you made

### Monthly
1. Complete one full Level
2. Ensure all checklist items are ticked
3. Attempt 2–3 LeetCode Hard problems from that level's domain
4. Move to next level

---

*Last updated: 2026-05-05 | Repository: viswa-techie/viswa_cpp | Branch: master*
