#!/usr/bin/env python3
"""Generate Level 10 C++ problem docs with real solutions (Elite Pro / Master)."""
import os, re

BASE = "/home/23u58g/work/ZZZ_LEARN_VISWA_DOCS/CPP_problem_solving/Level_10_Master"

def fname(name, idx):
    s = re.sub(r'[^\w\s-]', '', name)
    s = re.sub(r'\s+', '_', s.strip())[:80]
    return f"{idx:03d}_{s}.md"

# ============================================================
# Problem lists by cluster
# ============================================================
C100 = [
    # Cluster A: C++ Language Evolution 1-20
    "C++23 features overview deducing this expected flat_map print",
    "C++26 planned features reflection contracts executors",
    "Reflection TS proposal P2996",
    "Static reflection metaclasses Herb Sutter proposal",
    "Pattern matching P1371 inspect match",
    "Executors P2300 std execution",
    "Sender receiver model",
    "std execution networking P2762",
    "Contracts P2521 pre postconditions",
    "Precondition postcondition syntax",
    "Invariant syntax",
    "Safety profiles proposal Bjarne Stroustrup",
    "Carbon language interop with C++",
    "Circle C++ extension Sean Baxter",
    "Val language design ideas",
    "Safe C++ subset proposals",
    "std generator C++23 full design",
    "std expected T E full design",
    "std mdspan multi-dimensional spans",
    "std linalg C++26 linear algebra",
    # Cluster B: FP in C++ 21-35
    "Functor concept map in C++",
    "Monad concept bind flatMap in C++",
    "Applicative functor",
    "Monoid in C++ fold",
    "Free monad concept",
    "Continuation monad Cont monad",
    "Comonad concept",
    "Arrows in functional programming",
    "Lens optics in C++",
    "Prism optics",
    "Profunctor optics",
    "Zippers in C++",
    "Tagless final encoding",
    "Expression problem in C++",
    "Finally tagless DSL in C++",
    # Cluster C: Formal Verification 36-50
    "Hoare logic basics P C Q",
    "Floyd-Hoare triples",
    "Weakest precondition calculus",
    "Loop invariant formal proof",
    "Separation logic concept",
    "Concurrent separation logic",
    "Model checking SPIN TLA+",
    "TLA+ specification for C++ system",
    "SMT solvers Z3 usage from C++",
    "CBMC model checker",
    "Frama-C analysis WP plugin",
    "MISRA C++ compliance checking",
    "Undefined behavior formal semantics memory object model",
    "CompCert verified compiler concept",
    "Verified data structures Coq",
    # Cluster D: Compiler Internals 51-70
    "LLVM IR basics",
    "LLVM pass writing transform pass",
    "Clang AST traversal",
    "LibTooling basics",
    "Clang-Tidy check writing",
    "MLIR dialect concept",
    "GCC GIMPLE IR",
    "GCC RTL IR",
    "SSA form Static Single Assignment",
    "Phi nodes",
    "Dominator tree",
    "Dominator frontier",
    "Control flow graph",
    "Liveness analysis",
    "Register allocation graph coloring",
    "Instruction selection ISEL",
    "Instruction scheduling",
    "Peephole optimization",
    "Loop-invariant code motion LICM",
    "Strength reduction",
    # Cluster E: Advanced Optimizations 71-80
    "Vectorization analysis",
    "Polyhedral model",
    "Auto-vectorization with LLVM",
    "Profile-guided optimization internals",
    "Feedback-directed optimization",
    "Whole program optimization WPO",
    "Interprocedural analysis",
    "Escape analysis",
    "Scalar replacement of aggregates SROA",
    "Speculative execution and mitigation",
    # Cluster F: Distributed Systems Theory 81-100
    "CAP theorem formal statement and proof",
    "PACELC theorem",
    "Paxos consensus algorithm",
    "Multi-Paxos",
    "Raft consensus algorithm",
    "Raft leader election",
    "Raft log replication",
    "Raft snapshots",
    "Zab Zookeeper Atomic Broadcast protocol",
    "Viewstamped replication",
    "Byzantine fault tolerance PBFT",
    "Tendermint BFT",
    "Linearizability formal definition",
    "Sequential consistency formal",
    "Eventual consistency",
    "CRDT Conflict-free Replicated Data Types",
    "G-counter PN-counter CRDT",
    "OR-set CRDT",
    "Vector clocks",
    "Lamport clocks",
    # Cluster G: Advanced Systems Programming 101-120
    "Hybrid logical clocks",
    "Google Spanner TrueTime",
    "Calvin deterministic database",
    "CockroachDB MVCC",
    "LSM tree LevelDB RocksDB",
    "B-tree vs LSM trade-offs",
    "Custom memory allocator for OS",
    "Lock-free OS data structures",
    "Seqlock in Linux kernel",
    "RCU Read-Copy-Update in Linux kernel",
    "Futex implementation",
    "Priority inheritance mutex",
    "Real-time scheduling POSIX RT SCHED_FIFO",
    "WCET analysis",
    "Interrupt latency in C++",
    "DPC softirq concept",
    "NUMA memory policy in kernel",
    "cgroups and memory limits",
    "seccomp sandboxing from C++",
    "eBPF programs from C++",
]

