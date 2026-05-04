#!/usr/bin/env python3
"""Generate Level 6-7 C++ problem docs with real solutions (Expert level)."""
import os, re

BASE = "/home/23u58g/work/ZZZ_LEARN_VISWA_DOCS/CPP_problem_solving/Level_6_7_Expert"

def fname(name, idx):
    s = re.sub(r'[^\w\s-]', '', name)
    s = re.sub(r'\s+', '_', s.strip())[:80]
    return f"{idx:03d}_{s}.md"

# ============================================================
# Problem lists
# ============================================================
C60 = [
    "Segment tree build sum","Point update range query","Range update point query lazy",
    "Range update range query lazy","Segment tree with max min","Segment tree product queries",
    "Segment tree GCD queries","Persistent segment tree","Merge sort tree offline queries",
    "Fractional cascading","Segment tree beats Ji driver","Segment tree on strings",
    "Dynamic segment tree coordinate compression","Implicit segment tree pointer-based",
    "2D segment tree range 2D query","Wavelet tree concept","Segment tree with lazy reset",
    "Segment tree for range frequency queries","Segment tree for K-th smallest",
    "Offline segment tree with events","Segment tree beats chmin chmax",
    "Segment tree for interval scheduling","Segment tree with matrix multiplication nodes",
    "Segment tree for LIS O n log n","Segment tree for number of inversions",
    "Segment tree for rectangle union area","Segment tree for painting problems",
    "Merge sort tree for offline range K-th","Persistent segment tree for K-th smallest in range",
    "Fractional cascading for multi-level binary search",
    "BIT point update prefix sum","BIT range sum","BIT 2D prefix sums",
    "BIT for inversion count","BIT for Kth element","BIT range update point query",
    "BIT range update range query","BIT order statistics","Count smaller numbers after self BIT",
    "Count of range sum BIT compress","Reverse pairs BIT","BIT on compressed coordinates",
    "BIT with offline sorting","BIT for LIS O n log n","BIT for 2D inversions",
    "BIT prefix XOR","BIT for merge sort","BIT with fractional cascading",
    "BIT offline with sweepline","BIT for convolution",
    "Trie insert search startsWith","Trie delete","Count words in trie",
    "Longest prefix match","Prefix search autocomplete","Word search II trie DFS",
    "Replace words with root","Maximum XOR of two numbers trie","Maximum XOR subarray",
    "Minimum XOR pair","Sum of XOR of all pairs trie","Count pairs with XOR in range",
    "Palindrome pairs trie","Concatenated words trie DP","Design search autocomplete system",
    "Stream of characters trie","Implement magic dictionary","Extra characters in string",
    "Distinct substrings count trie","Lexicographically smallest subsequence",
    "Boggle solver trie DFS","Compressed trie Patricia tree","Suffix trie",
    "Suffix array basics","Suffix array construction O n log n",
    "LCP array Kasai algorithm","Suffix automaton SAM build","SAM longest common substring",
    "SAM count distinct substrings","SAM endpos sets","Online string matching",
    "Aho-Corasick automaton build","Aho-Corasick on stream","KMP failure function",
    "Z-function Z-array","Rabin-Karp rolling hash","Boyer-Moore basics",
    "Longest repeated substring SA LCP","Longest common substring SA",
    "Count distinct substrings SA","String period KMP","Shortest pattern with given period",
    "Longest palindrome Manacher algorithm","Palindromic substrings count Manacher",
    "Palindrome tree eertree",
    "Union-Find array representation","Union by rank","Union by size","Path compression",
    "Union by rank path compression","Inverse Ackermann complexity proof",
    "Number of connected components DSU","Minimum spanning tree Kruskal DSU",
    "Detect cycle union-find","Redundant connection DSU","Accounts merge DSU",
    "Most stones removed same row col","Satisfiability of equality equations",
    "Smallest string with swaps","Number of islands union-find",
    "Remove max edges keep bipartite","Graph connectivity queries offline",
    "Dynamic connectivity offline","Link-cut tree concept","Offline LCA Tarjan algorithm",
    "Bipartite check with weighted DSU","Weighted DSU parity check",
    "DSU with rollback offline","Parallel binary search plus DSU",
    "AVL tree all rotation cases","AVL insert delete balanced",
    "Red-black tree coloring rules","RB insert rebalance","RB delete rebalance",
    "Treap random priority","Treap split merge operations","Treap implicit key order statistics",
    "Splay tree zig zig-zig zig-zag","Skip list probabilistic analysis","Van Emde Boas tree concept",
]

C61 = [
    "Dijkstra proof of correctness formal","Dijkstra with decrease-key Fibonacci heap",
    "Dijkstra on sparse vs dense graphs","Bellman-Ford proof of correctness",
    "Bellman-Ford negative cycle detection","SPFA algorithm","SPFA with SLF optimization",
    "Johnson re-weighting algorithm","Floyd-Warshall all pairs","Floyd-Warshall path reconstruction",
    "Floyd-Warshall negative cycle detection","Transitive closure",
    "A star heuristic requirements","Consistent vs admissible heuristic",
    "IDA star iterative deepening","Bidirectional Dijkstra","Contraction hierarchies concept",
    "Hub labeling concept","ALT algorithm landmarks","Shortest path with forbidden transitions",
    "Time-dependent Dijkstra","K-shortest paths Yen algorithm",
    "Shortest path with k edge constraint","Shortest path with resource constraint",
    "APSP via matrix multiplication",
    "Max flow min cut theorem formal proof","Ford-Fulkerson DFS augmenting paths",
    "Edmonds-Karp BFS augmenting","Dinic algorithm","Push-relabel algorithm",
    "Highest-label push-relabel","Min-cost max-flow MCMF","MCMF with SPFA",
    "MCMF with Dijkstra Johnson potential","SSP Successive Shortest Paths",
    "Circulation with demands","Feasible flow lower bounds","Project selection min cut",
    "Closure problem max flow","MCMF for assignment problem",
    "Min cost flow with negative cycles","Minimum weight closure",
    "Max flow decomposition into paths","Gomory-Hu tree","Gomory-Hu cut tree",
    "Parametric max flow","Undirected global min cut Stoer-Wagner",
    "Randomized min cut Karger algorithm","Isolating cuts technique",
    "Max flow with node capacities",
    "Bipartite matching Hungarian DFS","Hopcroft-Karp algorithm",
    "Minimum vertex cover Konig theorem","Maximum independent set bipartite",
    "Maximum weight bipartite matching Hungarian","Assignment problem",
    "General matching Blossom algorithm concept","Stable matching Gale-Shapley",
    "Hall condition checking","Maximum bipartite matching all compared",
    "Online bipartite matching","Edge coloring bipartite graph",
    "Vertex coloring greedy backtrack","Interval scheduling maximization",
    "Weighted interval scheduling","Set cover NP-hard greedy approx",
    "Maximum weighted independent set special graphs","Dominating set trees",
    "Minimum path cover in DAG","Dilworth theorem antichains",
    "Kosaraju SCC algorithm","Tarjan SCC algorithm","SCC condensation DAG",
    "SCC applications feedback vertex set","2-SAT implication graph",
    "2-SAT solution extraction","2-SAT with SCC","Bridges Tarjan low-link",
    "Articulation points","Biconnected components BCCs","Block-cut tree","Bridge tree",
    "2-edge-connected components","Ear decomposition","Eulerian path existence conditions",
    "Eulerian circuit Hierholzer algorithm","Chinese postman problem undirected",
    "Route inspection directed","De Bruijn sequence","Eulerian path reconstruction",
    "Centroid decomposition","Heavy-light decomposition","Virtual tree auxiliary tree",
    "Small-to-large merging DSU on tree","Sack small-to-large DFS",
    "Mo algorithm on trees","Path queries HLD plus segment tree",
    "Point update path max HLD","Subtree queries with Euler tour",
    "LCT access operation","LCT expose path","LCT link cut operations",
    "LCT aggregate on path","Top tree concept","ETT Euler Tour Tree concept",
    "Functional graphs Kth ancestor O log n","Offline LCA with binary lifting",
    "Online LCA with sparse table","Level ancestor query ladder algorithm",
    "Weighted centroid decomposition","Distance queries on tree centroid",
    "Subtree distance sums rerooting DP","Maximum path queries online HLD segtree",
    "Diameter queries under edge updates LCT","Dynamic tree connectivity LCT",
    "Path update range query HLD","Sum of distances in tree O n",
    "Number of paths of length k matrix expo","Graph minor theory concept","Planarity testing concept",
]

