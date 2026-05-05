# Level 9 — Pro: System Design, Low-Level C++ & Competitive Mastery

> **Directory:** `Level_8_9_Pro/`  
> **Categories:** `C81_System_Design_Low_Level_CPP` · `C90_Competitive_Programming_Mastery`  
> **Total Files:** 120 + 145 = **265 files**  
> **Prerequisite:** Level 8 (Advanced Algorithms)  
> **Leads to:** Level 10 (Master / Research)

---

## Overview

Level 9 is the bridge between academic algorithm knowledge and production-grade systems engineering. C81 covers everything a principal/staff engineer needs: virtual memory, cache architecture, SIMD, lock-free data structures, NUMA, and systems programming with `epoll`/`io_uring`. C90 covers the full competitive programming toolkit: Mo's algorithm, matrix exponentiation, randomised algorithms, and probabilistic data structures.

---

## C81 — System Design & Low-Level C++ (120 files)

### What is Covered

#### Memory Architecture (001–030)

| Range | Topics |
|-------|--------|
| 001–010 | Virtual memory basics, page table concept, TLB and cache concept; cache hierarchy L1/L2/L3 performance model |
| 011–020 | Cache miss types (cold, capacity, conflict); MESI cache coherence protocol; false sharing cache-line collision measurement |
| 021–030 | NUMA architecture; huge pages (`mmap` with `MAP_HUGETLB`); memory-mapped files; custom allocators (slab, buddy) |

#### Concurrency & Lock-Free (031–060)

| Range | Topics |
|-------|--------|
| 031–040 | Lock-free stack (Michael-Scott), lock-free queue; hazard pointers; epoch-based reclamation (EBR) |
| 041–050 | RCU (Read-Copy-Update): publish-subscribe on shared data without locks; seqlock for writer-priority |
| 051–060 | Wait-free algorithms concept (progress guarantee); obstruction-free progress; Software Transactional Memory (STM) concept |

#### I/O & Networking (061–090)

| Range | Topics |
|-------|--------|
| 061–070 | Non-blocking I/O with `epoll` (edge-triggered vs level-triggered); `select` vs `poll` vs `epoll` comparison |
| 071–080 | `io_uring` submission queue / completion queue; zero-copy I/O; `sendfile`, `splice` |
| 081–090 | Reactor pattern implementation, proactor pattern, actor model concept, CSP (Communicating Sequential Processes) |

#### Performance Engineering (091–120)

| Range | Topics |
|-------|--------|
| 091–100 | SIMD intrinsics (SSE2/AVX2): `_mm_add_ps`, vectorised dot product, SIMD on ARM NEON |
| 101–110 | AVX-512 usage; branchless programming patterns; alignment-aware SIMD loads |
| 111–120 | Bitwise tricks: `std::bit_floor`, `std::bit_ceil`, `std::popcount` (C++20); power-of-2 arithmetic; fast modulo without division |

### Key Concepts Learned
- Cache line = 64 bytes; false sharing occurs when two threads write to different variables on the same cache line
- MESI protocol: Modified/Exclusive/Shared/Invalid — cache coherency state machine
- `epoll` is O(1) per event (kernel maintains event set); `select` is O(n) per call
- `io_uring` eliminates syscall overhead by using shared ring buffers between user and kernel space
- SIMD processes 4–16 floats per instruction — critical for signal processing and ML kernels
- Branchless code: replace `if/else` with arithmetic using `(condition ? a : b)` compiled to `cmov`
- Fast modulo: `x % (2^k) == x & (2^k - 1)` — works only for power-of-2 divisors

### Performance Hierarchy (Must Know)

| Operation | Approximate Cycles |
|-----------|-------------------|
| Register access | 1 |
| L1 cache hit | 4 |
| L2 cache hit | 12 |
| L3 cache hit | 40 |
| RAM access | 200 |
| SSD read | 50,000 |
| Network RTT (LAN) | 500,000 |
| Network RTT (WAN) | 50,000,000 |

### Patterns Introduced
- **Reactor** — single-thread event loop (Node.js model)
- **Proactor** — async I/O with completion callbacks (`io_uring`)
- **RCU** — high-read, low-write concurrent data sharing
- **Branchless arithmetic** — eliminate branch misprediction penalty
- **SoA vs AoS** — struct of arrays beats array of structs for SIMD

---

## C90 — Competitive Programming Mastery (145 files)

### What is Covered

#### Sqrt Decomposition & Offline Algorithms (001–020)

| Range | Topics |
|-------|--------|
| 001–010 | Mo's algorithm: offline range queries in O((n+q)√n); Mo's with updates; Mo's on trees |
| 011–020 | Sqrt decomposition blocks: range queries, range updates; block decomposition for general problems |

#### Advanced Tree Algorithms (021–040)

