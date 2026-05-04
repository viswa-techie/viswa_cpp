# PROMPT 01 — Level 0 & Level 1: Absolute Beginner + Beginner
## C++ Problem Solving — Book-Alike Deep Learning Guide

---

## HOW TO USE THIS PROMPT

Copy the section below (between the `===` markers) and paste it into an AI (ChatGPT / Claude / Gemini / Copilot). Replace `{{PROBLEM_NAME}}` with any problem listed in the **Problem Bank** at the bottom of this file. The AI will generate a full single-document learning chapter for that problem.

---

## MASTER GENERATION PROMPT

```
===
You are an expert C++ educator writing a BOOK CHAPTER for a self-learner.
The learner is at Level 0–1 (Absolute Beginner to Beginner).
The topic/problem is: {{PROBLEM_NAME}}

Generate a complete, standalone learning chapter with the following exact structure:

---

# Chapter: {{PROBLEM_NAME}}

## 1. Problem Statement
- Write a clear, precise problem statement in plain English.
- Give 2–3 concrete input/output examples with edge cases.
- State constraints (input size, data types, overflow risks).

## 2. What You Must Know Before Solving This
List ALL prerequisite concepts the learner must understand:
- C++ syntax constructs used (keywords, operators, control flow)
- Standard library headers and functions involved
- Memory model basics if applicable
- Any math or logic foundation needed

## 3. Mental Model — How to THINK About This Problem
- Explain the intuition step-by-step in plain English before any code.
- Use an analogy if possible (real-world mapping).
- Draw ASCII diagrams or trace tables where helpful.
- Explain what naive/wrong thinking looks like and why it fails.
- Guide the learner to the "aha" insight.

## 4. Solution Approaches (from Brute Force to Optimal)

### Approach 1: Brute Force / Naive
- Explain the idea in 2–3 sentences.
- Full compilable C++ code with line-by-line comments.
- Time complexity: O(?)  |  Space complexity: O(?)
- Why this works but why it might be too slow.

### Approach 2: Improved / Standard
- What improvement does this make over Approach 1?
- Full compilable C++ code with line-by-line comments.
- Time complexity: O(?)  |  Space complexity: O(?)

### Approach 3: Optimal / Idiomatic C++ (if applicable)
- What makes this the best solution?
- Full compilable C++ code with line-by-line comments.
- Time complexity: O(?)  |  Space complexity: O(?)
- Mention STL functions or language features that simplify this.

## 5. Dry Run / Trace
- Pick one of the examples from Section 1.
- Trace the OPTIMAL solution step by step showing variable state at each iteration.
- Use a table format: Step | Variables | Explanation

## 6. Common Mistakes & Pitfalls
List 4–6 specific mistakes beginners make on this exact problem:
- Off-by-one errors
- Uninitialized variables
- Integer overflow
- Wrong output format
- Missing edge cases (empty input, single element, all same, negative numbers)
- Undefined behavior traps

## 7. Special Learning Points
- What C++ feature does this problem best illustrate?
- Any compiler warning this problem triggers and why?
- Any behavior that differs between C++11/14/17/20?
- What would a code reviewer flag in a beginner's solution?
- Is there a common interview follow-up question for this?

## 8. Pattern Recognition
- What pattern/technique does this problem represent?
- List 3–5 other problems that use the EXACT SAME pattern so the learner can practice.
- When you see _______, think _______.

## 9. Practice Variants
Give 3 variants of this problem at increasing difficulty:
- Easy variant
- Medium variant  
- Hard variant
Each variant: one sentence description + what changes in the solution.

## 10. Quick Reference Card
One-page summary the learner can review before an interview:
- Core idea in 1 sentence
- Key code snippet (5–10 lines max)
- Complexity
- 3 things NOT to forget

---

Write everything in Markdown. All code must be standard C++17 and compile with `g++ -std=c++17 -Wall`.
Make the tone encouraging and educational — like a patient senior engineer explaining to a junior.
===
```

---

## BATCH GENERATION PROMPT (for entire category at once)

