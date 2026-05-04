# PROMPT 02 — Level 2 & Level 3: Elementary + Intermediate
## C++ Problem Solving — Book-Alike Deep Learning Guide

---

## HOW TO USE THIS PROMPT

Paste the generation prompt below into an AI with `{{PROBLEM_NAME}}` replaced by any problem from the **Problem Bank**. The AI generates a complete book chapter.

---

## MASTER GENERATION PROMPT

```
===
You are an expert C++ educator writing a BOOK CHAPTER for a self-learner.
The learner is at Level 2–3 (Elementary to Intermediate). They know basic C++ syntax,
control flow, functions, and basic arrays. Now they are learning memory management,
OOP, STL, linked lists, stacks/queues, and hashing.

The topic/problem is: {{PROBLEM_NAME}}

Generate a complete, standalone learning chapter with the following exact structure:

---

# Chapter: {{PROBLEM_NAME}}

## 1. Problem Statement
- Precise problem statement with all constraints.
- 3 input/output examples including: normal case, edge case, large case.
- State time and space constraints expected at this level.

## 2. Prerequisites
List what the learner must know BEFORE attempting this:
- C++ features required (pointers, references, classes, templates, etc.)
- STL containers or algorithms that may be needed
- Mathematical concepts (if any)
- Related simpler problems they should have solved first

## 3. Core Concept Deep Dive
Before the solution, teach the CORE CONCEPT this problem exercises:
- What is the concept? (e.g., "This is about pointer arithmetic and ownership")
- How does C++ implement this internally? (memory layout, vtable, etc.)
- What is the standard library's offering for this? (if applicable)
- Common misconceptions about this concept in C++

## 4. Mental Model & Intuition
- Step-by-step intuition building in plain English.
- ASCII diagram of data structure state (before/after operations).
- Trace through example 1 manually on paper.
- What PATTERN does this problem belong to?

## 5. Solution Approaches

### Approach 1: Brute Force / Naive
- Strategy in 2–3 sentences.
- Full compilable C++17 code with line-by-line comments.
- Time: O(?)  Space: O(?)
- Identify bottleneck.

### Approach 2: Optimized
- What insight removes the bottleneck?
- Full compilable C++17 code with line-by-line comments.
- Time: O(?)  Space: O(?)
- Compare to Approach 1.

### Approach 3: STL / Idiomatic C++ (if exists)
- How does the STL or modern C++ (C++17/20) solve this cleanly?
- Full compilable C++17 code with line-by-line comments.
- Time: O(?)  Space: O(?)
- When would you prefer this in production vs in an interview?

### Approach 4: Low-Level / Manual (for OOP/Pointer problems)
- Implement manually without STL to understand internals.
- Full code with comments.
- What does this teach about C++ memory model?

## 6. Dry Run / Step-by-Step Trace
- Trace the OPTIMAL solution on Example 1.
- Table format: Step | Data Structure State | Key Variable Values | What Happened
- Show at least 5–8 meaningful steps.

## 7. Complexity Analysis
- Time complexity: best / average / worst case with justification.
- Space complexity: stack + heap breakdown.
- Amortized analysis (if applicable — e.g., vector push_back).
- Cache behavior: is this cache-friendly or not? Why?

## 8. Common Mistakes at This Level
List 5–7 mistakes specific to this problem AND this level (Level 2–3):
- Memory management errors (leaks, dangling pointers, double free)
- Iterator invalidation traps
- OOP pitfalls (slicing, virtual destructor missing, copy vs move)
- STL misuse (wrong container choice, complexity surprise)
- Concurrency safety (if applicable)
- Off-by-one, null pointer dereference, uninitialized reads

## 9. What a Senior Engineer Would Do Differently
- Code review perspective: what would a senior flag?
- Production code vs interview code: what changes?
- Testing: what unit tests should be written for this?
- Error handling and defensive coding for this problem.

## 10. C++ Internals — What Happens Under the Hood
- What does the compiler generate for key lines?
- Memory layout of the key data structure used.
- Is there hidden cost (vtable lookup, hash collision, tree rebalance)?
- Use Compiler Explorer (godbolt.org) to illustrate if useful.

## 11. Pattern Recognition & Generalizations
- Formal name of the pattern/algorithm used.
- 5 other problems that use this EXACT pattern (with problem names).
- Fill-in: "When you see _______, immediately think _______."
- How does this problem extend to harder variants?

## 12. Practice Variants (3 levels)
- Easy variant: description + what changes in solution
- Medium variant: description + new constraint that forces re-think
- Hard variant: description + completely new technique needed

## 13. Interview Corner
- Is this a common interview problem? (FAANG / Automotive / Embedded?)
- Expected complexity the interviewer wants.
- Common follow-up questions.
- What does a STRONG vs WEAK interview answer look like?

## 14. Quick Reference Card
- Core idea: 1 sentence
- Key code snippet: 8–15 lines
- Complexity table
- Do NOT forget: 4 things

---
Code standard: C++17, compile with `g++ -std=c++17 -Wall -fsanitize=address`
Tone: Senior engineer mentoring a junior — precise, no hand-waving.
===
```

