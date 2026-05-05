# Code blocks and braces

> **Level:** 0 — Absolute Beginner  
> **Category:** C00  
> **Topic:** syntax

---

## Problem Statement

Master the use of Code blocks and braces in C++ programs. Understand when and why to use it.

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
Code blocks and braces is a technique in C++ that appears frequently in interviews and real projects.

### Why Does It Matter?
- Used extensively in production C++ code
- Commonly asked in technical interviews
- Helps write clean, maintainable code

### Mental Model
Think of code blocks and braces as a tool in your toolbox — know when to reach for it.

---

## Solution Approaches

### Approach 1: Direct / Straightforward
```cpp
#include <iostream>

/*
 * Code blocks and braces
 *
 * Approach: Direct implementation
 */
int main() {
    // Step 1: Read input
    int number;
    std::cout << "Enter a number: ";
    std::cin >> number;

    // Step 2: Process
    // Code block for if condition
    if (number > 0) {
        std::cout << "Number is positive" << std::endl;
    } else {
        std::cout << "Number is zero or negative" << std::endl;
    }

    // Code block for loop
    std::cout << "Counting using a loop:" << std::endl;
    for (int i = 0; i < number; i++) {
        std::cout << i << " ";
    }

    std::cout << std::endl;

    // Step 3: Output result
    std::cout << "Solution for: Code blocks and braces" << std::endl;
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
#include <vector>
#include <algorithm>
#include <numeric>

/*
 * Code blocks and braces — Optimized approach using STL
 * 
 * Uses standard library algorithms where applicable.
 * Generally preferred in production C++ code.
 */
int main() {
    // TODO: STL-based implementation
    // Use std::sort, std::find, std::accumulate, etc. as appropriate
#include <iostream>
#include <vector>
#include <algorithm>
    // Step 1: Input
    std::vector<int> numbers = {1, -2, 3, -4, 5};

    // Step 2: Process
    // Code block using lambda + braces
    std::cout << "Positive numbers: ";
    std::for_each(numbers.begin(), numbers.end(), [](int n) {
        if (n > 0) {
            std::cout << n << " ";
        }
    });

    std::cout << std::endl;
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
#include <vector>

/*
 * Code blocks and braces — Modern C++ approach
 * 
 * Uses features from C++17/20: structured bindings,
 * if-init, ranges, constexpr, etc.
 */
int main() {
    // TODO: Modern C++ implementation
    // Use auto, structured bindings, ranges, etc.
#include <iostream>
#include <vector>

    std::vector<int> values = {10, 20, 30};

    // if-init statement (C++17)
    if (int size = values.size(); size > 0) {
        std::cout << "Vector has " << size << " elements." << std::endl;
    }

    // Range-based for loop
    for (int value : values) {
        std::cout << value << " ";
    }

    std::cout << std::endl;
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
- Code blocks and braces demonstrates proper C++ idioms and best practices

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
- **Core idea:** Code blocks and braces
- **Key construct:** STL / Standard Library
- **Complexity:** O(n) typical
- **Don't forget:** Initialize variables, check edge cases, use `-Wall`

---

*Generated for C++ Level 0 — C00 Problem Solving Guide*