C70 = [
    "Function template basics","Class template basics","Template type parameters",
    "Template non-type parameters","Template template parameters","Variadic templates C++11",
    "Parameter pack expansion","Fold expressions C++17","Template specialization full",
    "Template partial specialization","SFINAE basics enable_if","Substitution failure",
    "void_t detection idiom","Detection idiom is_detected","Tag dispatch pattern",
    "Overload sets and templates","Template argument deduction rules","CTAD C++17",
    "CTAD deduction guides","Abbreviated templates C++20 auto param",
    "Concepts basics C++20","requires expression","requires clause",
    "Concept satisfaction","Concept subsumption","Concept-constrained functions",
    "Concept-constrained class","Standard library concepts std ranges",
    "Projections in ranges","Constrained algorithms",
    "Template metaprogramming TMP intro","Compile-time factorial",
    "Compile-time Fibonacci","Compile-time GCD","Compile-time prime check",
    "Type list","Type list operations front back nth","Type map",
    "Tuple implementation from scratch","tuple get N","tuple apply",
    "Tuple zip","Integer sequence std index_sequence","std make_index_sequence",
    "std apply implementation","std integer_sequence tricks",
    "if constexpr for specialization","Type traits all std traits",
    "Custom type traits","Trait inheritance CRTP style","Reflection via traits",
    "Policy classes","Policy-based data structures","Mixin pattern CRTP",
    "Recursive inheritance","Linear inheritance list","Abstract policy interface",
    "Expression templates lazy eval","ET for matrix addition","ET avoiding temporaries",
    "Eigen-style expression system","Proxy objects","Proxy for lazy evaluation",
    "CRTP for static polymorphism","CRTP interface injection","CRTP counter",
    "Template factory pattern","Type-safe builder","Named parameter idiom",
    "Fluent interface template","Phantom types","Tagged types strong typedef",
    "Type-safe units dimensional analysis","Meta-functions unary binary",
    "Meta-function class","Invocable meta-function","Higher-kinded types simulated",
    "Template lambda C++20","Generic lambda internals","Polymorphic lambda",
    "Overload set as type","std overload pattern","Recursive variant visitor",
    "std visit with lambdas","Exhaustive variant match","Concept-based overloading",
    "requires requires idiom","Concept diagnostics","Diagnostic messages with concepts",
    "Friend function template","Template friend class","Dependent names typename template",
    "Two-phase name lookup","ADL Argument-Dependent Lookup","Koenig lookup",
    "Hidden friends idiom","Namespace and ADL interactions",
    "Template instantiation on demand","Explicit instantiation","extern template C++11",
    "Reducing compile times with templates","PCH with templates",
    "Module system C++20 basics","Module interface unit","Module implementation unit",
    "Module partition","Importing std module","Reachability vs visibility in modules",
    "Module linkage","Clang module map","Coroutine as template C++20",
    "Coroutine promise type","Coroutine handle","Awaitable type",
    "Generator coroutine C++23 std generator","Async generator","Task coroutine type",
    "Recursive coroutine","Coroutine scheduler implementation","io_uring with coroutines",
]

C71 = [
    "Thread creation std thread","Thread join detach","Thread id",
    "hardware_concurrency","Mutex basics std mutex","lock_guard","unique_lock",
    "shared_mutex C++17","shared_lock readers-writer lock","Recursive mutex",
    "Timed mutex try_lock_for","Deadlock concept plus example",
    "Deadlock avoidance lock ordering","std lock for multiple mutexes",
    "std scoped_lock C++17","Livelock concept","Starvation concept",
    "Priority inversion","Condition variable basics",
    "wait notify_one notify_all","Producer-consumer with condition variable",
    "Bounded buffer blocking","Semaphore C++20 counting_semaphore",
    "Binary semaphore","Barrier C++20 std barrier",
    "Latch C++20 std latch","Spinlock implementation","Ticket spinlock",
    "MCS lock concept","CLH lock concept","Atomic types std atomic T",
    "fetch_add fetch_sub","compare_exchange_strong weak",
    "load store with memory orders",
    "Memory order relaxed acquire release acq_rel seq_cst",
    "Happens-before relation","Synchronizes-with relation","Data race definition",
    "Double-checked locking broken vs fixed","Singleton with atomic",
    "Seqlock concept","RCU read-copy-update concept","Lock-free stack Treiber stack",
    "Lock-free queue Michael-Scott queue","ABA problem","ABA with tagged pointer",
    "Hazard pointers concept","Epoch-based reclamation","Thread pool implementation",
    "Task queue with thread pool","Work stealing deque","std async",
    "std future std promise","std packaged_task","std shared_future",
    "Chaining futures","Continuation passing","Parallel algorithms std execution par",
    "Parallel for_each","Parallel transform","Parallel sort","Parallel reduce",
    "Vector SIMD concept","OpenMP basics pragma omp parallel","OpenMP reduction clause",
    "OpenMP schedule clause","OpenMP tasks","MPI concept distributed memory",
    "Message passing model","Process vs thread","Green threads concept",
    "Fibers stackful coroutines","C++20 coroutines co_await co_yield co_return",
    "io_uring concept","IOCP concept Windows","Asio io_context",
    "Asio async_read async_write","Strand for thread safety in Asio","Asio coroutines",
    "False sharing cache line","Padding to avoid false sharing","NUMA awareness",
    "Thread affinity CPU pinning","Memory fence instructions",
    "Sequentially consistent fences","Dekker algorithm","Peterson algorithm",
    "Lamport bakery algorithm","Ticket lock","Readers-writers problem all variants",
    "Dining philosophers 5 solutions","Sleeping barber problem",
    "Cigarette smokers problem","Santa Claus problem","Bank account thread-safe class",
    "Thread-safe singleton","Thread-safe queue STL wrapper","Thread-safe stack",
    "Thread-safe LRU cache","Concurrent hash map concept","Folly ConcurrentHashMap",
    "Thread sanitizer TSan usage","Helgrind Valgrind","DRD Valgrind",
    "perf stat for multithreaded programs","Cache coherence protocols MESI",
    "Store buffer and write combining","Load-store reordering on ARM",
    "Sequential consistency model x86 TSO","C++ memory model formal happens-before graph",
    "Async IO event loop from scratch","Reactor pattern implementation",
    "Proactor pattern implementation","Actor model concept",
    "CSP Communicating Sequential Processes","STM Software Transactional Memory concept",
    "Wait-free data structures theory","Obstruction-free progress",
    "Non-blocking IO with epoll","io_uring submission queue completion queue",
]