---

## BATCH GENERATION PROMPT

```
===
You are creating a COMPLETE STUDY GUIDE VOLUME for C++ Level 2–3 topics.

For the category "{{CATEGORY_NAME}}", generate a chapter-per-problem guide
covering ALL problems listed below.

Each chapter must include:
1. Problem statement + 2 examples
2. Core C++ concept it exercises (pointer arithmetic / RAII / vtable / hash collision / etc.)
3. Brute force solution (code + complexity)
4. Optimal solution (code + complexity)  
5. Memory/ownership analysis (who allocates? who frees? any leaks?)
6. OOP/STL note (which class/container is most natural here?)
7. 3 common mistakes
8. Pattern tag + 3 similar problems

Problems:
{{PASTE_PROBLEM_LIST_HERE}}

All code must be C++17, compile cleanly, include comments.
Format: H2 for each problem, consistent sub-headers throughout.
===
```

---

## PROBLEM BANK — LEVEL 2 & LEVEL 3

### LEVEL 2 — Elementary

#### Category C20: Pointers & Memory Management (125 problems)

**Pointer Fundamentals (1–25)**
1. Pointer declaration & initialization
2. Address-of operator `&`
3. Dereference operator `*`
4. Null pointer (`nullptr`)
5. Pointer arithmetic
6. Pointer to array
7. Array name as pointer
8. Pointer to pointer (`**`)
9. Pointer to function
10. `const T*` vs `T* const` vs `const T* const`
11. `void*` pointer
12. Pointer casting
13. Dangling pointer
14. Wild pointer
15. Pointer aliasing
16. `restrict` keyword (C99 concept)
17. Pointer comparison
18. Pointer subtraction
19. Pointer to struct member
20. Arrow operator `->`
21. Dynamic allocation: `new` / `delete`
22. `new[]` / `delete[]`
23. `malloc` / `calloc` / `realloc` / `free`
24. Operator `new` overload
25. Placement `new`

**Memory Management (26–60)**
26. Memory leak detection
27. Valgrind basics
28. RAII pattern
29. Destructor responsibility
30. Rule of 3
31. Rule of 5
32. Rule of 0
33. Copy constructor
34. Move constructor
35. Copy assignment operator
36. Move assignment operator
37. `std::unique_ptr`
38. `std::shared_ptr`
39. `std::weak_ptr`
40. `make_unique` / `make_shared`
41. Custom deleter
42. Deleter with lambda
43. `shared_ptr` reference count
44. Circular reference problem
45. Breaking cycles with `weak_ptr`
46. `enable_shared_from_this`
47. `intrusive_ptr` concept
48. Object pools
49. Arena allocator
50. Stack allocator
51. Pool allocator
52. Custom allocator for STL
53. `std::allocator<T>`
54. Allocator traits
55. Memory alignment
56. Aligned allocation (`aligned_new` C++17)
57. Over-aligned types
58. `alignas` / `alignof`
59. `std::launder`
60. Strict aliasing rule

