# INT_MAX / INT_MIN constants

> **Level:** 0 — Absolute Beginner  
> **Category:** C01  
> **Topic:** types

---

## Problem Statement

Master the use of INT_MAX / INT_MIN constants in C++ programs. Understand when and why to use it.

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
INT_MAX / INT_MIN constants is a technique in C++ that appears frequently in interviews and real projects.

### Why Does It Matter?
- Used extensively in production C++ code
- Commonly asked in technical interviews
- Helps write clean, maintainable code

### Mental Model
Think of int_max / int_min constants as a tool in your toolbox — know when to reach for it.

---

## Solution Approaches

### Approach 1: Direct / Straightforward
```cpp
#include <iostream>
#include <climits>
int main() {
    std::cout << "INT_MAX = " << INT_MAX << "
";   // 2147483647
    std::cout << "INT_MIN = " << INT_MIN << "
";   // -2147483648
    std::cout << "UINT_MAX = " << UINT_MAX << "
"; // 4294967295
    std::cout << "SHRT_MAX = " << SHRT_MAX << "
"; // 32767
    std::cout << "LLONG_MAX = " << LLONG_MAX << "
";
    std::cout << "CHAR_MAX = " << CHAR_MAX << "
";

    // Overflow check
    int x = INT_MAX;
    std::cout << "INT_MAX + 1 = UB (signed overflow)
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
    // Preferred C++ way: std::numeric_limits
    std::cout << "int max: " << std::numeric_limits<int>::max() << "
";
    std::cout << "int min: " << std::numeric_limits<int>::min() << "
";
    std::cout << "int lowest: " << std::numeric_limits<int>::lowest() << "
";
    std::cout << "uint max: " << std::numeric_limits<unsigned>::max() << "
";
    std::cout << "digits: " << std::numeric_limits<int>::digits << " bits
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
#include <limits>
#include <type_traits>
template<typename T>
void showLimits(const char* name) {
    std::cout << name << ": [" << std::numeric_limits<T>::lowest()
              << ", " << std::numeric_limits<T>::max() << "]
";
}
int main() {
    showLimits<short>("short");
    showLimits<int>("int");
    showLimits<long>("long");
    showLimits<long long>("long long");
    showLimits<unsigned>("unsigned");
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
- INT_MAX / INT_MIN constants demonstrates proper C++ idioms and best practices

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
- **Core idea:** INT_MAX / INT_MIN constants
- **Key construct:** STL / Standard Library
- **Complexity:** O(n) typical
- **Don't forget:** Initialize variables, check edge cases, use `-Wall`

---

*Generated for C++ Level 0 — C01 Problem Solving Guide*


## Key Takeaways
1. `<climits>` provides INT_MAX, INT_MIN, UINT_MAX etc. (C-style macros)
2. `<limits>` provides `std::numeric_limits<T>::max()/min()` (C++ way, preferred)
3. INT_MAX is typically 2,147,483,647 (2^31 - 1)
4. Use these to check for overflow before arithmetic
5. `lowest()` vs `min()`: for floats, min() is smallest positive, lowest() is most negative

## Common Mistakes (Specific)
- Using INT_MAX + 1 → undefined behavior (signed overflow)
- Confusing `numeric_limits<float>::min()` (smallest positive) with `lowest()` (most negative)
- Not including `<climits>` or `<limits>` → compilation error
