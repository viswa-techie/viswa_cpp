# PROMPT 05 — Level 8 & Level 9: Upper Expert + Pro
## C++ Problem Solving — Book-Alike Deep Learning Guide

---

## HOW TO USE THIS PROMPT

These prompts generate deep-dive research-grade chapters for topics at the intersection of advanced algorithms, system-level C++, competitive programming mastery, and software engineering at scale.

---

## MASTER GENERATION PROMPT

```
===
You are writing a PROFESSIONAL-GRADE BOOK CHAPTER for an expert C++ engineer.
The reader is at Level 8–9 (Upper Expert to Pro).
They are mastering: Advanced Algorithms (String, Math, Number Theory, FFT/NTT),
System Design & Low-Level C++, and Competitive Programming at ICPC/IOI level.

Topic: {{PROBLEM_NAME}}

Generate a complete, authoritative learning chapter:

---

# Chapter: {{PROBLEM_NAME}}

## 1. Precise Problem Definition
- Mathematical formulation with all edge cases specified.
- 4 examples: trivial / normal / adversarial / maximum constraint.
- Known sources: LeetCode #, Codeforces problem ID, or paper reference.
- Hardness class: P / NP-complete / NP-hard / unknown.

## 2. Theoretical Deep Dive
- Full mathematical proof of correctness.
- Proof of time complexity (not just a claim).
- Lower bound argument (is this algorithm asymptotically optimal?).
- Connection to other theoretical problems (reductions if any).
- Historical development: who discovered it and when?

## 3. Algorithm Design & Analysis

### The Core Insight
- State the non-obvious insight in ONE sentence.
- Why does every naive approach fail?
- Mathematical structure being exploited (modular arithmetic, polynomial identity, FFT convolution, etc.)

### Algorithm Description
- Precise pseudocode (language-agnostic).
- Loop invariant and termination argument.
- All sub-routines named and explained.

### Complexity Proof
- Time: best / average / worst with formal argument.
- Space: exact formula for n elements.
- Amortized analysis if applicable (potential function method or aggregate method).

## 4. Reference Implementation (C++17/20)

### Implementation 1: Clean Pedagogical Version
- Well-commented, readable C++17.
- Every non-obvious line explained.
- Compile: `g++ -std=c++17 -O2 -Wall -Wextra`

### Implementation 2: Competitive Programming Version
- Optimized for speed: fast I/O, minimal overhead.
- GCC pragmas if needed: `#pragma GCC optimize("O3,unroll-loops")`
- SIMD / bitset tricks if applicable.
- `__int128` / `__builtin_*` usage if needed.

### Implementation 3: Production/Library Version
- Template class with proper C++20 concepts constraints.
- `[[nodiscard]]`, `noexcept`, proper move semantics.
- Thread-safety documentation.
- Memory: allocator-aware if applicable.

## 5. Mathematical Pre-Requisites
For this topic, the learner must know:
- [List all mathematical theorems/identities used]
- [Derivation of key formulas used in the algorithm]
- [Number theory / combinatorics / probability theory needed]
- [Worked examples of the math without any code]

## 6. Advanced Edge Cases & Stress Testing
- 8+ pathological inputs (designed to break common implementations).
- How to write a brute force verifier.
- How to stress test: random generation + comparison loop.
- Known online judges that have anti-hash / anti-sort tests.
- Numerical stability issues (for FFT/geometry).

## 7. Variations & Extensions
For each variation:
- Problem statement change
- Algorithm modification required
- Complexity change
List at least 6 meaningful variations.

## 8. Real-World Applications
- Where does this algorithm appear in production systems?
  (compilers, databases, OS kernels, signal processing, cryptography, etc.)
- Open-source code that implements this (with GitHub links).
- Papers that use or extend this algorithm.

## 9. System-Level Considerations (for Level 8 System topics)
- CPU cache behavior of this algorithm.
- Branch misprediction hot spots.
- SIMD vectorization potential.
- Memory bandwidth requirements.
- Latency vs throughput tradeoffs.
- Profiling with `perf` / `VTune`: what to expect.