```
===
You are an expert C++ educator creating a COMPLETE BOOK VOLUME.

Generate a full structured learning guide for ALL problems in the category: {{CATEGORY_NAME}}
Level: {{LEVEL}} — {{LEVEL_TITLE}}

For EACH problem in the list below, create a mini-chapter with:
1. Problem Statement (3–5 lines + 2 examples)
2. Mental Model (intuition, analogy, ASCII diagram if helpful)
3. Two solutions: Brute Force (code + complexity) and Optimal (code + complexity)
4. Dry run of optimal on example 1
5. Top 3 pitfalls
6. Pattern tag: what family of problems this belongs to
7. 2 similar problems to practice next

Problems list:
{{PASTE_PROBLEM_LIST_HERE}}

Format: Each problem as a separate H2 section with consistent sub-headers.
All code: compilable C++17 with comments.
===
```

---

## PROBLEM BANK — LEVEL 0 & LEVEL 1

### LEVEL 0 — Absolute Beginner

#### Category C00: C++ Syntax & Program Structure (120 problems)

**Foundation Group (Programs 1–20)**
1. Hello World program
2. `#include`, `using namespace std`
3. `main()` function anatomy
4. Single-line & multi-line comments
5. Semicolons and statement termination
6. Whitespace and indentation rules
7. Case sensitivity
8. Identifiers & naming rules
9. Keywords list & usage
10. Basic input with `cin`
11. Basic output with `cout`
12. `endl` vs `\n`
13. Multiple variables on one line
14. Chained `cout` statements
15. Reading multiple inputs
16. Program compilation with `g++`
17. Common compile errors
18. Linker errors vs compile errors
19. Warnings and how to fix them
20. Using `-Wall` flag

**Code Structure Group (21–40)**
21. Code blocks and braces
22. Nested braces
23. Scope basics with braces
24. Blank lines and readability
25. Code formatting standards
26. Literal values (numbers, strings)
27. String literals with quotes
28. Escape sequences (`\n`, `\t`, `\\`)
29. Raw string literals `R"(...)"`
30. Unicode basics
31. ASCII values
32. `char` literals with single quotes
33. Printing special characters
34. Tab stops with `\t`
35. `printf` vs `cout`
36. `scanf` vs `cin`
37. `puts()` and `gets()` legacy
38. `iostream` header
39. `cstdio` header
40. Including multiple headers

**Preprocessor & Compilation Group (41–60)**
41. Header file purpose
42. Compilation steps overview
43. Preprocessor directives
44. `#define` basics
45. Macro constants
46. Conditional compilation `#ifdef`
47. `#pragma once`
48. Include guards
49. Multiple source files concept
50. Object files (`.o`)
51. Linking explained
52. `argc` and `argv` basics
53. Command-line arguments printing
54. `return 0` meaning
55. Non-zero return codes
56. `EXIT_SUCCESS` / `EXIT_FAILURE`
57. Program entry/exit flow
58. Debugger basics (gdb intro)
59. Breakpoints concept
60. Stepping through code

**I/O & Debugging Group (61–80)**
61. Print-based debugging
62. `cerr` for error output
63. `clog` for logging
64. `flush` output buffer
65. `std::endl` flushing
66. Buffered vs unbuffered output
67. Reading entire line with `getline`
68. Whitespace in `getline`
69. `cin.ignore()` usage
70. `cin.clear()` usage
71. Input failure states
72. Numeric input validation basics
73. Type mismatch in input
74. Overflow on small types
75. Garbage values without initialization
76. Undefined behavior intro
77. Stack memory concept (simple)
78. Static vs automatic storage basics
79. Global variables basics
80. Local variables basics

**Variables & Functions Basics Group (81–100)**
81. Variable lifetime basics
82. Block scope vs file scope
83. Forward declarations basics
84. Function prototypes concept
85. Simple function definition
86. Calling a function
87. Return value from function
88. `void` functions
89. Parameters vs arguments
90. Pass by value basics
91. Multiple return values (intro)
92. Overloading intro (concept only)
93. Inline concept (brief)
94. `constexpr` intro
95. `auto` keyword intro
96. `decltype` intro
97. `nullptr` intro
98. `NULL` vs `nullptr`
99. Basic boolean logic
100. `true`/`false` literals