CLUSTERS = {
    (1,20): ("A", "C++ Language Evolution"),
    (21,35): ("B", "Functional Programming in C++"),
    (36,50): ("C", "Formal Verification & Program Correctness"),
    (51,70): ("D", "Compiler Internals"),
    (71,80): ("E", "Advanced Optimizations"),
    (81,100): ("F", "Distributed Systems Theory"),
    (101,120): ("G", "Advanced Systems Programming"),
}

def get_cluster(idx):
    for (lo,hi),(cid,cname) in CLUSTERS.items():
        if lo <= idx <= hi:
            return cid, cname
    return "?", "Unknown"

# ============================================================
# Real solutions for iconic topics
# ============================================================
HOT = {
    "C++23 features overview deducing this expected flat_map print": (
"""C++23 brings deducing `this` (explicit object parameter), `std::expected<T,E>`, `std::flat_map`, `std::print`, `std::generator`, and more.""",
"""#include <expected>
#include <print>
#include <string>
#include <optional>

// Deducing this (P0847) — explicit object parameter
struct Widget {
    std::string name;
    // Single implementation for const/non-const/rvalue
    template<typename Self>
    auto&& getName(this Self&& self) { return std::forward<Self>(self).name; }
};

// std::expected<T,E> — value-or-error without exceptions
enum class Error { NotFound, Invalid };
std::expected<int, Error> parseInt(const std::string& s) {
    try { return std::stoi(s); }
    catch (...) { return std::unexpected(Error::Invalid); }
}

// std::print — type-safe formatted output (replaces printf + iostream)
void demo() {
    std::print("Hello, {}! The answer is {}\\n", "world", 42);
    auto result = parseInt("123");
    if (result) std::print("Parsed: {}\\n", *result);
    else std::print("Error\\n");
}

int main() { demo(); }""",
"""// Other C++23 features:
// - std::flat_map (sorted vector-backed map)
// - std::generator (coroutine range factory)
// - std::stacktrace
// - Multidimensional subscript operator
// - if consteval
// - auto(x) decay-copy
// Compiler support: GCC 14+, Clang 17+, MSVC 19.35+
int main() { return 0; }"""),

    "std expected T E full design": (
"""std::expected<T,E>: monadic error handling without exceptions. Like Rust's Result<T,E>.""",
"""#include <expected>
#include <string>
#include <iostream>

enum class ParseError { Empty, Overflow, Invalid };

std::expected<int, ParseError> parse(const std::string& s) {
    if (s.empty()) return std::unexpected(ParseError::Empty);
    try {
        size_t pos;
        int val = std::stoi(s, &pos);
        if (pos != s.size()) return std::unexpected(ParseError::Invalid);
        return val;
    } catch (...) {
        return std::unexpected(ParseError::Overflow);
    }
}

std::expected<double, ParseError> half(const std::string& s) {
    // Monadic chaining with and_then / transform
    return parse(s).transform([](int v) { return v / 2.0; });
}

int main() {
    auto r1 = half("42");
    if (r1) std::cout << "half = " << *r1 << "\\n"; // 21.0

    auto r2 = half("abc");
    if (!r2) std::cout << "error code = " << (int)r2.error() << "\\n";
}""",
"""// std::expected vs std::optional:
//   optional<T>: value or nothing
//   expected<T,E>: value or typed error
// Monadic ops: and_then(), transform(), or_else(), transform_error()
// Zero overhead in the success path (no exception unwinding).
int main() { return 0; }"""),

    "Raft consensus algorithm": (
"""Raft: understandable consensus for replicated logs. Leader election + log replication + safety. Equivalent to Multi-Paxos but easier to implement.""",
"""#include <vector>
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
              << " log_size=" << node.log.size() << "\\n";
}""",
"""// Raft guarantees:
// 1. Election Safety: at most one leader per term
// 2. Leader Append-Only: leader never overwrites/deletes its log
// 3. Log Matching: if two logs contain entry with same index+term, all preceding entries identical
// 4. Leader Completeness: if entry committed in term t, present in all leaders for terms > t
// 5. State Machine Safety: if server applies entry at index i, no other server applies different entry at i
// Reference: "In Search of an Understandable Consensus Algorithm" (Ongaro & Ousterhout, 2014)
int main() { return 0; }"""),

    "CRDT Conflict-free Replicated Data Types": (
"""CRDTs enable eventual consistency without coordination. Operations commute, so replicas converge automatically.""",
"""#include <map>
#include <algorithm>
#include <iostream>

// G-Counter: grow-only counter — each node has its own slot
struct GCounter {
    std::map<int, int> counts;  // node_id -> count

    void increment(int nodeId) { counts[nodeId]++; }

    int value() const {
        int sum = 0;
        for (auto& [_, c] : counts) sum += c;
        return sum;
    }

    // Merge: take max of each node's count
    void merge(const GCounter& other) {
        for (auto& [id, c] : other.counts)
            counts[id] = std::max(counts[id], c);
    }
};

// PN-Counter: supports increment AND decrement
struct PNCounter {
    GCounter pos, neg;
    void increment(int nodeId) { pos.increment(nodeId); }
    void decrement(int nodeId) { neg.increment(nodeId); }
    int value() const { return pos.value() - neg.value(); }
    void merge(const PNCounter& other) { pos.merge(other.pos); neg.merge(other.neg); }
};

int main() {
    GCounter a, b;
    a.increment(0); a.increment(0); // node 0 increments twice
    b.increment(1); b.increment(1); b.increment(1); // node 1 three times
    a.merge(b); b.merge(a);
    std::cout << "a=" << a.value() << " b=" << b.value() << "\\n"; // both 5
}""",
"""// CRDT types: state-based (CvRDT) vs operation-based (CmRDT).
// State-based: merge function must be commutative, associative, idempotent (join semilattice).
// Examples: G-Counter, PN-Counter, G-Set, OR-Set, LWW-Register, MV-Register.
// Used in: Redis CRDTs, Riak, Automerge, Yjs.
// Paper: "A comprehensive study of CRDTs" (Shapiro et al., 2011)
int main() { return 0; }"""),

    "Lamport clocks": (
"""Lamport logical clocks: if event a → b (happens-before), then LC(a) < LC(b). Simple scalar counter, not a total order on concurrent events.""",
"""#include <iostream>
#include <algorithm>

struct LamportClock {
    int time = 0;

    // Local event
    void tick() { ++time; }

    // Send: increment then attach timestamp
    int send() { return ++time; }

    // Receive: update to max(local, received) + 1
    void receive(int senderTime) {
        time = std::max(time, senderTime) + 1;
    }

    int now() const { return time; }
};

int main() {
    LamportClock a, b, c;

    a.tick();            // a.time = 1 (event a1)
    int msg1 = a.send(); // a.time = 2, msg carries 2
    b.receive(msg1);     // b.time = max(0,2)+1 = 3

    b.tick();            // b.time = 4
    int msg2 = b.send(); // b.time = 5, msg carries 5
    c.receive(msg2);     // c.time = max(0,5)+1 = 6

    c.tick();            // c.time = 7
    int msg3 = c.send(); // c.time = 8
    a.receive(msg3);     // a.time = max(2,8)+1 = 9

    std::cout << "A=" << a.now() << " B=" << b.now() << " C=" << c.now() << "\\n";
    // A=9 B=5 C=8
}""",
"""// Lamport clock limitation: LC(a) < LC(b) does NOT imply a → b.
// For that, use Vector Clocks: each process maintains a vector of N counters.
// VC(a) < VC(b) iff a causally precedes b. VC(a) || VC(b) = concurrent.
// Reference: "Time, Clocks, and the Ordering of Events" (Lamport, 1978)
int main() { return 0; }"""),

    "Vector clocks": (
"""Vector clocks: each process maintains a vector of N logical timestamps. Captures full causality: VC(a) < VC(b) iff a → b.""",
"""#include <vector>
#include <algorithm>
#include <iostream>

struct VectorClock {
    std::vector<int> vc;
    int id;

    VectorClock(int nodeId, int n) : vc(n, 0), id(nodeId) {}

    void tick() { vc[id]++; }

    std::vector<int> send() {
        vc[id]++;
        return vc;  // attach full vector to message
    }

    void receive(const std::vector<int>& senderVC) {
        for (int i = 0; i < (int)vc.size(); ++i)
            vc[i] = std::max(vc[i], senderVC[i]);
        vc[id]++;
    }

    // Causality check
    bool happensBefore(const VectorClock& other) const {
        bool atLeastOneLess = false;
        for (int i = 0; i < (int)vc.size(); ++i) {
            if (vc[i] > other.vc[i]) return false;
            if (vc[i] < other.vc[i]) atLeastOneLess = true;
        }
        return atLeastOneLess;
    }

    bool concurrent(const VectorClock& other) const {
        return !happensBefore(other) && !other.happensBefore(*this);
    }
};

int main() {
    VectorClock a(0, 3), b(1, 3), c(2, 3);
    a.tick();                 // a=[1,0,0]
    auto msg = a.send();     // a=[2,0,0]
    b.receive(msg);           // b=[2,1,0]
    b.tick();                 // b=[2,2,0]
    c.tick();                 // c=[0,0,1]  — concurrent with a and b!

    std::cout << "a→b? " << a.happensBefore(b) << "\\n";  // 1
    std::cout << "c||b? " << c.concurrent(b) << "\\n";    // 1
}""",
"""// Vector clocks: O(N) space per event, where N = number of processes.
// For large systems: use Bloom clocks, interval tree clocks, or hybrid logical clocks.
// Paper: "Virtual Time and Global States of Distributed Systems" (Mattern, 1989)
int main() { return 0; }"""),

    "LLVM IR basics": (
"""LLVM IR: typed SSA-form intermediate representation. Three forms: human-readable (.ll), bitcode (.bc), in-memory.""",
"""// Example: compile to LLVM IR with: clang -S -emit-llvm hello.cpp -o hello.ll
// hello.cpp:
#include <cstdio>
int add(int a, int b) { return a + b; }
int main() {
    int result = add(3, 4);
    printf("%d\\n", result);
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
""",
"""// Tools:
// clang -S -emit-llvm file.cpp -o file.ll  # generate IR
// llc file.ll -o file.s                     # IR to assembly
// opt -O2 file.ll -S -o file_opt.ll         # run optimization passes
// lli file.ll                                # interpret IR directly
// llvm-dis file.bc -o file.ll               # bitcode to text
// llvm-as file.ll -o file.bc                # text to bitcode
int main() { return 0; }"""),

    "SSA form Static Single Assignment": (
"""SSA: every variable is assigned exactly once. Multiple assignments use phi nodes at control flow merge points. Enables powerful optimizations.""",
"""// Example of SSA transformation:
// Original:
//   x = 1;
//   if (cond)
//     x = 2;
//   use(x);
//
// SSA form:
//   x1 = 1;
//   if (cond)
//     x2 = 2;
//   x3 = phi(x1, x2);  // selects based on which branch was taken
//   use(x3);

// In LLVM IR:
// entry:
//   br i1 %cond, label %then, label %merge
// then:
//   br label %merge
// merge:
//   %x = phi i32 [1, %entry], [2, %then]
//   call void @use(i32 %x)

// SSA enables:
// 1. Constant propagation (trivial: each def has one value)
// 2. Dead code elimination (no uses → remove def)
// 3. Global value numbering (detect redundant computations)
// 4. Sparse conditional constant propagation

#include <iostream>
int main() {
    // This code in SSA has distinct names for each assignment:
    int x1 = 5;       // x1 = 5
    int x2 = x1 + 3;  // x2 = x1 + 3 = 8
    int x3 = x2 * 2;  // x3 = x2 * 2 = 16
    std::cout << x3;   // use(x3)
}""",
"""// SSA construction: Cytron et al. algorithm
// 1. Compute dominance frontiers
// 2. Place phi nodes where needed
// 3. Rename variables (DFS over dominator tree)
// Destruction: replace phi nodes with copies (register allocation handles coalescing)
// Reference: "Efficiently Computing SSA Form and the Control Dependence Graph" (Cytron et al., 1991)
int main() { return 0; }"""),

    "LSM tree LevelDB RocksDB": (
"""LSM tree: write-optimized data structure. Writes go to in-memory buffer (memtable), flushed to sorted runs on disk, merged by compaction.""",
"""#include <map>
#include <vector>
#include <string>
#include <algorithm>
#include <iostream>
#include <optional>

// Simplified LSM tree concept
struct LSMTree {
    // L0: in-memory (memtable)
    std::map<std::string, std::string> memtable;
    size_t memtableLimit = 4;

    // L1+: sorted runs on "disk" (simulated)
    std::vector<std::map<std::string, std::string>> levels;

    void put(const std::string& key, const std::string& val) {
        memtable[key] = val;
        if (memtable.size() >= memtableLimit)
            flush();
    }

    std::optional<std::string> get(const std::string& key) {
        // Check memtable first (most recent)
        if (auto it = memtable.find(key); it != memtable.end())
            return it->second;
        // Check levels from newest to oldest
        for (int i = levels.size() - 1; i >= 0; --i) {
            if (auto it = levels[i].find(key); it != levels[i].end())
                return it->second;
        }
        return std::nullopt;
    }

    void flush() {
        if (memtable.empty()) return;
        levels.push_back(std::move(memtable));
        memtable.clear();
        // Trigger compaction if too many levels
        if (levels.size() > 4) compact();
    }

    void compact() {
        // Merge all levels into one sorted run
        std::map<std::string, std::string> merged;
        for (auto& level : levels)
            for (auto& [k, v] : level)
                merged[k] = v;  // newer overwrites older
        levels.clear();
        levels.push_back(std::move(merged));
    }
};

int main() {
    LSMTree lsm;
    lsm.put("name", "Alice");
    lsm.put("age", "30");
    lsm.put("city", "NYC");
    lsm.put("name", "Bob");  // update triggers flush
    lsm.put("dept", "Eng");

    auto val = lsm.get("name");
    std::cout << "name = " << val.value_or("NOT FOUND") << "\\n"; // Bob
}""",
"""// LSM trade-offs:
// Write: O(1) amortized (memtable insert + periodic flush)
// Read: O(L) where L = number of levels (mitigated by Bloom filters)
// Space amplification: ~10x due to compaction
// Write amplification: data rewritten during compaction (leveled: O(L * size_ratio))
//
// Real implementations: LevelDB, RocksDB, Cassandra, HBase, CockroachDB
// Compaction strategies: leveled (RocksDB default), tiered (Cassandra), FIFO
// Reference: "The Log-Structured Merge-Tree" (O'Neil et al., 1996)
int main() { return 0; }"""),

    "RCU Read-Copy-Update in Linux kernel": (
"""RCU: readers proceed without locks/barriers; writers create new version, wait for all readers to finish, then free old version. Extremely fast reads.""",
"""#include <atomic>
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
        std::cout << "Reader " << id << " sees: " << p->value << " " << p->info << "\\n";
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
}""",
"""// RCU characteristics:
// Read: zero overhead (no lock, no atomic, no barrier on x86)
// Write: must allocate new version + wait for grace period
// Use cases: routing tables, configuration, read-heavy data
// Linux kernel: rcu_read_lock(), rcu_dereference(), synchronize_rcu(), call_rcu()
// ~10,000+ uses in Linux kernel as of 6.x
// Paper: "Read-Copy Update" (McKenney & Slingwine, 1998)
int main() { return 0; }"""),

    "Hoare logic basics P C Q": (
"""Hoare logic: {P} C {Q} means "if precondition P holds before executing command C, then postcondition Q holds after." Foundation of program verification.""",
"""// Hoare triple: {P} C {Q}
// Example: {x == 5} x = x + 1 {x == 6}

// Hoare logic axioms:
// 1. Assignment: {Q[x/e]} x = e {Q}  (substitute e for x in Q)
// 2. Sequence:   {P} C1 {R}, {R} C2 {Q}  =>  {P} C1; C2 {Q}
// 3. Conditional: {P∧B} C1 {Q}, {P∧¬B} C2 {Q}  =>  {P} if B then C1 else C2 {Q}
// 4. While loop:  {P∧B} C {P}  =>  {P} while B do C {P∧¬B}
//    (P is the loop invariant)
// 5. Consequence: P=>P', {P'} C {Q'}, Q'=>Q  =>  {P} C {Q}

// C++ example with annotations:
#include <cassert>
#include <iostream>

// Verified: {n >= 0} sum(n) {result == n*(n+1)/2}
int sum(int n) {
    assert(n >= 0);          // Precondition
    int s = 0, i = 0;
    // Loop invariant: s == i*(i+1)/2 && 0 <= i <= n
    while (i < n) {
        i = i + 1;
        s = s + i;
        // Invariant maintained: s == i*(i+1)/2
    }
    // Post-loop: i == n && s == n*(n+1)/2
    assert(s == n * (n + 1) / 2);  // Postcondition
    return s;
}

int main() {
    std::cout << sum(100) << "\\n";  // 5050
}""",
"""// Partial correctness: if C terminates AND P holds, then Q holds.
// Total correctness: C MUST terminate AND Q holds.
// For total correctness: add a variant (decreasing measure) for loops.
// Tools: Frama-C (WP plugin), Dafny, Why3, KeY (Java)
// Reference: "An Axiomatic Basis for Computer Programming" (Hoare, 1969)
int main() { return 0; }"""),

    "Monad concept bind flatMap in C++": (
"""Monads in C++: types with bind (>>=) that chain computations. std::optional, std::expected, std::future are all monads.""",
"""#include <optional>
#include <functional>
#include <iostream>
#include <string>

// optional is a monad: and_then = bind/flatMap (C++23)
std::optional<int> parseInt(const std::string& s) {
    try { return std::stoi(s); } catch (...) { return std::nullopt; }
}

std::optional<double> safeDiv(int a, int b) {
    if (b == 0) return std::nullopt;
    return (double)a / b;
}

// Monadic chaining: parse string → divide by 2
std::optional<double> parseAndHalve(const std::string& s) {
    return parseInt(s).and_then([](int x) { return safeDiv(x, 2); });
}

// Generic monad-like bind for any M<T>
template<typename M, typename F>
auto mbind(M&& m, F&& f) -> decltype(f(*m)) {
    if (m) return f(*m);
    return std::nullopt;
}

int main() {
    auto r1 = parseAndHalve("42");
    std::cout << r1.value_or(-1) << "\\n";  // 21

    auto r2 = parseAndHalve("abc");
    std::cout << r2.value_or(-1) << "\\n";  // -1

    // Manual chaining:
    auto r3 = mbind(parseInt("100"), [](int x) {
        return mbind(safeDiv(x, 3), [](double d) -> std::optional<double> {
            return d + 1;
        });
    });
    std::cout << r3.value_or(-1) << "\\n";  // 34.333...
}""",
"""// Monad laws:
// 1. Left identity:  return a >>= f  ==  f(a)
// 2. Right identity: m >>= return    ==  m
// 3. Associativity:  (m >>= f) >>= g == m >>= (\\x -> f(x) >>= g)
//
// C++ monadic types:
// - std::optional (C++17, and_then in C++23)
// - std::expected (C++23)
// - std::future (then() in extensions)
// - ranges::views (transform = fmap, join = flatten)
int main() { return 0; }"""),

    "Paxos consensus algorithm": (
"""Paxos: foundational consensus protocol. Phase 1: prepare/promise. Phase 2: accept/accepted. Achieves safety (agreement) even with failures.""",
"""// Paxos is notoriously hard to implement correctly.
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
    std::cout << "Paxos: agreement among distributed processes\\n";
    std::cout << "Safety: at most one value chosen\\n";
    std::cout << "Liveness: guaranteed with majority alive\\n";
}""",
"""// Paxos vs Raft:
// Paxos: more general, harder to understand, many variants
// Raft: equivalent power, designed for understandability
// Both require majority (2f+1 nodes for f failures)
// Neither handles Byzantine faults (need BFT protocols for that)
// Reference: "The Part-Time Parliament" (Lamport, 1998)
// Reference: "Paxos Made Simple" (Lamport, 2001)
int main() { return 0; }"""),
}

