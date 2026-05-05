# Level 5 — Advanced: Dynamic Programming & Heaps/Sorting Mastery

> **Directory:** `Level_4_5_Advanced/`  
> **Categories:** `C50_Dynamic_Programming` · `C51_Heaps_PQ_Sorting`  
> **Total Files:** 150 + 110 = **260 files**  
> **Prerequisite:** Level 4 (Trees, Graphs)  
> **Leads to:** Level 6 (Advanced Trees, Advanced Graphs)

---

## Overview

Level 5 is where algorithmic thinking crystallises. Dynamic Programming is the single most-tested category in FAANG interviews — it requires pattern recognition across dozens of problem archetypes. Heaps and advanced sorting complete your toolkit for O(n log n) solutions and streaming algorithms.

---

## C50 — Dynamic Programming (150 files)

### What is Covered

| Range | Topics |
|-------|--------|
| 001–010 | DP philosophy (overlapping subproblems + optimal substructure); Fibonacci (top-down memo vs bottom-up tabulation); climbing stairs; min cost climbing stairs |
| 011–020 | House robber I/II (circular), House robber III (tree DP); jump game I/II; decode ways |
| 021–030 | Coin change I (min coins), coin change II (number of ways); perfect squares; word break I/II |
| 031–040 | Longest Increasing Subsequence (O(n²) DP, O(n log n) patience sort); LCS; edit distance (Levenshtein) |
| 041–050 | 0-1 Knapsack (2D, space-optimised 1D); unbounded knapsack; fractional knapsack (greedy) |
| 051–060 | Partition equal subset sum; target sum; last stone weight II; boolean partitioning |
| 061–070 | 2D DP: unique paths I/II (obstacles); minimum path sum; triangle; max square of 1s in grid |
| 071–080 | Interval DP: burst balloons, matrix chain multiplication, palindrome partitioning, remove boxes |
| 081–090 | String DP: longest palindromic subsequence/substring; distinct subsequences; interleaving strings; regex matching; wildcard matching |
| 091–100 | DP on trees: diameter, max independent set, subtree count, tree knapsack |
| 101–110 | State machine DP: stock problems (buy/sell once, unlimited, with cooldown, with k transactions) |
| 111–120 | Bitmask DP: travelling salesman (TSP), assignment problem, covering all nodes; subset DP |
| 121–130 | DP with binary search: LIS in O(n log n), Russian doll envelopes, minimum operations |
| 131–140 | Game theory DP: stone games I/II/III, predict winner, Nim game, flip game II |
| 141–150 | Count DP: count vowels permutation, number of ways to decode, minimum operations to make increasing; space optimisation techniques |

### Key Concepts Learned
- **Top-down (memoisation)**: natural recursion + cache; easier to write, harder to optimise space
- **Bottom-up (tabulation)**: fill table from smallest subproblems; easier to space-optimise
- State definition is 90% of DP: identify what changes between subproblems
- 0-1 Knapsack: iterate weights in **reverse** when using 1D array
- Interval DP: `dp[i][j]` depends on smaller intervals; loop by length
- Bitmask DP: `dp[mask][i]` — visited set encoded as bitmask

### DP Archetypes (Must Memorise)

| Archetype | State | Transition |
|-----------|-------|-----------|
| Linear DP | `dp[i]` | from `dp[i-1]`, `dp[i-k]` |
| 2D Grid DP | `dp[i][j]` | from up/left neighbours |
| Knapsack | `dp[i][w]` | include/exclude item i |
| Interval DP | `dp[l][r]` | split at k: `dp[l][k] + dp[k+1][r]` |
| Subsequence | `dp[i][j]` on two strings | match/mismatch/skip |
| Bitmask DP | `dp[mask][last]` | extend mask by one element |
| Tree DP | `dp[node][state]` | combine children results |
| State Machine | `dp[i][state]` | transition between states |

### Cross-Links
- Memoisation (C50) ↔ Recursion/memoisation intro (Level 1, C11)
- Tree DP (C50) ↔ Tree problems (Level 4, C40)
- Bitmask DP (C50) ↔ Bit manipulation (Level 8, C80)
- LCS/edit distance (C50) ↔ String algorithms (Level 8, C80)

---

## C51 — Heaps, Priority Queues & Sorting (110 files)

### What is Covered