**Modern C++ Basics Group (101–120)**
101. Boolean output (0/1)
102. Casting bool to int
103. `sizeof` operator
104. Addresses concept (`&`)
105. Dereferencing concept (`*`)
106. Basic struct definition
107. Struct member access
108. Struct initialization
109. Simple enum definition
110. `enum class` basics
111. `typedef` basics
112. `using` alias basics
113. Namespaces concept
114. `std::` prefix meaning
115. `using namespace std` risks
116. Named namespace basics
117. Anonymous namespace
118. Nested namespace (C++17)
119. One-definition rule basics
120. Translation unit concept + build systems intro

---

#### Category C01: Data Types & Variables (110 problems)

**Primitive Types Group (1–20)**
1. `int`, `float`, `double`, `char`, `bool`
2. `short`, `long`, `long long`
3. `unsigned` types
4. `signed` vs `unsigned`
5. Type sizes with `sizeof`
6. `INT_MAX` / `INT_MIN` constants
7. `FLT_MAX` / `DBL_MAX`
8. Overflow wrap-around (unsigned)
9. Signed overflow UB
10. Floating point precision issues
11. `0.1 + 0.2 != 0.3` explained
12. `NaN` and infinity (float)
13. `isinf()` `isnan()`
14. `std::numeric_limits<T>`
15. Fixed-width types (`int32_t`, `uint64_t`)
16. `<cstdint>` header
17. `ptrdiff_t` and `size_t`
18. Implicit type conversion
19. Explicit cast (C-style)
20. `static_cast<>`

**Casting & Conversion Group (21–40)**
21. `reinterpret_cast<>`
22. `const_cast<>`
23. `dynamic_cast<>`
24. Narrowing conversions
25. Brace-init prevents narrowing
26. Integer promotion rules
27. Usual arithmetic conversions
28. Integral vs floating arithmetic
29. Mixed-type expressions
30. Char arithmetic
31. `wchar_t`, `char16_t`, `char32_t`
32. String vs char array
33. `std::string` basics
34. String `length` vs `size`
35. Accessing string characters
36. String concatenation
37. String comparison
38. String to int (`stoi`)
39. String to double (`stod`)
40. Int to string (`to_string`)

**Strings & Collections Group (41–70)**
41. `std::stof`, `stol`, `stoul`
42. String `find()` method
43. String `substr()`
44. String `replace()`
45. String `insert()` / `erase()`
46. String `empty()` / `clear()`
47. C-string (`char` array) basics
48. `strlen` vs `string::size`
49. `strcpy` / `strncpy`
50. `strcmp` / `strncmp`
51. `strcat` / `strncat`
52. `sprintf` / `snprintf`
53. `atoi` / `atof` legacy
54. String literals and pointers
55. `const char*`
56. `string_view` intro (C++17)
57. Structured bindings (C++17)
58. Tuple basics
59. `pair<T1,T2>`
60. `make_pair()`
61. `tie()` for tuple unpack
62. `Optional<T>` (C++17)
63. `variant<T...>` (C++17)
64. `any` (C++17)
65. Bitfield basics
66. Union basics
67. Anonymous union
68. Alignment and `alignof`
69. `alignas` specifier
70. Padding in structs

**Storage & Type System Group (71–110)**
71. `#pragma pack`
72. POD types
73. Trivially copyable types
74. Standard layout types
75. Aggregate initialization
76. Designated initializers (C++20)
77. Uniform initialization `{}`
78. Value initialization
79. Default initialization
80. Zero initialization
81. Copy initialization
82. Direct initialization
83. List initialization
84. Brace elision
85. Narrowing in initializer lists
86. `constexpr` variables
87. `const` vs `constexpr`
88. `consteval` (C++20)
89. `constinit` (C++20)
90. `inline` variables (C++17)
91. `thread_local` storage
92. `volatile` keyword
93. `register` keyword (deprecated)
94. `extern` declaration
95. Linkage: internal vs external
96. One definition rule
97. Tentative definitions (C)
98. Multiple definitions error
99. Redeclaration vs redefinition
100. Forward declare struct
101. Incomplete types
102. Opaque pointer pattern
103. Type aliases with `using`
104. Template type aliases
105. `auto` type deduction rules
106. `decltype(auto)`
107. CTAD (Class Template Arg Deduction)
108. Concepts intro (C++20)
109. `requires` clause basics
110. Type traits overview

