# Signed overflow UB

> **Level:** 0 — Absolute Beginner  
> **Category:** C01  
> **Topic:** types

---

## Problem Statement

Master the use of Signed overflow UB in C++ programs. Understand when and why to use it.

### Examples
- **Input Example 1:** A typical/simple case
- **Input Example 2:** An edge case (empty input, boundary values)
- **Input Example 3:** A larger or tricky case

---

## Prerequisites
- Basic C++ syntax (variables, types, operators)
- Standard I/O operations
- Header files and namespaces

---

## Core Concept

### What Is It?
Signed overflow UB is a technique in C++ that appears frequently in interviews and real projects.

### Why Does It Matter?
- Used extensively in production C++ code
- Commonly asked in technical interviews
- Helps write clean, maintainable code

### Mental Model
Think of signed overflow ub as a tool in your toolbox — know when to reach for it.

---

## Solution Approaches

### Approach 1: Direct / Straightforward
```cpp
#include <iostream>
#include <climits>
int main() {
    int x = INT_MAX;
    std::cout << "INT_MAX = " << x << "";

    // UNDEFINED BEHAVIOR! Signed overflow has no guaranteed result
    // x + 1 could be anything — compiler can assume it never happens
    // x++;  // DON'T DO THIS

    // Safe overflow check BEFORE operation
    int a = 2000000000, b = 1000000000;
    if (a > INT_MAX - b)
        std::cout << "Addition would overflow!";
    else
        std::cout << "Safe: " << a + b << "";
    return 0;
}
```

**Time Complexity:** O(n) (typical)  
**Space Complexity:** O(1) or O(n)  
**When to use:** First attempt, when simplicity matters over performance.

### Approach 2: Optimized / STL-Based
```cpp
#include <iostream>
#include <limits>
int main() {
    // Why signed overflow is UB matters:
    // The compiler ASSUMES it never happens and optimizes accordingly
    // Example: compiler may optimize (x + 1 > x) to always true
    
    int x = std::numeric_limits<int>::max();
    // Compiler may assume x+1 > x is always true!
    // With UB, anything can happen
    
    // Safe multiplication check
    int a = 50000, b = 50000;
    long long product = static_cast<long long>(a) * b;
    if (product > std::numeric_limits<int>::max())
        std::cout << "Overflow! Result: " << product << "";
    else
        std::cout << "Safe: " << static_cast<int>(product) << "";
    return 0;
}
```

**Time Complexity:** Depends on STL algorithm used  
**Space Complexity:** Depends on approach  
**When to use:** Production code, when you know the right STL tool.

### Approach 3: Modern C++ (C++17/20)
```cpp
#include <iostream>
#include <cstdint>
// C++20: could use std::add_overflow if available
// GCC/Clang built-in:
int main() {
    int a = 2000000000, b = 1000000000;
    int result;
    
    #if defined(__GNUC__) || defined(__clang__)
    if (__builtin_add_overflow(a, b, &result))
        std::cout << "Overflow detected!";
    else
        std::cout << "Result: " << result << "";
    #endif

    // Alternative: use wider type
    int64_t safe = static_cast<int64_t>(a) + b;
    std::cout << "Safe (int64): " << safe << "";
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
- Signed overflow UB demonstrates proper C++ idioms and best practices

### Interview Tips
- Discuss tradeoffs between approaches
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

**Pattern:** Implementation pattern — combine concepts to build

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
- **Core idea:** Signed overflow UB
- **Key construct:** STL / Standard Library
- **Complexity:** O(n) typical
- **Don't forget:** Initialize variables, check edge cases, use `-Wall`

---

*Generated for C++ Level 0 — C01 Problem Solving Guide*


## Key Takeaways
1. Signed integer overflow is UNDEFINED BEHAVIOR in C++
2. The compiler assumes it never happens — enables aggressive optimizations
3. Check BEFORE performing arithmetic: `if (a > INT_MAX - b)`
4. Use `__builtin_add_overflow` (GCC/Clang) for safe checked arithmetic
5. Cast to wider type before operation: `(long long)a * b`

## Common Mistakes (Specific)
- Assuming signed overflow wraps like unsigned — it's UB, anything can happen
- Compiler may optimize away your overflow checks due to UB assumptions
- Testing for overflow AFTER the operation — too late, UB already occurred
- Using `-fwrapv` flag makes it defined but non-portable
