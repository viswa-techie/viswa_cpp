# Prefix sum 1D

> **Level:** 1 — Beginner  
> **Category:** C12  
> **Topic:** arrays_strings

---

## Problem Statement

Write a C++ program that solves the Prefix sum 1D problem.

### Examples
- **Input Example 1:** A typical/simple case
- **Input Example 2:** An edge case (empty input, boundary values)
- **Input Example 3:** A larger or tricky case

---

## Prerequisites
- Basic C++ syntax (variables, types, operators)
- Control flow (if/else, loops)
- Array/vector basics

---

## Core Concept

### What Is It?
Prefix sum 1D is a classic problem in C++ that appears frequently in interviews and real projects.

### Why Does It Matter?
- Builds problem-solving muscle for algorithmic thinking
- Commonly asked in technical interviews
- Helps write clean, maintainable code

### Mental Model
Think of prefix sum 1d as a puzzle — break it into smaller pieces and solve each one.

---

## Solution Approaches

### Approach 1: Direct / Straightforward
```cpp
#include <iostream>
#include <vector>

int main() {
    std::vector<int> arr = {1, 2, 3, 4, 5};
    int n = arr.size();
    
    // Build prefix sum
    std::vector<int> prefix(n + 1, 0);
    for (int i = 0; i < n; ++i)
        prefix[i + 1] = prefix[i] + arr[i];
    
    // Range sum query: sum of arr[l..r] = prefix[r+1] - prefix[l]
    int l = 1, r = 3;  // sum of arr[1..3] = 2+3+4 = 9
    std::cout << "Sum [" << l << ".." << r << "] = " 
              << prefix[r+1] - prefix[l] << "";
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
 * Prefix sum 1D — STL/Library approach
 */
int main() {
    std::vector<int> data = {5, 2, 8, 1, 9, 3, 7, 4, 6};
    
    // STL-based implementation
    std::sort(data.begin(), data.end());
    for (const auto& x : data) std::cout << x << " ";
    std::cout << "";
    
    auto it = std::lower_bound(data.begin(), data.end(), 5);
    if (it != data.end())
        std::cout << "Found: " << *it << " at index " << (it - data.begin()) << "";
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
 * Prefix sum 1D — Modern C++17/20 approach
 */
int main() {
    std::vector<int> data = {5, 2, 8, 1, 9, 3, 7, 4, 6};
    
    // Modern C++ features
    auto [min_it, max_it] = std::minmax_element(data.begin(), data.end());
    std::cout << "Range: [" << *min_it << ", " << *max_it << "]";
    
    // Partition with lambda
    auto pivot = std::partition(data.begin(), data.end(), [](int x) { return x <= 5; });
    std::cout << "Partitioned at index: " << (pivot - data.begin()) << "";
    for (int x : data) std::cout << x << " ";
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
- Prefix sum 1D demonstrates loop control and algorithmic thinking

### Interview Tips
- Start with brute force, then optimize
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

**Pattern:** Loop-based computation — iterate and accumulate

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
- **Core idea:** Prefix sum 1D
- **Key construct:** Loops
- **Complexity:** O(n) typical
- **Don't forget:** Initialize variables, check edge cases, use `-Wall`

---

*Generated for C++ Level 1 — C12 Problem Solving Guide*


## Key Takeaways
1. Build prefix array in O(n), answer range queries in O(1)
2. Range sum [l,r] = prefix[r+1] - prefix[l]
3. Use 1-indexed prefix array to simplify boundary handling
4. 2D prefix sums enable O(1) submatrix sum queries
5. Difference array is the inverse — O(1) range updates

## Common Mistakes (Specific)
- Off-by-one errors in array indices and loop bounds
- Not handling edge cases (empty array, single element)
- Integer overflow with large sums — use long long
- Modifying container while iterating — invalidates iterators
- Forgetting to sort before binary search