| Range | Topics |
|-------|--------|
| 021–030 | Heavy-Light Decomposition (advanced problems), centroid decomposition (advanced), DSU on tree (small-to-large merging / Sack) |
| 031–040 | Virtual tree (auxiliary tree for a subset of nodes), Kruskal reconstruction tree |

#### Geometry (041–060)

| Range | Topics |
|-------|--------|
| 041–050 | Convex hull (Graham scan, Jarvis march, Andrew's monotone chain); rotating calipers |
| 051–060 | Line intersection, half-plane intersection, Minkowski sum; closest pair of points (divide & conquer) |

#### Game Theory (061–080)

| Range | Topics |
|-------|--------|
| 061–070 | Sprague-Grundy theorem, Nim values (Grundy numbers), nimber arithmetic |
| 071–080 | Green Hackenbush, combinatorial game sums, Wythoff's game, misère games |

#### Randomised Algorithms (081–110)

| Range | Topics |
|-------|--------|
| 081–090 | Randomised quicksort analysis; reservoir sampling; Fisher-Yates shuffle |
| 091–100 | Bloom filter (false positive rate analysis), count-min sketch; HyperLogLog |
| 101–110 | Miller-Rabin error probability, Schwartz-Zippel lemma (polynomial identity testing), Freivalds' algorithm (matrix multiplication verification) |

#### Matrix & Combinatorics (111–130)

| Range | Topics |
|-------|--------|
| 111–120 | Matrix exponentiation: Fibonacci in O(log n), count paths of length k, linear recurrences |
| 121–130 | Combinatorics: Pascal's triangle modulo p, Lucas' theorem, Catalan numbers, Burnside's lemma (counting with symmetry) |

#### Final Mastery (131–145)

| Range | Topics |
|-------|--------|
| 131–145 | Randomised quicksort analysis, treap (randomised BST), skip list analysis, Bloom filter error rate, count-min sketch, Miller-Rabin error probability, Schwartz-Zippel lemma, Freivalds' algorithm |

### Key Concepts Learned
- Mo's algorithm: offline, sort queries by `(block(l), r)`, process in O((n+q)√n)
- Convex hull: Graham scan O(n log n); rotating calipers O(n) for diameter/width
- Sprague-Grundy: any impartial game position has a Grundy value; XOR of values determines winner
- Matrix exponentiation: compute `M^n` in O(k³ log n) — generalises any linear recurrence
- Reservoir sampling: uniform random sample of k from n items in O(n) with O(k) space
- Schwartz-Zippel: polynomial identity testing by random evaluation — error probability ≤ d/|F|
- HyperLogLog: estimates cardinality of large set with O(log log n) space and 2–3% error

### Patterns Introduced
- **Mo's algorithm** — offline sqrt-time range queries
- **Matrix exponentiation** — O(log n) linear recurrences
- **Sprague-Grundy** — reduce any impartial game to Nim
- **Randomised select** — quickselect O(n) expected
- **Reservoir sampling** — streaming uniform sampling

---

## Level 9 — Revision Checklist

### System Design / Low-Level
- [ ] Explain false sharing and write a benchmark demonstrating it
- [ ] Write an `epoll` event loop that handles 1000 concurrent connections
- [ ] Implement a lock-free stack with hazard pointers (ABA-safe)
- [ ] Write a vectorised dot product using AVX2 intrinsics
- [ ] Implement fast modulo for power-of-2 divisor and explain why it works
- [ ] Describe MESI protocol transitions for a two-core cache scenario

### Competitive Programming
- [ ] Implement Mo's algorithm for range sum queries with offline processing
- [ ] Use matrix exponentiation to compute F(10^18) mod 10^9+7
- [ ] Implement convex hull (Graham scan or monotone chain)
- [ ] Compute Grundy values for 4x4 Nim and determine winner
- [ ] Implement Bloom filter with k hash functions and compute false positive rate

## Common Mistakes at Level 9

| Mistake | Correct Approach |
|---------|-----------------|
| False sharing ignoring alignment | Pad struct to cache line size (`alignas(64)`) |
| `epoll` edge-triggered without loop | Must loop until `EAGAIN` in ET mode |
| Mo's algorithm online queries | Mo's requires offline sorting of queries |
| Matrix exp: wrong base matrix | Verify base matrix encodes the recurrence correctly |
| Bloom filter: too few hash functions | Optimal k = (m/n) · ln 2 |
| `io_uring` submission without ring drain | Must call `io_uring_submit` to flush SQ |

## Interview / Competitive Focus (Level 9)

| Topic | Skill |
|-------|-------|
| Cache performance | Measure L1/L2/L3 miss rates with `perf` |
| SIMD | Vectorise an inner loop manually |
| `io_uring` | Explain submission/completion queue model |
| Mo's algorithm | Offline range queries with sqrt-time |
| Matrix exponentiation | Fibonacci in O(log n) |
| Convex hull | Monotone chain from memory |
| Bloom filter | False positive formula derivation |
