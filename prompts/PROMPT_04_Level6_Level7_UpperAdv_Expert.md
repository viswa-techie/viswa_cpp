# PROMPT 04 — Level 6 & Level 7: Upper Advanced + Expert
## C++ Problem Solving — Book-Alike Deep Learning Guide

---

## HOW TO USE THIS PROMPT

Paste the generation prompt below with `{{PROBLEM_NAME}}` filled in. These problems require deep CS theory combined with C++ mastery — the prompts generate research-grade learning chapters.

---

## MASTER GENERATION PROMPT

```
===
You are writing a GRADUATE-LEVEL BOOK CHAPTER for a senior C++ developer.
The reader is at Level 6–7 (Upper Advanced to Expert).
They are mastering: Advanced Tree structures (Segment Tree, Fenwick, Trie, Suffix Arrays,
DSU), Advanced Graphs (flows, matching, advanced decompositions), Generic Programming
(templates, TMP, concepts), and Concurrent/Multithreaded C++.

Topic: {{PROBLEM_NAME}}

Generate a complete, deep learning chapter:

---

# Chapter: {{PROBLEM_NAME}}

## 1. Formal Problem Definition
- Mathematical definition of the problem.
- Constraints with justification for why each matters.
- 3 examples: simple / adversarial / maximum constraint.
- Related open problems or research connections (if any).

## 2. Theoretical Foundation
- Formal theorem or lemma that underlies the algorithm.
- Proof sketch (not hand-waving — real CS reasoning).
- Time/space lower bound: is the optimal algorithm known?
- Connection to other theoretical CS problems (reduction, hardness).

## 3. Data Structure / Algorithm Design
For the KEY data structure or algorithm:
- Design choices: WHY this structure and not alternatives?
- Memory layout: how it looks in RAM (byte-level if relevant).
- Build / Construction: algorithm + complexity proof.
- Query / Update: algorithm + amortized analysis.
- Lazy propagation / path compression / splay: formal explanation.

## 4. Implementation in C++17/20
### Minimal Clean Implementation
- Full compilable C++17 code — production quality.
- Template where appropriate.
- Proper use of `constexpr`, `noexcept`, `[[nodiscard]]`.
- No undefined behavior.

### Optimized Implementation (for competitive programming)
- Compact, fast implementation with pragmas if needed.
- SIMD / bitset tricks if applicable.
- `__builtin_*` GCC intrinsics if they apply.

### Library / Reusable Component Version
- Template class with clean API.
- Iterator support if applicable.
- Thread-safety annotations.

## 5. Correctness Proof / Invariants
- State the invariant maintained throughout all operations.
- Prove or argue why operations preserve the invariant.
- What invariant violation causes known bugs?

## 6. Complexity Analysis (Rigorous)
- Time: per-operation, amortized, worst-case separately.
- Space: actual bytes for n elements.
- Constants: the real constant factors that affect wall-clock time.
- Comparison with naive approaches (table format).
- When does the constant factor make the theoretically better algorithm lose in practice?

## 7. Advanced Edge Cases & Stress Testing
- 7+ pathological inputs that break naive implementations.
- How to generate stress tests in C++.
- How to validate correctness against brute force.
- Known anti-hash / anti-sort inputs.

## 8. Practical Engineering Notes
- When to use this vs simpler alternatives (engineering judgment).
- Cache behavior: access pattern analysis.
- False sharing / NUMA effects in concurrent use.
- Embedded systems use: can this work without dynamic allocation?
- ABI considerations for library APIs.

## 9. Connections to Other Topics
- Which other Level 6–7 structures/algorithms use this as a building block?
- How does this appear in real systems? (Linux kernel, databases, compilers)
- Academic papers to read for deeper understanding.

## 10. Competitive Programming Applications
- Standard templates used in ICPC / Codeforces / USACO.
- 8+ classic problems solvable with this technique.
- Variations and combinations with other structures.
- Common mistakes in competitive implementation.

## 11. Interview at FAANG/Senior Level
- When would a senior SWE interview ask about this?
- System design interview connection (if applicable).
- What demonstrates deep understanding vs surface knowledge?
- Example conversation: good answer vs great answer.

## 12. Quick Reference + Cheat Sheet
- Core operations and complexities table.
- 5-line essence of the algorithm.
- "When to use" decision criteria.

---
Code: C++17/20, `g++ -std=c++17 -O2 -Wall -Wextra`. Production quality.
===
```