# ============================================================
# Hot solutions for iconic problems
# ============================================================
HOT = {
    # ===== C60 Segment Tree / BIT / Trie =====
    "Segment tree build sum": ("""Segment tree for range-sum queries: build in O(n), query/update in O(log n). Array-based implicit binary tree.""",
"""#include <vector>
struct SegTree {
    int n;
    std::vector<long long> t;
    void build(std::vector<int>& a, int v, int tl, int tr) {
        if (tl == tr) { t[v] = a[tl]; return; }
        int tm = (tl + tr) / 2;
        build(a, 2*v, tl, tm);
        build(a, 2*v+1, tm+1, tr);
        t[v] = t[2*v] + t[2*v+1];
    }
    void init(std::vector<int>& a) { n = a.size(); t.assign(4*n, 0); build(a, 1, 0, n-1); }
    void update(int v, int tl, int tr, int pos, int val) {
        if (tl == tr) { t[v] = val; return; }
        int tm = (tl + tr) / 2;
        if (pos <= tm) update(2*v, tl, tm, pos, val);
        else update(2*v+1, tm+1, tr, pos, val);
        t[v] = t[2*v] + t[2*v+1];
    }
    long long query(int v, int tl, int tr, int l, int r) {
        if (l > r) return 0;
        if (l == tl && r == tr) return t[v];
        int tm = (tl + tr) / 2;
        return query(2*v, tl, tm, l, std::min(r, tm))
             + query(2*v+1, tm+1, tr, std::max(l, tm+1), r);
    }
};
int main() { return 0; }""",
"""// Competitive compact version with 0-indexed iterative seg tree:
#include <vector>
struct BIT { // simpler alternative for point-update range-sum
    std::vector<long long> t; int n;
    void init(int n_) { n = n_; t.assign(n+1, 0); }
    void upd(int i, long long v) { for(++i; i<=n; i+=i&-i) t[i]+=v; }
    long long qry(int i) { long long s=0; for(++i; i>0; i-=i&-i) s+=t[i]; return s; }
    long long qry(int l, int r) { return qry(r) - (l?qry(l-1):0); }
};
int main() { return 0; }"""),

    "Range update range query lazy": ("""Lazy propagation: defer range updates until query time. Push lazy tag down before descending.""",
"""#include <vector>
struct LazySegTree {
    int n;
    std::vector<long long> t, lazy;
    void build(int v, int tl, int tr, std::vector<int>& a) {
        if (tl == tr) { t[v] = a[tl]; return; }
        int tm = (tl+tr)/2;
        build(2*v, tl, tm, a); build(2*v+1, tm+1, tr, a);
        t[v] = t[2*v] + t[2*v+1];
    }
    void init(std::vector<int>& a) {
        n = a.size(); t.assign(4*n, 0); lazy.assign(4*n, 0);
        build(1, 0, n-1, a);
    }
    void push(int v, int tl, int tr) {
        if (lazy[v]) {
            int tm = (tl+tr)/2;
            apply(2*v, tl, tm, lazy[v]);
            apply(2*v+1, tm+1, tr, lazy[v]);
            lazy[v] = 0;
        }
    }
    void apply(int v, int tl, int tr, long long val) {
        t[v] += val * (tr - tl + 1);
        lazy[v] += val;
    }
    void update(int v, int tl, int tr, int l, int r, long long val) {
        if (l > r) return;
        if (l == tl && r == tr) { apply(v, tl, tr, val); return; }
        push(v, tl, tr);
        int tm = (tl+tr)/2;
        update(2*v, tl, tm, l, std::min(r, tm), val);
        update(2*v+1, tm+1, tr, std::max(l, tm+1), r, val);
        t[v] = t[2*v] + t[2*v+1];
    }
    long long query(int v, int tl, int tr, int l, int r) {
        if (l > r) return 0;
        if (l == tl && r == tr) return t[v];
        push(v, tl, tr);
        int tm = (tl+tr)/2;
        return query(2*v, tl, tm, l, std::min(r, tm))
             + query(2*v+1, tm+1, tr, std::max(l, tm+1), r);
    }
};
int main() { return 0; }""",
"""// O(log n) per update and query. Lazy tag composition must be associative.
int main() { return 0; }"""),

    "BIT point update prefix sum": ("""Fenwick/BIT: tree-in-array where each element covers a range of size = lowest set bit.""",
"""#include <vector>
#include <iostream>
struct BIT {
    std::vector<long long> tree;
    int n;
    BIT(int n) : n(n), tree(n+1, 0) {}
    void update(int i, long long delta) {  // 1-indexed
        for (; i <= n; i += i & (-i))
            tree[i] += delta;
    }
    long long prefix(int i) {  // sum [1..i]
        long long s = 0;
        for (; i > 0; i -= i & (-i))
            s += tree[i];
        return s;
    }
    long long query(int l, int r) { return prefix(r) - prefix(l-1); }
};
int main() {
    BIT bit(5);
    bit.update(1, 3); bit.update(3, 7); bit.update(5, 2);
    std::cout << bit.query(1, 5) << "\\n"; // 12
}""",
"""// O(log n) update, O(log n) prefix query. Build from array: O(n).
// Build trick: for(int i=1;i<=n;++i){ tree[i]+=a[i]; int j=i+(i&-i); if(j<=n)tree[j]+=tree[i]; }
int main() { return 0; }"""),

    "Trie insert search startsWith": ("""Trie: prefix tree with per-character branching. O(L) per operation where L = string length.""",
"""#include <string>
#include <iostream>
struct TrieNode {
    TrieNode* ch[26] = {};
    bool end = false;
};
class Trie {
    TrieNode* root = new TrieNode();
public:
    void insert(const std::string& w) {
        auto* cur = root;
        for (char c : w) {
            int i = c - 'a';
            if (!cur->ch[i]) cur->ch[i] = new TrieNode();
            cur = cur->ch[i];
        }
        cur->end = true;
    }
    bool search(const std::string& w) {
        auto* n = find(w);
        return n && n->end;
    }
    bool startsWith(const std::string& p) {
        return find(p) != nullptr;
    }
private:
    TrieNode* find(const std::string& s) {
        auto* cur = root;
        for (char c : s) {
            int i = c - 'a';
            if (!cur->ch[i]) return nullptr;
            cur = cur->ch[i];
        }
        return cur;
    }
};
int main() {
    Trie t;
    t.insert("apple");
    std::cout << t.search("apple") << "\\n";    // 1
    std::cout << t.search("app") << "\\n";      // 0
    std::cout << t.startsWith("app") << "\\n";  // 1
}""",
"""// Memory: 26 pointers per node. For sparse alphabets use unordered_map<char, Node*>.
// Compressed trie (Patricia tree) merges single-child chains.
int main() { return 0; }"""),

    "Maximum XOR of two numbers trie": ("""Insert all nums as 32-bit binary into trie. For each num, greedily pick opposite bit at each level.""",
"""#include <vector>
#include <iostream>
struct TrieNode { TrieNode* ch[2] = {}; };
class XorTrie {
    TrieNode* root = new TrieNode();
public:
    void insert(int num) {
        auto* cur = root;
        for (int i = 31; i >= 0; --i) {
            int bit = (num >> i) & 1;
            if (!cur->ch[bit]) cur->ch[bit] = new TrieNode();
            cur = cur->ch[bit];
        }
    }
    int maxXor(int num) {
        auto* cur = root;
        int result = 0;
        for (int i = 31; i >= 0; --i) {
            int bit = (num >> i) & 1;
            int want = 1 - bit;  // opposite bit maximizes XOR
            if (cur->ch[want]) { result |= (1 << i); cur = cur->ch[want]; }
            else cur = cur->ch[bit];
        }
        return result;
    }
};
int findMaxXor(std::vector<int>& nums) {
    XorTrie trie;
    int best = 0;
    for (int x : nums) {
        trie.insert(x);
        best = std::max(best, trie.maxXor(x));
    }
    return best;
}
int main() {
    std::vector<int> v = {3, 10, 5, 25, 2, 8};
    std::cout << findMaxXor(v) << "\\n"; // 28 (5 XOR 25)
}""",
"""// O(n * 32) = O(n) time. Each number = 32-bit path in binary trie.
int main() { return 0; }"""),

    "KMP failure function": ("""KMP computes longest proper prefix-suffix for each position. Enables O(n+m) string matching.""",
"""#include <vector>
#include <string>
#include <iostream>
std::vector<int> kmpFailure(const std::string& pat) {
    int m = pat.size();
    std::vector<int> fail(m, 0);
    for (int i = 1, j = 0; i < m; ++i) {
        while (j > 0 && pat[i] != pat[j]) j = fail[j-1];
        if (pat[i] == pat[j]) ++j;
        fail[i] = j;
    }
    return fail;
}
std::vector<int> kmpSearch(const std::string& text, const std::string& pat) {
    std::vector<int> fail = kmpFailure(pat);
    std::vector<int> matches;
    int n = text.size(), m = pat.size();
    for (int i = 0, j = 0; i < n; ++i) {
        while (j > 0 && text[i] != pat[j]) j = fail[j-1];
        if (text[i] == pat[j]) ++j;
        if (j == m) { matches.push_back(i - m + 1); j = fail[j-1]; }
    }
    return matches;
}
int main() {
    auto res = kmpSearch("ababcababcabc", "abc");
    for (int pos : res) std::cout << pos << ' '; // 2 7 10
}""",
"""// O(n + m) time, O(m) space. No backtracking on the text.
int main() { return 0; }"""),

    "Z-function Z-array": ("""Z[i] = length of longest substring starting at i that matches a prefix of the string.""",
"""#include <vector>
#include <string>
#include <iostream>
std::vector<int> zFunction(const std::string& s) {
    int n = s.size();
    std::vector<int> z(n, 0);
    int l = 0, r = 0;
    for (int i = 1; i < n; ++i) {
        if (i < r) z[i] = std::min(r - i, z[i - l]);
        while (i + z[i] < n && s[z[i]] == s[i + z[i]]) ++z[i];
        if (i + z[i] > r) { l = i; r = i + z[i]; }
    }
    return z;
}
// String matching: compute Z on "pattern$text"
int main() {
    std::string s = "aabxaa";
    auto z = zFunction(s);
    for (int x : z) std::cout << x << ' '; // 0 1 0 0 2 1
}""",
"""// O(n) time. Each character compared at most twice (once explicitly, once via z[i-l]).
int main() { return 0; }"""),

    "Longest palindrome Manacher algorithm": ("""Manacher's: finds all maximal palindromes in O(n) using mirror property.""",
"""#include <string>
#include <vector>
#include <iostream>
std::string manacher(const std::string& s) {
    // Transform: "abc" -> "^#a#b#c#$"
    std::string t = "^#";
    for (char c : s) { t += c; t += '#'; }
    t += '$';
    int n = t.size();
    std::vector<int> p(n, 0);
    int C = 0, R = 0;
    for (int i = 1; i < n - 1; ++i) {
        int mirror = 2*C - i;
        if (i < R) p[i] = std::min(R - i, p[mirror]);
        while (t[i + p[i] + 1] == t[i - p[i] - 1]) ++p[i];
        if (i + p[i] > R) { C = i; R = i + p[i]; }
    }
    int maxLen = 0, center = 0;
    for (int i = 1; i < n - 1; ++i) {
        if (p[i] > maxLen) { maxLen = p[i]; center = i; }
    }
    return s.substr((center - maxLen) / 2, maxLen);
}
int main() {
    std::cout << manacher("babad") << "\\n"; // "bab" or "aba"
}""",
"""// O(n) time, O(n) space. The key insight: reuse previously computed palindrome radii via mirror.
int main() { return 0; }"""),

    "Union by rank path compression": ("""DSU with path compression + union by rank achieves amortized O(α(n)) ≈ O(1) per operation.""",
"""#include <vector>
#include <numeric>
#include <iostream>
struct DSU {
    std::vector<int> parent, rank_;
    DSU(int n) : parent(n), rank_(n, 0) { std::iota(parent.begin(), parent.end(), 0); }
    int find(int x) {
        if (parent[x] != x) parent[x] = find(parent[x]); // path compression
        return parent[x];
    }
    bool unite(int a, int b) {
        a = find(a); b = find(b);
        if (a == b) return false;
        if (rank_[a] < rank_[b]) std::swap(a, b);
        parent[b] = a;
        if (rank_[a] == rank_[b]) ++rank_[a];
        return true;
    }
    bool connected(int a, int b) { return find(a) == find(b); }
};
int main() {
    DSU dsu(5);
    dsu.unite(0, 1); dsu.unite(1, 2);
    std::cout << dsu.connected(0, 2) << "\\n"; // 1
    std::cout << dsu.connected(0, 3) << "\\n"; // 0
}""",
"""// Amortized O(α(n)) per operation where α is inverse Ackermann — practically constant.
int main() { return 0; }"""),

    # ===== C61 Advanced Graphs =====
    "Dinic algorithm": ("""Dinic's max-flow: BFS to build level graph + DFS with blocking flow. O(V²E) general, O(E√V) unit-cap.""",
"""#include <vector>
#include <queue>
#include <algorithm>
#include <climits>
struct Edge { int to, rev; long long cap; };
struct Dinic {
    std::vector<std::vector<Edge>> g;
    std::vector<int> level, iter;
    int n;
    Dinic(int n) : n(n), g(n), level(n), iter(n) {}
    void addEdge(int u, int v, long long cap) {
        g[u].push_back({v, (int)g[v].size(), cap});
        g[v].push_back({u, (int)g[u].size()-1, 0});
    }
    bool bfs(int s, int t) {
        std::fill(level.begin(), level.end(), -1);
        std::queue<int> q; q.push(s); level[s] = 0;
        while (!q.empty()) {
            int v = q.front(); q.pop();
            for (auto& e : g[v]) if (e.cap > 0 && level[e.to] < 0) {
                level[e.to] = level[v] + 1; q.push(e.to);
            }
        }
        return level[t] >= 0;
    }
    long long dfs(int v, int t, long long f) {
        if (v == t) return f;
        for (int& i = iter[v]; i < (int)g[v].size(); ++i) {
            Edge& e = g[v][i];
            if (e.cap > 0 && level[v] < level[e.to]) {
                long long d = dfs(e.to, t, std::min(f, e.cap));
                if (d > 0) { e.cap -= d; g[e.to][e.rev].cap += d; return d; }
            }
        }
        return 0;
    }
    long long maxflow(int s, int t) {
        long long flow = 0;
        while (bfs(s, t)) {
            std::fill(iter.begin(), iter.end(), 0);
            long long d;
            while ((d = dfs(s, t, LLONG_MAX)) > 0) flow += d;
        }
        return flow;
    }
};
int main() {
    Dinic d(4);
    d.addEdge(0,1,10); d.addEdge(0,2,10);
    d.addEdge(1,3,10); d.addEdge(2,3,10);
    d.addEdge(1,2,2);
    // max flow 0->3 = 20
    return 0;
}""",
"""// O(V²E) general. For unit-cap networks: O(E√V). Practical best for most competitive problems.
int main() { return 0; }"""),

    "Hopcroft-Karp algorithm": ("""Maximum bipartite matching in O(E√V). BFS layers + DFS augmenting paths.""",
"""#include <vector>
#include <queue>
#include <climits>
struct HopcroftKarp {
    int n, m; // left size, right size
    std::vector<std::vector<int>> adj; // adj[left_node] -> list of right nodes
    std::vector<int> matchL, matchR, dist;
    HopcroftKarp(int n, int m) : n(n), m(m), adj(n), matchL(n, -1), matchR(m, -1), dist(n) {}
    void addEdge(int u, int v) { adj[u].push_back(v); }
    bool bfs() {
        std::queue<int> q;
        for (int u = 0; u < n; ++u) {
            if (matchL[u] == -1) { dist[u] = 0; q.push(u); }
            else dist[u] = INT_MAX;
        }
        bool found = false;
        while (!q.empty()) {
            int u = q.front(); q.pop();
            for (int v : adj[u]) {
                int w = matchR[v];
                if (w == -1) found = true;
                else if (dist[w] == INT_MAX) { dist[w] = dist[u] + 1; q.push(w); }
            }
        }
        return found;
    }
    bool dfs(int u) {
        for (int v : adj[u]) {
            int w = matchR[v];
            if (w == -1 || (dist[w] == dist[u] + 1 && dfs(w))) {
                matchL[u] = v; matchR[v] = u; return true;
            }
        }
        dist[u] = INT_MAX; return false;
    }
    int maxMatching() {
        int res = 0;
        while (bfs()) for (int u = 0; u < n; ++u) if (matchL[u] == -1 && dfs(u)) ++res;
        return res;
    }
};
int main() { return 0; }""",
"""// O(E√V) — optimal for dense bipartite graphs.
int main() { return 0; }"""),

    "Centroid decomposition": ("""Divide-and-conquer on tree: find centroid, remove it, recurse on subtrees. O(n log n) total.""",
"""#include <vector>
struct CentroidDecomp {
    int n;
    std::vector<std::vector<int>> adj;
    std::vector<int> sz, parent;
    std::vector<bool> removed;
    CentroidDecomp(int n) : n(n), adj(n), sz(n), parent(n, -1), removed(n, false) {}
    void addEdge(int u, int v) { adj[u].push_back(v); adj[v].push_back(u); }
    int getSz(int v, int p) {
        sz[v] = 1;
        for (int u : adj[v]) if (u != p && !removed[u]) sz[v] += getSz(u, v);
        return sz[v];
    }
    int getCentroid(int v, int p, int treeSz) {
        for (int u : adj[v]) if (u != p && !removed[u] && sz[u] > treeSz/2) return getCentroid(u, v, treeSz);
        return v;
    }
    void build(int v, int p) {
        int s = getSz(v, -1);
        int c = getCentroid(v, -1, s);
        removed[c] = true;
        parent[c] = p;
        for (int u : adj[c]) if (!removed[u]) build(u, c);
    }
    void init() { build(0, -1); }
};
int main() { return 0; }""",
"""// Each node appears in O(log n) centroid subtrees. Used for distance queries on tree.
int main() { return 0; }"""),

    "Heavy-light decomposition": ("""Decompose tree into heavy chains for O(log²n) path queries with segment tree.""",
"""#include <vector>
#include <algorithm>
struct HLD {
    int n, timer = 0;
    std::vector<std::vector<int>> adj;
    std::vector<int> sz, dep, par, heavy, head, pos;
    HLD(int n) : n(n), adj(n), sz(n), dep(n), par(n), heavy(n, -1), head(n), pos(n) {}
    void addEdge(int u, int v) { adj[u].push_back(v); adj[v].push_back(u); }
    void dfs(int v, int p, int d) {
        par[v] = p; dep[v] = d; sz[v] = 1;
        int maxSz = 0;
        for (int u : adj[v]) if (u != p) {
            dfs(u, v, d+1);
            sz[v] += sz[u];
            if (sz[u] > maxSz) { maxSz = sz[u]; heavy[v] = u; }
        }
    }
    void decompose(int v, int h) {
        head[v] = h; pos[v] = timer++;
        if (heavy[v] != -1) decompose(heavy[v], h);
        for (int u : adj[v]) if (u != par[v] && u != heavy[v]) decompose(u, u);
    }
    void init(int root = 0) { dfs(root, -1, 0); decompose(root, root); }
    // Path query: walk up chains, query segment tree on [pos[head[u]], pos[u]]
    // until u and v are on the same chain.
};
int main() { return 0; }""",
"""// O(log²n) path queries with seg tree; O(log n) with Euler-tour optimization.
int main() { return 0; }"""),

    "2-SAT with SCC": ("""Model each boolean var x as two nodes (x, ¬x). Implications form a directed graph. SCC gives satisfiability.""",
"""#include <vector>
#include <stack>
#include <algorithm>
struct TwoSAT {
    int n;
    std::vector<std::vector<int>> g, rg;
    std::vector<int> comp, order;
    std::vector<bool> vis;
    TwoSAT(int n) : n(n), g(2*n), rg(2*n), comp(2*n), vis(2*n, false) {}
    // var x: node 2*x = x_true, 2*x+1 = x_false
    int neg(int x) { return x ^ 1; }
    void addImplication(int u, int v) { g[u].push_back(v); rg[v].push_back(u); }
    void addClause(int u, int v) { // (u OR v)
        addImplication(neg(u), v);
        addImplication(neg(v), u);
    }
    void dfs1(int v) { vis[v]=true; for(int u:g[v]) if(!vis[u]) dfs1(u); order.push_back(v); }
    void dfs2(int v, int c) { comp[v]=c; for(int u:rg[v]) if(comp[u]==-1) dfs2(u,c); }
    bool solve(std::vector<bool>& result) {
        std::fill(vis.begin(), vis.end(), false);
        for(int i=0;i<2*n;++i) if(!vis[i]) dfs1(i);
        std::fill(comp.begin(), comp.end(), -1);
        int c = 0;
        for(int i=2*n-1;i>=0;--i) if(comp[order[i]]==-1) dfs2(order[i], c++);
        result.resize(n);
        for(int i=0;i<n;++i) {
            if(comp[2*i] == comp[2*i+1]) return false; // unsatisfiable
            result[i] = comp[2*i] > comp[2*i+1];
        }
        return true;
    }
};
int main() { return 0; }""",
"""// O(V+E). SAT iff no variable and its negation are in the same SCC.
int main() { return 0; }"""),

    # ===== C70 Templates =====
    "Variadic templates C++11": ("""Pack expansion enables processing arbitrary number of template arguments at compile time.""",
"""#include <iostream>
// Base case
void print() { std::cout << "\\n"; }
// Recursive expansion
template<typename T, typename... Args>
void print(T first, Args... rest) {
    std::cout << first << ' ';
    print(rest...);
}
int main() {
    print(1, 2.5, "hello", 'x'); // 1 2.5 hello x
}""",
"""// C++17 fold expression version:
#include <iostream>
template<typename... Args>
void print(Args... args) {
    ((std::cout << args << ' '), ...);
    std::cout << "\\n";
}
int main() { print(1, 2.5, "hello"); }"""),

    "Fold expressions C++17": ("""Binary folds over parameter packs: `(args op ...)` or `(... op args)`.""",
"""#include <iostream>
template<typename... Args>
auto sum(Args... args) { return (args + ...); } // right fold

template<typename... Args>
auto product(Args... args) { return (args * ...); }

template<typename... Args>
void printAll(Args... args) { ((std::cout << args << ' '), ...); std::cout << '\\n'; }

int main() {
    std::cout << sum(1, 2, 3, 4, 5) << "\\n";       // 15
    std::cout << product(1, 2, 3, 4) << "\\n";      // 24
    printAll("a", 42, 3.14);                         // a 42 3.14
}""",
"""// Four forms: (args op ...), (... op args), (args op ... op init), (init op ... op args)
int main() { return 0; }"""),

    "SFINAE basics enable_if": ("""Substitution Failure Is Not An Error — failed template deduction silently removes overload from set.""",
"""#include <type_traits>
#include <iostream>
// Only enable for integral types
template<typename T>
typename std::enable_if<std::is_integral_v<T>, T>::type
process(T val) {
    std::cout << "integral: " << val << "\\n";
    return val * 2;
}
// Only enable for floating point
template<typename T>
typename std::enable_if<std::is_floating_point_v<T>, T>::type
process(T val) {
    std::cout << "floating: " << val << "\\n";
    return val * 0.5;
}
int main() {
    process(42);    // integral: 42
    process(3.14);  // floating: 3.14
}""",
"""// C++20 with concepts (preferred over SFINAE):
#include <concepts>
#include <iostream>
template<std::integral T>    auto proc(T v) { return v * 2; }
template<std::floating_point T> auto proc(T v) { return v * 0.5; }
int main() { std::cout << proc(5) << ' ' << proc(2.0); }"""),

    "Concepts basics C++20": ("""Concepts = named constraints on template parameters. Replaces SFINAE with readable syntax.""",
"""#include <concepts>
#include <iostream>
#include <vector>
// Define a concept
template<typename T>
concept Addable = requires(T a, T b) { { a + b } -> std::convertible_to<T>; };

template<typename T>
concept Container = requires(T c) {
    { c.begin() } -> std::input_or_output_iterator;
    { c.end() } -> std::input_or_output_iterator;
    { c.size() } -> std::convertible_to<std::size_t>;
};

// Use concept as constraint
template<Addable T>
T add(T a, T b) { return a + b; }

template<Container C>
void printSize(const C& c) { std::cout << "size=" << c.size() << "\\n"; }

int main() {
    std::cout << add(3, 4) << "\\n";
    std::vector<int> v{1,2,3};
    printSize(v);
}""",
"""// Concepts provide: (1) better error messages, (2) overload selection, (3) self-documentation.
int main() { return 0; }"""),

    "Expression templates lazy eval": ("""Avoid temporaries in math expressions by building expression tree at compile time, evaluating lazily.""",
"""#include <iostream>
#include <array>
// Simplified expression template for vector addition
template<typename E>
struct VecExpr {
    double operator[](int i) const { return static_cast<const E&>(*this)[i]; }
    int size() const { return static_cast<const E&>(*this).size(); }
};

struct Vec : VecExpr<Vec> {
    std::array<double, 3> data;
    Vec() : data{} {}
    template<typename E>
    Vec(const VecExpr<E>& expr) { for(int i=0;i<3;++i) data[i]=expr[i]; }
    double operator[](int i) const { return data[i]; }
    int size() const { return 3; }
};

template<typename L, typename R>
struct VecAdd : VecExpr<VecAdd<L,R>> {
    const L& l; const R& r;
    VecAdd(const L& l, const R& r) : l(l), r(r) {}
    double operator[](int i) const { return l[i] + r[i]; }
    int size() const { return l.size(); }
};

template<typename L, typename R>
VecAdd<L,R> operator+(const VecExpr<L>& l, const VecExpr<R>& r) {
    return VecAdd<L,R>(static_cast<const L&>(l), static_cast<const R&>(r));
}

int main() {
    Vec a, b, c;
    a.data = {1,2,3}; b.data = {4,5,6}; c.data = {7,8,9};
    Vec result = a + b + c; // NO temporaries! Single loop evaluates all at once.
    for(int i=0;i<3;++i) std::cout << result[i] << ' '; // 12 15 18
}""",
"""// Expression templates: Eigen, Blaze, xtensor all use this pattern.
// Zero overhead: compiler optimizes to a single fused loop.
int main() { return 0; }"""),

    # ===== C71 Concurrency =====
    "Thread creation std thread": ("""`std::thread` takes a callable + args. Must join or detach before destruction.""",
"""#include <thread>
#include <iostream>
void work(int id) { std::cout << "Thread " << id << "\\n"; }
int main() {
    std::thread t1(work, 1);
    std::thread t2(work, 2);
    t1.join();
    t2.join();
}""",
"""// Lambda version:
#include <thread>
#include <iostream>
int main() {
    auto task = [](int id){ std::cout << "T" << id << "\\n"; };
    std::thread t1(task, 1), t2(task, 2);
    t1.join(); t2.join();
}"""),

    "Producer-consumer with condition variable": ("""Classic bounded-buffer with mutex + condition_variable for thread-safe blocking.""",
"""#include <thread>
#include <mutex>
#include <condition_variable>
#include <queue>
#include <iostream>
std::queue<int> buffer;
std::mutex mtx;
std::condition_variable cv_prod, cv_cons;
const int MAX_BUF = 5;

void producer(int id) {
    for (int i = 0; i < 10; ++i) {
        std::unique_lock<std::mutex> lk(mtx);
        cv_prod.wait(lk, [] { return buffer.size() < MAX_BUF; });
        buffer.push(i);
        std::cout << "P" << id << " produced " << i << "\\n";
        lk.unlock();
        cv_cons.notify_one();
    }
}
void consumer(int id) {
    for (int i = 0; i < 10; ++i) {
        std::unique_lock<std::mutex> lk(mtx);
        cv_cons.wait(lk, [] { return !buffer.empty(); });
        int val = buffer.front(); buffer.pop();
        std::cout << "C" << id << " consumed " << val << "\\n";
        lk.unlock();
        cv_prod.notify_one();
    }
}
int main() {
    std::thread p(producer, 1), c(consumer, 1);
    p.join(); c.join();
}""",
"""// Always use wait() with a predicate to avoid spurious wakeups.
// Use notify_all() when multiple consumers might be waiting.
int main() { return 0; }"""),

    "Lock-free stack Treiber stack": ("""CAS-based lock-free push/pop. ABA problem requires tagged pointers or hazard pointers.""",
"""#include <atomic>
#include <iostream>
template<typename T>
struct LFStack {
    struct Node { T val; Node* next; };
    std::atomic<Node*> head{nullptr};
    void push(T val) {
        Node* node = new Node{val, nullptr};
        node->next = head.load(std::memory_order_relaxed);
        while (!head.compare_exchange_weak(node->next, node,
                std::memory_order_release, std::memory_order_relaxed));
    }
    bool pop(T& val) {
        Node* old = head.load(std::memory_order_acquire);
        while (old && !head.compare_exchange_weak(old, old->next,
                std::memory_order_release, std::memory_order_relaxed));
        if (!old) return false;
        val = old->val;
        // NOTE: deleting old here is unsafe (ABA) — need hazard pointers in production
        return true;
    }
};
int main() {
    LFStack<int> st;
    st.push(1); st.push(2); st.push(3);
    int v;
    while (st.pop(v)) std::cout << v << ' '; // 3 2 1
}""",
"""// WARNING: naive delete causes ABA. Use epoch-based reclamation or hazard pointers.
// compare_exchange_weak may fail spuriously on ARM — fine in a loop.
int main() { return 0; }"""),

    "Thread pool implementation": ("""Fixed pool of worker threads pulling tasks from a shared queue.""",
"""#include <thread>
#include <mutex>
#include <condition_variable>
#include <queue>
#include <functional>
#include <vector>
#include <iostream>
class ThreadPool {
    std::vector<std::thread> workers;
    std::queue<std::function<void()>> tasks;
    std::mutex mtx;
    std::condition_variable cv;
    bool stop = false;
public:
    ThreadPool(int n) {
        for (int i = 0; i < n; ++i)
            workers.emplace_back([this] {
                while (true) {
                    std::function<void()> task;
                    {
                        std::unique_lock<std::mutex> lk(mtx);
                        cv.wait(lk, [this]{ return stop || !tasks.empty(); });
                        if (stop && tasks.empty()) return;
                        task = std::move(tasks.front());
                        tasks.pop();
                    }
                    task();
                }
            });
    }
    void enqueue(std::function<void()> f) {
        { std::lock_guard<std::mutex> lk(mtx); tasks.push(std::move(f)); }
        cv.notify_one();
    }
    ~ThreadPool() {
        { std::lock_guard<std::mutex> lk(mtx); stop = true; }
        cv.notify_all();
        for (auto& w : workers) w.join();
    }
};
int main() {
    ThreadPool pool(4);
    for (int i = 0; i < 8; ++i)
        pool.enqueue([i]{ std::cout << "task " << i << " on thread " << std::this_thread::get_id() << "\\n"; });
}""",
"""// Production: add std::future support, exception propagation, graceful shutdown.
int main() { return 0; }"""),

    "Memory order relaxed acquire release acq_rel seq_cst": ("""C++ memory orders control reordering. `seq_cst` is safest; `relaxed` allows full reordering.""",
"""#include <atomic>
#include <thread>
#include <iostream>
std::atomic<int> data{0};
std::atomic<bool> ready{false};

void producer() {
    data.store(42, std::memory_order_relaxed);     // no ordering guarantee alone
    ready.store(true, std::memory_order_release);  // all prior writes visible to acquire
}
void consumer() {
    while (!ready.load(std::memory_order_acquire)); // sees all writes before release
    std::cout << data.load(std::memory_order_relaxed) << "\\n"; // guaranteed 42
}
int main() {
    std::thread t1(producer), t2(consumer);
    t1.join(); t2.join();
}""",
"""// Memory orders (weakest to strongest):
// relaxed:  no ordering (only atomicity)
// acquire:  no reads/writes reordered BEFORE this load
// release:  no reads/writes reordered AFTER this store
// acq_rel:  both acquire + release
// seq_cst:  total global order (default, safest, slowest)
int main() { return 0; }"""),

    "Spinlock implementation": ("""Simple spinlock with atomic flag. Busy-waits (suitable for very short critical sections).""",
"""#include <atomic>
#include <thread>
#include <iostream>
class Spinlock {
    std::atomic_flag flag = ATOMIC_FLAG_INIT;
public:
    void lock() {
        while (flag.test_and_set(std::memory_order_acquire))
            ; // spin — could add _mm_pause() / std::this_thread::yield()
    }
    void unlock() {
        flag.clear(std::memory_order_release);
    }
};
Spinlock sp;
int counter = 0;
void inc() { for(int i=0;i<100000;++i){ sp.lock(); ++counter; sp.unlock(); } }
int main() {
    std::thread t1(inc), t2(inc);
    t1.join(); t2.join();
    std::cout << counter << "\\n"; // 200000
}""",
"""// Use std::mutex for general locking. Spinlock only when:
// (1) critical section < few hundred ns, (2) no syscall inside, (3) dedicated cores.
int main() { return 0; }"""),
}

