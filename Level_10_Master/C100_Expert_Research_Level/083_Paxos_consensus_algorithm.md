# Chapter: Paxos consensus algorithm

> **Level:** 10 — Elite Pro / Master | **Cluster:** F — Distributed Systems Theory

---

## 1. Formal Definition & Scope
**Topic:** Paxos consensus algorithm

**Where this lives:** Distributed computing theory / Consensus

**Why this matters:** Elite engineers need to understand not just how to use features, but why they exist, how they're implemented, and what trade-offs were made. This topic represents the frontier of building reliable distributed systems.

---

## 2. Historical Context & Motivation
Distributed computing theory: FLP impossibility (no deterministic consensus with one crash failure in async model), CAP theorem (choose 2 of 3), and consensus protocols (Paxos, Raft) that work with timing assumptions.

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
- **Zero-overhead principle:** does this add cost if unused? N/A — this is a design/theoretical concept.
- **ABI stability:** Not directly applicable.
- **Backward compatibility:** Implementation may require new tooling.

---

## 5. Implementation Deep Dive

### Reference C++ Implementation
```cpp
// Paxos is notoriously hard to implement correctly.
// Key concepts in pseudocode:

// PROPOSER:
// Phase 1a: Send PREPARE(n) to majority of acceptors
//   n = unique proposal number (must be higher than any seen)
//
// Phase 2a: If majority responds with PROMISE:
//   If any promises contain accepted values, pick highest-numbered one
//   Otherwise, choose own value v
//   Send ACCEPT(n, v) to majority
//
// ACCEPTOR:
// On PREPARE(n):
//   If n > highest_prepare_seen:
//     highest_prepare_seen = n
//     Reply PROMISE(n, accepted_proposal, accepted_value)
//   Else: reject
//
// On ACCEPT(n, v):
//   If n >= highest_prepare_seen:
//     accepted_proposal = n
//     accepted_value = v
//     Reply ACCEPTED(n, v)
//   Else: reject
//
// Value is CHOSEN when accepted by majority of acceptors.

#include <iostream>
int main() {
    // Paxos is primarily a distributed protocol, not a single-process algorithm.
    // Real implementations: libpaxos, Google Chubby (closed), etcd (uses Raft instead).
    //
    // Key insight: two-phase protocol ensures:
    //   Safety: only a single value is chosen
    //   Liveness: progress guaranteed if majority alive (with leader election)
    //
    // Multi-Paxos: elect a stable leader to skip Phase 1 for subsequent rounds.
    std::cout << "Paxos: agreement among distributed processes\n";
    std::cout << "Safety: at most one value chosen\n";
    std::cout << "Liveness: guaranteed with majority alive\n";
}
```

### Alternative / Competitive Version
```cpp
// Paxos vs Raft:
// Paxos: more general, harder to understand, many variants
// Raft: equivalent power, designed for understandability
// Both require majority (2f+1 nodes for f failures)
// Neither handles Byzantine faults (need BFT protocols for that)
// Reference: "The Part-Time Parliament" (Lamport, 1998)
// Reference: "Paxos Made Simple" (Lamport, 2001)
int main() { return 0; }
```

### Real-World Usage
- Used in production by: etcd, CockroachDB, TiKV, Spanner

---

## 6. Interaction with Other Features
- Interacts with: networking, serialization, error handling
- Known pitfalls: undefined behavior edges, compiler-specific extensions, platform dependencies.

---

## 7. Formal Verification / Proof Obligations
For this topic, key properties to verify:
- Safety: the system never enters an invalid state.
- Liveness: the system eventually makes progress.
- Tools: TLA+ (distributed protocols), Frama-C (C programs), CBMC (bounded model checking), Z3 (SMT solving).

---

## 8. Connection to Programming Language Theory
- **Type theory:** Type systems can encode correctness properties.
- **Category theory:** Categorical semantics of programming constructs.
- **Comparison:** How would this be expressed in Erlang (actor model), Go (goroutines)?

---

## 9. Performance Characteristics
- **Compile-time:** Network latency dominates; consensus adds round-trip overhead.
- **Runtime:** Zero-cost abstraction where possible; profile to verify.
- **Debuggability:** Optimized code may be harder to debug; use -O0 + sanitizers.

---

## 10. Research Frontier
- **Open problems:** active areas of research and standardization.
- **C++26/29 direction:** Byzantine consensus efficiency, CRDTs for strong consistency.
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

**In one paragraph:** Paxos: foundational consensus protocol. Phase 1: prepare/promise. Phase 2: accept/accepted. Achieves safety (agreement) even with failures.

**Key references:**
- ISO C++ Standard (latest draft: N4950+)
- Relevant WG21 papers (see proposal numbers)
- Academic papers in the reading list

**Pattern:** Consensus / Replication / Consistency Models / Distributed Time

**5 expert pitfalls:**
1. Confusing specification with implementation (compilers may differ).
2. Assuming a feature is zero-cost without measuring.
3. Ignoring ABI implications for library interfaces.
4. Not testing with multiple compilers (GCC, Clang, MSVC).
5. Over-abstracting when simplicity would suffice.

---
Use existing Raft libraries (NuRaft, etcd/raft) rather than implementing from scratch. Test with Jepsen for correctness. Design for partition tolerance first.

*Compile:* `g++ -std=c++23 -O2 -Wall -Wextra main.cpp` (or `-std=c++2b` for bleeding edge)