## 10. Competitive Programming Playbook
- Template code ready to paste in a contest.
- 10+ classic problems that directly use this algorithm.
- How to identify this algorithm is needed from the problem statement.
- Common contest pitfalls (overflow, modular arithmetic, precision).
- Time pressure tips: what can be safely cut for speed?

## 11. Interview at Staff/Principal Engineer Level
- When and where does this come up in senior interviews?
- System design interview connection.
- What is the minimum you need to know vs deep expertise?
- What demonstrates mastery to an interviewer?

## 12. Quick Reference
- Algorithm in pseudocode (< 10 lines)
- Complexity table
- "This problem needs this algorithm when you see ______"
- Top 5 pitfalls to avoid

---
Code: C++17/20. Production quality + competitive quality variants both.
===
```

---

## PROBLEM BANK — LEVEL 8 & LEVEL 9

### LEVEL 8 — Upper Expert

#### Category C80: Advanced Algorithms (String, Math, Number Theory) (130 problems)

**Advanced String Algorithms (1–30)**
1. KMP pattern matching (full derivation)
2. KMP prefix function
3. Z-function pattern matching
4. Rabin-Karp multi-pattern matching
5. Boyer-Moore bad-character heuristic
6. Boyer-Moore good-suffix heuristic
7. Aho-Corasick multi-string search
8. Aho-Corasick on stream
9. Suffix array (SA-IS O(n))
10. Suffix array (O(n log n) DC3 / Skew)
11. LCP array Kasai's algorithm
12. LCP array sparse table
13. Longest repeated substring
14. Longest common substring (SA)
15. Count distinct substrings (SA)
16. Lexicographically smallest rotation
17. String period (KMP)
18. Shortest pattern with period
19. Longest palindrome (Manacher's algorithm)
20. Palindromic substrings count
21. Palindrome tree (eertree)
22. Suffix automaton (SAM) build
23. SAM longest common substring
24. SAM count substrings
25. SAM endpos sets
26. Online string matching
27. Two-dimensional pattern matching
28. Parameterized pattern matching
29. Approximate string matching (edit distance DP + bitmask)
30. Bitap algorithm (shift-or / shift-and)

**Number Theory (31–70)**
31. Sieve of Eratosthenes optimized
32. Linear sieve (Euler's sieve)
33. Segmented sieve
34. Bitset sieve
35. Trial division factorization
36. Pollard's rho factorization
37. Miller-Rabin primality test (deterministic bounds)
38. Lucas primality test
39. Fermat's little theorem
40. Euler's theorem
41. Modular exponentiation (fast power)
42. Modular inverse (Fermat's little theorem)
43. Modular inverse (extended GCD)
44. Extended Euclidean algorithm
45. Chinese Remainder Theorem (CRT)
46. Garner's algorithm (arbitrary modulus CRT)
47. Euler's totient function
48. Totient sieve
49. Möbius function
50. Möbius inversion
51. Dirichlet convolution
52. Multiplicative functions
53. Sum of divisors function (sigma)
54. Number of divisors function (tau)
55. Liouville function
56. Von Mangoldt function
57. Primitive root modulo p
58. Discrete logarithm (Baby-step Giant-step)
59. Pohlig-Hellman algorithm
60. Index calculus concept
61. Legendre symbol
62. Jacobi symbol
63. Quadratic reciprocity
64. Tonelli-Shanks square root mod p
65. Cipolla's algorithm
66. Lucas sequences
67. Pell's equation
68. Continued fractions
69. Stern-Brocot tree
70. Farey sequence

**Combinatorics & Generating Functions (71–100)**
71. Binomial coefficients (Pascal's triangle)
72. nCr mod p (Lucas' theorem)
73. nCr mod prime (precompute factorial + inverse)
74. Catalan number formula
75. Catalan applications (all 14 interpretations)
76. Stirling numbers 1st/2nd kind
77. Bell numbers (partition of sets)
78. Bernoulli numbers
79. Euler numbers
80. Derangements formula D(n)
81. Inclusion-exclusion principle
82. Inclusion-exclusion with Möbius
83. Burnside's lemma (Polya counting)
84. Polya enumeration theorem
85. Necklace counting
86. Bracelet counting
87. Lindström-Gessel-Viennot lemma
88. Lattice path counting
89. Generating functions basics
90. OGF (ordinary generating functions)
91. EGF (exponential generating functions)
92. GF for Fibonacci
93. Formal power series (addition, multiplication)
94. Polynomial multiplication (naive O(n²))
95. Polynomial GCD
96. Polynomial evaluation multi-point
97. Polynomial interpolation
98. Lagrange interpolation
99. Newton's forward difference interpolation
100. Berlekamp-Massey algorithm

**FFT / NTT & Polynomial Algorithms (101–130)**
101. DFT/IDFT basics
102. FFT (Cooley-Tukey radix-2)
103. FFT iterative (bit-reversal permutation)
104. FFT for polynomial multiplication
105. NTT (Number Theoretic Transform)
106. NTT prime choice (998244353)
107. NTT inverse
108. Karatsuba multiplication
109. Polynomial inverse (Newton's method)
110. Polynomial square root
111. Polynomial exp / log
112. Polynomial GCD (Euclidean)
113. Polynomial evaluation multi-point
114. Polynomial interpolation (multi-point)
115. Lagrange interpolation O(n log² n)
116. Newton's forward difference
117. Berlekamp-Massey + Kitamasa
118. Linear recurrence via matrix exponentiation
119. Sum of infinite polynomial series
120. Multivariate polynomial multiplication
121. Fast multiplication (GMP-style)
122. Floating-point FFT precision issues
123. Integer FFT with modular arithmetic
124. Convolution with multiple moduli (Garner)
125. Sparse polynomial multiplication
126. Polynomial composition
127. Polynomial power
128. Polynomial truncated exp
129. Formal Laurent series
130. Dirichlet series convolution (multiplicative functions)

---

#### Category C81: System Design & Low-Level C++ (120 problems)

**Memory Architecture (1–25)**
1. Virtual memory basics
2. Page table concept
3. TLB and cache concept
4. Cache hierarchy (L1/L2/L3) performance model
5. Cache miss types (cold, capacity, conflict)
6. MESI cache coherence protocol
7. False sharing (cache line collision) with measurement
8. NUMA architecture
9. Memory barriers (fence instructions)
10. Load-store reordering
11. Store buffer / invalidation queue
12. Sequential consistency model
13. Total store order (TSO) — x86 memory model
14. ARM relaxed memory model
15. C++ memory model formal (happens-before graph)
16. Data-race-free programs
17. Process vs thread creation cost
18. Context switch overhead measurement
19. User-mode vs kernel-mode transitions
20. System calls overhead (`strace` / `perf`)
21. `mmap` vs `malloc`
22. Huge pages and transparent huge pages
23. Copy-on-write pages
24. Demand paging
25. POSIX signals and `signal()` / `sigaction()`

**OS Interfaces & IPC (26–50)**
26. Signal handlers in C++ (async-signal-safe)
27. `fork` + `exec` pattern
28. Zombie process
29. Orphan process
30. Shared memory (POSIX shm)
31. Message queues (POSIX mq)
32. Named / unnamed pipes
33. Unix domain sockets
34. TCP/IP socket programming
35. Blocking vs non-blocking socket
36. `select` / `poll` / `epoll` comparison
37. `kqueue` (macOS/BSD)
38. `io_uring` (Linux 5.1+)
39. Event loop pattern implementation
40. Reactor vs Proactor pattern
41. IOCP (Windows)
42. Zero-copy networking (`sendfile()`)
43. DMA concept
44. Non-blocking I/O with `epoll`
45. Asynchronous I/O (POSIX AIO)
46. libuv event loop concept
47. `select` vs `epoll` scalability
48. Vectored I/O (`readv` / `writev`)
49. Memory-mapped files
50. File descriptor limits and `ulimit`

**Compilation & ABI (51–80)**
51. Compilation pipeline (cpp→asm→obj→exe)
52. ELF binary format
53. GOT and PLT (dynamic linking)
54. Position-independent code (PIC)
55. ASLR (address space layout randomization)
56. Stack canary (stack protection)
57. Stack frames and calling conventions
58. x86-64 System V calling convention
59. ARM AAPCS calling convention
60. Inline assembly basics
61. Compiler intrinsics (SSE/AVX)
62. SIMD vectorization
63. Auto-vectorization flags
64. Loop unrolling pragma
65. Profile-guided optimization (PGO)
66. Link-time optimization (LTO)
67. Devirtualization
68. Inlining decision heuristics
69. `constexpr` evaluation at compile time
70. Constant folding
71. Dead code elimination
72. Alias analysis
73. C++ ABI (Itanium ABI)
74. Name mangling rules
75. vtable ABI layout
76. RTTI layout
77. `dynamic_cast` ABI
78. Exception handling ABI (zero-cost exceptions)
79. Landing pads and call-site tables
80. Unwind tables (`.eh_frame`)

**Interop & Profiling (81–120)**
81. C interop (`extern "C"`)
82. C++ from Python (ctypes/cffi)
83. Python bindings (pybind11)
84. Node.js native addon (N-API)
85. JNI (Java Native Interface)
86. Rust FFI with C++
87. Profiling: `gprof`, `perf`, VTune
88. Flame graphs interpretation
89. PMU hardware counters
90. IPC (instructions per cycle)
91. Branch misprediction cost measurement
92. Speculative execution
93. Meltdown / Spectre mitigations
94. Prefetching strategies (`__builtin_prefetch`)
95. Cache-oblivious algorithms
96. Memory pool design
97. Slab allocator
98. `jemalloc` / `tcmalloc` internals
99. Huge page allocation
100. Memory-mapped files
101. Lock-free data structures theory
102. Wait-free progress guarantees
103. Obstruction-free progress
104. Real-time C++ constraints
105. Deterministic latency patterns
106. High-frequency trading C++ patterns
107. FPGA programming concept
108. Embedded C++ (no exceptions/RTTI)
109. Freestanding C++
110. CUDA C++ basics
111. GPU memory model
112. CUDA kernel launch parameters
113. SIMD on ARM (NEON intrinsics)
114. AVX-512 usage
115. Branchless programming patterns
116. Bitwise tricks for performance
117. Alignment-aware SIMD loads
118. `std::bit_floor`, `std::bit_ceil`, `std::popcount` (C++20)
119. Power-of-2 arithmetic tricks
120. Fast modulo without division

---

### LEVEL 9 — Pro

#### Category C90: Competitive Programming Mastery (150 problems)

**Advanced Data Structure Techniques (1–30)**
1. Mo's algorithm offline range queries
2. Mo's with updates
3. Mo's on trees
4. Sqrt decomposition (blocks)
5. Sqrt decomp range queries
6. Heavy path decomp advanced problems
7. Centroid decomp advanced problems
8. DSU on tree (Sack)
9. Virtual tree construction
10. Auxiliary tree queries
11. Offline LCA (Tarjan union-find)
12. Parallel binary search
13. CDQ divide and conquer (offline 3D)
14. Slope trick optimization
15. Aliens trick (lambda optimization / SMAWK)
16. SMAWK algorithm
17. Divide and conquer DP optimization
18. Convex hull trick (CHT)
19. Li Chao tree (line container)
20. Kinetic heaps concept
21. Sqrt decomp on segment tree
22. Block decomp for offline queries
23. Offline dynamic connectivity
24. Euler tour + DSU for subtree queries
25. Offline K-th ancestor queries
26. Offline LCT queries
27. Suffix array + LCP for string queries
28. Suffix automaton extended problems
29. Aho-Corasick + DP on automaton
30. Palindrome automaton + DP

**Advanced DP (31–50)**
31. DP profile (broken profile / plug DP)
32. Digit DP advanced
33. DP on strings (palindromes advanced)
34. DP on trees advanced (rerooting)
35. DP on graphs (shortest path gadgets)
36. DP with convex hull trick
37. DP with monotone queue optimization
38. DP SOS (sum over subsets)
39. Subset DP (bitmask all subsets)
40. SOS DP O(n·2^n)
41. DP on matroid intersection concept
42. DP Knuth optimization
43. Knuth-Yao speedup
44. Hirschberg space-optimized LCS
45. Four Russians method
46. Divide and conquer LCS
47. DP on intervals with offline
48. DP with persistence
49. DP with sqrt decomp
50. DP with segment tree optimization

**Computational Geometry (51–75)**
51. Computational geometry primitives
52. Cross product sign (CW/CCW)
53. Point in polygon (ray casting)
54. Convex hull Graham scan
55. Convex hull Andrew monotone chain
56. Jarvis march
57. Convex hull trick rotating calipers
58. Diameter of convex polygon
59. Closest pair of points (divide & conquer)
60. Voronoi diagram concept
61. Delaunay triangulation concept
62. Line sweep algorithm
63. Area of union of rectangles
64. Area of union of circles
65. Half-plane intersection
66. Minkowski sum
67. Rotating calipers technique
68. Point location in triangulation
69. Segment intersection (Bentley-Ottmann)
70. Shamos-Hoey algorithm
71. K-d tree (range queries 2D)
72. Range tree
73. Interval tree queries
74. Orthogonal range searching
75. Fractional cascading advanced

**Persistent Data Structures (76–90)**
76. Persistent segment tree
77. Persistent array
78. Persistent stack
79. Persistent queue
80. Persistent DSU
81. Persistent trie
82. Functional persistent data structures
83. Link-cut tree (full) for dynamic trees
84. Top tree for path decompositions
85. Offline persistent DS with time travel

**Game Theory (91–105)**
91. Sprague-Grundy theorem
92. Nimber computation
93. Nim game variants
94. Staircase Nim
95. Wythoff's Nim
96. Grundy values for Kayles
97. Grundy values for Turning Turtles
98. Green hackenbush
99. Blue-red hackenbush
100. Surreal numbers concept
101. Alpha-beta pruning
102. Minimax with memoization
103. Retrograde analysis
104. Endgame tablebase concept
105. Monte Carlo tree search (MCTS)

**Linear Algebra & Probability in CP (106–125)**
106. Matrix exponentiation O(k³ log n)
107. Fibonacci matrix expo
108. Counting paths of length n
109. Linear recurrence via Kitamasa
110. Gaussian elimination over GF(2)
111. XOR basis (linear basis)
112. Rank of matrix over GF(2)
113. Berlekamp-Massey + matrix expo
114. Gaussian elimination floating point
115. LU decomposition
116. QR decomposition concept
117. Eigenvalue power iteration
118. PageRank concept
119. Markov chains in CP
120. Expected value DP
121. Probability DP advanced
122. Linearity of expectation tricks
123. Contribution technique
124. Combinatorial identity proofs
125. Generating function approach to DP

**Advanced Flow & Matching (126–140)**
126. Project selection (min cut)
127. Closure problem (max flow)
128. MCMF minimum cost matching
129. Min cost flow with negative cycles
130. MCMF for assignment
131. Minimum weight closure
132. Hall's condition checking
133. Max flow decomposition
134. Gomory-Hu tree
135. Gomory-Hu cut tree
136. Parametric max flow
137. Undirected global min cut (Stoer-Wagner)
138. Randomized min cut (Karger's algorithm)
139. Isolating cuts technique
140. Maximum matching in general graphs (Blossom)

**Randomized Algorithms (141–150)**
141. Las Vegas vs Monte Carlo algorithms
142. Randomized quick select
143. Randomized quick sort analysis
144. Treap randomized
145. Skip list probabilistic analysis
146. Bloom filter false positive rate
147. Count-min sketch error analysis
148. Miller-Rabin error probability
149. Schwartz-Zippel lemma
150. Freivalds algorithm

---

## SUPPLEMENTARY PROBLEMS (Level 8–9 from online platforms)

### Codeforces (Div. 1 D/E Level)
- Educational CF: Advanced Segment Tree problems
- CF 840D: Destiny (Segment tree + persistent)
- CF 671D: Roads in Berland (MST + shortest path)
- CF 1558E: Optimal Segments (Li Chao tree)
- CF 755G: PolandBall and Many Other Balls (Matrix expo)
- CF 1063F: String Journey (Z-function + DP)
- CF 1063G: Expensive Strings (SAM + DP)

### USACO Platinum Level
- Centroid decomposition problems
- HLD + segment tree range queries
- Offline algorithms with rollback DSU
- Geometry: convex hull + rotating calipers

### AtCoder ABC/ARC/AGC
- AtCoder ABC D/E/F problems
- AtCoder AGC problems (Game theory, flow)
- AtCoder Educational DP contest

### LeetCode Hard (algorithmic)
- #745 Prefix and Suffix Search (Trie)
- #732 My Calendar III (Segment tree)
- #715 Range Module (Segment tree)
- #850 Rectangle Area II (Segment tree + coordinate compression)
- #1707 Maximum XOR With an Element From Array (Trie offline)

---

## LEARNING ROADMAP — Level 8 → Level 9

```
Week 1–3:   C80 (1–30)    Advanced string algorithms (KMP, Z, SA, SAM, Aho-Corasick)
Week 4–6:   C80 (31–70)   Number theory (sieve, factorization, modular arithmetic)
Week 7–8:   C80 (71–100)  Combinatorics, generating functions
Week 9–11:  C80 (101–130) FFT/NTT, polynomial algorithms
Week 12–14: C81 (1–50)    Memory architecture, OS interfaces, IPC
Week 15–17: C81 (51–120)  Compilation, ABI, profiling, SIMD
Week 18–19: C90 (1–30)    Advanced DS techniques (Mo's, sqrt, CDQ)
Week 20–21: C90 (31–75)   Advanced DP + Computational geometry
Week 22–23: C90 (76–105)  Persistent DS + Game theory
Week 24–26: C90 (106–150) Linear algebra in CP + Advanced flows + Randomized
```

---

## RESOURCES

| Resource | Link | Best For |
|----------|------|----------|
| Competitive Programmer's Handbook | https://cses.fi/book | CP fundamentals |
| KACTL (contest templates) | https://github.com/kth-competitive-programming/kactl | Reference implementations |
| CP-Algorithms | https://cp-algorithms.com | Deep algorithm explanations |
| Codeforces Blog (e-maxx) | CF | Classic algorithm articles |
| USACO Guide Platinum | https://usaco.guide | Structured platinum problems |
| Project Nayuki | https://www.nayuki.io | Number theory + algorithms |
| Stanford ICPC Notebook | GitHub | Contest reference |
- "The Art of Problem Solving" (math olympiad) | Book | Combinatorics + NT |
| CLRS (Cormen et al.) Chapters 15–35 | Book | Advanced algorithms |
| Algorithms (Sedgewick) | Book | Implementation-focused |
| Hacker's Delight | Book | Bit manipulation + low-level tricks |
| Computer Systems: A Programmer's Perspective | Book | Definitive systems book |
| perf wiki | https://perf.wiki.kernel.org | Linux performance tools |
| Brendan Gregg's blog | https://brendangregg.com | Systems performance |
| Godbolt Compiler Explorer | https://godbolt.org | SIMD, assembly analysis |
| Quick C++ Benchmarks | https://quick-bench.com | Micro-benchmarking |