---

### LEVEL 1 — Beginner

#### Category C10: Control Flow & Loops (115 problems)

**Basic Control Flow (1–20)**
1. `if` / `else if` / `else`
2. Nested `if` statements
3. Dangling else problem
4. Switch-case statement
5. Switch fall-through
6. Switch with enum
7. Ternary operator `?:`
8. Nested ternary (anti-pattern)
9. `while` loop
10. `do-while` loop
11. `for` loop
12. Range-based `for` loop
13. Range-for with index trick
14. Infinite loop patterns
15. `break` statement
16. `continue` statement
17. `goto` (and why to avoid)
18. Loop unrolling concept
19. FizzBuzz
20. Sum 1 to N

**Math Problems (21–50)**
21. Factorial (iterative)
22. Fibonacci (iterative)
23. Prime check
24. Sieve of Eratosthenes
25. GCD (Euclidean)
26. LCM from GCD
27. Count digits
28. Reverse digits
29. Palindrome number
30. Armstrong number
31. Perfect number
32. Abundant number
33. Sum of digits
34. Digital root
35. Power (iterative)
36. Modular exponentiation
37. Binary to decimal
38. Decimal to binary
39. Octal / Hexadecimal conversion
40. Base conversion generic
41. Leap year check
42. Day of week calculation
43. Number of days in month
44. Time addition (HH:MM:SS)
45. Matrix loop (row-major)
46. Column-major access
47. Stars and pattern (triangle)
48. Inverted triangle
49. Diamond pattern
50. Floyd's triangle

**Patterns & String Loops (51–80)**
51. Pascal's triangle (print)
52. Number pyramid
53. Hollow rectangle pattern
54. Spiral matrix print
55. Loop invariant reasoning
56. Off-by-one errors
57. Index out of bounds
58. Infinite loop debugging
59. Early exit pattern
60. Guard clauses
61. Loop with multiple conditions
62. Boolean flags in loops
63. Counting with modulo
64. Cyclic iteration
65. Two-pointer in loops (intro)
66. Sliding window intro
67. Nested loop complexity
68. Reducing O(n²) loops
69. Loop fusion
70. Loop fission
71. Prefix sum with loop
72. Running average
73. Running max/min
74. Mode of array in loop
75. Frequency count with array
76. Histogram in loop
77. String reversal loop
78. Palindrome string check
79. Count vowels/consonants
80. Caesar cipher loop

**String Processing (81–115)**
81. ROT13
82. String to uppercase/lowercase
83. Remove spaces from string
84. Count words in string
85. Find substring manually
86. Replace char in string
87. Compress string (run-length encoding)
88. Expand compressed string
89. Anagram check (sort approach)
90. Isomorphic strings
91. Longest run of character
92. Most frequent character
93. String rotation check
94. Shift string by k
95. Toggle case
96. Title case conversion
97. Trim leading/trailing spaces
98. Tokenize by delimiter
99. Count specific char
100. Unique chars in string
101. Remove duplicates in string
102. Interleave two strings
103. Merge sorted strings
104. Longest common prefix (loop)
105. `atoi` implementation
106. `itoa` implementation
107. `strtol` manual implementation
108. Number formatting with commas
109. Scientific notation parse
110. Binary string to int
111. Hex string to int
112. IP address parse & validate
113. Roman numeral to int
114. Int to Roman numeral
115. Luhn algorithm / checksum

---

#### Category C11: Functions & Recursion (120 problems)

