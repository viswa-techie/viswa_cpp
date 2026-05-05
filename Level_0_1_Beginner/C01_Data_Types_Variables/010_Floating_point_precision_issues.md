# Floating point precision issues

> **Level:** 0 — Absolute Beginner  
> **Category:** C01  
> **Topic:** types

---

## Problem Statement

Master the use of Floating point precision issues in C++ programs. Understand when and why to use it.

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
Floating point precision issues is a technique in C++ that appears frequently in interviews and real projects.

### Why Does It Matter?
- Used extensively in production C++ code
- Commonly asked in technical interviews
- Helps write clean, maintainable code

### Mental Model
Think of floating point precision issues as a tool in your toolbox — know when to reach for it.

---

## Solution Approaches

### Approach 1: Direct / Straightforward
```cpp
#include <iostream>
#include <iomanip>
int main() {
    // The classic: 0.1 + 0.2 != 0.3
    double a = 0.1 + 0.2;
    double b = 0.3;
    std::cout << std::setprecision(20);
    std::cout << "0.1 + 0.2 = " << a << "
";
    std::cout << "0.3       = " << b << "
";
    std::cout << "Equal? " << (a == b) << "
";  // 0 (false!)
    std::cout << "Difference: " << (a - b) << "
";

    // Loss of precision with large + small
    float big = 1000000.0f;
    float small_val = 0.001f;
    float sum = big + small_val;
    std::cout << "1000000 + 0.001 = " << sum << "
";  // 1000000 (small lost!)
    return 0;
}
```

**Time Complexity:** O(n) (typical)  
**Space Complexity:** O(1) or O(n)  
**When to use:** First attempt, when simplicity matters over performance.

### Approach 2: Optimized / STL-Based
```cpp
#include <iostream>
#include <cmath>
#include <limits>
int main() {
    // Epsilon-based comparison
    double a = 0.1 + 0.2;
    double b = 0.3;
    double eps = std::numeric_limits<double>::epsilon();

    // Absolute comparison (for values near zero)
    bool eq1 = std::abs(a - b) < eps * 100;
    std::cout << "Absolute compare: " << std::boolalpha << eq1 << "
";

    // Relative comparison (for larger values)
    auto relEqual = [](double x, double y, double tol = 1e-9) {
        return std::abs(x - y) <= tol * std::max(std::abs(x), std::abs(y));
    };
    std::cout << "Relative compare: " << relEqual(a, b) << "
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
#include <iomanip>
#include <cmath>
int main() {
    // Catastrophic cancellation
    double x = 1e15;
    double y = x + 1.0;
    std::cout << "(1e15 + 1) - 1e15 = " << (y - x) << "
";  // May be 0 or 1!

    // Summation order matters (Kahan summation)
    float naive_sum = 0.0f;
    for (int i = 0; i < 1000000; ++i)
        naive_sum += 0.1f;
    std::cout << "Naive sum of 0.1 * 1M: " << naive_sum << "
";

    // Kahan compensated summation
    float kahan_sum = 0.0f, c = 0.0f;
    for (int i = 0; i < 1000000; ++i) {
        float y2 = 0.1f - c;
        float t = kahan_sum + y2;
        c = (t - kahan_sum) - y2;
        kahan_sum = t;
    }
    std::cout << "Kahan sum of 0.1 * 1M: " << kahan_sum << "
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
- Floating point precision issues demonstrates proper C++ idioms and best practices

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
- **Core idea:** Floating point precision issues
- **Key construct:** STL / Standard Library
- **Complexity:** O(n) typical
- **Don't forget:** Initialize variables, check edge cases, use `-Wall`

---

*Generated for C++ Level 0 — C01 Problem Solving Guide*


## Key Takeaways
1. Most decimals (0.1, 0.2) cannot be represented exactly in binary floating-point
2. NEVER use `==` to compare floats — use epsilon-based comparison
3. Adding small numbers to large numbers loses the small value
4. Subtraction of nearly-equal values causes catastrophic cancellation
5. Summation order matters — Kahan summation reduces accumulated error

## Common Mistakes (Specific)
- Using `==` to compare floating-point numbers
- Assuming `0.1 + 0.2 == 0.3` → it's false
- Accumulating many small floats without compensation → drift
- Using `float` when `double` precision is needed
