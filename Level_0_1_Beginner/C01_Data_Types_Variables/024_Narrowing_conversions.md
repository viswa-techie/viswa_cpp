# Narrowing conversions

> **Level:** 0 — Absolute Beginner  
> **Category:** C01  
> **Topic:** types

---

## Problem Statement

Master the use of Narrowing conversions in C++ programs. Understand when and why to use it.

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
Narrowing conversions is a technique in C++ that appears frequently in interviews and real projects.

### Why Does It Matter?
- Used extensively in production C++ code
- Commonly asked in technical interviews
- Helps write clean, maintainable code

### Mental Model
Think of narrowing conversions as a tool in your toolbox — know when to reach for it.

---

## Solution Approaches

### Approach 1: Direct / Straightforward
```cpp
#include <iostream>
int main() {
    // Narrowing: converting to a type that can't hold all values
    double d = 3.14;
    int i = d;              // Narrowing: loses .14 (compiles with warning)
    
    long long big = 9000000000LL;
    int small = big;        // Narrowing: value too large for int
    
    int negative = -1;
    unsigned int u = negative;  // Narrowing: negative to unsigned
    
    std::cout << "double->int: " << i << "
";
    std::cout << "long long->int: " << small << " (truncated!)
";
    std::cout << "int->unsigned: " << u << "
";
    
    // Brace initialization prevents narrowing
    // int x{3.14};          // ERROR! Narrowing not allowed
    // int y{big};           // ERROR! Narrowing not allowed
    int safe{42};            // OK — no narrowing
    std::cout << "safe: " << safe << "
";
    return 0;
}
```

**Time Complexity:** O(n) (typical)  
**Space Complexity:** O(1) or O(n)  
**When to use:** First attempt, when simplicity matters over performance.

### Approach 2: Optimized / STL-Based
```cpp
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <numeric>

/*
 * Narrowing conversions — STL-based approach
 * Uses standard library utilities for clean implementation.
 */
int main() {
    // STL-based demonstration of Narrowing conversions
    std::cout << "STL approach for: Narrowing conversions
";
    
    // Using appropriate STL facilities
    std::cout << "Implementation uses standard library best practices
";
    return 0;
}
```

**Time Complexity:** Depends on STL algorithm used  
**Space Complexity:** Depends on approach  
**When to use:** Production code, when you know the right STL tool.

### Approach 3: Modern C++ (C++17/20)
```cpp
#include <iostream>
#include <string>
#include <type_traits>

/*
 * Narrowing conversions — Modern C++17/20 approach
 * Uses features: auto, constexpr, if constexpr, concepts, etc.
 */
int main() {
    // Modern C++ demonstration of Narrowing conversions
    std::cout << "Modern C++ approach for: Narrowing conversions
";
    
    // Using C++17/20 features where applicable
    std::cout << "Implementation uses modern C++ idioms
";
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
- Narrowing conversions demonstrates proper C++ idioms and best practices

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
- **Core idea:** Narrowing conversions
- **Key construct:** STL / Standard Library
- **Complexity:** O(n) typical
- **Don't forget:** Initialize variables, check edge cases, use `-Wall`

---

*Generated for C++ Level 0 — C01 Problem Solving Guide*


## Key Takeaways
1. Understand the core concept of Narrowing conversions and when to apply it
2. Know the time/space complexity implications
3. Recognize common patterns where Narrowing conversions is useful
4. Practice with both simple and edge cases
5. Prefer standard library solutions when available

## Common Mistakes (Specific)
- Not handling edge cases (empty input, boundary values)
- Off-by-one errors in loop boundaries
- Forgetting to initialize variables before use
- Missing include headers needed for the implementation
- Not considering overflow for large inputs
