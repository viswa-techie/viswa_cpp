# 1D array declaration & init

> **Level:** 1 — Beginner  
> **Category:** C12  
> **Topic:** arrays_strings

---

## Problem Statement

Master the use of 1D array declaration & init in C++ programs. Understand when and why to use it.

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
1D array declaration & init is a technique in C++ that appears frequently in interviews and real projects.

### Why Does It Matter?
- Used extensively in production C++ code
- Commonly asked in technical interviews
- Helps write clean, maintainable code

### Mental Model
Think of 1d array declaration & init as a tool in your toolbox — know when to reach for it.

---

## Solution Approaches

### Approach 1: Direct / Straightforward
```cpp
#include <iostream>
int main() {
    // Declaration and initialization
    int arr1[5] = {1, 2, 3, 4, 5};
    int arr2[] = {10, 20, 30};  // Size deduced: 3
    int arr3[5] = {1, 2};      // Rest are 0: {1,2,0,0,0}
    int arr4[5] = {};           // All zeros
    
    // Access and modify
    std::cout << "arr1[0] = " << arr1[0] << "
";
    arr1[2] = 99;
    
    // Iterate
    int size = sizeof(arr1) / sizeof(arr1[0]);
    for (int i = 0; i < size; ++i)
        std::cout << arr1[i] << " ";
    std::cout << "
";
    
    // Range-based for
    for (int x : arr2) std::cout << x << " ";
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
 * 1D array declaration init — STL/Library approach
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
 * 1D array declaration init — Modern C++17/20 approach
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
- 1D array declaration & init demonstrates proper C++ idioms and best practices

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
- **Core idea:** 1D array declaration & init
- **Key construct:** STL / Standard Library
- **Complexity:** O(n) typical
- **Don't forget:** Initialize variables, check edge cases, use `-Wall`

---

*Generated for C++ Level 1 — C12 Problem Solving Guide*


## Key Takeaways
1. C-arrays have fixed size determined at compile time
2. Arrays are zero-indexed: first element is arr[0]
3. Use `sizeof(arr)/sizeof(arr[0])` for element count (only works locally)
4. Prefer std::array or std::vector over raw C arrays
5. Uninitialized arrays contain garbage values

## Common Mistakes (Specific)
- Out-of-bounds access: no runtime check for C arrays (UB!)
- Forgetting that arrays are zero-indexed (last element at size-1)
- sizeof in function gives pointer size, not array size
- Uninitialized array elements contain garbage values
- Using VLAs (variable-length arrays) — not standard C++
