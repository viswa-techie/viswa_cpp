# Level 4 — Advanced: Trees, BST & Graph Fundamentals

> **Directory:** `Level_4_5_Advanced/`  
> **Categories:** `C40_Trees_BST` · `C41_Graphs_Fundamentals`  
> **Total Files:** 140 + 125 = **265 files**  
> **Prerequisite:** Level 3 (STL, Linked Lists, Hashing)  
> **Leads to:** Level 5 (Dynamic Programming, Heaps/Sorting)

---

## Overview

Level 4 introduces hierarchical and network data structures — the two most common categories in technical interviews. Trees model hierarchical relationships (file systems, expression trees, org charts). Graphs model arbitrary networks (social graphs, maps, dependency graphs). Mastering BFS/DFS on both unlocks a huge swath of hard problems.

---

## C40 — Trees & BST (140 files)

### What is Covered

| Range | Topics |
|-------|--------|
| 001–010 | Binary tree node structure, insertion, deletion, search; inorder / preorder / postorder traversals (recursive) |
| 011–020 | Level-order traversal (BFS), iterative inorder (stack-based), Morris traversal (O(1) space) |
| 021–030 | Tree height, diameter, mirror/flip, symmetric check, same tree check, subtree check |
| 031–040 | BST: insertion, deletion (3 cases), search, floor/ceiling, rank/select, BST validation |
| 041–050 | BST to sorted array, sorted array to balanced BST, BST to doubly linked list in-place |
| 051–060 | LCA (Lowest Common Ancestor): naive, BST-optimised, Euler tour + RMQ, Tarjan offline |
| 061–070 | Path sum problems: root-to-leaf, any path, max path sum (DP on tree), count paths with sum K |
| 071–080 | Serialise/deserialise binary tree (BFS string, preorder string); tree reconstruction from inorder+preorder/postorder |
| 081–090 | AVL tree: rotation (LL/RR/LR/RL), balance factor maintenance; Red-Black tree properties (conceptual) |
| 091–100 | Segment tree (basic), Binary Indexed Tree / Fenwick tree: point update + prefix sum query |
| 101–110 | Trie (prefix tree): insert/search/startsWith, wildcard search, word dictionary |
| 111–120 | N-ary tree traversal, expression tree evaluation, B-tree concepts |
| 121–130 | Heavy-Light Decomposition (intro), centroid decomposition (intro); tree DP: subtree sums, rerooting |
| 131–140 | Advanced BST problems: recover BST (swap two nodes), kth smallest in BST, unique BSTs (Catalan), max sum BST in binary tree, informing all employees, deepest leaves sum, good nodes |

### Key Concepts Learned
- Inorder of BST = sorted order — the defining property
- Tree recursion: compute answer from left result + right result + root
- Morris traversal threads tree nodes using null right pointers — O(1) space traversal
- AVL maintains height balance via rotations — guarantees O(log n) operations
- Fenwick tree: prefix sum in O(log n) time and O(log n) update; bit trick `i & (-i)` finds lowest set bit
- LCA is the foundation for many tree path problems

### Patterns Introduced
- **Post-order DP on tree** — compute from leaves up
- **Rerooting technique** — solve root-dependent DP for all nodes in O(n)
- **Euler tour** — flatten tree to array for LCA/range queries
- **Trie** — prefix-based string indexing

### Cross-Links
- BFS level-order (C40) ↔ BFS in graphs (C41)
- Segment tree (C40) ↔ Full segment tree chapter (Level 6, C60)
- Trie (C40) ↔ Advanced Trie in C60

---

## C41 — Graphs: Fundamentals (125 files)

### What is Covered