| Range | Topics |
|-------|--------|
| 001–010 | Binary heap property, max-heap vs min-heap, heap array representation; heapify sift-down; build heap O(n) |
| 011–020 | Heap insert (sift-up), extract max/min, delete arbitrary element; heap sort |
| 021–030 | `std::priority_queue` (max-heap), min-heap with `greater<>`, custom comparator, `make_heap` / `push_heap` / `pop_heap` |
| 031–040 | K-way merge of sorted arrays/lists; merge K sorted linked lists; top-K frequent words |
| 041–050 | Median of stream (two heaps), sliding window median, K closest points to origin |
| 051–060 | Task scheduler (CPU burst), find K pairs with smallest sums, ugly numbers II, super ugly numbers |
| 061–070 | Sorting algorithms deep-dive: bubble, selection, insertion; shell sort; counting sort; radix sort; bucket sort |
| 071–080 | Merge sort (stable, O(n log n)), quick sort (Lomuto/Hoare partition, 3-way), intro-sort (hybrid) |
| 081–090 | `std::sort` (introsort), `std::stable_sort` (merge sort), `std::partial_sort` (heap select), `std::nth_element` (quickselect) |
| 091–100 | Custom sort comparators: `std::less<>`, `std::greater<>`, lambda comparators, comparator for pairs/tuples |
| 101–110 | Advanced sort problems: custom sort string, sort by frequency, sort array by parity, minimum difference in k scores; greedy sorting |

### Key Concepts Learned
- Building a heap is O(n) — not O(n log n); this is the key insight for heap sort
- `std::priority_queue` is a max-heap by default; for min-heap use `priority_queue<int, vector<int>, greater<int>>`
- Two-heap pattern: max-heap for lower half, min-heap for upper half → median in O(1)
- Counting sort: O(n + k) but requires bounded integer keys
- Radix sort: O(d(n + b)) for d digits, base b — linear for fixed-width integers
- `std::nth_element` = O(n) average (quickselect) — finds Kth element without full sort

### Sorting Complexity Reference

| Algorithm | Best | Average | Worst | Space | Stable? |
|-----------|------|---------|-------|-------|---------|
| Bubble | O(n) | O(n²) | O(n²) | O(1) | Yes |
| Insertion | O(n) | O(n²) | O(n²) | O(1) | Yes |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes |
| Quick Sort | O(n log n) | O(n log n) | O(n²) | O(log n) | No |
| Heap Sort | O(n log n) | O(n log n) | O(n log n) | O(1) | No |
| Counting | O(n+k) | O(n+k) | O(n+k) | O(k) | Yes |
| Radix | O(d·n) | O(d·n) | O(d·n) | O(n+b) | Yes |
| `std::sort` | — | O(n log n) | O(n log n) | O(log n) | No |

---

## Level 5 — Revision Checklist

### Dynamic Programming
- [ ] Implement coin change (min coins) both top-down and bottom-up
- [ ] Solve 0-1 Knapsack with 1D space-optimised DP
- [ ] Implement LIS in O(n log n) using binary search + patience sorting
- [ ] Solve matrix chain multiplication (interval DP)
- [ ] Solve TSP with bitmask DP for 4 cities from memory
- [ ] Solve stock with cooldown (state machine DP)
- [ ] Identify which DP archetype applies to a new problem

### Heaps & Sorting
- [ ] Implement `heapify` (sift-down) from memory
- [ ] Build heap in O(n) (bottom-up heapification)
- [ ] Solve median of stream with two heaps
- [ ] Implement merge sort (divide + merge step)
- [ ] Implement quicksort with Lomuto partition
- [ ] Use `std::nth_element` for O(n) Kth element

## Common Mistakes at Level 5

| Mistake | Correct Approach |
|---------|-----------------|
| 1D knapsack iterating forward | Iterate weights in **reverse** for 0-1 knapsack |
| Returning memoised value before base case | Always check base case first in recursion |
| Using max-heap when min-heap needed | `priority_queue<int, vector<int>, greater<int>>` |
| Interval DP inner loop wrong | Loop by interval length, not by left index |
| Quick sort choosing first element as pivot | Random pivot or median-of-three to avoid O(n²) |
| Heap sort is not stable | Use merge sort when stability is required |

## Interview Focus (Level 5 Topics)

| Problem | DP Type | Complexity |
|---------|---------|------------|
| Coin Change | Linear knapsack | O(n·amount) |
| Edit Distance | 2-string subsequence | O(m·n) |
| Burst Balloons | Interval DP | O(n³) |
| Stock with K Transactions | State machine | O(n·k) |
| TSP (4 cities) | Bitmask DP | O(2^n · n²) |
| LIS | Binary search | O(n log n) |
| Median of Stream | Two heaps | O(log n) insert |
| Kth Largest | Min-heap size K | O(n log k) |
