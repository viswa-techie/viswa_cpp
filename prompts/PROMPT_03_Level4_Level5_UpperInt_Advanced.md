# PROMPT 03 — Level 4 & Level 5: Upper Intermediate + Advanced
## C++ Problem Solving — Book-Alike Deep Learning Guide

---

## HOW TO USE THIS PROMPT

Paste the generation prompt below into an AI with `{{PROBLEM_NAME}}` filled in. The AI generates a complete book chapter covering this advanced topic in depth.

---

## MASTER GENERATION PROMPT

```
===
You are an expert C++ educator writing a BOOK CHAPTER for a self-learner.
The learner is at Level 4–5 (Upper Intermediate to Advanced).
They are comfortable with OOP, STL, pointers, and basic data structures.
Now they are mastering Trees/BST, Graphs, Dynamic Programming, and Heaps/Sorting.

The topic/problem is: {{PROBLEM_NAME}}

Generate a complete, standalone learning chapter with the following exact structure:

---

# Chapter: {{PROBLEM_NAME}}

## 1. Problem Statement
- Exact problem statement with full constraints.
- 3 examples: simple / tricky / maximum-constraint case.
- LeetCode / GFG / Codeforces problem number if applicable.
- Follow-up variants asked in interviews.

## 2. Category & Difficulty
- Problem category: [Tree | Graph | DP | Sorting | etc.]
- Sub-category: [BST | DFS/BFS | 1D DP | Interval DP | etc.]
- Difficulty: Easy / Medium / Hard
- Interview frequency: [Google | Amazon | Meta | etc.]
- Estimated solve time for a prepared candidate: X minutes

## 3. Prerequisites
- Data structures needed (which STL or custom)
- Algorithms needed (DFS, BFS, DP recurrence, divide & conquer)
- Mathematical background (if needed)
- Which simpler problems to solve first

## 4. Core Algorithmic Concept
Teach the core concept from first principles:
- Why does this algorithm/approach work? (formal argument, not just claim)
- What invariant does it maintain?
- What is the intuition — describe WITHOUT using technical jargon first.
- Visual/ASCII diagram of the algorithm in progress.
- Historical context (who invented it? why?)

## 5. Recurrence / State Definition (for DP problems)
- Define the DP state clearly: `dp[i][j]` means...
- Base cases
- Recurrence relation (mathematical notation)
- Direction of computation (bottom-up vs top-down)
- Dimension analysis (why 1D/2D/3D?)

## 6. Solution Approaches

### Approach 1: Brute Force
- Strategy + Time/Space
- Full C++17 code with comments
- What makes this TLE or MLE?

### Approach 2: Recursive with Memoization (Top-Down)
- Strategy + Time/Space
- Full C++17 code with comments
- Stack depth analysis

### Approach 3: Bottom-Up DP / Iterative
- Strategy + Time/Space
- Full C++17 code with comments
- Space optimization if possible

### Approach 4: Optimal / Mathematical
- Is there a closed-form or greedy insight?
- Full C++17 code with comments
- Time: O(?)  Space: O(?)
- When to use this over Approach 3?

## 7. Trace Through Example
- Choose example 2 (tricky case).
- For DP: show the filled DP table step by step.
- For Trees: show recursive call tree or stack states.
- For Graphs: show the BFS/DFS frontier expansion.
- Table format with state snapshots.

## 8. Complexity Deep Dive
- Formal proof or sketch of time complexity.
- Space complexity with recursion stack counted.
- Are there hidden constant factors that matter in practice?
- Amortized analysis if applicable (e.g., splay tree, union-find).
- Comparison table: Approach 1 vs 2 vs 3 vs 4.

## 9. Edge Cases & Gotchas
7+ specific edge cases for THIS problem:
- Empty input / single node / single element
- All same values
- All increasing / all decreasing
- Integer overflow
- Graph: disconnected, self-loops, negative weights
- Tree: skewed tree, complete tree, null children
- DP: when memoization leads to TLE if done naively

## 10. Optimization Techniques
- Space optimization: how to reduce from O(n) → O(1)?
- Time optimization: can we use monotonic queue, binary search, segment tree?
- Early termination conditions.
- Pruning in backtracking.
- SIMD or bit-parallel tricks (if applicable).

## 11. Code Quality & Production Considerations
- What would fail code review? (naming, error handling, magic numbers)
- How to write unit tests for this problem?
- Can this be parallelized?
- Embedded/RTOS constraint: what if no heap allocation allowed?

## 12. Pattern Recognition
- Name of the algorithmic pattern.
- Decision tree: "If I see ________, I should try ________."
- 6 other problems using the EXACT same pattern.
- How to distinguish this pattern from a similar-looking one.

## 13. Practice Variants
- Easy variant: what is relaxed?
- Medium variant: what constraint tightens it?
- Hard variant: what combination of techniques is needed?
- Competition variant: under strict time limits.

## 14. Interview Playbook
- First 2 minutes: what to say and ask.
- How to go from brute force to optimal in the interview.
- What if stuck: systematic hints to give yourself.
- Example strong verbal walkthrough (write it out).

## 15. Quick Reference Card
- One-liner description
- Key recurrence or algorithm in 3 lines
- Complexity
- 5 things NOT to forget

---
All code: C++17, compilable, with comments. Use `g++ -std=c++17 -O2 -Wall`.
===
```

