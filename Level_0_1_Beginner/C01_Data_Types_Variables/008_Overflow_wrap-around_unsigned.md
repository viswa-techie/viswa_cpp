# Overflow wrap-around (unsigned)

> **Level:** 0 — Absolute Beginner  
> **Category:** C01  
> **Topic:** types

---

## Problem Statement

Master the use of Overflow wrap-around (unsigned) in C++ programs. Understand when and why to use it.

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
Overflow wrap-around (unsigned) is a technique in C++ that appears frequently in interviews and real projects.

### Why Does It Matter?
- Used extensively in production C++ code
- Commonly asked in technical interviews
- Helps write clean, maintainable code

### Mental Model
Think of overflow wrap-around (unsigned) as a tool in your toolbox — know when to reach for it.

---

## Solution Approaches

### Approach 1: Direct / Straightforward
```cpp
#include <iostream>
#include <climits>
int main() {
    unsigned int u = 0;
    u--;  // Well-defined: wraps to UINT_MAX
    std::cout << "0u - 1 = " << u << "";  // 4294967295

    unsigned int max = UINT_MAX;
    max++;  // Well-defined: wraps to 0
    std::cout << "UINT_MAX + 1 = " << max << "";  // 0

    // Modular arithmetic
    unsigned int a = 4294967290U;
    unsigned int b = a + 10;  // wraps: (4294967290 + 10) mod 2^32 = 4
    std::cout << "4294967290 + 10 = " << b << "";
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
int main() {
    // Common bug: unsigned subtraction in loop
    std::vector<int> v = {1, 2, 3};
    // BAD: if v is empty, v.size()-1 wraps to huge number!
    // for (size_t i = 0; i <= v.size() - 1; ++i)  // BUG if empty

    // SAFE approach:
    for (size_t i = 0; i < v.size(); ++i)
        std::cout << v[i] << " ";
    std::cout << "";

    // SAFE reverse loop with unsigned
    for (size_t i = v.size(); i-- > 0; )
        std::cout << v[i] << " ";
    std::cout << "";
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
int main() {
    // Demonstrate wrap behavior with different widths
    uint8_t byte = 255;
    byte++;
    std::cout << "uint8_t 255+1 = " << +byte << "";  // 0

    uint16_t word = 65535;
    word++;
    std::cout << "uint16_t 65535+1 = " << word << "";  // 0

    // Detecting overflow before it happens
    uint32_t a = 4000000000U, b = 1000000000U;
    if (a > UINT32_MAX - b)
        std::cout << "Addition would overflow!";
    else
        std::cout << "Safe: " << a + b << "";
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
- Overflow wrap-around (unsigned) demonstrates proper C++ idioms and best practices

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
- **Core idea:** Overflow wrap-around (unsigned)
- **Key construct:** STL / Standard Library
- **Complexity:** O(n) typical
- **Don't forget:** Initialize variables, check edge cases, use `-Wall`

---

*Generated for C++ Level 0 — C01 Problem Solving Guide*


## Key Takeaways
1. Unsigned overflow is WELL-DEFINED — wraps modulo 2^N
2. `0u - 1` = UINT_MAX (wraps around)
3. This is unlike signed overflow which is undefined behavior
4. Common trap: `vector.size() - 1` when vector is empty
5. Check for overflow BEFORE performing the operation

## Common Mistakes (Specific)
- Using unsigned loop counter decrementing past 0 → infinite loop
- `size() - 1` on empty container → wraps to enormous value
- Assuming unsigned can be negative — it can't, it wraps instead