**Low-Level Memory (61–100)**
61. Type punning via `memcpy`
62. Union type punning
63. Bit manipulation via pointer
64. Endianness check
65. Big-endian vs little-endian
66. Network byte order (`htonl`/`ntohl`)
67. `memcpy` / `memmove` / `memset` / `memcmp`
68. Overlapping memory regions
69. Buffer overflow (concept & danger)
70. Stack smashing
71. Heap overflow
72. Use-after-free
73. Double free
74. Address sanitizer output interpretation
75. Garbage collection concept (vs C++)
76. Reference counting
77. Mark-and-sweep concept
78. Tracing GC concept
79. Smart pointer internals
80. Implementing `shared_ptr` from scratch
81. Implementing `unique_ptr` from scratch
82. Implementing `vector` from scratch
83. Implementing `string` from scratch
84. Copy-on-write string
85. Small buffer optimization (SBO)
86. Short string optimization (SSO)
87. `std::span` (C++20)
88. `std::mdspan` (C++23)
89. `std::byte`
90. `bit_cast` (C++20)
91. Casting pointers safely
92. `reinterpret_cast` dangers
93. Dynamic cast with polymorphism
94. CRTP and static polymorphism
95. Pointer to member (`T::*`)
96. Calling via pointer-to-member
97. `std::mem_fn`
98. Pointer-to-member function
99. `std::invoke`
100. Type-erased callable

**Design Patterns with Pointers (101–125)**
101. Pimpl idiom
102. Opaque pointer
103. Hidden implementation
104. ABI stability
105. Forward declaration for pimpl
106. `unique_ptr` in pimpl
107. Factory pattern with `unique_ptr`
108. Observer with `weak_ptr`
109. Singleton with static local
110. Memory model basics
111. Sequenced-before relation
112. Observable side effects
113. Sequence point rules
114. Unspecified evaluation order
115. Undefined behavior catalog
116. Sanitizer-driven debugging
117. Valgrind memcheck workflow
118. Valgrind massif (heap profiling)
119. AddressSanitizer (ASan) workflow
120. MemorySanitizer (MSan)
121. LeakSanitizer (LSan)
122. UndefinedBehaviorSanitizer
123. Cache-friendly memory access
124. False sharing
125. Struct of Arrays vs Array of Structs

---

#### Category C21: OOP — Classes & Objects (120 problems)

**Class Basics (1–25)**
1. Class vs struct (access default)
2. Member variables
3. Member functions
4. `this` pointer
5. Access specifiers (public/private/protected)
6. Encapsulation
7. Getters and setters
8. `const` member functions
9. `mutable` keyword
10. `static` member variables
11. `static` member functions
12. Friend functions
13. Friend classes
14. Nested classes
15. Local classes
16. Anonymous classes
17. Constructor types (default, param, copy)
18. Constructor init list
19. Delegating constructors (C++11)
20. Inheriting constructors
21. `explicit` keyword
22. Converting constructors
23. Implicit conversions via constructor
24. Destructor
25. Virtual destructor

**Operator Overloading & Inheritance (26–70)**
26. Pure virtual destructor
27. Operator overloading (`+,-,*,/`)
28. Comparison operators (`<=>`)
29. Spaceship operator (C++20)
30. Stream operators `<< >>`
31. Subscript operator `[]`
32. Call operator `()`
33. Increment/decrement (pre/post)
34. Conversion operator
35. Assignment operator chaining
36. Copy-and-swap idiom
37. Inheritance basics (public)
38. Protected inheritance
39. Private inheritance
40. Multiple inheritance
41. Diamond problem
42. Virtual inheritance
43. Virtual base class constructor order
44. Method overriding
45. `override` keyword
46. `final` keyword (class & function)
47. Covariant return types
48. Base class pointer to derived
49. Object slicing
50. Dynamic dispatch (vtable)
51. vtable layout
52. vptr overhead
53. Pure virtual functions
54. Abstract classes
55. Interface pattern (pure abstract class)
56. CRTP (Curiously Recurring Template Pattern)
57. Mixin via CRTP
58. Static polymorphism vs dynamic
59. Type erasure
60. `std::any` for type erasure
61. Polymorphic wrappers
62. `std::variant` visitor
63. `std::visit` with overloaded
64. Strategy pattern
65. Command pattern
66. Observer pattern
67. Decorator pattern
68. Chain of responsibility
69. Composite pattern
70. Template method pattern