# ============================================================
# Chapter builder
# ============================================================
def _theory(cluster):
    return {
        "A": "Based on ISO C++ standard evolution (WG21 process). Each feature undergoes proposal → design review → wording → vote → published standard. Zero-overhead principle and backward compatibility are primary design constraints.",
        "B": "Rooted in category theory: functors preserve structure (fmap), monads compose effectful computations (bind), and applicatives combine independent effects. C++ approximates these via templates and operator overloading.",
        "C": "Founded on mathematical logic: Hoare logic (partial/total correctness), separation logic (pointer reasoning), and temporal logic (liveness/safety properties). Tools mechanize proof checking.",
        "D": "Compiler theory: lexing (regular languages) → parsing (context-free grammars) → semantic analysis (type checking) → IR generation (SSA) → optimization passes → code generation (instruction selection + register allocation).",
        "E": "Performance engineering meets compiler theory: auto-vectorization via loop analysis, polyhedral model for affine loop nests, profile-guided optimization for branch prediction and inlining.",
        "F": "Distributed computing theory: FLP impossibility (no deterministic consensus with one crash failure in async model), CAP theorem (choose 2 of 3), and consensus protocols (Paxos, Raft) that work with timing assumptions.",
        "G": "Systems programming at the OS/kernel boundary: lock-free algorithms, memory management (RCU, seqlocks), real-time constraints (WCET), and hardware interaction (interrupts, DMA, NUMA).",
    }.get(cluster, "")

