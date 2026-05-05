# Majority element (Moore's voting)

> **Level:** 1 — Beginner  
> **Category:** C12  
> **Topic:** arrays_strings

---

## Problem Statement

Master the use of Majority element (Moore's voting) in C++ programs. Understand when and why to use it.

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
Majority element (Moore's voting) is a technique in C++ that appears frequently in interviews and real projects.

### Why Does It Matter?
- Used extensively in production C++ code
- Commonly asked in technical interviews
- Helps write clean, maintainable code

### Mental Model
Think of majority element (moore's voting) as a tool in your toolbox — know when to reach for it.

---

## Solution Approaches

### Approach 1: Direct / Straightforward
```cpp
#include <iostream>
#include <vector>

int majorityElement(const std::vector<int>& nums) {
    // Boyer-Moore Voting Algorithm
    int candidate = nums[0], count = 1;
    for (int i = 1; i < (int)nums.size(); ++i) {
        if (count == 0) { candidate = nums[i]; count = 1; }
        else if (nums[i] == candidate) count++;
        else count--;
    }
    return candidate;  // Verify if needed
}

int main() {
    std::vector<int> nums = {2, 2, 1, 1, 1, 2, 2};
    std::cout << "Majority: " << majorityElement(nums) << "
";  // 2
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
 * Majority element Moores voting — STL/Library approach
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
 * Majority element Moores voting — Modern C++17/20 approach
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
- Majority element (Moore's voting) demonstrates proper C++ idioms and best practices

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
- **Core idea:** Majority element (Moore's voting)
- **Key construct:** STL / Standard Library
- **Complexity:** O(n) typical
- **Don't forget:** Initialize variables, check edge cases, use `-Wall`

---

*Generated for C++ Level 1 — C12 Problem Solving Guide*


## Key Takeaways
1. Understand the algorithm and its time/space complexity
2. Handle edge cases: empty array, single element, all same values
3. Consider both brute-force and optimized approaches
4. Test with small inputs and verify with larger ones
5. Know when to use STL algorithms vs manual implementation

## Common Mistakes (Specific)
- Off-by-one errors in array indices and loop bounds
- Not handling edge cases (empty array, single element)
- Integer overflow with large sums — use long long
- Modifying container while iterating — invalidates iterators
- Forgetting to sort before binary search