---

## PROBLEM BANK — LEVEL 6 & LEVEL 7

### LEVEL 6 — Upper Advanced

#### Category C60: Advanced Trees (Segment Tree, Fenwick, Trie, etc.) (130 problems)

**Segment Tree (1–30)**
1. Segment tree build (sum)
2. Point update / range query
3. Range update / point query (lazy propagation)
4. Range update / range query (lazy propagation)
5. Segment tree with max/min
6. Segment tree product queries
7. Segment tree GCD queries
8. Persistent segment tree
9. Merge sort tree (offline queries)
10. Fractional cascading
11. Segment tree beats (Ji driver segment tree)
12. Segment tree on strings
13. Dynamic segment tree (coordinate compression)
14. Implicit segment tree (pointer-based)
15. 2D segment tree (range 2D query)
16. Wavelet tree concept
17. Segment tree with lazy reset
18. Segment tree for range frequency queries
19. Segment tree for K-th smallest
20. Offline segment tree with events
21. Segment tree beats for chmin/chmax
22. Segment tree for interval scheduling
23. Segment tree with matrix multiplication nodes
24. Segment tree for LIS (O(n log n))
25. Segment tree for number of inversions
26. Segment tree for rectangle union area
27. Segment tree for painting problems
28. Merge sort tree for offline range K-th
29. Persistent segment tree for K-th smallest in range
30. Fractional cascading for multi-level binary search

**Fenwick Tree / BIT (31–50)**
31. BIT point update prefix sum
32. BIT range sum
33. BIT 2D (2D prefix sums)
34. BIT for inversion count
35. BIT for Kth element
36. BIT range update point query
37. BIT range update range query
38. BIT order statistics
39. Count smaller numbers after self (BIT)
40. Count of range sum (BIT + compress)
41. Reverse pairs (BIT)
42. BIT on compressed coordinates
43. BIT with offline sorting
44. BIT for LIS (O(n log n))
45. BIT for 2D inversions
46. BIT prefix XOR
47. BIT for merge sort
48. BIT with fractional cascading
49. BIT offline with sweepline
50. BIT for convolution

**Trie (51–75)**
51. Trie insert / search / startsWith
52. Trie delete
53. Count words in trie
54. Longest prefix match
55. Prefix search autocomplete
56. Word search II (trie + DFS)
57. Replace words with root
58. Maximum XOR of two numbers (trie)
59. Maximum XOR subarray
60. Minimum XOR pair
61. Sum of XOR of all pairs (trie)
62. Count pairs with XOR in range
63. Palindrome pairs (trie)
64. Concatenated words (trie + DP)
65. Design search autocomplete system
66. Stream of characters (trie)
67. Implement magic dictionary
68. Extra characters in string
69. Distinct substrings count (trie)
70. Lexicographically smallest subsequence
71. Boggle solver (trie + DFS)
72. Compressed trie (Patricia tree)
73. Suffix trie
74. Suffix array basics
75. Suffix array construction O(n log n)

