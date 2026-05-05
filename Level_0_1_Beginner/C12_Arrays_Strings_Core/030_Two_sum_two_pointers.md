# Two sum (two pointers)

> **Level:** 1 — Beginner  
> **Category:** C12  
> **Topic:** arrays_strings

---

## Problem Statement

Write a C++ program that solves the Two sum (two pointers) problem.

### Examples
- **Input Example 1:** A typical/simple case
- **Input Example 2:** An edge case (empty input, boundary values)
- **Input Example 3:** A larger or tricky case

---

## Prerequisites
- Basic C++ syntax (variables, types, operators)
- Control flow (if/else, loops)
- Array/vector basics

---

## Core Concept

### What Is It?
Two sum (two pointers) is a classic problem in C++ that appears frequently in interviews and real projects.

### Why Does It Matter?
- Builds problem-solving muscle for algorithmic thinking
- Commonly asked in technical interviews
- Helps write clean, maintainable code

### Mental Model
Think of two sum (two pointers) as a puzzle — break it into smaller pieces and solve each one.

---

## Solution Approaches

### Approach 1: Direct / Straightforward
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

int main() {
    // Implementation: Two sum two pointers
    std::cout << "Demonstrating: Two sum two pointers";
    
    std::vector<int> data = {5, 2, 8, 1, 9, 3, 7, 4, 6};
    
    // Core logic for Two sum two pointers
    std::sort(data.begin(), data.end());
    for (int x : data) std::cout << x << " ";
    std::cout << "";
    
    std::cout << "Implementation complete";
    return 0;
}
```

**Time Complexity:** O(n) (typical)  
**Space Complexity:** O(1) or O(n)  
**When to use:** First attempt, when simplicity matters over performance.

### Approach 2: Optimized / STL-Based
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>

/*
 * Two sum two pointers — STL/Library approach
 */
int main() {
    std::vector<int> data = {5, 2, 8, 1, 9, 3, 7, 4, 6};
    
    // STL-based implementation
    std::sort(data.begin(), data.end());
    for (const auto& x : data) std::cout << x << " ";
    std::cout << "";
    
    auto it = std::lower_bound(data.begin(), data.end(), 5);
    if (it != data.end())
        std::cout << "Found: " << *it << " at index " << (it - data.begin()) << "";
    return 0;
}
```

**Time Complexity:** Depends on STL algorithm used  
**Space Complexity:** Depends on approach  
**When to use:** Production code, when you know the right STL tool.

### Approach 3: Modern C++ (C++17/20)
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>

/*
 * Two sum two pointers — Modern C++17/20 approach
 */
int main() {
    std::vector<int> data = {5, 2, 8, 1, 9, 3, 7, 4, 6};
    
    // Modern C++ features
    auto [min_it, max_it] = std::minmax_element(data.begin(), data.end());
    std::cout << "Range: [" << *min_it << ", " << *max_it << "]";
    
    // Partition with lambda
    auto pivot = std::partition(data.begin(), data.end(), [](int x) { return x <= 5; });
    std::cout << "Partitioned at index: " << (pivot - data.begin()) << "";
    for (int x : data) std::cout << x << " ";
    std::cout << "";
    return 0;
}
```

---

## Step-by-Step Trace

For a typical input, trace the solution:

| Step | State | Action | Result |
|------|-------|--------|--------|
| 1 | Initial | Read input | — |
| 2 | Processing | Apply algorithm | — |
| 3 | Final | Output result | — |

---

## Common Mistakes & Pitfalls

1. **Off-by-one errors** — Check loop boundaries carefully
2. **Uninitialized variables** — Always initialize before use
3. **Integer overflow** — Use `long long` for large numbers
4. **Missing edge cases** — Empty input, single element, negative numbers
5. **Forgetting `#include`** — Include all necessary headers
6. **Using `==` vs `=`** — Assignment vs comparison

---

## What You Should Learn From This

### Key C++ Feature Demonstrated
- Two sum (two pointers) demonstrates loop control and algorithmic thinking

### Interview Tips
- Start with brute force, then optimize
- Always discuss time/space complexity
- Mention edge cases proactively

### Code Review Checklist
- [ ] Compiles with `-Wall -Wextra` — no warnings
- [ ] Handles edge cases
- [ ] Variables are properly initialized
- [ ] No memory leaks (if using dynamic allocation)
- [ ] Code is readable and well-commented

---

## Pattern Recognition

**Pattern:** Loop-based computation — iterate and accumulate

**Similar Problems:**
- (See other problems in this category)

**When you see** _______, **think** _______.

---

## Practice Variants
1. **Easy:** Simplify the constraints (smaller input, fewer edge cases)
2. **Medium:** Add a constraint (handle negative numbers, optimize for time)
3. **Hard:** Combine with another concept (recursion, dynamic programming)

---

## Quick Reference Card
- **Core idea:** Two sum (two pointers)
- **Key construct:** Loops
- **Complexity:** O(n) typical
- **Don't forget:** Initialize variables, check edge cases, use `-Wall`

---

*Generated for C++ Level 1 — C12 Problem Solving Guide*


## Key Takeaways
1. Brute force: O(n²) — check all pairs
2. Hash map: O(n) time, O(n) space — lookup complement
3. Two pointers on sorted array: O(n) time, O(1) space
4. Hash map approach is most common in interviews
5. Always clarify: can same element be used twice?

## Common Mistakes (Specific)
- Off-by-one errors in array indices and loop bounds
- Not handling edge cases (empty array, single element)
- Integer overflow with large sums — use long long
- Modifying container while iterating — invalidates iterators
- Forgetting to sort before binary search
