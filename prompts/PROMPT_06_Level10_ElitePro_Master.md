# PROMPT 06 — Level 10: Elite Pro / Master
## C++ Problem Solving — Book-Alike Deep Learning Guide

---

## HOW TO USE THIS PROMPT

Level 10 is not about solving problems from a problem bank — it is about understanding the **frontiers of computing**: the C++ standard evolution, programming language theory, formal verification, compiler internals, distributed systems theory, and kernel-level C++. Use these prompts to generate deep research-level chapters.

---

## MASTER GENERATION PROMPT

```
===
You are writing a RESEARCH-GRADE TEXTBOOK CHAPTER for a master-level C++ engineer.
The reader is at Level 10 (Elite Pro / Master).
They are exploring: C++ language evolution (C++23/26), functional programming in C++,
formal verification, compiler internals (LLVM/GCC), distributed systems theory,
and kernel/RTOS-level C++.

Topic: {{TOPIC_NAME}}

Generate a complete, research-level learning chapter:

---

# Chapter: {{TOPIC_NAME}}

## 1. Formal Definition & Scope
- Precise technical definition (reference ISO C++ standard / relevant paper / RFC if applicable).
- Where this topic lives in the spectrum: language spec / compiler / OS / theory.
- Why this matters to an elite engineer (practical + theoretical importance).
- Current status: proposed / approved / in compilers / production-ready.

## 2. Historical Context & Motivation
- What problem does this solve that didn't have a good solution before?
- Who proposed it? (WG21 paper number, authors, date)
- What alternatives were considered and why were they rejected?
- How did this evolve from earlier C++ standards?

## 3. Formal Semantics
- Mathematical / logical specification of the feature or concept.
- For language features: BNF grammar fragment + type rules.
- For algorithms: formal proof of correctness.
- For distributed systems: formal model (state machine / message passing).
- For formal verification: Hoare triple or separation logic specification.

## 4. Design Principles & Tradeoffs
- Zero-overhead principle: does this add no cost if unused?
- Don't pay for what you don't use: analysis.
- ABI stability impact.
- Backward compatibility considerations.
- What was sacrificed to achieve the design goals?

## 5. Implementation Deep Dive
### Compiler Implementation (for language features)
- How does Clang/GCC/MSVC implement this?
- What IR is generated? (show LLVM IR snippet)
- Compile-time overhead.
- Diagnostic quality (error messages).

### Reference C++ Implementation
- Complete, standards-compliant C++23 code.
- Usage examples from 3 different domains.
- Common patterns and idioms.
- What NOT to do (anti-patterns with explanations).

### Real-World Usage
- Code from open-source projects (LLVM, Linux, Chromium, folly, abseil).
- How is this used differently in HFT / embedded / RTOS / OS kernels?

## 6. Interaction with Other Features
- Which other C++ features does this interact with (positively and negatively)?
- Known issues or bugs in compiler implementations.
- Undefined behavior traps specific to this feature.
- Surprising interaction with optimizations.

## 7. Formal Verification / Proof Obligations
For correctness-critical topics:
- What property should be verified?
- How to express this in TLA+ / Coq / Isabelle / Frama-C?
- Known verified implementations in literature.
- Practical tools: CBMC, KLEE, Z3 SMT solver usage.

## 8. Connection to Programming Language Theory
- Category theory connection (functor, monad, etc.) if applicable.
- Type theory connection (dependent types, linear types, etc.).
- Lambda calculus / denotational semantics connection.
- How would this be expressed in Haskell / Rust / Idris for comparison?

## 9. Performance Characteristics
- Compile-time: what is the cost to the build system?
- Runtime: zero-cost? What is the assembly output?
- Binary size impact.
- Debuggability: does this make debugging harder?
- Profiling: how does this appear in flame graphs?

## 10. Research Frontier
- What open problems remain in this area?
- Relevant academic papers (last 5 years).
- What is C++26 / C++29 planning in this area?
- Connections to active research (Rust, Carbon, Val, Swift evolution).

## 11. Mastery Assessment
- 5 deep questions that distinguish surface knowledge from mastery.
- A mini-project that requires integrating this topic with 3 others.
- How would you teach this topic? Design a 1-hour lecture.

## 12. Reference Card
- Feature / Algorithm in one paragraph.
- Key papers / standard references.
- Key companies using this at scale.
- 5 things that trip up even experts.

---
Code: C++20/23. Standards-correct. Cite WG21 papers where appropriate.
===
```

---

## PROBLEM BANK — LEVEL 10

#### Category C100: Expert / Research-Level C++ & CS (120 topics)