**Design Patterns (71–120)**
71. Bridge pattern
72. Flyweight pattern
73. Proxy pattern
74. Iterator pattern (custom)
75. Visitor pattern
76. State machine with classes
77. Builder pattern
78. Factory method
79. Abstract factory
80. Singleton (thread-safe)
81. Prototype pattern
82. Object pools (OOP)
83. RAII wrapper class
84. Handle-Body idiom
85. NVI (Non-Virtual Interface)
86. Policy-based design
87. Traits classes
88. Tag dispatch
89. Class invariants
90. Assertion checks in constructor
91. Exception in constructor
92. Exception in destructor (danger)
93. `noexcept` specifier
94. `noexcept` operator
95. Exception safety: basic, strong, nothrow
96. Copy-on-write
97. Lazy initialization
98. `std::optional` as member
99. `variant` member
100. Bitfield members
101. Padding optimization
102. Empty base optimization (EBO)
103. `[[no_unique_address]]` (C++20)
104. Class template basics
105. Member templates
106. Template specialization for class
107. Partial specialization
108. Variable templates
109. Class with concepts (C++20)
110. `if constexpr` in methods
111. `static_assert` in class
112. Serialization of objects
113. JSON serialization pattern
114. Binary serialization
115. Comparison of classes (total order)
116. Custom hash for class
117. Class in `unordered_map`
118. Class in `std::set`
119. Pimpl idiom in class design
120. ABI-stable class design

---

#### Category C22: STL Containers & Iterators (130 problems)

**Containers (1–35)**
1. `std::vector` (all operations)
2. `std::deque`
3. `std::list` (doubly linked)
4. `std::forward_list`
5. `std::array<T,N>`
6. `std::string` as container
7. `std::stack<T>`
8. `std::queue<T>`
9. `std::priority_queue` (max-heap)
10. `std::priority_queue` (min-heap)
11. `std::set<T>`
12. `std::multiset<T>`
13. `std::map<K,V>`
14. `std::multimap<K,V>`
15. `std::unordered_set<T>`
16. `std::unordered_multiset`
17. `std::unordered_map<K,V>`
18. `std::unordered_multimap`
19. Choosing the right container
20. Container complexity table
21. Iterator concepts (input/output/forward/bi/random)
22. Iterator invalidation rules
23. `begin()` / `end()` / `cbegin()` / `rbegin()`
24. `std::distance` / `std::advance`
25. `std::next` / `std::prev`
26. Iterator arithmetic
27. Reverse iteration
28. `const_iterator` usage
29. Range-based for with iterators
30. Custom iterator class
31. Iterator adaptor (`back_inserter`)
32. `istream_iterator`
33. `ostream_iterator`
34. `move_iterator`
35. Insert iterator types

**Ranges & Algorithms (36–80)**
36. `counted_iterator` (C++20)
37. `std::ranges::view`
38. Lazy ranges (C++20)
39. View adapters (filter, transform)
40. Range pipeline `|`
41. `take` / `drop` / `enumerate`
42. `zip` / `zip_transform`
43. Sorted ranges algorithms
44. Set operations on sorted ranges
45. `std::sort` (Introsort)
46. `std::stable_sort`
47. `std::partial_sort`
48. `std::nth_element`
49. `std::find` / `find_if` / `find_if_not`
50. `std::count` / `count_if`
51. `std::all_of` / `any_of` / `none_of`
52. `std::for_each`
53. `std::transform`
54. `std::accumulate`
55. `std::reduce` (parallel)
56. `std::inclusive_scan` / `exclusive_scan`
57. `std::inner_product`
58. `std::adjacent_difference`
59. `std::partial_sum`
60. `std::fill` / `fill_n`
61. `std::generate` / `generate_n`
62. `std::iota`
63. `std::copy` / `copy_if` / `copy_n`
64. `std::move` (algorithm)
65. `std::remove` / `remove_if`
66. Erase-remove idiom
67. `std::unique` (for sorted)
68. `std::reverse`
69. `std::rotate`
70. `std::shuffle`
71. `std::sample`
72. `std::replace` / `replace_if`
73. `std::swap` / `iter_swap` / `swap_ranges`
74. `std::merge`
75. `std::inplace_merge`
76. `std::includes`
77. `std::set_union` / `set_intersection` / `set_difference`
78. `std::set_symmetric_difference`
79. `std::min` / `max` / `minmax`
80. `std::min_element` / `max_element`