def _engineering(cluster):
    return {
        "A": "Check compiler support before using C++23/26 features. Use feature-test macros (__cpp_*). Gradual adoption: start with std::expected and std::print, which have wide support.",
        "B": "Functional patterns in C++ have overhead (virtual dispatch, type erasure) unless using templates. Prefer compile-time polymorphism. std::optional::and_then (C++23) is the practical entry point.",
        "C": "Formal verification is expensive but worth it for safety-critical code (automotive, aerospace, medical). Use Frama-C for C, CBMC for bounded model checking, TLA+ for distributed protocol verification.",
        "D": "Writing LLVM passes: use the new PassManager API. Start with analysis passes (read-only) before transform passes. LibTooling for source-level transformations, Clang-Tidy for lint rules.",
        "E": "Profile first (perf stat), then optimize. Auto-vectorization: check with -Rpass=loop-vectorize. PGO: build, profile, rebuild. LTO: significant binary size reduction and cross-TU inlining.",
        "F": "Use existing Raft libraries (NuRaft, etcd/raft) rather than implementing from scratch. Test with Jepsen for correctness. Design for partition tolerance first.",
        "G": "Kernel C++: no exceptions, no RTTI, no dynamic allocation. Use C-compatible interfaces. RCU/seqlocks require careful memory ordering. Test with KCSAN, lockdep, and kmemleak.",
    }.get(cluster, "")

