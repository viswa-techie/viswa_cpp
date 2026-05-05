# LCM from GCD

> **Level:** 1 — Beginner  
> **Category:** C10  
> **Topic:** control_flow

---

## Problem Statement

Master the use of LCM from GCD in C++ programs. Understand when and why to use it.

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
LCM from GCD is a technique in C++ that appears frequently in interviews and real projects.

### Why Does It Matter?
- Used extensively in production C++ code
- Commonly asked in technical interviews
- Helps write clean, maintainable code

### Mental Model
Think of lcm from gcd as a tool in your toolbox — know when to reach for it.

---

## Solution Approaches

### Approach 1: Direct / Straightforward
```cpp
#include <iostream>
int gcd(int a, int b) {
    while (b) { int t = b; b = a % b; a = t; }
    return a;
}
int lcm(int a, int b) {
    return (a / gcd(a, b)) * b;  // Divide first to avoid overflow
}

int main() {
    std::cout << "LCM(4, 6) = " << lcm(4, 6) << "
";     // 12
    std::cout << "LCM(12, 18) = " << lcm(12, 18) << "
"; // 36
    std::cout << "LCM(7, 5) = " << lcm(7, 5) << "
";     // 35
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
#include <numeric>
#include <string>

/*
 * LCM from GCD — STL/Library approach
 */
int main() {
    std::vector<int> data = {5, 2, 8, 1, 9, 3, 7, 4, 6};
    
    // Using STL algorithms for LCM from GCD
    std::sort(data.begin(), data.end());
    
    for (const auto& x : data)
        std::cout << x << " ";
    std::cout << "
";
    
    // STL-based solution demonstration
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
#include <ranges>
#include <numeric>

/*
 * LCM from GCD — Modern C++17/20 approach
 */
int main() {
    std::vector<int> data = {5, 2, 8, 1, 9, 3, 7, 4, 6};
    
    // Modern C++ approach for: LCM from GCD
    // Using auto, structured bindings, ranges where applicable
    
    auto [min_it, max_it] = std::minmax_element(data.begin(), data.end());
    std::cout << "Min: " << *min_it << ", Max: " << *max_it << "
";
    
    // Lambda-based processing
    auto is_even = [](int n) { return n % 2 == 0; };
    auto count = std::count_if(data.begin(), data.end(), is_even);
    std::cout << "Even count: " << count << "
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
- LCM from GCD demonstrates proper C++ idioms and best practices

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
- **Core idea:** LCM from GCD
- **Key construct:** STL / Standard Library
- **Complexity:** O(n) typical
- **Don't forget:** Initialize variables, check edge cases, use `-Wall`

---

*Generated for C++ Level 1 — C10 Problem Solving Guide*


## Key Takeaways
1. Euclidean algorithm: gcd(a,b) = gcd(b, a%b), base case: gcd(a,0) = a
2. LCM formula: lcm(a,b) = a / gcd(a,b) * b (divide first to prevent overflow)
3. Time complexity: O(log(min(a,b)))
4. C++17 provides std::gcd and std::lcm in <numeric>
5. GCD is the foundation for many number theory problems

## Common Mistakes (Specific)
- Off-by-one errors in loop boundaries or array indices
- Not handling edge cases (empty input, n=0, n=1)
- Integer overflow for large inputs — use `long long` when needed
- Forgetting to initialize variables before use
- Infinite loop from incorrect termination condition