---

## BATCH PROMPT (for whole category)

```
===
You are creating a COMPLETE STUDY VOLUME for C++ Level 4–5 topics.

Category: {{CATEGORY_NAME}}  
Level: {{LEVEL}} — {{LEVEL_TITLE}}

For each problem in the list, generate a focused chapter with:
1. Problem statement + 2 I/O examples
2. Core algorithm/pattern name
3. DP recurrence or algorithm invariant (formal)
4. Brute force (code + complexity)
5. Optimal solution (code + complexity)
6. DP table trace or call tree trace (5–8 steps)
7. 3 edge cases that break naive solutions
8. Space optimization technique (if applicable)
9. Pattern tag + 5 similar problems
10. Interview frequency rating (Common / Occasional / Rare)

Problems:
{{PASTE_PROBLEM_LIST}}

C++17 code throughout. H2 per problem, consistent sub-headers.
===
```

---

## PROBLEM BANK — LEVEL 4 & LEVEL 5

### LEVEL 4 — Upper Intermediate

#### Category C40: Trees & Binary Search Trees (140 problems)

**Tree Basics & Traversals (1–30)**
1. Binary tree node structure
2. Tree insertion
3. Tree deletion
4. Tree search
5. Inorder traversal (recursive)
6. Preorder traversal
7. Postorder traversal
8. Level order traversal
9. Zigzag level order
10. Vertical order traversal
11. Boundary traversal
12. Diagonal traversal
13. Morris inorder traversal
14. Morris preorder traversal
15. Iterative inorder
16. Iterative preorder (two stacks)
17. Iterative postorder
18. Iterative level order
19. Height of tree
20. Depth of node
21. Count nodes
22. Count leaf nodes
23. Count internal nodes
24. Sum of all nodes
25. Max node value / Min node value
26. Diameter of tree
27. Width of tree (max level width)
28. Check balanced tree
29. Check complete tree
30. Check perfect tree

