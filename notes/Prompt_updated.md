Level 3 — Intermediate: STL, Linked Lists, Stacks/Queues & Hashing
Directory: Level_2_3_Intermediate/
Categories: C22_STL_Containers_Iterators · C30_Linked_Lists · C31_Stacks_Queues · C32_Hashing
Total Files: 130 + 120 + 115 + 110 = 475 files
Prerequisite: Level 2 (Pointers, OOP)
Leads to: Level 4 (Trees, Graphs)

Overview
Level 3 is the data-structures chapter that every software engineer is tested on. You master the full STL container library, then build fundamental linked/sequential structures manually (to understand pointer mechanics), and finally tackle hashing — the engine behind O(1) lookup. After Level 3 you can solve 90%+ of LeetCode Easy and ~50% of Medium problems.

C22 — STL Containers & Iterators (130 files)
What is Covered
Range	Topics
001–010	std::vector (all operations), std::deque, std::list, std::forward_list, std::array; std::string as container
011–020	std::stack, std::queue, std::priority_queue (max/min heap); adaptor pattern over underlying containers
021–030	std::set, std::multiset, std::map, std::multimap — red-black tree internals; lower_bound/upper_bound on ordered containers
031–040	std::unordered_set, std::unordered_map, std::unordered_multiset/map — hash table internals, load factor, rehash
041–050	std::bitset, std::valarray, std::span (C++20), std::mdspan (C++23); byte-level containers
051–060	Iterator categories: input, output, forward, bidirectional, random-access, contiguous; iterator invalidation rules
061–070	std::begin/end, std::advance, std::distance, std::next, std::prev; reverse iterators; stream iterators
071–080	<algorithm> core: std::sort, std::find, std::count, std::transform, std::copy, std::accumulate, std::reduce
081–090	<algorithm> advanced: std::partition, std::nth_element, std::stable_sort, std::merge, std::set_intersection, std::unique
091–100	C++17/20 algorithms: std::for_each with CTAD, parallel STL (std::execution::par), std::ranges intro
101–110	std::ranges: range adaptors, pipe `
111–120	std::views::join, std::views::zip (C++23), std::views::enumerate (C++23), std::views::chunk, std::generator
121–130	Heap problems with priority_queue: two-heap median, K closest elements, Kth largest, top-K frequent; C++26 std::inplace_vector; std::flat_map/std::flat_set (C++23)
Key Concepts Learned
std::vector is contiguous; std::list is pointer-linked — cache impact is enormous
Ordered containers (set/map) = O(log n) but sorted; unordered = O(1) amortised but no order
Iterator invalidation: push_back can invalidate all vector iterators; know the rules per container
std::ranges is lazy — no computation until iterated
std::nth_element is O(n) average for partial sorting (uses introselect)
Patterns Introduced
Two-heap pattern — maintain median of stream
Lazy range pipeline — nums | views::filter | views::transform
Iterator erasure idiom — v.erase(std::remove(...), v.end())
C30 — Linked Lists (120 files)
What is Covered
Range	Topics
001–010	Singly linked list (manual impl), doubly linked list, circular linked list, XOR linked list; insert at head/tail/position
011–020	Delete by value/position, search, length; reverse a singly linked list (iterative + recursive)
021–030	Floyd's cycle detection (tortoise & hare), cycle start detection, cycle removal
031–040	Merge two sorted lists, merge K sorted lists (priority queue), intersection point of two lists
041–050	Middle of linked list (fast/slow pointer), reverse in groups of K, palindrome linked list check
051–060	Flatten a multilevel doubly linked list, copy list with random pointer (deep copy with hash map)
061–070	LRU cache (doubly linked list + hash map), LFU cache, sliding window with list
071–080	Skip list implementation (probabilistic), skip list search/insert/delete
081–090	Sorted insert, merge sort on linked list, quick sort on linked list
091–100	Rotate list by K, remove Nth node from end (two pointers), add two numbers as lists
101–110	Reorder list (interleave), odd-even grouping, partition around value
111–120	Skip list O(1) random access, doubly linked list as deque, circular buffer with list, embedded systems list (no heap)
Key Concepts Learned
Linked list has O(1) insert/delete at known position; O(n) random access
Fast/slow pointer: after k iterations, fast has moved 2k nodes — finds midpoint in one pass
Floyd's cycle detection: meet inside cycle → distance from head = distance from meeting point to cycle start
LRU cache: O(1) get + O(1) put using unordered_map + std::list
Deep copy of a list with random pointers needs a mapping from old → new nodes
Patterns Introduced
Fast/Slow Pointer (Two Pointers on list)
Dummy head node — simplifies edge cases at head
Reverse in-place — three-pointer technique
Floyd's Cycle Detection
C31 — Stacks & Queues (115 files)
What is Covered
Range	Topics
001–010	Stack (array impl, linked list impl, std::stack, std::vector); Queue (circular array, linked list, std::queue, std::deque)
011–020	Monotonic stack: next greater element, next smaller element, stock span problem; daily temperatures
021–030	Balanced parentheses, evaluate reverse Polish notation (RPN), infix to postfix conversion, calculator
031–040	Min stack (O(1) getMin), max stack; queue using two stacks; stack using two queues
041–050	Largest rectangle in histogram (monotonic stack), maximal rectangle (extend histogram row by row)
051–060	BFS via queue: level-order traversal, shortest path in unweighted graph, 01-matrix, rotting oranges
061–070	Priority queue patterns: K-way merge, sliding window maximum, task scheduler
071–080	Deque applications: sliding window min/max (monotonic deque), palindrome check with deque
081–090	std::deque internals (block-based), memory layout comparison with vector
091–100	Circular queue / ring buffer implementation; producer-consumer with bounded queue (lock-based)
101–115	Monotonic queue problems: shortest subarray with sum ≥ K, jump game VI; priority-queue-based graph algorithms preview
Key Concepts Learned
Monotonic stack maintains sorted order → solves "next greater/smaller" in O(n)
Queue = FIFO = natural for BFS (process level by level)
Stack = LIFO = natural for DFS, function call simulation, expression evaluation
Min-stack trick: store (value, current_min) pairs or use auxiliary stack
Histogram rectangle: for each bar, find left/right boundary of shorter bars — monotonic stack!
Patterns Introduced
Monotonic Stack — next greater/smaller element family
BFS with Queue — shortest path, level-order
Two-Stack Queue — amortised O(1) enqueue/dequeue
Sliding Window with Deque — O(n) window maximum/minimum
C32 — Hashing (110 files)
What is Covered
Range	Topics
001–010	Hash function design, division method, multiplication method, universal hashing, perfect hashing concept
011–020	Chaining (separate chaining), open addressing (linear probing), quadratic probing, double hashing
021–030	Load factor, rehashing trigger, amortised analysis of insertions; dynamic resizing
031–040	std::unordered_map internals: bucket count, max_load_factor(), reserve(), custom hash functions
041–050	Custom hash: std::hash specialisation, hash combining (seed ^= hash(v) + 0x9e3779b9 ...), hashing pairs/tuples
051–060	Two Sum / Count pairs, frequency maps, group anagrams, isomorphic strings, word pattern
061–070	LRU cache, all O(1) data structure, design Twitter feed (hash + heap), design phone book
071–080	Bloom filter implementation, count-min sketch concept; probabilistic data structures
081–090	Consistent hash ring, jump consistent hash, rendezvous hashing — distributed systems use cases
091–100	Rolling hash (Rabin-Karp), polynomial hash, string matching with hash; Z-function preview
101–110	Cuckoo hashing, Robin Hood hashing, cache-efficient hash table; fingerprinting for file deduplication; hash collision probability analysis
Key Concepts Learned
A good hash distributes uniformly → average O(1) operations
Separate chaining: simple, degrades to O(n) worst case in one bucket
Open addressing: better cache performance, sensitive to load factor (keep < 0.7)
Why hash maps are not ordered — iteration order is non-deterministic
Rolling hash: slide a window in O(1) by adding new char and removing old
Bloom filter: space-efficient probabilistic membership test (false positives, no false negatives)
Patterns Introduced
Frequency Map — count occurrences in O(n)
Two Sum via Hash — store complement as key
Rolling Hash — O(n) substring search (Rabin-Karp)
Consistent Hashing — distributed key-node mapping
Level 3 — Revision Checklist
STL
 Know iterator invalidation rules for vector, list, map, unordered_map
 Use std::ranges pipeline with filter + transform + take
 Implement top-K using priority_queue with custom comparator
 Know when std::set (sorted, O(log n)) vs std::unordered_set (O(1), no order) is better
Linked Lists
 Reverse a singly linked list in-place (3-pointer technique)
 Detect cycle and find cycle start (Floyd's algorithm)
 Implement LRU cache in O(1) get and put
 Merge K sorted lists using a min-heap
Stacks & Queues
 Solve "Next Greater Element" with monotonic stack
 Implement BFS for shortest path in unweighted graph
 Solve "Largest Rectangle in Histogram" from memory
 Implement min-stack with O(1) getMin
Hashing
 Implement unordered_map with custom hash for pair<int,int>
 Write rolling hash for substring search
 Explain load factor and when to rehash
 Implement basic Bloom filter (bit array + k hash functions)
Common Mistakes at Level 3
Mistake	Correct Approach
Using map when order doesn't matter	Use unordered_map for O(1) average
Hashing pair<int,int> without custom hash	Provide struct PairHash
Forgetting dummy head node in linked list	Always add dummy head for uniform logic
Not handling stack empty before pop	Check !stack.empty() before every pop
Assuming unordered_map iteration order	Order is undefined — use map if order needed
Using std::list::size() expecting O(1)	Since C++11 it IS O(1), but know the history
Interview Focus (Level 3 Topics)
Problem	Data Structure	Complexity
LRU Cache	HashMap + DLL	O(1) get/put
Two Sum	Hash Map	O(n)
Largest Rectangle in Histogram	Monotonic Stack	O(n)
Merge K Sorted Lists	Min-Heap	O(n log k)
Sliding Window Maximum	Monotonic Deque	O(n)
Group Anagrams	Hash Map + Sort	O(n·k log k)
Top-K Frequent Elements	Hash Map + Heap	O(n log k)
"""		
with open(f"{BASE}/LEVEL_03_STL_DataStructures.md", "w") as f: f.write(L3) print("Written: LEVEL_03") PYEOF` completed