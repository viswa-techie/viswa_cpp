# short, long, long long

> **Level:** 0 — Absolute Beginner  
> **Category:** C01  
> **Topic:** types

---

## Problem Statement

Master the use of short, long, long long in C++ programs. Understand when and why to use it.

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
short, long, long long is a technique in C++ that appears frequently in interviews and real projects.

### Why Does It Matter?
- Used extensively in production C++ code
- Commonly asked in technical interviews
- Helps write clean, maintainable code

### Mental Model
Think of short, long, long long as a tool in your toolbox — know when to reach for it.

---

## Solution Approaches

### Approach 1: Direct / Straightforward
```cpp
#include <iostream>
int main() {
    short s = 32767;           // Typically 2 bytes
    long l = 2147483647L;      // At least 4 bytes
    long long ll = 9223372036854775807LL;  // At least 8 bytes

    std::cout << "short: " << s << " (size: " << sizeof(short) << ")
";
    std::cout << "long: " << l << " (size: " << sizeof(long) << ")
";
    std::cout << "long long: " << ll << " (size: " << sizeof(long long) << ")
";

    // Overflow demo
    short overflow = 32767;
    overflow++;  // UB for signed, but typically wraps to -32768
    std::cout << "short overflow: " << overflow << "
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
#include <limits>

int main() {
    std::cout << "short range: [" << std::numeric_limits<short>::min()
              << ", " << std::numeric_limits<short>::max() << "]
";
    std::cout << "long range: [" << std::numeric_limits<long>::min()
              << ", " << std::numeric_limits<long>::max() << "]
";
    std::cout << "long long range: [" << std::numeric_limits<long long>::min()
              << ", " << std::numeric_limits<long long>::max() << "]
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
#include <cstdint>

int main() {
    // Modern C++: prefer fixed-width types for clarity
    int16_t s = 32767;       // Exactly 16 bits
    int32_t i = 2147483647;  // Exactly 32 bits
    int64_t ll = 9223372036854775807LL;  // Exactly 64 bits

    std::cout << "int16_t max: " << s << "
";
    std::cout << "int32_t max: " << i << "
";
    std::cout << "int64_t max: " << ll << "
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
- short, long, long long demonstrates proper C++ idioms and best practices

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
- **Core idea:** short, long, long long
- **Key construct:** STL / Standard Library
- **Complexity:** O(n) typical
- **Don't forget:** Initialize variables, check edge cases, use `-Wall`

---

*Generated for C++ Level 0 — C01 Problem Solving Guide*


## Key Takeaways
1. `short` ≥ 16 bits, `long` ≥ 32 bits, `long long` ≥ 64 bits
2. Use `long long` when values exceed ~2 billion (INT_MAX)
3. Suffix literals: `L` for long, `LL` for long long
4. Prefer `<cstdint>` fixed-width types (`int32_t`, `int64_t`) for portability
5. Size guarantees are minimums — actual sizes vary by platform

## Common Mistakes (Specific)
- Forgetting `LL` suffix on large literals — treated as `int` and may overflow
- Assuming `long` is 8 bytes — it's 4 bytes on Windows 64-bit
- Using `short` for micro-optimization — rarely saves anything due to alignment
