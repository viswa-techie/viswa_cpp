# Infinite loop patterns

> **Level:** 1 — Beginner  
> **Category:** C10  
> **Topic:** control_flow

---

## Problem Statement

Write a C++ program that solves the Infinite loop patterns problem.

### Examples
- **Input Example 1:** A typical/simple case
- **Input Example 2:** An edge case (empty input, boundary values)
- **Input Example 3:** A larger or tricky case

---

## Prerequisites
- Basic C++ syntax (variables, types, operators)
- Control flow (if/else, loops)
- Header files and namespaces

---

## Core Concept

### What Is It?
Infinite loop patterns is a common programming pattern in C++ that tests your understanding of loops and logic.

### Why Does It Matter?
- Builds problem-solving muscle for algorithmic thinking
- Commonly asked in technical interviews
- Helps write clean, maintainable code

### Mental Model
Think of infinite loop patterns as a recipe — follow the steps in order and you'll get the right output.

---

## Solution Approaches

### Approach 1: Direct / Straightforward
```cpp
#include <iostream>
int main() {
    // Pattern 1: while(true)
    int count = 0;
    while (true) {
        if (count >= 5) break;
        std::cout << count++ << " ";
    }
    std::cout << "
";
    
    // Pattern 2: for(;;)
    count = 0;
    for (;;) {
        if (count >= 5) break;
        std::cout << count++ << " ";
    }
    std::cout << "
";
    
    // Common use: event loop / server loop
    // while (true) { process_event(); }
    
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
 * Infinite loop patterns — STL/Library approach
 */
int main() {
    std::vector<int> data = {5, 2, 8, 1, 9, 3, 7, 4, 6};
    
    // Using STL algorithms for Infinite loop patterns
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
 * Infinite loop patterns — Modern C++17/20 approach
 */
int main() {
    std::vector<int> data = {5, 2, 8, 1, 9, 3, 7, 4, 6};
    
    // Modern C++ approach for: Infinite loop patterns
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
- Infinite loop patterns demonstrates loop control and algorithmic thinking

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

**Pattern:** Nested loop pattern — control spacing and characters

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
- **Core idea:** Infinite loop patterns
- **Key construct:** Loops
- **Complexity:** O(n) typical
- **Don't forget:** Initialize variables, check edge cases, use `-Wall`

---

*Generated for C++ Level 1 — C10 Problem Solving Guide*


## Key Takeaways
1. Choose loop type based on pattern: for (known count), while (condition), do-while (at least once)
2. Range-based for is preferred for iterating containers
3. Use `++i` (pre-increment) by default — avoids unnecessary copy for iterators
4. Declare loop variables in the smallest scope possible
5. Watch for off-by-one: `<` vs `<=`, starting index 0 vs 1

## Common Mistakes (Specific)
- Off-by-one errors: using `<=` when `<` is correct (or vice versa)
- Infinite loops from forgetting to update loop variable
- Modifying container while iterating (invalidates iterators)
- Using post-increment on complex iterators (unnecessary copy)