### Cluster A: C++ Language Evolution (1–20)
1. C++23 features overview (deducing `this`, `std::expected`, `std::flat_map`, `std::print`)
2. C++26 planned features (reflection TS, static reflection, contracts, executors)
3. Reflection TS proposal (P2996)
4. Static reflection (metaclasses concept — Herb Sutter's proposal)
5. Pattern matching (P1371 — inspect/match)
6. Executors (P2300 — `std::execution`)
7. Sender/receiver model
8. `std::execution` networking (P2762)
9. Contracts (P2521 — pre/postconditions)
10. Precondition / postcondition syntax
11. Invariant syntax
12. Safety profiles proposal (Bjarne Stroustrup)
13. Carbon language interop with C++
14. Circle C++ extension (Sean Baxter)
15. Val language design ideas
16. Safe C++ subset proposals
17. `std::generator` (C++23) full design
18. `std::expected<T,E>` full design
19. `std::mdspan` multi-dimensional spans
20. `std::linalg` (C++26 linear algebra)

### Cluster B: Functional Programming in C++ (21–35)
21. Functor concept (map) in C++
22. Monad concept (bind/flatMap) in C++
23. Applicative functor
24. Monoid in C++ (fold)
25. Free monad concept
26. Continuation monad (Cont monad)
27. Comonad concept
28. Arrows in functional programming
29. Lens optics in C++
30. Prism optics
31. Profunctor optics
32. Zippers in C++
33. Tagless final encoding
34. Expression problem in C++
35. Finally tagless DSL in C++

### Cluster C: Formal Verification & Program Correctness (36–50)
36. Hoare logic basics (`{P} C {Q}`)
37. Floyd-Hoare triples
38. Weakest precondition calculus
39. Loop invariant formal proof
40. Separation logic concept
41. Concurrent separation logic
42. Model checking (SPIN, TLA+)
43. TLA+ specification for a C++ system
44. SMT solvers (Z3) usage from C++
45. CBMC model checker
46. Frama-C analysis (WP plugin)
47. MISRA C++ compliance checking
48. Undefined behavior formal semantics (memory object model)
49. CompCert verified compiler concept
50. Verified data structures (Coq)

### Cluster D: Compiler Internals (51–70)
51. LLVM IR basics
52. LLVM pass writing (transform pass)
53. Clang AST traversal
54. LibTooling basics
55. Clang-Tidy check writing
56. MLIR dialect concept
57. GCC GIMPLE IR
58. GCC RTL IR
59. SSA form (Static Single Assignment)
60. Phi nodes
61. Dominator tree
62. Dominator frontier
63. Control flow graph
64. Liveness analysis
65. Register allocation (graph coloring)
66. Instruction selection (ISEL)
67. Instruction scheduling
68. Peephole optimization
69. Loop-invariant code motion (LICM)
70. Strength reduction

### Cluster E: Advanced Optimizations (71–80)
71. Vectorization analysis
72. Polyhedral model
73. Auto-vectorization with LLVM
74. Profile-guided optimization internals
75. Feedback-directed optimization
76. Whole program optimization (WPO)
77. Interprocedural analysis
78. Escape analysis
79. Scalar replacement of aggregates (SROA)
80. Speculative execution and mitigation

### Cluster F: Distributed Systems Theory (81–100)
81. CAP theorem formal statement and proof
82. PACELC theorem
83. Paxos consensus algorithm
84. Multi-Paxos
85. Raft consensus algorithm
86. Raft leader election
87. Raft log replication
88. Raft snapshots
89. Zab (Zookeeper Atomic Broadcast) protocol
90. Viewstamped replication
91. Byzantine fault tolerance (PBFT)
92. Tendermint BFT
93. Linearizability formal definition
94. Sequential consistency (formal)
95. Eventual consistency
96. CRDT (Conflict-free Replicated Data Types)
97. G-counter, PN-counter CRDT
98. OR-set CRDT
99. Vector clocks
100. Lamport clocks

### Cluster G: Advanced Systems Programming (101–120)
101. Hybrid logical clocks
102. Google Spanner TrueTime
103. Calvin deterministic database
104. CockroachDB MVCC
105. LSM tree (LevelDB / RocksDB)
106. B-tree vs LSM trade-offs
107. Custom memory allocator for OS
108. Lock-free OS data structures
109. Seqlock in Linux kernel
110. RCU (Read-Copy-Update) in Linux kernel
111. Futex implementation
112. Priority inheritance mutex
113. Real-time scheduling (POSIX RT, SCHED_FIFO)
114. WCET analysis
115. Interrupt latency in C++
116. DPC / softirq concept
117. NUMA memory policy in kernel
118. cgroups and memory limits
119. seccomp sandboxing from C++
120. eBPF programs from C++

---

## LEVEL 10 CAPSTONE PROJECTS

These are multi-week projects that synthesize Level 10 knowledge:

### Project 1: Write a Toy Compiler in C++
- Implement a subset of C (or a toy language) using LLVM IR.
- Topics covered: lexer, parser (recursive descent), semantic analysis, codegen.
- Use: LibTooling, LLVM API, SSA form, register allocation.
- Deliverable: compiler that translates your language to native x86-64 binary.

### Project 2: Distributed Key-Value Store
- Implement Raft consensus in C++.
- Use: `io_uring` for I/O, atomic operations, lock-free queues.
- Formally verify the leader election invariant with TLA+.
- Benchmark: linearizable reads under 1ms p99 latency.

### Project 3: Custom Memory Allocator
- Implement a jemalloc-like arena allocator from scratch.
- Support huge pages, NUMA awareness, thread-local caching.
- Benchmark against system malloc, TCMalloc, jemalloc.
- Measure: allocation latency, fragmentation, cache behavior.

### Project 4: Lock-Free Hash Map
- Implement a wait-free hash map using compare-exchange.
- Handle: ABA problem with tagged pointers, memory reclamation with hazard pointers.
- Verify with Thread Sanitizer and a model checker.
- Benchmark vs `std::unordered_map` with `std::mutex`.

### Project 5: Policy-Based Data Structure Library
- Design a generic sorted container with pluggable:
  - Comparison policy (total order, partial order)
  - Allocation policy (heap, pool, arena)
  - Threading policy (none, mutex, lock-free)
- Use C++20 Concepts to constrain policies.
- Zero overhead when policies are default.

### Project 6: Formal Verification of a C++ Algorithm
- Choose a well-known algorithm (LRU cache, red-black tree, lock-free stack).
- Write the algorithm in C++.
- Write its formal specification in TLA+ or Frama-C.
- Verify it with CBMC or Z3.
- Write a paper-style report of the proof.

---

## READING LIST — Level 10

### Papers (WG21 / Academic)
- P2996: Reflection for C++26 (Daveed Vandevoorde et al.)
- P2300: `std::execution` (Eric Niebler et al.)
- P0443: A Unified Executors Proposal
- "Composable C++ Coroutines" (Gor Nishanov)
- "Memory Model for C/C++" (Batty et al., POPL 2011)
- "Foundations of the C++ Concurrency Memory Model" (Boehm & Adve)
- "Raft: In Search of an Understandable Consensus Algorithm" (Ongaro & Ousterhout)
- "Spanner: Google's Globally Distributed Database"
- "CRDTs: Consistency Without Concurrency Control" (Shapiro et al.)
- "The Verified Software Toolchain" (AppEl et al.)

### Books
| Book | Author | Why Read It |
|------|--------|-------------|
| Programming Language Pragmatics | Scott | PL theory foundation |
| Types and Programming Languages | Pierce | Type theory |
| Software Foundations (Coq) | Pierce et al. | Formal verification |
| Category Theory for Programmers | Milewski | FP theory |
| Computer Architecture (Hennessy+Patterson) | H+P | Cache, NUMA, memory model |
| The Art of Multiprocessor Programming | Herlihy+Shavit | Lock-free DS theory |
| Engineering a Compiler | Cooper+Torczon | Compiler internals |
| Distributed Systems (van Steen) | van Steen | Distributed theory |
| Database Internals | Petrov | LSM, B-tree, MVCC |
| C++ Templates: The Complete Guide (2e) | Vandevoorde | Template metaprogramming |
| The Design and Evolution of C++ | Stroustrup | C++ philosophy |

### Projects / Codebases to Study
| Project | What to Learn |
|---------|--------------|
| LLVM / Clang | Template metaprogramming at scale, IR design |
| folly (Facebook) | Lock-free DS, coroutines, NUMA-aware code |
| abseil-cpp (Google) | Modern C++ patterns, portability |
| Redis | Event loop, I/O multiplexing, data structures |
| RocksDB | LSM tree, memory management, compaction |
| Linux kernel (selected files) | RCU, futex, memory model |
| CPython | C API, GIL, memory allocator |
| V8 (Node.js) | JIT, garbage collection |
| TiKV (Rust, but Raft impl) | Raft reference implementation |
| Seastar | Async C++ with io_uring |

---

## LEARNING ROADMAP — Level 10

```
Month 1:  C++23/26 features — implement everything, read WG21 papers
Month 2:  Functional programming in C++ — implement each FP concept
Month 3:  Formal verification — TLA+, CBMC, Frama-C, Z3 basics
Month 4:  Compiler internals — write an LLVM pass, study Clang AST
Month 5:  Distributed systems — implement Raft from scratch
Month 6:  Capstone projects — choose 2 from the list above
Ongoing:  Read 1 WG21 paper per week, study 1 open-source codebase per month
```

---

## SELF-ASSESSMENT MATRIX

Rate yourself (1–5) on each cluster:

| Cluster | Topic | 1-Novice | 3-Proficient | 5-Expert |
|---------|-------|----------|--------------|----------|
| A | C++ Language Evolution | | | |
| B | Functional Programming in C++ | | | |
| C | Formal Verification | | | |
| D | Compiler Internals | | | |
| E | Advanced Optimizations | | | |
| F | Distributed Systems Theory | | | |
| G | Systems Programming | | | |

**Target:** All clusters at 4+ before calling yourself Level 10.

---

## QUICK PROMPT FOR INDIVIDUAL TOPICS

```
===
I am studying {{TOPIC}} at an expert / research level.
I have strong C++ knowledge (all standard features through C++20).

Please generate:
1. Formal definition with mathematical notation
2. The key insight that makes this work (one sentence)
3. Complete C++23 implementation with documentation
4. Connection to 3 other Level 10 topics
5. The single most important paper to read on this
6. A 15-minute hands-on exercise to solidify understanding
===
```
