# signed vs unsigned

> **Level:** 0 — Absolute Beginner  
> **Category:** C01  
> **Topic:** types

---

## Problem Statement

Master the use of signed vs unsigned in C++ programs. Understand when and why to use it.

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
signed vs unsigned is a technique in C++ that appears frequently in interviews and real projects.

### Why Does It Matter?
- Used extensively in production C++ code
- Commonly asked in technical interviews
- Helps write clean, maintainable code

### Mental Model
Think of signed vs unsigned as a tool in your toolbox — know when to reach for it.

---

## Solution Approaches

### Approach 1: Direct / Straightforward
```cpp
#include <iostream>
int main() {
    int s = -1;
    unsigned int u = 1;

    // Dangerous comparison: signed vs unsigned
    if (s < u) {
        std::cout << "-1 < 1: Expected!
";
    } else {
        std::cout << "-1 >= 1: Surprise! (signed converted to unsigned)
";
    }
    // s is converted to unsigned: -1 becomes 4294967295, which > 1

    // Safe: cast explicitly
    if (s < static_cast<int>(u)) {
        std::cout << "Correct comparison with cast
";
    }
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

int main() {
    std::vector<int> v = {5, 3, 8, 1};

    // v.size() is size_t (unsigned) — careful with subtraction
    int target = 2;
    // BAD: if v.size() < target, v.size() - target wraps!
    // GOOD: compare first
    if (static_cast<int>(v.size()) > target)
        std::cout << "Safe to subtract
";

    // STL uses unsigned (size_t) everywhere
    for (std::vector<int>::size_type i = 0; i < v.size(); ++i)
        std::cout << v[i] << " ";
    std::cout << "
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
#include <compare>

int main() {
    int32_t signed_val = -5;
    uint32_t unsigned_val = 10;

    // C++20: std::cmp_less handles mixed sign correctly
    #if __cplusplus >= 202002L
    if (std::cmp_less(signed_val, unsigned_val))
        std::cout << "-5 < 10: Correct with cmp_less!
";
    #endif

    // Pre-C++20 safe comparison
    auto safe_less = [](auto a, auto b) -> bool {
        if constexpr (std::is_signed_v<decltype(a)> && std::is_unsigned_v<decltype(b)>)
            return a < 0 || static_cast<std::make_unsigned_t<decltype(a)>>(a) < b;
        else
            return a < b;
    };
    std::cout << safe_less(signed_val, unsigned_val) << "
";  // 1
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
- signed vs unsigned demonstrates proper C++ idioms and best practices

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
- **Core idea:** signed vs unsigned
- **Key construct:** STL / Standard Library
- **Complexity:** O(n) typical
- **Don't forget:** Initialize variables, check edge cases, use `-Wall`

---

*Generated for C++ Level 0 — C01 Problem Solving Guide*


## Key Takeaways
1. Comparing signed with unsigned triggers implicit conversion — signed becomes unsigned
2. `-1 < 1u` is FALSE because -1 converts to UINT_MAX
3. Use `-Wsign-compare` flag to catch these bugs at compile time
4. C++20 `std::cmp_less/cmp_greater` handles mixed sign correctly
5. Prefer same signedness in comparisons, or cast explicitly

## Common Mistakes (Specific)
- Comparing `int` with `size_t` without thinking — common source of bugs
- `vector.size() - 1` when vector is empty → wraps to huge number
- Ignoring `-Wsign-compare` warnings — they indicate real bugs
- Assuming `-1 < 1u` is true — it's false due to unsigned promotion