def _pattern(cluster):
    return {
        "A": "Language Evolution / Standard Proposals / Feature Design",
        "B": "Functional Abstractions / Category Theory / Monadic Composition",
        "C": "Program Verification / Formal Methods / Correctness Proofs",
        "D": "Compiler IR / Optimization Passes / Code Generation",
        "E": "Performance Analysis / Auto-vectorization / PGO / LTO",
        "F": "Consensus / Replication / Consistency Models / Distributed Time",
        "G": "Kernel Programming / Lock-Free / Real-Time / Hardware Interaction",
    }.get(cluster, "")

def make_chapter(name, idx, cluster_id, cluster_name, concept="", impl1="", impl2=""):
    if not concept:
        concept = f"This chapter covers **{name}** — a research-level topic in {cluster_name}."
    if not impl1:
        impl1 = _default(name, "impl1")
    if not impl2:
        impl2 = _default(name, "impl2")

    return f"""# Chapter: {name}

> **Level:** 10 — Elite Pro / Master | **Cluster:** {cluster_id} — {cluster_name}

---

## 1. Formal Definition & Scope
**Topic:** {name}

**Where this lives:** {'Language specification / WG21 proposals' if cluster_id=='A' else 'Programming language theory / Category theory' if cluster_id=='B' else 'Mathematical logic / Verification tools' if cluster_id=='C' else 'Compiler engineering / IR design' if cluster_id=='D' else 'Compiler optimization / Microarchitecture' if cluster_id=='E' else 'Distributed computing theory / Consensus' if cluster_id=='F' else 'OS kernel / Hardware abstraction / Systems programming'}

**Why this matters:** Elite engineers need to understand not just how to use features, but why they exist, how they're implemented, and what trade-offs were made. This topic represents the frontier of {'C++ language design' if cluster_id=='A' else 'functional programming in a systems language' if cluster_id=='B' else 'software correctness guarantees' if cluster_id=='C' else 'program compilation and optimization' if cluster_id=='D' else 'extracting maximum performance from hardware' if cluster_id=='E' else 'building reliable distributed systems' if cluster_id=='F' else 'high-performance systems at the OS boundary'}.

---

## 2. Historical Context & Motivation
{_theory(cluster_id)}

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
- **Zero-overhead principle:** does this add cost if unused? {'Generally yes — C++ features are designed for zero overhead.' if cluster_id in ('A','D','E') else 'N/A — this is a design/theoretical concept.'}
- **ABI stability:** {'Critical concern for C++ standard library additions.' if cluster_id=='A' else 'Not directly applicable.'}
- **Backward compatibility:** {'Must not break existing code.' if cluster_id=='A' else 'Implementation may require new tooling.'}

---

## 5. Implementation Deep Dive

### Reference C++ Implementation
```cpp
{impl1.strip()}
```

### Alternative / Competitive Version
```cpp
{impl2.strip()}
```

### Real-World Usage
- Used in production by: {'LLVM, Chromium, folly, abseil' if cluster_id in ('A','B') else 'Frama-C, CompCert, seL4' if cluster_id=='C' else 'LLVM, GCC, MSVC compiler backends' if cluster_id in ('D','E') else 'etcd, CockroachDB, TiKV, Spanner' if cluster_id=='F' else 'Linux kernel, DPDK, Seastar, io_uring'}

---

## 6. Interaction with Other Features
- Interacts with: {'coroutines, concepts, ranges, modules' if cluster_id=='A' else 'templates, concepts, ranges' if cluster_id=='B' else 'undefined behavior, memory model, type system' if cluster_id=='C' else 'link-time optimization, debug info, sanitizers' if cluster_id in ('D','E') else 'networking, serialization, error handling' if cluster_id=='F' else 'memory model, atomics, syscalls, interrupt handlers'}
- Known pitfalls: undefined behavior edges, compiler-specific extensions, platform dependencies.

---

## 7. Formal Verification / Proof Obligations
{'For this topic, key properties to verify:' if cluster_id in ('C','F','G') else 'Verification is recommended for correctness-critical usage:'}
- Safety: the system never enters an invalid state.
- Liveness: the system eventually makes progress.
- Tools: TLA+ (distributed protocols), Frama-C (C programs), CBMC (bounded model checking), Z3 (SMT solving).

---

## 8. Connection to Programming Language Theory
- **Type theory:** {'Dependent types, linear types, and ownership relate to C++ concepts and move semantics.' if cluster_id in ('A','B') else 'Type systems can encode correctness properties.'}
- **Category theory:** {'Functors (ranges::transform), monads (optional::and_then), natural transformations.' if cluster_id=='B' else 'Categorical semantics of programming constructs.'}
- **Comparison:** How would this be expressed in {'Rust (ownership), Haskell (type classes), Idris (dependent types)' if cluster_id in ('A','B') else 'Coq/Isabelle (proof assistants)' if cluster_id=='C' else 'MLIR/Cranelift (alternative IRs)' if cluster_id in ('D','E') else 'Erlang (actor model), Go (goroutines)'}?

---

## 9. Performance Characteristics
- **Compile-time:** {'May increase with heavy template/concept usage.' if cluster_id in ('A','B') else 'Verification tools run separately from compilation.' if cluster_id=='C' else 'Optimization passes add to compile time; PGO requires two builds.' if cluster_id in ('D','E') else 'Network latency dominates; consensus adds round-trip overhead.' if cluster_id=='F' else 'Kernel-level code must meet strict latency requirements.'}
- **Runtime:** Zero-cost abstraction where possible; profile to verify.
- **Debuggability:** {'Concepts provide better error messages than SFINAE.' if cluster_id=='A' else 'Formal proofs eliminate debugging need for verified code.' if cluster_id=='C' else 'Optimized code may be harder to debug; use -O0 + sanitizers.'}

---

## 10. Research Frontier
- **Open problems:** active areas of research and standardization.
- **C++26/29 direction:** {'reflection, pattern matching, contracts.' if cluster_id=='A' else 'dependent types for C++?' if cluster_id=='B' else 'automated verification at scale.' if cluster_id=='C' else 'MLIR unification, machine learning in compilers.' if cluster_id in ('D','E') else 'Byzantine consensus efficiency, CRDTs for strong consistency.' if cluster_id=='F' else 'io_uring evolution, eBPF for observability.'}
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

**In one paragraph:** {concept}

**Key references:**
- ISO C++ Standard (latest draft: N4950+)
- Relevant WG21 papers (see proposal numbers)
- Academic papers in the reading list

**Pattern:** {_pattern(cluster_id)}

**5 expert pitfalls:**
1. Confusing specification with implementation (compilers may differ).
2. Assuming a feature is zero-cost without measuring.
3. Ignoring ABI implications for library interfaces.
4. Not testing with multiple compilers (GCC, Clang, MSVC).
5. Over-abstracting when simplicity would suffice.

---
{_engineering(cluster_id)}

*Compile:* `g++ -std=c++23 -O2 -Wall -Wextra main.cpp` (or `-std=c++2b` for bleeding edge)
"""

