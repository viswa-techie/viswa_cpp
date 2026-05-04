# Chapter: Raft consensus algorithm

> **Level:** 10 — Elite Pro / Master | **Cluster:** F — Distributed Systems Theory

---

## 1. Formal Definition & Scope
**Topic:** Raft consensus algorithm

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
#include <vector>
#include <string>
#include <random>
#include <iostream>

// Simplified Raft state machine (conceptual)
enum class Role { Follower, Candidate, Leader };

struct LogEntry {
    int term;
    std::string command;
};

struct RaftNode {
    int id;
    Role role = Role::Follower;
    int currentTerm = 0;
    int votedFor = -1;
    std::vector<LogEntry> log;
    int commitIndex = 0;
    int lastApplied = 0;

    // Leader state
    std::vector<int> nextIndex;   // for each peer
    std::vector<int> matchIndex;  // for each peer

    void startElection(int clusterSize) {
        role = Role::Candidate;
        ++currentTerm;
        votedFor = id;
        int votes = 1; // vote for self
        // In real impl: send RequestVote RPCs to all peers
        // If majority responds with voteGranted: become leader
        if (votes > clusterSize / 2) {
            role = Role::Leader;
            nextIndex.assign(clusterSize, log.size());
            matchIndex.assign(clusterSize, 0);
        }
    }

    void appendEntry(const std::string& cmd) {
        if (role != Role::Leader) return; // redirect to leader
        log.push_back({currentTerm, cmd});
        // Send AppendEntries RPC to all followers
    }

    // RequestVote RPC handler
    bool handleRequestVote(int candidateTerm, int candidateId, int lastLogIdx, int lastLogTerm) {
        if (candidateTerm < currentTerm) return false;
        if (candidateTerm > currentTerm) {
            currentTerm = candidateTerm;
            role = Role::Follower;
            votedFor = -1;
        }
        if (votedFor == -1 || votedFor == candidateId) {
            // Check log is at least as up-to-date
            int myLastTerm = log.empty() ? 0 : log.back().term;
            int myLastIdx = log.size() - 1;
            if (lastLogTerm > myLastTerm || (lastLogTerm == myLastTerm && lastLogIdx >= myLastIdx)) {
                votedFor = candidateId;
                return true;
            }
        }
        return false;
    }
};

int main() {
    RaftNode node{0};
    node.startElection(5);
    if (node.role == Role::Leader)
        node.appendEntry("SET x 42");
    std::cout << "Node " << node.id << " term=" << node.currentTerm
              << " log_size=" << node.log.size() << "\n";
}
```

### Alternative / Competitive Version
```cpp
// Raft guarantees:
// 1. Election Safety: at most one leader per term
// 2. Leader Append-Only: leader never overwrites/deletes its log
// 3. Log Matching: if two logs contain entry with same index+term, all preceding entries identical
// 4. Leader Completeness: if entry committed in term t, present in all leaders for terms > t
// 5. State Machine Safety: if server applies entry at index i, no other server applies different entry at i
// Reference: "In Search of an Understandable Consensus Algorithm" (Ongaro & Ousterhout, 2014)
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

**In one paragraph:** Raft: understandable consensus for replicated logs. Leader election + log replication + safety. Equivalent to Multi-Paxos but easier to implement.

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
