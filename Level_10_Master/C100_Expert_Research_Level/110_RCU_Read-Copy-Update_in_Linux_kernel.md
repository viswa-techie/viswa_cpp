# Chapter: RCU Read-Copy-Update in Linux kernel

> **Level:** 10 — Elite Pro / Master | **Cluster:** G — Advanced Systems Programming

---

## 1. Formal Definition & Scope
**Topic:** RCU Read-Copy-Update in Linux kernel

**Where this lives:** OS kernel / Hardware abstraction / Systems programming

**Why this matters:** Elite engineers need to understand not just how to use features, but why they exist, how they're implemented, and what trade-offs were made. This topic represents the frontier of high-performance systems at the OS boundary.

---

## 2. Historical Context & Motivation
Systems programming at the OS/kernel boundary: lock-free algorithms, memory management (RCU, seqlocks), real-time constraints (WCET), and hardware interaction (interrupts, DMA, NUMA).

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
#include <atomic>
#include <thread>
#include <iostream>
#include <vector>

// Simplified userspace RCU concept (real RCU is in Linux kernel)
struct Data {
    int value;
    std::string info;
};

std::atomic<Data*> global_data{nullptr};

// Reader: just load the pointer (lock-free!)
void reader(int id) {
    Data* p = global_data.load(std::memory_order_acquire);
    if (p) {
        std::cout << "Reader " << id << " sees: " << p->value << " " << p->info << "\n";
    }
    // In real RCU: rcu_read_lock() / rcu_read_unlock() mark the critical section
    // No actual lock acquired — just marks a quiescent state boundary
}

// Writer: allocate new, publish, wait for readers, free old
void writer(int newVal, const std::string& newInfo) {
    Data* newData = new Data{newVal, newInfo};  // 1. Copy + Update
    Data* old = global_data.exchange(newData, std::memory_order_release); // 2. Publish
    // 3. synchronize_rcu() — wait for all pre-existing readers to finish
    // In userspace: sleep or epoch-based waiting
    std::this_thread::sleep_for(std::chrono::milliseconds(10));
    delete old;  // 4. Free old version (safe: no reader holds it)
}

int main() {
    global_data.store(new Data{42, "initial"});

    std::thread r1(reader, 1);
    std::thread w1(writer, 100, "updated");
    std::thread r2(reader, 2);

    r1.join(); w1.join(); r2.join();
    delete global_data.load();
}
```

### Alternative / Competitive Version
```cpp
// RCU characteristics:
// Read: zero overhead (no lock, no atomic, no barrier on x86)
// Write: must allocate new version + wait for grace period
// Use cases: routing tables, configuration, read-heavy data
// Linux kernel: rcu_read_lock(), rcu_dereference(), synchronize_rcu(), call_rcu()
// ~10,000+ uses in Linux kernel as of 6.x
// Paper: "Read-Copy Update" (McKenney & Slingwine, 1998)
int main() { return 0; }
```

### Real-World Usage
- Used in production by: Linux kernel, DPDK, Seastar, io_uring

---

## 6. Interaction with Other Features
- Interacts with: memory model, atomics, syscalls, interrupt handlers
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
- **Compile-time:** Kernel-level code must meet strict latency requirements.
- **Runtime:** Zero-cost abstraction where possible; profile to verify.
- **Debuggability:** Optimized code may be harder to debug; use -O0 + sanitizers.

---

## 10. Research Frontier
- **Open problems:** active areas of research and standardization.
- **C++26/29 direction:** io_uring evolution, eBPF for observability.
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

**In one paragraph:** RCU: readers proceed without locks/barriers; writers create new version, wait for all readers to finish, then free old version. Extremely fast reads.

**Key references:**
- ISO C++ Standard (latest draft: N4950+)
- Relevant WG21 papers (see proposal numbers)
- Academic papers in the reading list

**Pattern:** Kernel Programming / Lock-Free / Real-Time / Hardware Interaction

**5 expert pitfalls:**
1. Confusing specification with implementation (compilers may differ).
2. Assuming a feature is zero-cost without measuring.
3. Ignoring ABI implications for library interfaces.
4. Not testing with multiple compilers (GCC, Clang, MSVC).
5. Over-abstracting when simplicity would suffice.

---
Kernel C++: no exceptions, no RTTI, no dynamic allocation. Use C-compatible interfaces. RCU/seqlocks require careful memory ordering. Test with KCSAN, lockdep, and kmemleak.

*Compile:* `g++ -std=c++23 -O2 -Wall -Wextra main.cpp` (or `-std=c++2b` for bleeding edge)
