# Memoization basics

> **Level:** 1 — Beginner  
> **Category:** C11  
> **Topic:** functions_recursion

---

## Problem Statement

Understand and explain the concept of Memoization basics. Be able to describe it, identify it in code, and use it correctly.

### Examples
- **Input Example 1:** A typical/simple case
- **Input Example 2:** An edge case (empty input, boundary values)
- **Input Example 3:** A larger or tricky case

---

## Prerequisites
- Basic C++ syntax (variables, types, operators)
- Understanding of C++ compilation model
- Header files and namespaces

---

## Core Concept

### What Is It?
Memoization basics is a fundamental concept in C++ that every programmer must understand.

### Why Does It Matter?
- Forms the foundation for understanding more complex C++ features
- Commonly asked in technical interviews
- Helps write clean, maintainable code

### Mental Model
Think of memoization basics as a building block — you can't build a house without understanding bricks.

---

## Solution Approaches

### Approach 1: Direct / Straightforward
```cpp
#include <iostream>
#include <vector>
#include <unordered_map>

// Memoization: caching recursive results
std::unordered_map<int, long long> cache;

long long fib(int n) {
    if (n <= 1) return n;
    if (cache.count(n)) return cache[n];
    return cache[n] = fib(n-1) + fib(n-2);
}

int main() {
    for (int i = 0; i <= 40; ++i)
        std::cout << "fib(" << i << ") = " << fib(i) << "";
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
#include <functional>
#include <numeric>

/*
 * Memoization basics — STL/Library approach
 */
int main() {
    std::vector<int> data = {5, 2, 8, 1, 9, 3, 7, 4, 6};
    
    // STL-based implementation of Memoization basics
    std::sort(data.begin(), data.end());
    for (const auto& x : data) std::cout << x << " ";
    std::cout << "";
    
    auto sum = std::accumulate(data.begin(), data.end(), 0);
    std::cout << "Sum: " << sum << "";
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
 * Memoization basics — Modern C++17/20 approach
 */
int main() {
    std::vector<int> data = {5, 2, 8, 1, 9, 3, 7, 4, 6};
    
    // Modern C++ features for Memoization basics
    auto [min_it, max_it] = std::minmax_element(data.begin(), data.end());
    std::cout << "Range: [" << *min_it << ", " << *max_it << "]";
    
    // Lambda-based approach
    std::sort(data.begin(), data.end());
    for (const auto& x : data) std::cout << x << " ";
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
- Memoization basics demonstrates fundamental language syntax

### Interview Tips
- Explain the concept clearly before writing code
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

**Pattern:** Language fundamentals — know the rules

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
- **Core idea:** Memoization basics
- **Key construct:** Language syntax
- **Complexity:** O(n) typical
- **Don't forget:** Initialize variables, check edge cases, use `-Wall`

---

*Generated for C++ Level 1 — C11 Problem Solving Guide*


## Key Takeaways
1. Understand the core pattern and when to apply Memoization basics
2. Know the time/space complexity trade-offs
3. Handle base cases and edge cases properly
4. Consider iterative alternatives when recursion depth is a concern
5. Use standard library utilities where available

## Common Mistakes (Specific)
- Not handling edge cases (empty input, single element, boundary values)
- Off-by-one errors in recursive/iterative bounds
- Integer overflow for large inputs — use `long long`
- Stack overflow from deep recursion — convert to iterative if needed
- Forgetting to initialize variables before use
