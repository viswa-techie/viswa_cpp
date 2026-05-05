# Level 1 — Beginner: Control Flow, Functions & Arrays/Strings

> **Directory:** `Level_0_1_Beginner/`  
> **Categories:** `C10_Control_Flow_Loops` · `C11_Functions_Recursion` · `C12_Arrays_Strings_Core`  
> **Total Files:** 120 + 122 + 124 = **366 files**  
> **Prerequisite:** Level 0 (Syntax, Data Types)  
> **Leads to:** Level 2 (Pointers, OOP)

---

## Overview

Level 1 is where real problem-solving begins. You master the complete control vocabulary of C++, learn to structure code into reusable functions (including recursion), and tackle the most common interview data structure: arrays and strings. By the end, you can solve 60–70% of LeetCode Easy problems.

---

## C10 — Control Flow & Loops (120 files)

### What is Covered

| Range | Topics |
|-------|--------|
| 001–010 | `if`/`else if`/`else`, dangling-else, `switch`/`case`/`default`, fall-through, `[[fallthrough]]`, ternary `?:` |
| 011–020 | `while` loop, `do-while`, `for` loop (classic), range-based `for`, loop variable scope, infinite loops |
| 021–030 | `break`, `continue`, `goto` (and why to avoid it), nested loop control, label-based continue |
| 031–040 | FizzBuzz (canonical), factorial iterative, Fibonacci iterative, prime check, Sieve of Eratosthenes |
| 041–050 | GCD/LCM, digit extraction (sum/count/reverse digits), palindrome number, Armstrong number, perfect number |
| 051–060 | Number patterns: triangle, pyramid, diamond; star patterns; Floyd's triangle; Pascal's triangle (loop-based) |
| 061–070 | String iteration: character counting, vowel/consonant check, frequency map with array, anagram check |
| 071–080 | Parsing: integer from string (manual `atoi`), string splitting by delimiter, CSV parsing basics |
| 081–090 | Expression evaluation: shunting-yard concept, balanced parentheses check, bracket matching |
| 091–100 | Loop optimization: early exit, short-circuit evaluation, sentinel values, two-pointer pattern (intro) |
| 101–110 | Nested loops for matrix printing, spiral matrix traversal, zigzag patterns |
| 111–120 | Classic loop puzzles: collatz sequence, happy number, ugly number, count set bits, Roman numeral conversion |

### Key Concepts Learned
- Difference between `while` and `do-while` — when each is correct
- How range-based `for` works with arrays, strings, and containers
- Why `switch` is O(1) vs `if-else if` chain is O(n)
- Short-circuit evaluation: `&&` stops on first `false`, `||` on first `true`
- Loop invariants — how to reason about correctness

### Patterns Introduced
- **Sieve of Eratosthenes** — O(n log log n) prime generation
- **Digit decomposition** — `n % 10`, `n / 10` loop
- **Two-pointer (intro)** — palindrome check with two indices

---

## C11 — Functions & Recursion (122 files)

### What is Covered

| Range | Topics |
|-------|--------|
| 001–010 | Function declaration vs definition, return types, `void`, parameter passing (by value/reference/pointer), `const` ref |
| 011–020 | Default parameters, function overloading, name mangling, `inline` functions, `constexpr` functions |
| 021–030 | Function pointers: syntax, arrays of function pointers, callbacks; `std::function<>`, `std::bind` |
| 031–040 | Lambdas: capture by value/reference, mutable lambda, generic lambda (`auto` param), immediately-invoked lambda |
| 041–050 | Lambda captures: `[=]`, `[&]`, `[this]`, `[x=expr]`; recursive lambdas with `std::function`; `auto` return type |
| 051–060 | Recursion fundamentals: base case, recursive case, call stack visualisation; factorial, Fibonacci (naive vs memo) |
| 061–070 | Tower of Hanoi, permutations of a string, subsets/power set generation, combination sum |
| 071–080 | Backtracking: N-Queens, Sudoku solver, word search, generate parentheses, letter combinations |
| 081–090 | Divide & conquer: merge sort (recursive), quick sort (recursive + partition strategies), binary search (recursive) |
| 091–100 | Memoisation: top-down DP intro, fibonacci with `unordered_map`, coin change (recursive + memo) |
| 101–110 | Tail recursion, tail-call optimisation (compiler perspective), mutual recursion |
| 111–122 | Number theory functions: GCD (Euclidean), LCM, fast power `pow(base, exp, mod)`, Miller-Rabin primality (intro), sieve functions |

### Key Concepts Learned
- Stack frame per function call — why deep recursion causes stack overflow
- Pass-by-value copies; pass-by-reference is an alias
- Why `const T&` is the default for large objects
- Difference: function pointer vs `std::function` (type-erased) vs lambda
- Memoisation converts exponential to polynomial time