**Function Fundamentals (1–25)**
1. Function declaration vs definition
2. Return types
3. `void` functions
4. Multiple return values via reference
5. Default parameter values
6. Default params ordering rules
7. Function overloading
8. Overload resolution rules
9. Ambiguous overloads
10. Name mangling
11. `extern "C"` linkage
12. Inline functions
13. `constexpr` functions
14. `consteval` functions (C++20)
15. Function pointers
16. `typedef` for function pointer
17. `using` alias for function pointer
18. Calling via function pointer
19. Array of function pointers
20. Callback pattern
21. Passing functions to functions
22. Returning function pointers
23. `std::function<>`
24. `std::bind()`
25. Partial application with bind

**Lambdas (26–40)**
26. Lambda expressions
27. Lambda capture by value
28. Lambda capture by reference
29. Generic lambdas (C++14)
30. Lambda in algorithms
31. Immediately invoked lambda
32. Recursive lambda
33. Higher-order functions
34. Currying in C++
35. Functor objects
36. Memoize wrapper
37. LRU cache concept
38. Fibonacci with matrix expo
39. Nth root binary search (float)
40. Newton's method sqrt

**Recursion Basics (41–75)**
41. Factorial (recursive)
42. Fibonacci (recursive)
43. Sum of array (recursive)
44. Power (recursive)
45. GCD (recursive)
46. Binary search (recursive)
47. Tower of Hanoi
48. Flood fill (recursive)
49. Permutations of string
50. Subsets of set
51. Combinations nCr
52. Generate parentheses
53. Sudoku solver
54. N-Queens problem
55. Rat in a maze
56. Word search in grid
57. Letter combinations phone
58. Palindrome partitioning
59. Restore IP addresses
60. Combination sum
61. Combination sum II (duplicates)
62. Subset sum check
63. Count paths in grid
64. Unique paths (recursive)
65. Staircase problem (1/2 steps)
66. Min cost staircase
67. Print all paths in maze
68. Paint fill
69. Boolean parenthesization
70. Evaluate expression tree
71. Tree traversal (recursive)
72. Depth of tree (recursive)
73. Reverse linked list (recursive)
74. Merge sort
75. Quick sort

**Advanced Recursion Concepts (76–120)**
76. Recursive binary search
77. Ackermann function
78. Hofstadter sequence
79. Mutual recursion (even/odd)
80. Indirect recursion
81. Tail recursion
82. Tail call optimization
83. Memoization basics
84. Top-down DP with memo
85. Stack overflow (too deep)
86. Max recursion depth
87. Iterative DFS vs recursive
88. Convert recursion to iteration
89. Call stack visualization
90. Recursion tree analysis
91. Recurrence relations `T(n)=2T(n/2)+n`
92. Master theorem basics
93. Divide and conquer paradigm
94. Merge two sorted arrays
95. Count inversions
96. Closest pair of points
97. Fast exponentiation
98. Extended Euclidean algorithm
99. Modular inverse
100. Catalan numbers recursive
101. Bell numbers
102. Derangements
103. Inclusion-exclusion principle
104. Bisection method
105. Fixed-point iteration
106. Pass by reference in recursion
107. Accumulator pattern
108. Continuation-passing style
109. Trampolining pattern
110. Y-combinator concept
111. Fibonacci with matrix expo
112. Binary GCD
113. Sieve segmented (recursive)
114. Prime factorization recursive
115. Euler's totient
116. Pigeonhole principle problems
117. Partition numbers
118. Stirling numbers
119. Karatsuba multiplication concept
120. Chinese Remainder Theorem basics

---

#### Category C12: Arrays & Strings (Core) (130 problems)

**Array Basics (1–25)**
1. 1D array declaration & init
2. Array size pitfalls
3. Out-of-bounds access (UB)
4. `std::array<T,N>`
5. `std::vector` basics
6. `vector::push_back`
7. `vector::at()` vs `[]`
8. `vector::size` vs `capacity`
9. `vector::resize` vs `reserve`
10. 2D vector
11. 2D array (C-style)
12. Multidimensional arrays
13. Array decay to pointer
14. Passing array to function
15. Array length tricks
16. Sorted array check
17. Linear search
18. Binary search iterative
19. Binary search on answer
20. `lower_bound` / `upper_bound`
21. Find first/last occurrence
22. Count occurrences (sorted)
23. Insertion into sorted array
24. Deletion from array
25. Rotate array left/right