**Tree Property Problems (31–70)**
31. Check full binary tree
32. Check identical trees
33. Check mirror/symmetric tree
34. Subtree check
35. Path sum (root to leaf)
36. All root-to-leaf paths
37. Path sum II (all paths with target)
38. Path sum III (any path, not just root-to-leaf)
39. Max path sum
40. Lowest common ancestor (BST)
41. LCA (binary tree)
42. LCA with parent pointer
43. Distance between nodes
44. Nodes at distance K
45. Burning tree problem
46. Time to burn tree from node
47. Count nodes in range [L,R]
48. Floor in BST
49. Ceil in BST
50. Predecessor in BST
51. Successor in BST
52. Kth smallest in BST
53. Kth largest in BST
54. Rank of element in BST
55. BST from sorted array
56. BST from sorted linked list
57. BST from preorder
58. BST from postorder
59. Validate BST
60. Convert BST to sorted DLL
61. Convert BST to greater sum tree
62. Merge two BSTs
63. Two sum in BST
64. Find pair with given sum in BST
65. Closest value in BST
66. Largest BST subtree
67. BST to min heap
68. Serialize / deserialize binary tree
69. Serialize BST (compact)
70. Construct from inorder + preorder

**Tree Construction & Advanced (71–110)**
71. Construct from inorder + postorder
72. Construct from level order
73. Recover BST (two swapped nodes)
74. Trim BST to range
75. Prune tree
76. Flatten tree to linked list
77. Right side view
78. Left side view
79. Top view
80. Bottom view
81. Sum of nodes at level K
82. Count nodes at level K
83. Nodes at odd levels vs even
84. Parent array representation
85. Children sum property
86. Modify tree to satisfy children sum
87. BST iterator (inorder)
88. BST iterator (reverse inorder)
89. Two pointer on BST iterators
90. Maximum width using indices
91. Check BST with range method
92. Find duplicate subtrees
93. Unique BSTs count (Catalan number)
94. Generate all BSTs (n nodes)
95. All possible full binary trees
96. All structurally unique trees
97. AVL tree rotations
98. AVL insert / delete
99. Red-black tree properties
100. RB insert concept

**Special Trees (101–140)**
101. Treap (BST + heap priority)
102. Splay tree concept
103. Scapegoat tree
104. Weight-balanced tree
105. B-tree structure
106. B+ tree structure
107. Persistent BST concept
108. Order statistic tree
109. Augmented BST (rank/select)
110. Interval tree
111. Segment tree basics (intro)
112. Fenwick tree intro
113. Euler tour technique
114. Heavy-light decomposition intro
115. Centroid decomposition intro
116. Ternary tree
117. K-ary tree
118. Expression tree
119. Huffman tree
120. Cartesian tree
121. Threaded binary tree
122. Right-threaded vs full-threaded
123. Inorder successor (threaded)
124. Level order using queue (review)
125. Spiral using two stacks
126. Reverse level order
127. Count nodes in complete tree (O(log²n))
128. Delete leaves with value
129. Max depth of N-ary tree
130. Serialize N-ary tree
131. Encode N-ary tree as binary
132. Diameter of N-ary tree
133. Sum root to leaf numbers
134. Maximum sum BST in binary tree
135. Find all the lonely nodes
136. Count good nodes in binary tree
137. Deepest leaves sum
138. Maximum product of splitted binary tree
139. Number of nodes in the sub-tree with the same label
140. Time needed to inform all employees

---

#### Category C41: Graphs — Fundamentals & Traversal (125 problems)

**Graph Representations (1–15)**
1. Adjacency matrix representation
2. Adjacency list representation
3. Edge list representation
4. Implicit graph
5. Weighted vs unweighted
6. Directed vs undirected
7. Simple graph vs multigraph
8. Dense vs sparse graphs
9. Degree sequence
10. Handshaking lemma
11. Trees are graphs (n-1 edges)
12. Graph from grid
13. Compressed coordinate graph
14. Virtual node trick
15. Complement graph