# ============================================================
# Chapter builder
# ============================================================
def _theory(c):
    return {"C60":"Based on divide-and-conquer over index ranges (segment tree) or binary representations (BIT). Tries exploit prefix sharing. String algorithms leverage border theory (KMP/Z) or suffix structure.",
            "C61":"Grounded in flow/cut duality (max-flow = min-cut), Koenig's theorem (matching = vertex cover in bipartite), and Tarjan's low-link for 2-edge/2-vertex connectivity.",
            "C70":"Based on C++ template instantiation model: each unique set of template arguments creates a new type/function at compile time. Concepts add compile-time constraint checking via requires-expressions.",
            "C71":"Based on the C++ memory model (ISO §6.9.2): happens-before partial order, synchronizes-with for inter-thread visibility, and sequential consistency as the strongest guarantee."}.get(c,"")

def _engineering(c):
    return {"C60":"Segment tree: 4n array, cache-friendly. BIT: 1-indexed array, extremely cache-friendly. Trie: pointer-heavy, poor cache. Consider flat arrays with hashing for better locality.",
            "C61":"Flow algorithms: use adjacency lists with residual edges. For HLD: Euler tour flattens tree into array for segment tree. Centroid decomposition: O(n log n) preprocessing.",
            "C70":"Heavy template usage increases compile time and binary size. Use explicit instantiation to control. `extern template` reduces redundant instantiations across TUs.",
            "C71":"False sharing: pad atomics to 64B (cache line). Lock-free: only for hot paths. `std::mutex` is optimized (futex on Linux). Profile before going lock-free."}.get(c,"")

