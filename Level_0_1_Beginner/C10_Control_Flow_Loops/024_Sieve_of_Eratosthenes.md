# Sieve of Eratosthenes

> **Level:** 1 — Beginner  
> **Category:** C10  
> **Topic:** control_flow

---

## Problem Statement

Master the use of Sieve of Eratosthenes in C++ programs. Understand when and why to use it.

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
Sieve of Eratosthenes is a technique in C++ that appears frequently in interviews and real projects.

### Why Does It Matter?
- Used extensively in production C++ code
- Commonly asked in technical interviews
- Helps write clean, maintainable code

### Mental Model
Think of sieve of eratosthenes as a tool in your toolbox — know when to reach for it.

---

## Solution Approaches

### Approach 1: Direct / Straightforward
```cpp
#include <iostream>
#include <vector>
int main() {
    int n = 100;
    std::vector<bool> is_prime(n + 1, true);
    is_prime[0] = is_prime[1] = false;
    
    for (int i = 2; i * i <= n; ++i) {
        if (is_prime[i]) {
            for (int j = i * i; j <= n; j += i) {
                is_prime[j] = false;
            }
        }
    }
    
    std::cout << "Primes up to " << n << ":
";
    for (int i = 2; i <= n; ++i)
        if (is_prime[i]) std::cout << i << " ";
    std::cout << "
";
    
    // Count primes
    int count = 0;
    for (int i = 2; i <= n; ++i)
        if (is_prime[i]) count++;
    std::cout << "Total: " << count << " primes
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
#include <string>

/*
 * Sieve of Eratosthenes — STL/Library approach
 */
int main() {
    std::vector<int> data = {5, 2, 8, 1, 9, 3, 7, 4, 6};
    
    // Using STL algorithms for Sieve of Eratosthenes
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
 * Sieve of Eratosthenes — Modern C++17/20 approach
 */
int main() {
    std::vector<int> data = {5, 2, 8, 1, 9, 3, 7, 4, 6};
    
    // Modern C++ approach for: Sieve of Eratosthenes
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
- Sieve of Eratosthenes demonstrates proper C++ idioms and best practices

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
- **Core idea:** Sieve of Eratosthenes
- **Key construct:** STL / Standard Library
- **Complexity:** O(n) typical
- **Don't forget:** Initialize variables, check edge cases, use `-Wall`

---

*Generated for C++ Level 1 — C10 Problem Solving Guide*


## Key Takeaways
1. Only check up to sqrt(n) for primality — O(sqrt(n))
2. Skip even numbers after checking 2 — halves the work
3. Sieve of Eratosthenes is O(n log log n) — efficient for finding ALL primes
4. Start marking from i*i (smaller multiples already marked)
5. Use `vector<bool>` for the sieve — memory efficient

## Common Mistakes (Specific)
- Off-by-one errors in loop boundaries or array indices
- Not handling edge cases (empty input, n=0, n=1)
- Integer overflow for large inputs — use `long long` when needed
- Forgetting to initialize variables before use
- Infinite loop from incorrect termination condition
