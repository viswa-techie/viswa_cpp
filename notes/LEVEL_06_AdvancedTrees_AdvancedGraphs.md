# Level 6 — Expert: Advanced Trees & Advanced Graph Algorithms

> **Directory:** `Level_6_7_Expert/`  
> **Categories:** `C60_Advanced_Trees_SegTree_Trie_DSU` · `C61_Advanced_Graph_Algorithms`  
> **Total Files:** 130 + 120 = **250 files**  
> **Prerequisite:** Level 5 (DP, Heaps, Sorting)  
> **Leads to:** Level 7 (Templates, Concurrency)

---

## Overview

Level 6 moves from standard interview prep into competitive programming and systems-level algorithmic expertise. Segment trees, DSU with rollback, advanced graph algorithms (flow, matching, Hamilton paths) — these are the tools that separate a "good" engineer from an "exceptional" one in competitive contexts and high-performance systems.

---

## C60 — Advanced Trees: SegTree, Trie & DSU (130 files)

### What is Covered

| Range | Topics |
|-------|--------|
| 001–010 | Segment tree: build (sum), point update + range query, range update + point query (lazy), range update + range query (lazy propagation) |
| 011–020 | Segment tree with max/min, product queries, GCD queries; persistent segment tree (functional approach) |
| 021–030 | Merge sort tree; segment tree beats (Ji driver segmentation); offline segment tree queries |
| 031–040 | Trie deep-dive: wildcard search, prefix frequency count, XOR maximum pair, auto-complete system |
| 041–050 | Aho-Corasick automaton: build failure links, multi-string search, dictionary matching on stream |
| 051–060 | Suffix array (SA-IS / prefix-doubling), LCP array; suffix automaton; suffix tree (Ukkonen's algorithm concept) |
| 061–070 | DSU advanced: union by rank, path compression, weighted DSU, rollback DSU (persistent/offline) |
| 071–080 | Link-Cut Tree (LCT): access, link, cut, path queries on dynamic forest |
| 081–090 | Heavy-Light Decomposition (HLD): path queries + updates in O(log² n), HLD with segment tree |
| 091–100 | Centroid decomposition: offline path queries, distance queries on tree, centroid decomp + DSU |
| 101–110 | Euler tour technique: subtree queries with BIT/seg tree, LCA with RMQ (sparse table) |
| 111–120 | Sparse table: O(1) RMQ after O(n log n) build; Disjoint Sparse Table |
| 121–130 | Treap (split/merge, implicit key), Splay tree, Skip list analysis, Van Emde Boas tree concept |

### Key Concepts Learned
- Segment tree lazy propagation: defer updates to children until needed — critical for range updates
- Persistent segment tree: each update creates a new root, sharing unchanged nodes (functional style)
- Aho-Corasick extends KMP failure function to a trie — O(n + m + z) multi-pattern search
- Suffix array with LCP enables string LCP queries in O(1) after O(n log n) build
- HLD + segment tree: any path query in O(log² n) by decomposing into O(log n) heavy chains
- Link-Cut Tree: dynamic connectivity with O(log n) amortised operations using splay trees

### Patterns Introduced
- **Offline query processing** — sort queries, use DSU or segment tree
- **Persistent data structures** — immutable versioned updates
- **Heavy path decomposition** — linearise tree paths to arrays
- **Centroid decomposition** — divide tree by centroid for path queries

---

## C61 — Advanced Graph Algorithms (120 files)

### What is Covered

| Range | Topics |
|-------|--------|
| 001–010 | Dijkstra proofs, Dijkstra with Fibonacci heap (theoretical), Dijkstra sparse vs dense graph analysis |
| 011–020 | Bellman-Ford proof, negative cycle detection, SPFA + SLF optimisation; Johnson's re-weighting |
| 021–030 | Floyd-Warshall: all-pairs shortest path, transitive closure, minimax path; Floyd on graphs with negative cycles |
| 031–040 | Max-flow: Ford-Fulkerson (augmenting paths), Edmonds-Karp (BFS augmentation), Dinic's algorithm |
| 041–050 | Min-cut, max-flow min-cut theorem; push-relabel algorithm; min-cost max-flow (MCMF) |
| 051–060 | Bipartite matching: Hungarian algorithm, Hopcroft-Karp, König's theorem applications |
| 061–070 | Eulerian path/circuit (Hierholzer's algorithm); Hamiltonian path concept, TSP in graph context |
| 071–080 | Strongly connected components: Tarjan's (one DFS), Kosaraju's (two DFS passes); 2-SAT problem |
| 081–090 | Bridges, articulation points (Tarjan's bridge-finding); block-cut tree; ear decomposition |
| 091–100 | Planarity testing (Kuratowski's theorem concept); graph minor theory; graph colouring (greedy + chromatic number) |
| 101–110 | Virtual node technique, shortest path on DAG (DP), tree path problems via LCA + HLD |
| 111–120 | Path update range query with HLD, sum of distances in tree O(n), number of paths of length k (matrix exponentiation), planarity testing concept |

### Key Concepts Learned
- Dinic's algorithm: O(V² · E) worst case, but very fast in practice; uses blocking flows in level graphs
- Max-flow = Min-cut (fundamental theorem): useful for modelling partitioning problems
- Bipartite matching = max-flow with unit capacities; König's: max matching = min vertex cover
- 2-SAT: build implication graph → solve SCCs → each variable has consistent assignment
- Hierholzer's Eulerian circuit: O(V + E), exists iff all vertices have even degree (undirected)
- TSP: NP-hard in general; DP bitmask is O(2^n · n²) — only feasible for n ≤ 20

### Patterns Introduced
- **Max-flow modelling** — turn problem into network flow
- **2-SAT** — boolean satisfiability via SCC
- **Matrix exponentiation** — O(k³ log n) for counting paths of length n
- **Virtual source/sink** — add super-source to multi-source BFS/flow

---

## Level 6 — Revision Checklist

### Advanced Trees
- [ ] Implement segment tree with lazy propagation (range update + range query)
- [ ] Build Trie with XOR maximum pair problem
- [ ] Build Aho-Corasick automaton for multi-pattern search
- [ ] Explain HLD decomposition and how it maps paths to array ranges
- [ ] Build sparse table for O(1) range minimum query
- [ ] Implement weighted DSU with rollback

### Advanced Graphs
- [ ] Implement Dinic's max-flow algorithm
- [ ] Apply max-flow min-cut to a partitioning problem
- [ ] Implement Tarjan's SCC (single DFS with lowlink)
- [ ] Solve 2-SAT using implication graph + SCC
- [ ] Run Floyd-Warshall for all-pairs shortest path
- [ ] Find bridges and articulation points in undirected graph

## Common Mistakes at Level 6

| Mistake | Correct Approach |
|---------|-----------------|
| Lazy segment tree — not pushing down before recursing | Always `push_down(node)` before accessing children |
| DSU rollback — using path compression | Use union by rank only (path compression ruins rollback) |
| Dinic's level graph — re-running BFS every time | Only re-run BFS when augmenting path returns 0 |
| Aho-Corasick — forgetting to propagate match flags via failure links | During build, merge parent's matches into child |
| 2-SAT — checking wrong SCC order | Variable `x` is true iff `scc[x] > scc[¬x]` (reverse topo order) |
| Segment tree build — 1-indexed vs 0-indexed confusion | Choose one convention and stick to it throughout |

## Interview / Competitive Focus (Level 6 Topics)

| Problem | Algorithm | Complexity |
|---------|-----------|------------|
| Range sum with point updates | Segment Tree | O(log n) |
| Multi-pattern string search | Aho-Corasick | O(n + m + z) |
| Maximum flow in network | Dinic's | O(V²E) |
| Bipartite matching | Hopcroft-Karp | O(E√V) |
| SCC in directed graph | Tarjan's | O(V+E) |
| 2-SAT | Implication graph + SCC | O(V+E) |
| LCA with O(1) queries | Euler tour + RMQ | O(n log n) build |