**Two-Pointer & Sliding Window (26–55)**
26. Find rotation pivot
27. Search in rotated sorted array
28. Two sum (brute)
29. Two sum (hash map)
30. Two sum (two pointers)
31. Three sum
32. Four sum
33. Max subarray (Kadane's algorithm)
34. Max product subarray
35. Min subarray (Kadane's variant)
36. Subarray with given sum
37. Subarray with 0 sum
38. Longest subarray with sum k
39. Merge two sorted arrays (in-place)
40. Merge intervals
41. Insert interval
42. Non-overlapping intervals
43. Meeting rooms I & II
44. Minimum platforms
45. Activity selection greedy
46. Fractional knapsack
47. 0-1 Knapsack basics
48. Partition equal subset sum
49. Count subsets with sum
50. Target sum (± assign)
51. Move zeros to end
52. Remove duplicates (sorted)
53. Remove duplicates (unsorted)
54. Remove element in-place
55. Dutch national flag

**Sorting & Searching (56–90)**
56. Sort 0s 1s 2s
57. Sort by parity
58. Sort by sign
59. Wiggle sort
60. Relative sort
61. Custom comparator sort
62. Sort structs
63. Stable sort vs unstable
64. Counting sort
65. Radix sort
66. Bucket sort
67. Majority element (Moore's Voting)
68. Majority element II
69. Find duplicate (Floyd's cycle)
70. Find missing number
71. Find two missing numbers
72. First missing positive
73. Single number (XOR)
74. Two singles (XOR)
75. Three singles
76. Maximum consecutive 1s
77. Minimum consecutive 0s
78. Longest consecutive sequence
79. Trapping rain water
80. Container with most water
81. Largest rectangle histogram
82. Maximal rectangle in matrix
83. Spiral order traversal
84. Rotate matrix 90°
85. Set matrix zeros
86. Search in 2D matrix
87. Search in sorted 2D matrix II
88. Diagonal traversal
89. Anti-diagonal traversal
90. Layer-by-layer traversal

**Prefix / Sliding Window / Stock Problems (91–130)**
91. Transpose matrix
92. Matrix multiplication
93. Prefix sum 1D
94. Prefix sum 2D (range sum query)
95. Difference array
96. Range update range query
97. Product array except self
98. Stock buy sell (one transaction)
99. Stock buy sell (multiple transactions)
100. Stock with cooldown
101. Stock with transaction fee
102. Best time to buy (k transactions)
103. Jump game I (can reach end?)
104. Jump game II (min jumps)
105. Gas station problem
106. Candy distribution
107. Task scheduler
108. Minimum cost to connect ropes
109. Check if array is a permutation
110. Find all anagrams in string
111. Longest substring no repeat
112. Longest substring k distinct
113. Minimum window substring
114. Substring permutation check
115. Sliding window maximum
116. Sliding window minimum
117. Count distinct in window
118. Average of subarrays size k
119. Substrings with exactly k distinct
120. Replace with rank
121. Minimum number of arrows (balloons)
122. Smallest range covering all lists
123. Minimum operations to make equal
124. Minimum swaps to sort
125. Check if array is a permutation
126. Count subarrays with bounded max
127. Longest turbulent subarray
128. Maximum sum circular subarray
129. Find pivot index
130. Sort colors in-place

---

## SUPPLEMENTARY PROBLEMS (from LeetCode / GeeksForGeeks / GitHub)

These are commonly asked problems at this level not in the original list:

### From LeetCode Easy (Level 0–1 aligned)
- Two Sum (#1)
- Palindrome Number (#9)
- Roman to Integer (#13)
- Longest Common Prefix (#14)
- Valid Parentheses (#20)
- Merge Two Sorted Lists (#21)
- Remove Duplicates from Sorted Array (#26)
- Remove Element (#27)
- Find the Index of the First Occurrence (#28)
- Plus One (#66)
- Add Binary (#67)
- Sqrt(x) (#69)
- Climbing Stairs (#70)
- Best Time to Buy and Sell Stock (#121)
- Valid Palindrome (#125)
- Missing Number (#268)
- Move Zeroes (#283)
- Reverse String (#344)
- Reverse Vowels of a String (#345)
- Intersection of Two Arrays (#349)
- Pascal's Triangle (#118)
- Pascal's Triangle II (#119)
- Contains Duplicate (#217)
- Majority Element (#169)
- Excel Sheet Column Number (#171)
- Happy Number (#202)
- Count Primes (#204)
- Reverse Bits (#190)
- Number of 1 Bits (#191)
- Reverse Linked List (#206)
- First Bad Version (#278)
- Word Pattern (#290)
- Nim Game (#292)
- Range Sum Query - Immutable (#303)
- Power of Two (#231)
- Fizz Buzz (#412)
- Ransom Note (#383)

### From GeeksForGeeks School / Basic
- Find the largest element in an array
- Second largest element in an array
- Check if array is sorted
- Reverse an array
- Count zeros in an array
- Sum of array elements
- Maximum and minimum in array
- Left rotate an array by d positions
- Leaders in an array
- Frequency of each element

### From HackerRank C++ Track
- Say "Hello, World!" With C++
- Input and Output
- Basic Data Types
- Conditional Statements
- For Loop
- While Loop
- Functions
- Pointer
- Array Introduction

---

## TEMPLATE FOR SELF-STUDY (fill one per problem)

```markdown
## Problem: {{NAME}}
**Date Studied:** ___________
**Source:** LeetCode / GFG / Custom

### My First Attempt (before looking at solution)
- My approach:
- My code:
- What went wrong:

### What I Learned
- Key concept:
- Pattern this belongs to:
- Similar to:

### Time to Solve Next Time
- [ ] Can solve without hints
- [ ] Need pattern hint
- [ ] Need to look up code
```

---

## LEARNING ROADMAP — Level 0 → Level 1

```
Week 1:  C00 (1–40)   → Programs 1–40: Setup, I/O, Compilation
Week 2:  C00 (41–80)  → Preprocessor, Debugging, Variables
Week 3:  C00 (81–120) → Functions basics, Scope, Namespaces
Week 4:  C01 (1–40)   → Types, Casting, Strings
Week 5:  C01 (41–110) → String ops, Storage classes, Type system
Week 6:  C10 (1–50)   → Control flow, Basic math problems
Week 7:  C10 (51–115) → String loops, Pattern problems
Week 8:  C11 (1–40)   → Functions deep dive, Lambdas
Week 9:  C11 (41–80)  → Recursion basics, Backtracking intro
Week 10: C11 (81–120) → Advanced recursion, Divide & Conquer
Week 11: C12 (1–55)   → Arrays, Two pointers, Sliding window
Week 12: C12 (56–130) → Sorting, Prefix sums, Stock problems
```

---

## RESOURCES

| Resource | Link | Best For |
|----------|------|----------|
| cppreference.com | https://en.cppreference.com | Definitive C++ reference |
| LeetCode | https://leetcode.com | Problem practice |
| GeeksForGeeks | https://geeksforgeeks.org | Concept + code |
| Codeforces | https://codeforces.com | Competitive problems |
| Compiler Explorer | https://godbolt.org | See assembly output |
| C++ Insights | https://cppinsights.io | See template expansion |
| learncpp.com | https://learncpp.com | Best free C++ tutorial |
| The Cherno YouTube | https://youtube.com/@TheCherno | Visual C++ explanations |
| Back To Basics (CppCon) | YouTube search "CppCon Back to Basics" | Deep fundamentals |
| GitHub: TheAlgorithms/C-Plus-Plus | https://github.com/TheAlgorithms/C-Plus-Plus | Algorithm implementations |