**Advanced STL (81–130)**
81. `std::clamp`
82. `std::lower_bound` / `upper_bound`
83. `std::equal_range`
84. `std::binary_search`
85. `std::is_sorted` / `is_sorted_until`
86. `std::is_permutation`
87. `std::next_permutation` / `prev_permutation`
88. Heap operations
89. `make_heap` / `push_heap` / `pop_heap` / `sort_heap`
90. `std::lexicographical_compare`
91. `std::mismatch`
92. `std::equal`
93. `std::search` / `search_n`
94. `std::starts_with` / `ends_with` (C++20)
95. Custom comparator with lambda
96. `std::less` / `std::greater`
97. `std::greater<void>` (transparent)
98. `std::hash` specialization
99. Custom hash function
100. Collision handling concept
101. Open addressing vs chaining
102. Load factor and rehashing
103. `unordered_map::reserve()`
104. Bucket count and max load factor
105. `map::emplace` / `try_emplace`
106. `map::insert_or_assign`
107. `map::merge` (C++17)
108. `map::extract` node (C++17)
109. `multimap::equal_range`
110. `set::erase` by iterator vs value
111. `set::lower_bound` / `upper_bound`
112. Ordered vs unordered perf comparison
113. Flat map (sorted vector of pairs)
114. `std::span` over container
115. `std::string_view` over string
116. Container adaptors internals
117. Priority queue with custom struct
118. Monotonic stack pattern
119. Monotonic deque pattern
120. Sliding window with deque
121. Two-heap median
122. K closest elements
123. Kth largest element
124. Top-K frequent elements
125. Sort characters by frequency
126. Small vector optimization concept
127. `inplace_vector` (C++26 concept)
128. `std::flat_map` (C++23)
129. `std::flat_set` (C++23)
130. `std::generator` (C++23)

---

### LEVEL 3 — Intermediate

#### Category C30: Linked Lists (120 problems)