**BFS / DFS (16–45)**
16. BFS iterative
17. BFS with levels
18. DFS iterative (stack)
19. DFS recursive
20. Connected components (undirected)
21. Connected components (directed = SCC)
22. Number of islands (DFS)
23. Number of islands (BFS)
24. Number of islands (Union-Find)
25. Max area of island
26. Flood fill
27. Count enclaves
28. Number of closed islands
29. Surrounded regions
30. Pacific Atlantic water flow
31. Making a large island
32. Check bipartite (BFS)
33. Check bipartite (DFS)
34. Possible bipartition
35. Graph coloring (2-coloring)
36. Cycle detection undirected (DFS)
37. Cycle detection undirected (BFS)
38. Cycle detection directed (DFS)
39. Cycle detection directed (coloring)
40. Topological sort (DFS)
41. Topological sort (Kahn's BFS)
42. Course schedule I
43. Course schedule II
44. Parallel courses minimum semesters
45. Build order (compile deps)

**Shortest Paths (46–80)**
46. Alien dictionary (topo sort)
47. Sequence reconstruction
48. Redundant connection (undirected)
49. Redundant connection II (directed)
50. Detect cycle with Union-Find
51. Find eventual safe states
52. Keys and rooms
53. Path existence query
54. All paths from source to target
55. Shortest path (unweighted BFS)
56. Shortest path (Dijkstra)
57. Shortest path (Bellman-Ford)
58. Negative cycle detection
59. Shortest path in DAG
60. Floyd-Warshall APSP
61. Reconstruct path (parent array)
62. Bidirectional BFS
63. A* search algorithm
64. Network delay time
65. Cheapest flights K stops
66. Path with max probability
67. Path with minimum effort
68. Swim in rising water
69. Minimum cost to connect all points
70. MST: Kruskal's algorithm
71. MST: Prim's algorithm
72. Second minimum spanning tree
73. Maximum spanning tree
74. Critical connections (bridges)
75. Bridge finding (Tarjan's)
76. Articulation points
77. Biconnected components
78. Strongly connected components (Kosaraju)
79. SCC (Tarjan's)
80. Condensation DAG

**Advanced Graph Problems (81–125)**
81. 2-SAT problem
82. Euler path / Euler circuit
83. Hierholzer's algorithm
84. Hamiltonian path (brute)
85. Traveling salesman (bitmask DP)
86. Graph isomorphism concept
87. Sparse table on tree (LCA)
88. Binary lifting (LCA)
89. Kth ancestor query
90. Distance between nodes (LCA)
91. Level ancestor query
92. Grid as graph problems
93. Word ladder BFS
94. Minimum knight moves
95. Snakes and ladders BFS
96. Sliding puzzle BFS
97. Open the lock BFS
98. Minimum genetic mutation
99. Jump game BFS
100. Bus routes BFS
101. Minimum obstacle removal
102. Multi-source BFS (matrix)
103. 0-1 BFS (0/1 weight edges)
104. Dial's algorithm
105. Count paths in DAG
106. Longest path in DAG
107. Maximum bipartite matching (intro)
108. Hall's theorem
109. Graph with constraints (scheduling)
110. Number of ways to reach in graph
111. Reachability matrix
112. Transitive closure
113. Strongly connected tournament
114. Minimum edge reversal to make path
115. Minimum edges to make graph connected
116. Graph valid tree
117. Clone graph
118. Reconstruct itinerary (Euler path)
119. Find the celebrity
120. Accounts merge (graph component)
121. Similar string groups
122. Minimum cost to reach destination (layered BFS)
123. Making A Large Island
124. Shortest Bridge (multi-source BFS)
125. Maximize the Number of Target Nodes After Connecting Trees

---

### LEVEL 5 — Advanced

#### Category C50: Dynamic Programming (150 problems)

**DP Foundations (1–20)**
1. DP philosophy: overlapping subproblems + optimal substructure
2. Fibonacci (memoization)
3. Fibonacci (tabulation)
4. Climbing stairs
5. Min cost climbing stairs
6. House robber I
7. House robber II (circular)
8. House robber III (tree)
9. Delete and earn
10. Jump game (DP)
11. Jump game II (min jumps DP)
12. Decode ways
13. Decode ways II (with `*`)
14. Coin change (min coins)
15. Coin change II (count ways)
16. Integer break
17. Perfect squares
18. Ugly number II
19. Super ugly number
20. Nth Tribonacci

**Knapsack Family (21–40)**
21. 0-1 Knapsack
22. Unbounded knapsack
23. Fractional knapsack (greedy comparison)
24. Rod cutting
25. Partition equal subset sum
26. Count subsets with sum k
27. Target sum (±1 assign)
28. Last stone weight II
29. Minimum subset sum difference
30. Ones and zeros (2D knapsack)
31. Profitable schemes
32. Number of dice rolls with target sum
33. Combination sum IV (order matters)
34. Maximum profit in job scheduling
35. Weighted job scheduling
36. Two city scheduling greedy vs DP
37. Minimum cost to hire K workers
38. Reducing dishes (smarter knapsack)
39. Shopping offers
40. Tallest billboard

**String DP (41–65)**
41. Longest Common Subsequence (LCS)
42. LCS reconstruction
43. Shortest Common Supersequence
44. Longest Common Substring
45. Edit distance (Levenshtein)
46. Delete operations for same strings
47. Minimum ASCII delete sum
48. Longest palindromic subsequence
49. Longest palindromic substring
50. Count palindromic substrings
51. Palindrome partitioning (min cuts)
52. Palindrome partitioning II
53. Wildcard matching (`* ?`)
54. Regex matching (`. *`)
55. Interleaving strings
56. Distinct subsequences
57. Longest increasing subsequence O(n log n)
58. LIS count
59. LIS reconstruction
60. Longest decreasing subsequence
61. Longest bitonic subsequence
62. Number of LIS
63. Longest divisible subset
64. Russian doll envelopes
65. Maximum sum increasing subsequence

**Grid DP (66–80)**
66. Unique paths I
67. Unique paths II (obstacles)
68. Minimum path sum grid
69. Maximum gold in grid
70. Cherry pickup I
71. Cherry pickup II (two robots)
72. Triangle min path sum
73. Dungeon game (reverse DP)
74. Count paths with sum (grid)
75. Minimum falling path sum
76. Minimum falling path sum II
77. Out of boundary paths
78. Knight probability in chessboard
79. Number of paths in k moves
80. Minimum cost path with at most k turns

**Interval DP (81–95)**
81. Matrix chain multiplication
82. Burst balloons
83. Strange printer
84. Remove boxes
85. Minimum cost to cut stick
86. Minimum cost to merge stones
87. Optimal binary search tree
88. Palindrome partitioning I (all parts)
89. Boolean parenthesization
90. Minimum cost to repair edges
91. Zuma game
92. Minimum cost to make string valid
93. Minimum score triangulation polygon
94. Minimum difficulty of a job schedule
95. Strange printer II

**Tree DP (96–105)**
96. House robber III (tree DP)
97. Diameter of binary tree (DP)
98. Max path sum in tree
99. Longest ZigZag path in tree
100. Binary tree cameras
101. Sum of distances in tree
102. Maximum product of splitted tree
103. Count nodes equal to avg of subtree
104. Distribute coins in tree
105. Minimum time to visit subtree nodes

**Bitmask DP (106–115)**
106. TSP bitmask DP
107. Minimum XOR sum assignment
108. Shortest path visiting all nodes
109. Stickers to spell word
110. Can I win (bitmask game)
111. Count sets of friends
112. Maximize score after N operations
113. Minimum cost to connect groups
114. Number of ways to wear hats
115. Partition to K equal sum subsets

**Stock & State Machine DP (116–125)**
116. Stock I (one transaction)
117. Stock II (unlimited transactions)
118. Stock III (two transactions)
119. Stock IV (k transactions)
120. Stock with cooldown
121. Stock with transaction fee
122. Best team with no conflicts
123. Max profit from jobs (DP + binary search)
124. Max profit from scheduling (DP + sort)
125. Paint fence (k colors)

**Digit DP & Miscellaneous (126–150)**
126. Count numbers with at most k digits
127. Count numbers with digit sum S
128. Count numbers without digit d
129. Count numbers with all unique digits
130. Numbers with repeated digits
131. Count special numbers
132. Digit DP template
133. Non-decreasing digits
134. Longest subarray with constraints (DP+deque)
135. Kadane as DP
136. DP with binary search (patience sort)
137. DP on DAG (shortest/longest path)
138. DP with SOS (sum over subsets)
139. Knight probability
140. New 21 game
141. Dice roll simulation
142. Stone game I
143. Stone game II
144. Stone game III
145. Predict winner
146. Nim game
147. Flip game II
148. Count vowels permutation
149. Number of ways to decode message
150. Minimum operations to make array increasing

---

#### Category C51: Heaps, Priority Queues & Advanced Sorting (110 problems)

**Heap Fundamentals (1–20)**
1. Binary heap property
2. Max-heap vs min-heap
3. Heap array representation
4. Heapify (sift-down)
5. Build heap O(n)
6. Heap insert (sift-up)
7. Heap extract-max/min
8. Heap delete arbitrary element
9. Heap increase/decrease key
10. Heap sort
11. K largest elements
12. K smallest elements
13. Kth largest in stream
14. Kth smallest in stream
15. Top K frequent elements (heap)
16. Top K frequent words
17. Sort nearly sorted (k-sorted array)
18. Merge K sorted arrays
19. Merge K sorted linked lists
20. Smallest range covering K lists

**Heap Problems (21–55)**
21. Find median from data stream
22. Sliding window median
23. Running median
24. Median of stream (two heaps)
25. K closest points to origin
26. K closest points in stream
27. Minimum cost to connect ropes
28. Task scheduler (heap)
29. Reorganize string (heap)
30. Distant barcodes
31. Find the most competitive subsequence
32. Remove stones to minimize total
33. Minimum number of refueling stops
34. IPO (max capital)
35. Maximum number of events (greedy + heap)
36. Meeting rooms III
37. Car pooling
38. Single-threaded CPU
39. Process tasks using servers
40. Minimum time to finish jobs
41. Reduce array size to half
42. Sort characters by frequency
43. Trapping rain water II (3D BFS + heap)
44. Swim in rising water
45. Cut off trees for golf event
46. Dijkstra with heap
47. Prim's with heap
48. Huffman coding tree build
49. d-ary heap
50. Fibonacci heap concept
51. Pairing heap
52. Leftist tree
53. Skew heap
54. Binomial heap
55. Mergeable heap operations

**Sorting Algorithms Deep Dive (56–110)**
56. Counting sort deep dive
57. Radix sort (LSD vs MSD)
58. Bucket sort with distribution
59. Flash sort
60. American flag sort (in-place radix)
61. Timsort internals
62. Introsort internals
63. Smoothsort
64. Tournament sort
65. External merge sort
66. Polyphase merge sort
67. Replacement selection sort
68. Sorting networks
69. Bitonic sort
70. Odd-even merge sort
71. Pancake sort
72. Gnome sort
73. Cycle sort
74. Strand sort
75. Library sort
76. Sample sort (parallel concept)
77. Inversion count (merge sort)
78. Count smaller after self
79. Count of range sum
80. Reverse pairs
81. Global inversions local inversions
82. Minimum number of swaps to sort
83. Sort transformed array
84. Wiggle sort II
85. Largest number (custom sort)
86. Maximum gap (radix/bucket)
87. H-index I & II
88. Relative ranks
89. Sort list (merge sort, O(n log n))
90. Patience sorting (connection to LIS)
91. External sort file (concept)
92. Tournament tree (k-way merge)
93. Cache-oblivious sorting
94. Parallel sort concepts
95. AKS sorting network
96. Sort using comparator (complex objects)
97. Stable vs unstable sort implications
98. Sort with custom equivalence relation
99. Minimum cost to make array non-decreasing
100. Number of operations to sort binary array
101. Minimum adjacent swaps to make valid
102. Sort integers by number of 1 bits
103. Custom sort string
104. Sorting by frequency then alphabetically
105. Sort array by parity II
106. Maximum product after cutting ropes
107. Minimum difference between highest and lowest of k scores
108. Average salary excluding minimum and maximum
109. Minimum operations to make sorted
110. Largest perimeter triangle (sort + greedy)

---

## SUPPLEMENTARY PROBLEMS (Level 4–5 additions)

### LeetCode Medium/Hard (Level 4–5 aligned)
- Binary Tree Level Order Traversal (#102)
- Binary Tree Zigzag Level Order (#103)
- Maximum Depth of Binary Tree (#104)
- Construct Binary Tree from Preorder+Inorder (#105)
- Binary Tree Maximum Path Sum (#124)
- Word Ladder (#127)
- Longest Consecutive Sequence (#128)
- Number of Islands (#200)
- House Robber (#198)
- Course Schedule (#207)
- Number of Islands II (#305)
- Coin Change (#322)
- Longest Increasing Subsequence (#300)
- Partition Equal Subset Sum (#416)
- Pacific Atlantic Water Flow (#417)
- Burst Balloons (#312)
- Edit Distance (#72)
- Wildcard Matching (#44)
- Regular Expression Matching (#10)
- Unique Paths (#62)
- Maximum Subarray (#53)
- Trapping Rain Water (#42)
- Median of Two Sorted Arrays (#4)
- Sliding Window Maximum (#239)
- Find Median from Data Stream (#295)

### Additional DP problems (GFG / Codeforces)
- Longest Common Subsequence variations
- Matrix Chain Multiplication
- 0-1 Knapsack all variants
- DP on trees (maximum independent set)
- DP with profile (broken profile DP)

---

## LEARNING ROADMAP — Level 4 → Level 5

```
Week 1–3:  C40 (1–70)     Tree traversals, BST operations, LCA
Week 4–5:  C40 (71–140)   AVL/RB/Segment tree intro, special trees
Week 6–7:  C41 (1–60)     Graph representations, BFS/DFS, shortest paths
Week 8–9:  C41 (61–125)   MST, SCC, topological sort, bridge/articulation
Week 10:   C50 (1–40)     DP foundations + knapsack family
Week 11:   C50 (41–80)    String DP (LCS, edit distance, LIS, palindrome)
Week 12:   C50 (81–115)   Grid DP, interval DP, tree DP, bitmask DP
Week 13:   C50 (116–150)  Stock DP, digit DP, game theory DP
Week 14:   C51 (1–55)     Heap fundamentals + heap-based problems
Week 15:   C51 (56–110)   Sorting algorithms deep dive + merge-sort problems
```

---

## RESOURCES

| Resource | Link | Best For |
|----------|------|----------|
| Introduction to Algorithms (CLRS) | Book | Formal proofs |
| Competitive Programmer's Handbook | https://cses.fi/book | Algorithms + problems |
| USACO Guide | https://usaco.guide | Structured learning paths |
| Aditya Verma DP Playlist | YouTube | DP from scratch |
| Striver's SDE Sheet | https://takeuforward.org | Interview-focused roadmap |
| LeetCode Patterns | https://seanprashad.com/leetcode-patterns | Pattern groupings |
| CP-algorithms.com | https://cp-algorithms.com | Deep algorithm explanations |
| AlgoMonster | https://algo.monster | Pattern-based interview prep |
| Codeforces Edu Section | https://codeforces.com/edu | Segment tree, DSU, flows |
| GitHub: labuladong/fucking-algorithm | Chinese DP/tree bible | DP mindset |
| GitHub: neetcode-io/neetcode | NeetCode 150/250 | Top interview problems |
| Visualgo | https://visualgo.net | Visual algorithm traces |