| Range | Topics |
|-------|--------|
| 001–010 | Graph representations: adjacency matrix, adjacency list, edge list, implicit graph; weighted vs unweighted; directed vs undirected |
| 011–020 | DFS (recursive + iterative), BFS; connected components, transitive closure |
| 021–030 | Cycle detection: undirected (DFS colours), directed (DFS with recursion stack / topological) |
| 031–040 | Topological sort: Kahn's algorithm (BFS), DFS-based; course schedule problems |
| 041–050 | Shortest path: Dijkstra (binary heap), Bellman-Ford, SPFA |
| 051–060 | Minimum spanning tree: Prim's algorithm, Kruskal's algorithm + DSU |
| 061–070 | Disjoint Set Union (DSU / Union-Find): naive, union by rank, path compression; cycle detection |
| 071–080 | Bipartite check (2-colouring), bipartite matching (König's theorem concept) |
| 081–090 | Flood fill, number of islands, max area of island, Pacific Atlantic water flow |
| 091–100 | Bridges and articulation points (Tarjan's algorithm), strongly connected components (Tarjan's / Kosaraju's) |
| 101–110 | Multi-source BFS, 0-1 BFS (deque-based), bidirectional BFS |
| 111–120 | Grid graphs: wall-breaking shortest path, knight's minimum moves, sliding puzzle (BFS on state) |
| 121–125 | Accounts merge (graph component), similar string groups, layered BFS, making a large island, shortest bridge |

### Key Concepts Learned
- DFS explores depth-first (uses stack/recursion); BFS explores breadth-first (uses queue) = shortest path
- Topological sort only exists for Directed Acyclic Graphs (DAGs)
- Dijkstra requires non-negative edge weights; Bellman-Ford handles negatives
- DSU path compression + union by rank → near-O(1) amortised per operation (inverse Ackermann)
- Kruskal = sort edges + DSU; Prim = greedy from one node with priority queue
- Tarjan SCC: single DFS with lowlink values

### Patterns Introduced
- **BFS for shortest path** (unweighted graph)
- **Dijkstra with priority queue** (weighted, non-negative)
- **Kahn's Topological Sort** — in-degree array + queue
- **DSU (Union-Find)** — connectivity queries
- **Multi-source BFS** — multiple starting points simultaneously
- **0-1 BFS** — deque, edge weight 0 or 1

---

## Level 4 — Revision Checklist

### Trees & BST
- [ ] Write all 4 traversals iteratively (no recursion)
- [ ] Implement AVL rotation (LL case) from memory
- [ ] Solve LCA for BST and for general binary tree
- [ ] Implement Fenwick tree for range sum with point updates
- [ ] Implement Trie insert/search/startsWith
- [ ] Reconstruct binary tree from preorder + inorder arrays

### Graphs
- [ ] Detect cycle in directed graph with DFS coloring (white/gray/black)
- [ ] Implement Dijkstra from memory (heap-based)
- [ ] Implement Kruskal's MST with DSU
- [ ] Run topological sort (both Kahn's and DFS-based)
- [ ] Find bridges in undirected graph (Tarjan's)
- [ ] Implement SCC with Kosaraju's (two DFS passes)

## Common Mistakes at Level 4

| Mistake | Correct Approach |
|---------|-----------------|
| Forgetting visited array in graph DFS | Always mark visited before processing |
| Using Dijkstra with negative edges | Use Bellman-Ford or Johnson's algorithm |
| BST deletion — forgetting inorder successor | Replace with inorder successor/predecessor |
| Checking `if (node)` after using `node->val` | Check null before any member access |
| Topological sort on cyclic graph | Verify cycle detection before attempting |
| DFS without stack overflow guard | Iterative DFS or increase stack size |

## Interview Focus (Level 4 Topics)

| Problem | Algorithm | Complexity |
|---------|-----------|------------|
| Number of Islands | DFS/BFS | O(m·n) |
| Course Schedule (Topological) | Kahn's BFS | O(V+E) |
| Dijkstra Shortest Path | Heap + Greedy | O((V+E) log V) |
| LCA Binary Tree | DFS post-order | O(n) |
| Kruskal MST | Sort + DSU | O(E log E) |
| Serialize/Deserialize Tree | BFS/Preorder | O(n) |
| Word Ladder | BFS | O(n·L²) |