### Patterns Introduced
- **Backtracking template** — choose → explore → unchoose
- **Divide & conquer** — split, solve sub-problems, combine
- **Memoisation (top-down DP)** — cache recursive calls
- **Recursive descent** — parsing and tree generation

---

## C12 — Arrays & Strings Core (124 files)

### What is Covered

| Range | Topics |
|-------|--------|
| 001–010 | 1D C-array declaration, `std::array<T,N>`, `std::vector<T>` basics; `push_back`, `emplace_back`, `pop_back` |
| 011–020 | Array pitfalls: out-of-bounds, sizeof-in-function decay, VLAs; `at()` for bounds-checked access |
| 021–030 | 2D arrays, `std::vector<vector<T>>`, row/column iteration, matrix transpose, matrix multiplication |
| 031–040 | Linear search, binary search (iterative + recursive), `std::lower_bound`, `std::upper_bound`, `std::binary_search` |
| 041–050 | Two Sum (brute/hash map/two-pointer), Three Sum, Four Sum; pair existence patterns |
| 051–060 | Kadane's algorithm (max subarray sum), max/min subarray with indices, circular subarray max |
| 061–070 | Dutch National Flag (sort 0s/1s/2s), majority element (Boyer-Moore), rotate array, move zeros |
| 071–080 | Merge intervals, insert interval, non-overlapping intervals; sliding window (fixed & variable size) |
| 081–090 | Prefix sum 1D/2D, difference array, range sum query, range update in O(1) |
| 091–100 | Trapping rain water (two-pointer), best time to buy/sell stocks I/II/III, container with most water |
| 101–110 | String: reverse, palindrome check, anagram groups, longest substring without repeating chars, minimum window substring |
| 111–124 | Sorting: bubble, insertion, selection, merge, quick, counting, radix; `std::sort` with custom comparators; 0-1 Knapsack intro |

### Key Concepts Learned
- Why `std::vector` is preferred over C-arrays (size tracking, bounds checking, iterators)
- Binary search requires **sorted** input — always verify
- Two-pointer technique reduces O(n²) brute force to O(n)
- Sliding window avoids recomputing overlapping subarray values
- Prefix sum trades space for O(1) range queries

### Patterns Introduced
- **Two Pointers** — left/right converging, fast/slow
- **Sliding Window** — fixed vs variable size
- **Prefix Sum / Difference Array**
- **Kadane's Algorithm** — local vs global max
- **Boyer-Moore Voting** — linear-time majority element
- **Dutch National Flag** — 3-way partition

---

## Level 1 — Revision Checklist

### Control Flow
- [ ] Explain why `switch` needs `break` (fall-through by default)
- [ ] Use range-based `for` with index when needed (`enumerate` pattern)
- [ ] Write Sieve of Eratosthenes from memory
- [ ] Implement FizzBuzz in 3 different ways

### Functions & Recursion
- [ ] Write merge sort and quick sort from scratch
- [ ] Solve N-Queens with backtracking
- [ ] Use `std::function` to store a recursive lambda
- [ ] Explain when recursion causes stack overflow and how to prevent it

### Arrays & Strings
- [ ] Implement binary search with correct `left <= right` termination
- [ ] Solve Two Sum in O(n) with hash map
- [ ] Implement Kadane's algorithm with actual subarray indices
- [ ] Solve trapping rain water with two pointers
- [ ] Write merge sort and know its time/space complexity

## Common Mistakes at Level 1

| Mistake | Correct Approach |
|---------|-----------------|
| Binary search with `mid = (l+r)/2` | Use `mid = l + (r-l)/2` to avoid overflow |
| Infinite recursion — missing base case | Always define base case first |
| Modifying vector while iterating | Use index-based loop or erase idiom |
| `switch` without `break` | Add `break` or use `[[fallthrough]]` explicitly |
| Forgetting to sort before binary search | Always confirm precondition: array is sorted |
| Sliding window shrink loop missing | Use `while` not `if` to shrink window |

## Interview Focus (Level 1 Topics)

| Problem | Pattern | Complexity |
|---------|---------|------------|
| Two Sum | Hash Map | O(n) time, O(n) space |
| Max Subarray (Kadane's) | DP / Greedy | O(n) time, O(1) space |
| Trapping Rain Water | Two Pointers | O(n) time, O(1) space |
| Binary Search | Divide & Conquer | O(log n) |
| Merge Sort | Divide & Conquer | O(n log n) |
| N-Queens | Backtracking | O(n!) worst |
| Sliding Window Max | Deque | O(n) |
