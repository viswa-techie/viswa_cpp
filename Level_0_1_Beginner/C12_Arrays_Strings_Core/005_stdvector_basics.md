# std::vector basics

> **Level:** 1 — Beginner  
> **Category:** C12  
> **Topic:** arrays_strings

---

## Problem Statement

Understand and explain the concept of std::vector basics. Be able to describe it, identify it in code, and use it correctly.

### Examples
- **Input Example 1:** A typical/simple case
- **Input Example 2:** An edge case (empty input, boundary values)
- **Input Example 3:** A larger or tricky case

---

## Prerequisites
- Basic C++ syntax (variables, types, operators)
- Understanding of C++ compilation model
- Header files and namespaces

---

## Core Concept

### What Is It?
std::vector basics is a fundamental concept in C++ that every programmer must understand.

### Why Does It Matter?
- Forms the foundation for understanding more complex C++ features
- Commonly asked in technical interviews
- Helps write clean, maintainable code

### Mental Model
Think of std::vector basics as a building block — you can't build a house without understanding bricks.

---

## Solution Approaches

### Approach 1: Direct / Straightforward
```cpp
#include <iostream>
#include <vector>
int main() {
    // Dynamic array — grows/shrinks as needed
    std::vector<int> v1;                    // Empty
    std::vector<int> v2(5);                 // 5 zeros
    std::vector<int> v3(5, 42);            // 5 copies of 42
    std::vector<int> v4 = {1, 2, 3, 4, 5}; // Initializer list
    
    // Access
    std::cout << "v4[0] = " << v4[0] << "
";
    std::cout << "v4.at(2) = " << v4.at(2) << "
"; // Bounds-checked
    std::cout << "front = " << v4.front() << "
";
    std::cout << "back = " << v4.back() << "
";
    
    // Size info
    std::cout << "size = " << v4.size() << "
";
    std::cout << "empty? " << v4.empty() << "
";
    
    // Add/remove
    v4.push_back(6);
    v4.pop_back();
    
    // Iterate
    for (const auto& x : v4) std::cout << x << " ";
    std::cout << "
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
#include <numeric>

/*
 * stdvector basics — STL/Library approach
 */
int main() {
    std::vector<int> data = {5, 2, 8, 1, 9, 3, 7, 4, 6};
    
    // STL-based implementation
    std::sort(data.begin(), data.end());
    for (const auto& x : data) std::cout << x << " ";
    std::cout << "
";
    
    auto it = std::lower_bound(data.begin(), data.end(), 5);
    if (it != data.end())
        std::cout << "Found: " << *it << " at index " << (it - data.begin()) << "
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
 * stdvector basics — Modern C++17/20 approach
 */
int main() {
    std::vector<int> data = {5, 2, 8, 1, 9, 3, 7, 4, 6};
    
    // Modern C++ features
    auto [min_it, max_it] = std::minmax_element(data.begin(), data.end());
    std::cout << "Range: [" << *min_it << ", " << *max_it << "]
";
    
    // Partition with lambda
    auto pivot = std::partition(data.begin(), data.end(), [](int x) { return x <= 5; });
    std::cout << "Partitioned at index: " << (pivot - data.begin()) << "
";
    for (int x : data) std::cout << x << " ";
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
- std::vector basics demonstrates fundamental language syntax

### Interview Tips
- Explain the concept clearly before writing code
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

**Pattern:** Language fundamentals — know the rules

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
- **Core idea:** std::vector basics
- **Key construct:** Language syntax
- **Complexity:** O(n) typical
- **Don't forget:** Initialize variables, check edge cases, use `-Wall`

---

*Generated for C++ Level 1 — C12 Problem Solving Guide*


## Key Takeaways
1. std::vector is a dynamic array that grows automatically
2. push_back/emplace_back add to the end in amortized O(1)
3. size() returns current elements; capacity() returns allocated space
4. .at() does bounds checking; [] does not
5. Vectors are contiguous in memory — cache-friendly

## Common Mistakes (Specific)
- Accessing elements before push_back (empty vector)
- Invalidating iterators after push_back (if reallocation occurs)
- Using [] without bounds check on untrusted indices
- Not reserving capacity when size is known — causes reallocation
- Comparing size() (unsigned) with negative int — promotion bug