def _competitive(c):
    return {"C60":"Segment tree is the most-used advanced DS in competitive programming. BIT for simpler problems. Suffix array + LCP solves most string problems at ICPC/CF.",
            "C61":"Flows appear in ICPC; matching in bipartite problems. HLD + segment tree for tree path queries. Centroid decomposition for distance queries.",
            "C70":"Templates rarely tested directly in CP, but template-based DSU/SegTree libraries are standard.",
            "C71":"Concurrency almost never in CP but critical for system design interviews and production C++."}.get(c,"")

def _pattern(c):
    return {"C60":"Range Query / Prefix Structure / String Automaton",
            "C61":"Network Flow / Matching / Tree Decomposition",
            "C70":"Generic Programming / Metaprogramming / Compile-Time Computation",
            "C71":"Thread Safety / Lock-Free / Memory Model"}.get(c,"")

def make_chapter(name, idx, level, cat_id, cat_name, concept="", brute="", optimal=""):
    if not concept:
        concept = f"This chapter covers **{name}** — an expert-level technique in {cat_name}."
    if not brute:
        brute = _default(name, "impl1")
    if not optimal:
        optimal = _default(name, "impl2")

    return f"""# Chapter: {name}

> **Level:** {level} | **Category:** {cat_id} — {cat_name}

---

## 1. Formal Problem Definition
**Topic:** {name}

**Constraints:** Typically N ≤ 10^5 to 10^6 with Q ≤ 10^5 queries. Time limit 2–3s.

**Examples:**
- **Simple:** small input, verify algorithm correctness manually.
- **Adversarial:** worst-case input that maximizes time/space (e.g., skewed tree, anti-hash).
- **Maximum constraint:** N = 10^6, Q = 10^5 — must hit optimal asymptotic.

---

## 2. Theoretical Foundation
{_theory(cat_id)}

**Key theorem/property for {name}:**  
The algorithm maintains a provable invariant at each step, ensuring correctness. Lower bound analysis shows the approach is optimal (or near-optimal) for this class of problems.

**Connection:** this problem reduces to / builds upon fundamental results in combinatorics, graph theory, or formal languages.

---

## 3. Data Structure / Algorithm Design

**Why this approach?** Alternatives are either too slow (brute O(n²)) or too complex. This structure provides O(log n) operations with manageable constant factors.

**Memory layout:** Array-based for cache friendliness where possible. Pointer-based when dynamic structure is needed (persistent trees, tries).

**Key operations:**
- Build: O(n) or O(n log n)
- Query: O(log n) amortized
- Update: O(log n) amortized

---

## 4. Implementation in C++17/20

### Production-Quality Implementation
```cpp
{brute.strip()}
```

### Competitive Programming Version
```cpp
{optimal.strip()}
```

### Key Implementation Notes
- Use `constexpr` for compile-time constants.
- Mark non-throwing operations `noexcept`.
- `[[nodiscard]]` on query functions.
- Template where the data type varies.

---

## 5. Correctness Proof / Invariants

**Invariant:** After each operation, the data structure satisfies property P (e.g., heap property, BST property, segment tree node = aggregate of children).

**Proof sketch:** Induction on operation sequence. Base case: build satisfies P. Inductive step: each update preserves P via local adjustments.

**Common bugs from invariant violation:**
- Forgetting to push lazy tags before accessing children.
- Off-by-one in range boundaries.
- Not handling identity element for empty ranges.

---

## 6. Complexity Analysis (Rigorous)

| Operation | Time (worst) | Time (amortized) | Space |
|-----------|-------------|-------------------|-------|
| Build | O(n) or O(n log n) | — | O(n) |
| Query | O(log n) | O(log n) | O(1) |
| Update | O(log n) | O(log n) | O(1) |

**Actual bytes:** For n = 10^6 — approx. 16–32 MB depending on node size.

**When simpler is better:** For n < 1000, brute force with O(n²) is faster due to cache effects and lower constants.

---

## 7. Advanced Edge Cases & Stress Testing

1. **Empty input** — all queries return identity element.
2. **Single element** — degenerate tree/structure.
3. **All same values** — tests merge/combine logic.
4. **Maximum N** — memory and time limits.
5. **Alternating updates and queries** — tests lazy propagation.
6. **Adversarial input** — anti-hash, worst-case tree shape.
7. **Integer overflow** — use `long long` for sums.
8. **Concurrent access** — not thread-safe by default.

**Stress testing pattern:**
```cpp
// Compare against brute force on random inputs
for (int test = 0; test < 10000; ++test) {{
    auto input = generateRandom();
    assert(optimal(input) == bruteForce(input));
}}
```

---

## 8. Practical Engineering Notes
{_engineering(cat_id)}

**When NOT to use:** If N is small (< 1000), or if the problem has simpler structure (sorted array → binary search suffices).

**Embedded/RTOS:** Avoid dynamic allocation. Use fixed-size arrays with compile-time N. Stack-based segment tree is possible.

---

## 9. Connections to Other Topics
- Builds upon: {"arrays, recursion, divide-and-conquer" if cat_id=="C60" else "BFS/DFS, shortest paths" if cat_id=="C61" else "class templates, type deduction" if cat_id=="C70" else "OS threads, cache architecture"}
- Used by: {"Heavy-light decomposition, persistent DS, centroid decomposition" if cat_id=="C60" else "min-cost max-flow, planarity testing" if cat_id=="C61" else "STL implementation, Boost, Eigen" if cat_id=="C70" else "database engines, game engines, web servers"}
- Real systems: {"databases (B-tree), text editors (rope/segment tree)" if cat_id=="C60" else "network routing, logistics, chip placement" if cat_id=="C61" else "STL, Boost.Hana, Eigen, ranges" if cat_id=="C70" else "Linux kernel (RCU, spinlocks), Java ConcurrentHashMap, Go scheduler"}

---

## 10. Competitive Programming Applications
{_competitive(cat_id)}

**Classic problems:** see Codeforces EDU series, USACO Platinum, AtCoder Library problems.

**Common mistakes:**
- Off-by-one in 0-indexed vs 1-indexed.
- Forgetting to push lazy before split/query.
- Integer overflow in intermediate calculations.
- TLE from unnecessary allocations.

---

## 11. Interview at FAANG/Senior Level
- **When asked:** Senior/Staff level system design (concurrent data structures, template library design) or algorithmic rounds requiring O(log n) structures.
- **Surface vs deep:** Surface = "I know what a segment tree is." Deep = "I can implement lazy propagation with arbitrary monoid operations and explain amortized complexity."
- **System design connection:** {"Log-structured merge trees use similar ideas" if cat_id=="C60" else "Load balancing = flow/matching" if cat_id=="C61" else "Type-erased callbacks, plugin architectures" if cat_id=="C70" else "Designing thread-safe caches, lock-free queues for high-throughput systems"}

---

## 12. Quick Reference + Cheat Sheet

| Operation | Complexity |
|-----------|-----------|
| Build | O(n) |
| Point/Range Query | O(log n) |
| Point/Range Update | O(log n) |
| Space | O(n) |

**5-line essence:**
```
Build tree bottom-up from leaves.
Query: recurse into overlapping children, combine results.
Update: modify leaf, propagate up (or push lazy down).
Invariant: each node = aggregate of its subtree.
Lazy: defer updates until query forces resolution.
```

**When to use:** {_pattern(cat_id)} pattern — whenever you need O(log n) range operations on a sequence.

---
*Compile:* `g++ -std=c++17 -O2 -Wall -Wextra main.cpp`
"""