**Basic Operations (1–30)**
1. Singly linked list implementation
2. Doubly linked list
3. Circular linked list
4. XOR linked list
5. Insert at head/tail/position
6. Delete by value/position
7. Search in linked list
8. Length of list
9. Print list forward
10. Print list reverse (recursive)
11. Reverse a linked list (iterative)
12. Reverse (recursive)
13. Reverse in groups of K
14. Reverse between positions L and R
15. Detect cycle (Floyd's algorithm)
16. Find cycle start node
17. Remove cycle
18. Length of cycle
19. Intersection of two lists
20. Check if palindrome
21. Remove duplicates (sorted)
22. Remove duplicates (unsorted)
23. Remove Nth from end
24. Middle of list
25. Merge two sorted lists
26. Merge K sorted lists
27. Sort linked list (merge sort)
28. Sort linked list (quick sort)
29. Add two numbers (list digits)
30. Multiply two numbers (list)

**Intermediate Operations (31–70)**
31. Subtract two numbers (list)
32. Add 1 to list number
33. Swap nodes in pairs
34. Swap every K nodes
35. Rotate list right by K
36. Flatten multilevel list
37. Flatten sorted doubly nested list
38. Copy list with random pointer
39. Clone graph via list
40. Odd-even node rearrangement
41. Segregate even/odd positions
42. Move zeros to end (list)
43. Partition list around x
44. Sort list 0/1/2
45. Intersection node value
46. Check list is sorted
47. Find Kth from end
48. Find Kth from start
49. Skip M delete N
50. Delete without head pointer
51. Delete all occurrences of value
52. Delete all duplicates (keep unique)
53. Remove nodes with greater right value
54. Remove nodes not in range
55. Merge in between lists
56. Insert greatest common divisors
57. Spiral order linked list
58. Zigzag reorder
59. Reorder list (L0→Ln→L1→Ln-1)
60. Split list into two halves
61. Split into k parts
62. Merge alternating from two lists
63. Interleave two lists
64. List from array / array from list
65. Convert BST to doubly linked list
66. Convert binary tree to list (in-order)
67. Flatten binary tree to linked list
68. LRU Cache implementation (hash+DLL)
69. LFU Cache implementation
70. Skip list basics

**Advanced List Concepts (71–120)**
71. Skip list search / insert / delete
72. Skip list vs BST comparison
73. Unroll linked list (cache optimization)
74. Self-organizing list
75. Move-to-front heuristic
76. Frequency-based ordering
77. Josephus problem (list)
78. Queue using two stacks
79. Stack using queues
80. Deque from scratch
81. Priority queue from linked list
82. Sorted insert in linked list
83. Insert into circular sorted list
84. In-place merge sorted lists
85. Difference of two lists
86. Union of two sorted lists
87. Intersection of two sorted lists
88. Maximum twin sum
89. Sum of nodes between zeros
90. Maximum pair sum
91. Double a number (list)
92. Swapping nodes (not values)
93. Nodes in even/odd positions swap
94. Link nodes at k distance
95. Node with next greater element
96. Next larger node
97. List memory layout analysis
98. Cache-unfriendly nature of lists
99. `std::list` vs `std::vector` performance
100. `std::forward_list` usage
101. List `splice()`
102. List `unique()`
103. List `remove()` / `remove_if()`
104. List `sort()` (stable, merge sort)
105. List `merge()` (sorted)
106. List `reverse()`
107. Intrusive linked list concept
108. Lock-free linked list concept
109. XOR doubly linked list memory trick
110. Sentinel node pattern
111. Dummy head node pattern
112. Two-pointer approach on lists
113. Fast-slow pointer all applications
114. List serialization / deserialization
115. Thread-safe linked list
116. Memory pool for list nodes
117. List with O(1) random access (skip list)
118. Doubly-linked list as deque
119. Circular buffer with linked list
120. Linked list in embedded systems (no heap)

---

#### Category C31: Stacks & Queues (115 problems)

**Implementation (1–20)**
1. Stack using array
2. Stack using linked list
3. Stack using `std::stack`
4. Stack using `std::vector`
5. Queue using array (circular)
6. Queue using linked list
7. Queue using `std::queue`
8. Deque using `std::deque`
9. Priority queue implementation
10. Min-stack (O(1) `getMin`)
11. Max-stack
12. Two-stack queue
13. Two-queue stack
14. Stack with increment operation
15. Queue with max operation
16. Circular buffer
17. Ring buffer for streaming data
18. Monotonic stack intro
19. Next greater element I
20. Next greater element II (circular)

**Monotonic Stack Problems (21–50)**
21. Next smaller element
22. Previous greater element
23. Previous smaller element
24. Largest rectangle in histogram
25. Maximal rectangle (matrix)
26. Sum of subarray minimums
27. Sum of subarray maximums
28. Remove k digits (smallest number)
29. 132 pattern detection
30. Daily temperatures
31. Online stock span
32. Asteroid collision
33. Score of parentheses
34. Remove duplicate letters
35. Smallest subsequence of distinct chars
36. Remove all adjacent duplicates
37. Remove all adjacent duplicates (k times)
38. Decode string (`k[str]`)
39. Simplify Unix path
40. Valid parentheses
41. Check redundant brackets
42. Minimum remove to valid parens
43. Count valid parentheses substrings
44. Longest valid parentheses
45. Minimum add to make valid
46. Balance parentheses
47. Evaluate reverse Polish notation
48. Basic calculator I
49. Basic calculator II
50. Basic calculator III

**Queue & BFS Problems (51–115)**
51. Implement queue using stacks (amortized)
52. Design bounded blocking queue
53. Design front/middle/back queue
54. Circular queue design
55. Sliding window max (deque)
56. Sliding window min
57. K sliding window averages
58. Max of all subarrays size k
59. BFS using queue (graph)
60. BFS level order (tree)
61. Zigzag level order
62. Level averages
63. Level right side view
64. Populating next right pointers
65. Multi-source BFS
66. 0-1 BFS
67. Dijkstra with priority queue
68. Prim's with priority queue
69. A* algorithm (priority queue)
70. Huffman coding (priority queue)
71. Merge K sorted arrays (heap)
72. K-way merge
73. Find median from data stream
74. Sliding window median
75. Top K frequent words
76. Sort nearly sorted (k-sorted)
77. Design Twitter (top 10 tweets)
78. Task scheduler (queue)
79. CPU scheduling FCFS/SJF
80. Round-robin scheduling
81. Print binary numbers 1 to N
82. First negative in window
83. Gas station circular queue
84. Number of islands (BFS)
85. Walls and gates BFS
86. Rotten oranges BFS
87. Shortest path binary matrix
88. 01 matrix (BFS distance)
89. Pacific Atlantic water flow
90. Snakes and ladders BFS
91. Jump game BFS variant
92. Open the lock BFS
93. Word ladder I
94. Word ladder II (all shortest paths)
95. Minimum knight moves
96. Sliding puzzle BFS
97. Minimum steps to reach target
98. Minimum genetic mutation
99. Alien dictionary (topological sort)
100. Course schedule BFS
101. Network delay time
102. Cheapest flights within K stops
103. Deque-based LRU cache
104. Priority queue with lazy deletion
105. Monotonic deque (all operations)
106. Stack-sortable permutations
107. Tower of Hanoi with explicit stack
108. Expression tree construction
109. Infix to postfix conversion
110. Postfix to infix conversion
111. Balanced parentheses all combinations
112. Minimum cost to sort with stack
113. Stock price span (stack)
114. Sum of subarray ranges
115. Number of visible people in queue

---

#### Category C32: Hashing & Hash Tables (110 problems)

**Hash Table Internals (1–25)**
1. Hash function design principles
2. Division method
3. Multiplication method
4. Universal hashing concept
5. Perfect hashing concept
6. Chaining (separate chaining)
7. Open addressing (linear probing)
8. Quadratic probing
9. Double hashing
10. Robin Hood hashing
11. Cuckoo hashing
12. Load factor and rehashing
13. Hash table implementation from scratch
14. Dynamic resizing
15. Amortized cost analysis
16. `unordered_map` internals
17. Custom hash for struct/class
18. FNV hash function
19. DJB2 hash function
20. MurmurHash concept
21. CityHash / SipHash concept
22. Rolling hash (Rabin-Karp)
23. Polynomial rolling hash
24. Anti-hash test (worst case)
25. Bloom filter

**Hash-Based Problems (26–70)**
26. Count-min sketch
27. HyperLogLog concept
28. Consistent hashing
29. Two sum (classic hash)
30. Four sum with hash
31. Subarray zero sum
32. Longest subarray with sum k
33. Count subarrays with sum k
34. Count subarrays XOR k
35. Subarray equal 0s and 1s
36. Longest equal 0s and 1s
37. Group anagrams
38. Valid anagram
39. Isomorphic strings (hash)
40. Word pattern
41. Ransom note
42. Contains duplicate
43. Contains duplicate within k distance
44. Contains duplicate within value diff
45. Happy number (cycle detect)
46. Repeated DNA sequences
47. Find all duplicates in array
48. Find all disappeared numbers
49. Intersection of two arrays
50. Intersection of two arrays II
51. Union of two arrays
52. Common characters
53. Unique number of occurrences
54. Top K frequent elements
55. Sort characters by frequency
56. Degree of array
57. Max points on a line (slope hash)
58. Number of boomerangs
59. Brick wall minimum cuts
60. Employee importance BFS+hash
61. First unique character
62. First recurring character
63. Jewels and stones
64. Destination city (hash)
65. Minimum index sum (two lists)
66. Longest harmonious subsequence
67. Continuous subarray sum (k×n)
68. Longest arithmetic subsequence
69. Longest geometric subsequence
70. Equal row and column pairs

**Advanced Hashing (71–110)**
71. Check if graph bipartite (color hash)
72. Count paths with given XOR
73. Minimum consecutive cards to pick up
74. Max number of k-sum pairs
75. Count good meals (power of 2 sum)
76. Number of wonderful substrings
77. Find the difference (hash/XOR)
78. Missing number (hash)
79. Buddy strings
80. Close strings
81. Reorganize string
82. Task scheduler with counts
83. Bulls and cows
84. Word frequency counter
85. Design hashmap from scratch
86. Design hashset from scratch
87. Time-based key-value store
88. LRU Cache (hash + doubly linked list)
89. LFU Cache (two hashmaps + heap)
90. Design in-memory file system
91. Design phone directory
92. Find anagram mappings
93. Subdomain visit count
94. Max frequency stack (FreqStack)
95. Number of atoms (chemistry formula)
96. Random pick with blacklist
97. Encode and decode TinyURL
98. Minimum window containing all chars
99. Check if all chars appear equal times
100. Longest substring with at most K distinct
101. Substring with concatenation of all words
102. Pattern match with hash
103. Count number of texts (hash DP)
104. Minimum number of operations to make array beautiful
105. Distinct values in window
106. Cache-efficient hash table (Robin Hood)
107. Consistent hash ring implementation
108. Fingerprinting with hash (file dedup)
109. Rolling hash for substring search
110. Polynomial hash collision probability

---

## SUPPLEMENTARY PROBLEMS (Level 2–3 additions from LeetCode/GFG/GitHub)

### LeetCode Medium (Level 2–3 aligned)
- Add Two Numbers (#2)
- Longest Substring Without Repeating (#3)
- Container With Most Water (#11)
- 3Sum (#15)
- Letter Combinations of Phone (#17)
- Remove Nth Node From End (#19)
- Merge Two Sorted Lists → Merge K Sorted Lists (#23)
- Next Permutation (#31)
- Search in Rotated Sorted Array (#33)
- Group Anagrams (#49)
- Maximum Subarray / Kadane's (#53)
- Jump Game (#55)
- Merge Intervals (#56)
- Unique Paths (#62)
- Word Search (#79)
- Linked List Cycle II (#142)
- LRU Cache (#146)
- Min Stack (#155)
- Reverse Linked List (#206) → Reverse in K Groups (#25)
- Number of Islands (#200)
- House Robber (#198)
- Course Schedule (#207)
- Implement Trie (Prefix Tree) (#208)
- Design Add and Search Words Data Structure (#211)

### GeeksForGeeks Medium
- Detect loop in a linked list
- Floyd's Cycle Detection
- Reverse a linked list in groups of K
- Flatten a multilevel doubly linked list
- Clone a linked list with random pointers
- Expression evaluation using stack
- Next greater element
- Largest Rectangle in Histogram
- Design LRU Cache

---

## LEARNING ROADMAP — Level 2 → Level 3

```
Week 1–2:  C20 (1–60)    Pointer fundamentals, RAII, smart pointers
Week 3–4:  C20 (61–125)  Low-level memory, sanitizers, cache effects
Week 5–6:  C21 (1–60)    OOP basics, inheritance, polymorphism
Week 7–8:  C21 (61–120)  Design patterns, exceptions, template basics
Week 9–10: C22 (1–70)    STL containers, iterators, algorithms
Week 11:   C22 (71–130)  Advanced STL, ranges, complexity analysis
Week 12:   C30 (1–60)    Linked list implementation + problems
Week 13:   C30 (61–120)  Advanced list problems, skip list, LRU/LFU
Week 14:   C31 (1–50)    Stack/queue implementations + monotonic stack
Week 15:   C31 (51–115)  BFS patterns, priority queue problems
Week 16:   C32 (1–55)    Hash table internals + problems
Week 17:   C32 (56–110)  Advanced hashing, design problems
```

---

## RESOURCES

| Resource | Link | Best For |
|----------|------|----------|
| cppreference.com | https://en.cppreference.com | STL definitive reference |
| Back to Basics CppCon | YouTube | Memory model, smart ptrs |
| Effective C++ (Meyers) | Book | OOP/STL best practices |
| More Effective C++ | Book | Exception safety, efficiency |
| LeetCode Medium | https://leetcode.com | Problem practice |
| GeeksForGeeks | https://geeksforgeeks.org/data-structures | DS theory + code |
| Visualgo | https://visualgo.net | Visual DS/algorithm traces |
| CS Dojo (YouTube) | YouTube | Interview problem walkthroughs |
| GitHub: striver-fraz/A2Z-DSA | Striver's A2Z sheet | Complete roadmap |
| GitHub: TheAlgorithms/C-Plus-Plus | https://github.com/TheAlgorithms/C-Plus-Plus | Algorithm reference |
| Compiler Explorer | https://godbolt.org | Assembly + optimization |
| Quick C++ Benchmarks | https://quick-bench.com | Performance measurement |
