# Chapter: LLVM IR basics

> **Level:** 10 — Elite Pro / Master | **Cluster:** D — Compiler Internals

---

## 1. Formal Definition & Scope
**Topic:** LLVM IR basics

**Where this lives:** Compiler engineering / IR design

**Why this matters:** Elite engineers need to understand not just how to use features, but why they exist, how they're implemented, and what trade-offs were made. This topic represents the frontier of program compilation and optimization.

---

## 2. Historical Context & Motivation
Compiler theory: lexing (regular languages) → parsing (context-free grammars) → semantic analysis (type checking) → IR generation (SSA) → optimization passes → code generation (instruction selection + register allocation).

**Evolution:** This topic emerged from decades of research and industrial practice. Understanding its history reveals why current designs look the way they do and where they're headed.

---

## 3. Formal Semantics
- For language features: formal grammar + type rules per ISO standard.
- For algorithms: correctness proof via invariants or reduction.
- For distributed systems: state machine specification + safety/liveness properties.
- For verification: Hoare triples or separation logic assertions.

The formal treatment ensures precise reasoning about correctness and performance guarantees.

---

## 4. Design Principles & Tradeoffs
- **Zero-overhead principle:** does this add cost if unused? Generally yes — C++ features are designed for zero overhead.
- **ABI stability:** Not directly applicable.
- **Backward compatibility:** Implementation may require new tooling.

---

## 5. Implementation Deep Dive

### Reference C++ Implementation
```cpp
// Example: compile to LLVM IR with: clang -S -emit-llvm hello.cpp -o hello.ll
// hello.cpp:
#include <cstdio>
int add(int a, int b) { return a + b; }
int main() {
    int result = add(3, 4);
    printf("%d\n", result);
    return 0;
}

// Corresponding LLVM IR (simplified):
// define i32 @_Z3addii(i32 %a, i32 %b) {
//   %1 = add nsw i32 %a, %b
//   ret i32 %1
// }
//
// define i32 @main() {
//   %1 = call i32 @_Z3addii(i32 3, i32 4)
//   %2 = call i32 (i8*, ...) @printf(i8* getelementptr(...), i32 %1)
//   ret i32 0
// }

// Key IR features:
// - SSA: each variable assigned exactly once (%1, %2, ...)
// - Typed: i32, i64, float, ptr, [N x T], {T1, T2}
// - Instructions: add, sub, mul, icmp, br, phi, call, ret, load, store
// - Metadata: !dbg, !tbaa for debug info and aliasing
```

### Alternative / Competitive Version
```cpp
// Tools:
// clang -S -emit-llvm file.cpp -o file.ll  # generate IR
// llc file.ll -o file.s                     # IR to assembly
// opt -O2 file.ll -S -o file_opt.ll         # run optimization passes
// lli file.ll                                # interpret IR directly
// llvm-dis file.bc -o file.ll               # bitcode to text
// llvm-as file.ll -o file.bc                # text to bitcode
int main() { return 0; }
```

### Real-World Usage
- Used in production by: LLVM, GCC, MSVC compiler backends

---

## 6. Interaction with Other Features
- Interacts with: link-time optimization, debug info, sanitizers
- Known pitfalls: undefined behavior edges, compiler-specific extensions, platform dependencies.

---

## 7. Formal Verification / Proof Obligations
Verification is recommended for correctness-critical usage:
- Safety: the system never enters an invalid state.
- Liveness: the system eventually makes progress.
- Tools: TLA+ (distributed protocols), Frama-C (C programs), CBMC (bounded model checking), Z3 (SMT solving).

---

## 8. Connection to Programming Language Theory
- **Type theory:** Type systems can encode correctness properties.
- **Category theory:** Categorical semantics of programming constructs.
- **Comparison:** How would this be expressed in MLIR/Cranelift (alternative IRs)?

---

## 9. Performance Characteristics
- **Compile-time:** Optimization passes add to compile time; PGO requires two builds.
- **Runtime:** Zero-cost abstraction where possible; profile to verify.
- **Debuggability:** Optimized code may be harder to debug; use -O0 + sanitizers.

---

## 10. Research Frontier
- **Open problems:** active areas of research and standardization.
- **C++26/29 direction:** MLIR unification, machine learning in compilers.
- **Related languages:** Rust, Carbon, Val, Circle, Swift — each exploring different design points.

---

## 11. Mastery Assessment

**5 deep questions:**
1. What is the fundamental trade-off this feature/concept addresses?
2. How does the implementation handle the hardest edge case?
3. What formal property does this maintain, and how would you prove it?
4. Where does this appear in a real production system you've used?
5. If you could redesign this from scratch, what would you change?

**Mini-project:** Implement a simplified version that integrates with 2-3 other Level 10 topics.

---

## 12. Reference Card

**In one paragraph:** LLVM IR: typed SSA-form intermediate representation. Three forms: human-readable (.ll), bitcode (.bc), in-memory.

**Key references:**
- ISO C++ Standard (latest draft: N4950+)
- Relevant WG21 papers (see proposal numbers)
- Academic papers in the reading list

**Pattern:** Compiler IR / Optimization Passes / Code Generation

**5 expert pitfalls:**
1. Confusing specification with implementation (compilers may differ).
2. Assuming a feature is zero-cost without measuring.
3. Ignoring ABI implications for library interfaces.
4. Not testing with multiple compilers (GCC, Clang, MSVC).
5. Over-abstracting when simplicity would suffice.

---
Writing LLVM passes: use the new PassManager API. Start with analysis passes (read-only) before transform passes. LibTooling for source-level transformations, Clang-Tidy for lint rules.

*Compile:* `g++ -std=c++23 -O2 -Wall -Wextra main.cpp` (or `-std=c++2b` for bleeding edge)