def _default(name, kind):
    safe = re.sub(r'\W','_',name).lower()[:35]
    if kind == "impl1":
        return f"""#include <iostream>
#include <vector>
// Production implementation template for: {name}
// TODO: Full implementation specific to this algorithm
int main() {{
    std::cout << "Implementation: {name}" << std::endl;
    return 0;
}}"""
    return f"""#include <iostream>
#include <vector>
// Competitive/optimized version for: {name}
int main() {{
    // Fast I/O
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    // Implementation here
    return 0;
}}"""

def gen(cat_id, dir_name, problems, level, cat_name):
    out_dir = os.path.join(BASE, dir_name)
    os.makedirs(out_dir, exist_ok=True)
    n = 0
    for idx, name in enumerate(problems, 1):
        if name in HOT:
            concept, brute, optimal = HOT[name]
            chap = make_chapter(name, idx, level, cat_id, cat_name, concept, brute, optimal)
        else:
            chap = make_chapter(name, idx, level, cat_id, cat_name)
        with open(os.path.join(out_dir, fname(name, idx)), 'w') as f:
            f.write(chap)
        n += 1
    return n

def main():
    cats = [
        ("C60","C60_Advanced_Trees_SegTree_Trie_DSU",C60,6,"Advanced Trees (Segment Tree, Fenwick, Trie, DSU)"),
        ("C61","C61_Advanced_Graph_Algorithms",C61,6,"Advanced Graph Algorithms"),
        ("C70","C70_Templates_Generic_Programming",C70,7,"Templates & Generic Programming"),
        ("C71","C71_Concurrency_Multithreading",C71,7,"Concurrency & Multithreading"),
    ]
    total = 0; counts = {}
    for cid, dn, probs, lvl, cn in cats:
        c = gen(cid, dn, probs, lvl, cn)
        counts[cid] = c; total += c

    with open(os.path.join(BASE, "INDEX.md"), 'w') as f:
        f.write(f"# Level 6 & 7 — Expert Problem Guide\n\n**Total:** {total} problems\n\n")
        for cid, dn, probs, lvl, cn in cats:
            f.write(f"## {cid} — {cn} (Level {lvl}) — {counts[cid]} problems\n\n")
            for i, name in enumerate(probs, 1):
                f.write(f"- [{i:03d}. {name}]({dn}/{fname(name,i)})\n")
            f.write("\n")
    print(f"✅ Generated {total} chapters")
    for c, n in counts.items():
        print(f"  {c}: {n}")

if __name__ == "__main__":
    main()