def _default(name, kind):
    if kind == "impl1":
        return f"""#include <iostream>
// Research-level implementation template for: {name}
// This topic requires deep understanding of the underlying theory.
// See references in the chapter for complete implementations.
int main() {{
    std::cout << "Topic: {name}" << std::endl;
    return 0;
}}"""
    return f"""#include <iostream>
// Alternative perspective / comparison for: {name}
// Consider how this would be expressed in Rust, Haskell, or formal specification.
int main() {{
    return 0;
}}"""

def gen():
    out_dir = os.path.join(BASE, "C100_Expert_Research_Level")
    os.makedirs(out_dir, exist_ok=True)
    n = 0
    for idx, name in enumerate(C100, 1):
        cluster_id, cluster_name = get_cluster(idx)
        if name in HOT:
            concept, impl1, impl2 = HOT[name]
            chap = make_chapter(name, idx, cluster_id, cluster_name, concept, impl1, impl2)
        else:
            chap = make_chapter(name, idx, cluster_id, cluster_name)
        with open(os.path.join(out_dir, fname(name, idx)), 'w') as f:
            f.write(chap)
        n += 1
    return n

def main():
    count = gen()

    with open(os.path.join(BASE, "INDEX.md"), 'w') as f:
        f.write(f"# Level 10 — Elite Pro / Master Problem Guide\n\n**Total:** {count} topics\n\n")
        for (lo, hi), (cid, cname) in sorted(CLUSTERS.items()):
            f.write(f"## Cluster {cid}: {cname} (Topics {lo}–{hi})\n\n")
            for i in range(lo, hi+1):
                name = C100[i-1]
                f.write(f"- [{i:03d}. {name}]({f'C100_Expert_Research_Level/{fname(name, i)}'})\n")
            f.write("\n")
    print(f"✅ Generated {count} chapters")

if __name__ == "__main__":
    main()