**Suffix Structures & String Algorithms (76–95)**
76. LCP array (Kasai's algorithm)
77. Suffix automaton (SAM) build
78. SAM longest common substring
79. SAM count distinct substrings
80. SAM endpos sets
81. Online string matching
82. Aho-Corasick automaton build
83. Aho-Corasick on stream
84. KMP failure function
85. Z-function (Z-array)
86. Rabin-Karp rolling hash
87. Boyer-Moore basics
88. Longest repeated substring (SA + LCP)
89. Longest common substring (SA)
90. Count distinct substrings (SA)
91. String period (KMP)
92. Shortest pattern with given period
93. Longest palindrome (Manacher's algorithm)
94. Palindromic substrings count (Manacher's)
95. Palindrome tree (eertree)

**DSU / Union-Find (96–115)**
96. Union-Find array representation
97. Union by rank
98. Union by size
99. Path compression
100. Union by rank + path compression
101. Inverse Ackermann complexity proof
102. Number of connected components (DSU)
103. Minimum spanning tree (Kruskal)
104. Detect cycle (union-find)
105. Redundant connection
106. Accounts merge
107. Most stones removed (same row/col)
108. Satisfiability of equality equations
109. Smallest string with swaps
110. Number of islands (union-find)
111. Remove max edges (keep bipartite)
112. Graph connectivity queries offline
113. Dynamic connectivity offline
114. Link-cut tree concept
115. Offline LCA (Tarjan's offline algorithm)

**Balanced BSTs & Advanced Trees (116–130)**
116. Bipartite check with DSU (weighted DSU)
117. Weighted DSU (parity check)
118. DSU with rollback (offline)
119. Parallel binary search + DSU
120. AVL tree all rotation cases
121. AVL insert/delete balanced
122. Red-black tree coloring rules
123. RB insert rebalance
124. RB delete rebalance
125. Treap random priority
126. Treap split/merge operations
127. Treap implicit key (order statistics)
128. Splay tree zig/zig-zig/zig-zag
129. Skip list probabilistic analysis
130. Van Emde Boas tree concept

---

#### Category C61: Advanced Graph Algorithms (120 problems)

**Shortest Paths Advanced (1–25)**
1. Dijkstra proof of correctness (formal)
2. Dijkstra with decrease-key (Fibonacci heap)
3. Dijkstra on sparse vs dense graphs
4. Bellman-Ford proof of correctness
5. Bellman-Ford negative cycle detection
6. SPFA (Shortest Path Faster Algorithm)
7. SPFA with SLF optimization
8. Johnson's re-weighting algorithm
9. Floyd-Warshall all pairs
10. Floyd-Warshall path reconstruction
11. Floyd-Warshall negative cycle detection
12. Transitive closure
13. A* heuristic requirements (admissibility, consistency)
14. Consistent vs admissible heuristic
15. IDA* (iterative deepening A*)
16. Bidirectional Dijkstra
17. Contraction hierarchies concept
18. Hub labeling concept
19. ALT algorithm (landmarks)
20. Shortest path with forbidden transitions
21. Time-dependent Dijkstra
22. K-shortest paths (Yen's algorithm)
23. Shortest path with k edge constraint
24. Shortest path with resource constraint
25. APSP via matrix multiplication

**Network Flow (26–50)**
26. Max flow min cut theorem (formal proof)
27. Ford-Fulkerson (DFS augmenting paths)
28. Edmonds-Karp (BFS augmenting, O(VE²))
29. Dinic's algorithm (O(V²E))
30. Push-relabel algorithm
31. Highest-label push-relabel
32. Min-cost max-flow (MCMF)
33. MCMF with SPFA
34. MCMF with Dijkstra (Johnson potential)
35. SSP (Successive Shortest Paths)
36. Circulation with demands
37. Feasible flow (lower bounds)
38. Project selection (min cut)
39. Closure problem (max flow)
40. MCMF for assignment problem
41. Min cost flow with negative cycles
42. Minimum weight closure
43. Max flow decomposition into paths
44. Gomory-Hu tree
45. Gomory-Hu cut tree
46. Parametric max flow
47. Undirected global min cut (Stoer-Wagner)
48. Randomized min cut (Karger's algorithm)
49. Isolating cuts technique
50. Max flow with node capacities

**Matching & Covering (51–70)**
51. Bipartite matching (Hungarian DFS)
52. Hopcroft-Karp O(E√V)
53. Minimum vertex cover (König's theorem)
54. Maximum independent set bipartite
55. Maximum weight bipartite matching (Hungarian O(n³))
56. Assignment problem
57. General matching (Blossom algorithm concept)
58. Stable matching (Gale-Shapley)
59. Hall's condition checking
60. Maximum bipartite matching (all algorithms compared)
61. Online bipartite matching
62. Edge coloring bipartite graph
63. Vertex coloring (greedy, backtrack)
64. Interval scheduling maximization
65. Weighted interval scheduling
66. Set cover (NP-hard, greedy approx)
67. Maximum weighted independent set (special graphs)
68. Dominating set (trees)
69. Minimum path cover in DAG
70. Dilworth's theorem (antichains)

**SCC, Bridges, Euler (71–90)**
71. Kosaraju's SCC algorithm
72. Tarjan's SCC algorithm
73. SCC condensation DAG
74. SCC applications (feedback vertex set)
75. 2-SAT implication graph
76. 2-SAT solution extraction
77. 2-SAT with SCC
78. Bridges (Tarjan low-link)
79. Articulation points
80. Biconnected components (BCCs)
81. Block-cut tree
82. Bridge tree
83. 2-edge-connected components
84. Ear decomposition
85. Eulerian path existence conditions
86. Eulerian circuit (Hierholzer's algorithm)
87. Chinese postman problem (undirected)
88. Route inspection directed
89. De Bruijn sequence
90. Eulerian path reconstruction

**Tree Decompositions (91–120)**
91. Centroid decomposition
92. Heavy-light decomposition
93. Virtual tree (auxiliary tree)
94. Small-to-large merging (DSU on tree)
95. Sack (small-to-large DFS)
96. Mo's algorithm on trees
97. Path queries HLD + segment tree
98. Point update path max (HLD)
99. Subtree queries with Euler tour
100. LCT (Link-cut tree) access operation
101. LCT expose path
102. LCT link / cut operations
103. LCT aggregate on path
104. Top tree concept
105. ETT (Euler Tour Tree) concept
106. Functional graphs (Kth ancestor in O(log n))
107. Offline LCA with binary lifting
108. Online LCA with sparse table
109. Level ancestor query (ladder algorithm)
110. Weighted centroid decomposition
111. Distance queries on tree (centroid)
112. Subtree distance sums (rerooting DP)
113. Maximum path queries online (HLD + segtree)
114. Diameter queries under edge updates (LCT)
115. Dynamic tree connectivity (LCT)
116. Path update range query (HLD)
117. Sum of distances in tree (O(n))
118. Number of paths of length k (matrix expo)
119. Graph minor theory concept
120. Planarity testing concept

---

### LEVEL 7 — Expert

#### Category C70: Templates & Generic Programming (120 problems)

**Template Fundamentals (1–25)**
1. Function template basics
2. Class template basics
3. Template type parameters
4. Template non-type parameters
5. Template template parameters
6. Variadic templates (C++11)
7. Parameter pack expansion
8. Fold expressions (C++17)
9. Template specialization (full)
10. Template partial specialization
11. SFINAE basics (`enable_if`)
12. Substitution failure
13. `void_t` detection idiom
14. Detection idiom (`is_detected`)
15. Tag dispatch pattern
16. Overload sets and templates
17. Template argument deduction rules
18. CTAD (C++17)
19. CTAD deduction guides
20. Abbreviated templates (C++20 auto param)
21. Concepts basics (C++20)
22. `requires` expression
23. `requires` clause
24. Concept satisfaction
25. Concept subsumption

**Concepts & TMP (26–60)**
26. Concept-constrained functions
27. Concept-constrained class
28. Standard library concepts (`std::ranges::*`)
29. Projections in ranges
30. Constrained algorithms
31. Template metaprogramming (TMP) intro
32. Compile-time factorial
33. Compile-time Fibonacci
34. Compile-time GCD
35. Compile-time prime check
36. Type list
37. Type list operations (front/back/nth)
38. Type map
39. Tuple implementation from scratch
40. `tuple::get<N>`
41. `tuple::apply()`
42. Tuple zip
43. Integer sequence (`std::index_sequence`)
44. `std::make_index_sequence`
45. `std::apply` implementation
46. `std::integer_sequence` tricks
47. `if constexpr` for specialization
48. Type traits all `std::` traits
49. Custom type traits
50. Trait inheritance CRTP style
51. Reflection via traits
52. Policy classes
53. Policy-based data structures
54. Mixin pattern (CRTP)
55. Recursive inheritance
56. Linear inheritance list
57. Abstract policy interface
58. Expression templates (lazy eval)
59. ET for matrix addition
60. ET avoiding temporaries

**Advanced Generic Patterns (61–100)**
61. Eigen-style expression system
62. Proxy objects
63. Proxy for lazy evaluation
64. CRTP for static polymorphism
65. CRTP interface injection
66. CRTP counter
67. Template factory pattern
68. Type-safe builder
69. Named parameter idiom
70. Fluent interface template
71. Phantom types
72. Tagged types (strong typedef)
73. Type-safe units (dimensional analysis)
74. Meta-functions (unary/binary)
75. Meta-function class
76. Invocable meta-function
77. Higher-kinded types (simulated)
78. Template lambda (C++20)
79. Generic lambda internals
80. Polymorphic lambda
81. Overload set as type
82. `std::overload` pattern
83. Recursive variant visitor
84. `std::visit` with lambdas
85. Exhaustive variant match
86. Concept-based overloading
87. `requires requires` idiom
88. Concept diagnostics
89. Diagnostic messages with concepts
90. Friend function template
91. Template friend class
92. Dependent names (`typename`/`template`)
93. Two-phase name lookup
94. ADL (Argument-Dependent Lookup)
95. Koenig lookup
96. Hidden friends idiom
97. Namespace and ADL interactions
98. Template instantiation on demand
99. Explicit instantiation
100. `extern template` (C++11)

**Modules & Coroutines (101–120)**
101. Reducing compile times with templates
102. PCH with templates
103. Module system (C++20) basics
104. Module interface unit
105. Module implementation unit
106. Module partition
107. Importing `std` module
108. Reachability vs visibility in modules
109. Module linkage
110. Clang module map
111. Coroutine as template (C++20)
112. Coroutine promise type
113. Coroutine handle
114. Awaitable type
115. Generator coroutine (C++23 `std::generator`)
116. Async generator
117. Task coroutine type
118. Recursive coroutine
119. Coroutine scheduler implementation
120. io_uring with coroutines

---

#### Category C71: Concurrency & Multithreading (120 problems)

**Thread Basics (1–25)**
1. Thread creation (`std::thread`)
2. Thread join / detach
3. Thread id
4. `hardware_concurrency()`
5. Mutex basics (`std::mutex`)
6. `lock_guard<>`
7. `unique_lock<>`
8. `shared_mutex` (C++17)
9. `shared_lock` (readers-writer lock)
10. Recursive mutex
11. Timed mutex (`try_lock_for`)
12. Deadlock concept + example
13. Deadlock avoidance (lock ordering)
14. `std::lock()` for multiple mutexes
15. `std::scoped_lock` (C++17)
16. Livelock concept
17. Starvation concept
18. Priority inversion
19. Condition variable basics
20. `wait()` / `notify_one()` / `notify_all()`
21. Producer-consumer with condition variable
22. Bounded buffer (blocking)
23. Semaphore (C++20 `counting_semaphore`)
24. Binary semaphore
25. Barrier (C++20 `std::barrier`)

**Lock-Free & Atomics (26–60)**
26. Latch (C++20 `std::latch`)
27. Spinlock implementation
28. Ticket spinlock
29. MCS lock concept
30. CLH lock concept
31. Atomic types (`std::atomic<T>`)
32. `fetch_add` / `fetch_sub`
33. `compare_exchange_strong` / `weak`
34. `load` / `store` with memory orders
35. Memory order: relaxed, acquire, release, acq_rel, seq_cst
36. Happens-before relation
37. Synchronizes-with relation
38. Data race definition
39. Double-checked locking (broken vs fixed)
40. Singleton with atomic
41. Seqlock concept
42. RCU (read-copy-update) concept
43. Lock-free stack (Treiber stack)
44. Lock-free queue (Michael-Scott queue)
45. ABA problem
46. ABA with tagged pointer
47. Hazard pointers concept
48. Epoch-based reclamation
49. Thread pool implementation
50. Task queue with thread pool
51. Work stealing deque
52. `std::async`
53. `std::future` / `std::promise`
54. `std::packaged_task`
55. `std::shared_future`
56. Chaining futures
57. Continuation passing
58. Parallel algorithms (`std::execution::par`)
59. Parallel `for_each`
60. Parallel `transform`

**Parallel Patterns (61–90)**
61. Parallel sort
62. Parallel reduce
63. Vector SIMD concept
64. OpenMP basics (`#pragma omp parallel`)
65. OpenMP reduction clause
66. OpenMP schedule clause
67. OpenMP tasks
68. MPI concept (distributed memory)
69. Message passing model
70. Process vs thread
71. Green threads concept
72. Fibers (stackful coroutines)
73. C++20 coroutines (`co_await`/`co_yield`/`co_return`)
74. `io_uring` concept
75. IOCP concept (Windows)
76. Asio `io_context`
77. Asio `async_read` / `async_write`
78. Strand for thread safety in Asio
79. Asio coroutines
80. False sharing (cache line)
81. Padding to avoid false sharing
82. NUMA awareness
83. Thread affinity / CPU pinning
84. Memory fence instructions
85. Sequentially consistent fences
86. Dekker's algorithm
87. Peterson's algorithm
88. Lamport's bakery algorithm
89. Ticket lock
90. Readers-writers problem (all variants)

**Classic Concurrency Problems (91–120)**
91. Dining philosophers (5 solutions)
92. Sleeping barber problem
93. Cigarette smokers problem
94. Santa Claus problem
95. Bank account thread-safe class
96. Thread-safe singleton
97. Thread-safe queue STL wrapper
98. Thread-safe stack
99. Thread-safe LRU cache
100. Concurrent hash map concept
101. Folly `ConcurrentHashMap`
102. Thread sanitizer (TSan) usage
103. Helgrind (Valgrind)
104. DRD (Valgrind)
105. `perf stat` for multithreaded programs
106. Cache coherence protocols (MESI)
107. Store buffer and write combining
108. Load-store reordering on ARM
109. Sequential consistency model (x86 TSO)
110. C++ memory model formal (happens-before graph)
111. Async I/O event loop from scratch
112. Reactor pattern implementation
113. Proactor pattern implementation
114. Actor model concept
115. CSP (Communicating Sequential Processes)
116. STM (Software Transactional Memory) concept
117. Wait-free data structures (theory)
118. Obstruction-free progress
119. Non-blocking I/O with `epoll`
120. `io_uring` submission queue / completion queue

---

## SUPPLEMENTARY PROBLEMS (Level 6–7 additions)

### Competitive Programming (Codeforces / USACO / ICPC Level)
- Codeforces EDU: Segment Tree (Parts 1–3)
- Codeforces EDU: DSU (all problems)
- Codeforces EDU: Flows and Matching
- USACO Platinum: HLD problems
- USACO Platinum: Centroid decomposition
- AtCoder ABC/ARC: Segment tree beats
- LeetCode Hard: #327 (Count of Range Sum), #315 (Count Smaller), #493 (Reverse Pairs)
- LeetCode Hard: #295 (Find Median Stream), #239 (Sliding Window Max)

### Template / Metaprogramming Practice
- Implement `std::tuple` from scratch
- Implement `std::variant` from scratch
- Write a compile-time JSON parser
- Implement a type-safe printf
- Write a policy-based sorted container
- Implement `std::expected` (C++23)

---

## LEARNING ROADMAP — Level 6 → Level 7

```
Week 1–3:   C60 (1–30)    Segment tree all variants
Week 4–5:   C60 (31–50)   Fenwick tree + offline techniques
Week 6–7:   C60 (51–95)   Trie + suffix arrays + string algorithms
Week 8–9:   C60 (96–130)  DSU advanced + balanced BSTs + LCT concept
Week 10–11: C61 (1–50)    Advanced shortest paths + network flow
Week 12–13: C61 (51–90)   Matching, SCC, 2-SAT, Euler
Week 14–15: C61 (91–120)  Tree decompositions (HLD, centroid, LCT)
Week 16–17: C70 (1–60)    Templates, SFINAE, Concepts, TMP
Week 18–19: C70 (61–120)  Expression templates, modules, coroutines
Week 20–21: C71 (1–60)    Thread safety, atomics, lock-free
Week 22–24: C71 (61–120)  Parallel patterns, NUMA, memory model
```

---

## RESOURCES

| Resource | Link | Best For |
|----------|------|----------|
| CP-Algorithms | https://cp-algorithms.com | Segment tree, flows, matching |
| Codeforces EDU | https://codeforces.com/edu | Structured advanced problems |
| AtCoder Library (ACL) | https://github.com/atcoder/ac-library | Reference implementations |
| KACTL (KTH Library) | https://github.com/kth-competitive-programming/kactl | Competition templates |
| Competitive Programming 3 (Halim) | Book | ICPC-level algorithms |
| C++ Templates (Vandevoorde) | Book | Deep template metaprogramming |
| Modern C++ Design (Alexandrescu) | Book | Policy-based design |
| Effective Modern C++ (Meyers) | Book | C++11/14 best practices |
| C++ Concurrency in Action (Williams) | Book | Definitive concurrency guide |
| Preshing on Programming | https://preshing.com | Memory model + lock-free |
| 1024cores | https://www.1024cores.net | Lock-free data structures |
| Jeff Preshing's blog | https://preshing.com | Atomic operations |
| CppCon talks (YouTube) | YouTube | Expert C++ techniques |
| Jason Turner C++ Weekly | YouTube | Modern C++ features |
