# Lambda capture by reference

> **Level:** 1 — Beginner  
> **Category:** C11  
> **Topic:** functions_recursion

---

## Problem Statement

Master the use of Lambda capture by reference in C++ programs. Understand when and why to use it.

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
Lambda capture by reference is a technique in C++ that appears frequently in interviews and real projects.

### Why Does It Matter?
- Used extensively in production C++ code
- Commonly asked in technical interviews
- Helps write clean, maintainable code

### Mental Model
Think of lambda capture by reference as a tool in your toolbox — know when to reach for it.

---

## Solution Approaches

### Approach 1: Direct / Straightforward
```cpp
#include <iostream>
#include <vector>

int main() {
    int total = 0;
    std::vector<int> nums = {1, 2, 3, 4, 5};
    
    // Capture by reference: [&total]
    auto accumulate = [&total](int val) {
        total += val;  // Modifies the ORIGINAL variable
    };
    
    for (int n : nums) accumulate(n);
    std::cout << "Total: " << total << "
";  // 15
    
    // [&] captures ALL by reference
    int min_val = nums[0], max_val = nums[0];
    auto find_range = [&]() {
        for (int n : nums) {
            if (n < min_val) min_val = n;
            if (n > max_val) max_val = n;
        }
    };
    find_range();
    std::cout << "Range: [" << min_val << ", " << max_val << "]
";
    
    // Mix: [=, &total] — all by value except total by reference
    int multiplier = 2;
    auto scale = [=, &total]() { total *= multiplier; };
    scale();
    std::cout << "Scaled total: " << total << "
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
#include <vector>
#include <algorithm>
#include <functional>
#include <numeric>

/*
 * Lambda capture by reference — STL/Library approach
 */
int main() {
    std::vector<int> data = {5, 2, 8, 1, 9, 3, 7, 4, 6};
    
    // STL-based implementation of Lambda capture by reference
    std::sort(data.begin(), data.end());
    for (const auto& x : data) std::cout << x << " ";
    std::cout << "
";
    
    auto sum = std::accumulate(data.begin(), data.end(), 0);
    std::cout << "Sum: " << sum << "
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
#include <vector>
#include <algorithm>
#include <numeric>

/*
 * Lambda capture by reference — Modern C++17/20 approach
 */
int main() {
    std::vector<int> data = {5, 2, 8, 1, 9, 3, 7, 4, 6};
    
    // Modern C++ features for Lambda capture by reference
    auto [min_it, max_it] = std::minmax_element(data.begin(), data.end());
    std::cout << "Range: [" << *min_it << ", " << *max_it << "]
";
    
    // Lambda-based approach
    std::sort(data.begin(), data.end());
    for (const auto& x : data) std::cout << x << " ";
    std::cout << "
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
- Lambda capture by reference demonstrates proper C++ idioms and best practices

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
- **Core idea:** Lambda capture by reference
- **Key construct:** STL / Standard Library
- **Complexity:** O(n) typical
- **Don't forget:** Initialize variables, check edge cases, use `-Wall`

---

*Generated for C++ Level 1 — C11 Problem Solving Guide*


## Key Takeaways
1. Lambda syntax: `[captures](params) -> return { body }`
2. `[=]` captures all by value, `[&]` captures all by reference
3. Captured-by-value vars are const unless `mutable` is used
4. Lambdas are anonymous function objects (each has unique type)
5. Prefer lambdas over function pointers for inline callbacks

## Common Mistakes (Specific)
- Capturing local variable by reference when lambda outlives the variable → dangling reference
- Forgetting `mutable` when needing to modify captured-by-value variables
- Capturing `this` in a lambda stored beyond object lifetime
- Over-capturing with `[=]` or `[&]` — be explicit about what you need
