# unsigned types

> **Level:** 0 — Absolute Beginner  
> **Category:** C01  
> **Topic:** types

---

## Problem Statement

Master the use of unsigned types in C++ programs. Understand when and why to use it.

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
unsigned types is a technique in C++ that appears frequently in interviews and real projects.

### Why Does It Matter?
- Used extensively in production C++ code
- Commonly asked in technical interviews
- Helps write clean, maintainable code

### Mental Model
Think of unsigned types as a tool in your toolbox — know when to reach for it.

---

## Solution Approaches

### Approach 1: Direct / Straightforward
```cpp
#include <iostream>
int main() {
    unsigned int ui = 4294967295U;    // Max for 32-bit unsigned
    unsigned short us = 65535;
    unsigned long ul = 4294967295UL;
    unsigned long long ull = 18446744073709551615ULL;

    std::cout << "unsigned int: " << ui << " (size: " << sizeof(ui) << ")";
    std::cout << "unsigned short: " << us << " (size: " << sizeof(us) << ")";
    std::cout << "unsigned long: " << ul << " (size: " << sizeof(ul) << ")";
    std::cout << "unsigned long long: " << ull << " (size: " << sizeof(ull) << ")";

    // Wrap-around (defined behavior for unsigned)
    unsigned int zero = 0;
    zero--;  // Wraps to UINT_MAX
    std::cout << "0 - 1 = " << zero << "";
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
    std::cout << "unsigned int max: " << std::numeric_limits<unsigned int>::max() << "";
    std::cout << "unsigned long long max: " << std::numeric_limits<unsigned long long>::max() << "";
    std::cout << "size_t max: " << std::numeric_limits<size_t>::max() << "";

    // size_t is unsigned — used for sizes and indices
    std::string s = "hello";
    for (size_t i = 0; i < s.size(); ++i)
        std::cout << s[i];
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
#include <vector>

int main() {
    // Modern: fixed-width unsigned types
    uint8_t byte = 255;
    uint16_t word = 65535;
    uint32_t dword = 4294967295U;
    uint64_t qword = 18446744073709551615ULL;

    std::cout << "uint8_t: " << +byte << "";  // + promotes to int for printing
    std::cout << "uint32_t: " << dword << "";

    // Correct loop with unsigned (avoid underflow)
    std::vector<int> v = {1, 2, 3};
    for (auto i = v.size(); i-- > 0; )
        std::cout << v[i] << " ";
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
- unsigned types demonstrates proper C++ idioms and best practices

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
- **Core idea:** unsigned types
- **Key construct:** STL / Standard Library
- **Complexity:** O(n) typical
- **Don't forget:** Initialize variables, check edge cases, use `-Wall`

---

*Generated for C++ Level 0 — C01 Problem Solving Guide*


## Key Takeaways
1. Unsigned types can't be negative — wrap around from 0 to MAX
2. `unsigned int` has double the positive range vs `int`
3. `size_t` is an unsigned type used for sizes and array indices
4. Unsigned overflow is well-defined (wraps), unlike signed overflow (UB)
5. Use `uint8_t`, `uint32_t` etc. from `<cstdint>` for exact widths

## Common Mistakes (Specific)
- Subtracting from 0 with unsigned → wraps to huge number, not -1
- Mixing signed and unsigned in comparisons → implicit conversion bugs
- `for(unsigned i = n-1; i >= 0; i--)` is an infinite loop (never < 0)
- Using `unsigned` just because a value "shouldn't be negative" — causes subtle bugs
