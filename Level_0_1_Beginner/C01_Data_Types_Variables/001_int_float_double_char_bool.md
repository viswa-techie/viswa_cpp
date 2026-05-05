# int, float, double, char, bool

> **Level:** 0 — Absolute Beginner  
> **Category:** C01  
> **Topic:** types

---

## Problem Statement

Master the use of int, float, double, char, bool in C++ programs. Understand when and why to use it.

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
int, float, double, char, bool is a technique in C++ that appears frequently in interviews and real projects.

### Why Does It Matter?
- Used extensively in production C++ code
- Commonly asked in technical interviews
- Helps write clean, maintainable code

### Mental Model
Think of int, float, double, char, bool as a tool in your toolbox — know when to reach for it.

---

## Solution Approaches

### Approach 1: Direct / Straightforward
```cpp
#include <iostream>
int main() {
    int age = 25;
    float height = 5.9f;
    double pi = 3.14159265358979;
    char grade = 'A';
    bool passed = true;

    std::cout << "Age: " << age << "";
    std::cout << "Height: " << height << "";
    std::cout << "Pi: " << pi << "";
    std::cout << "Grade: " << grade << "";
    std::cout << "Passed: " << std::boolalpha << passed << "";

    // Size of each type
    std::cout << "sizeof(int)=" << sizeof(int) << "";
    std::cout << "sizeof(float)=" << sizeof(float) << "";
    std::cout << "sizeof(double)=" << sizeof(double) << "";
    std::cout << "sizeof(char)=" << sizeof(char) << "";
    std::cout << "sizeof(bool)=" << sizeof(bool) << "";
    return 0;
}
```

**Time Complexity:** O(n) (typical)  
**Space Complexity:** O(1) or O(n)  
**When to use:** First attempt, when simplicity matters over performance.

### Approach 2: Optimized / STL-Based
```cpp
#include <iostream>
#include <typeinfo>
#include <limits>

int main() {
    // Using numeric_limits for type information
    std::cout << "int range: [" << std::numeric_limits<int>::min()
              << ", " << std::numeric_limits<int>::max() << "]";
    std::cout << "float max: " << std::numeric_limits<float>::max() << "";
    std::cout << "double precision: " << std::numeric_limits<double>::digits10 << " digits";
    std::cout << "char is signed: " << std::boolalpha << std::numeric_limits<char>::is_signed << "";
    return 0;
}
```

**Time Complexity:** Depends on STL algorithm used  
**Space Complexity:** Depends on approach  
**When to use:** Production code, when you know the right STL tool.

### Approach 3: Modern C++ (C++17/20)
```cpp
#include <iostream>
#include <type_traits>

int main() {
    auto age = 25;          // deduced as int
    auto height = 5.9f;    // deduced as float
    auto pi = 3.14159;     // deduced as double
    auto grade = 'A';      // deduced as char
    auto passed = true;    // deduced as bool

    // C++17: compile-time type checks
    static_assert(std::is_same_v<decltype(age), int>);
    static_assert(std::is_same_v<decltype(height), float>);
    static_assert(std::is_same_v<decltype(pi), double>);
    static_assert(std::is_same_v<decltype(grade), char>);
    static_assert(std::is_same_v<decltype(passed), bool>);

    std::cout << "All type checks passed!";
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
- int, float, double, char, bool demonstrates proper C++ idioms and best practices

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
- **Core idea:** int, float, double, char, bool
- **Key construct:** STL / Standard Library
- **Complexity:** O(n) typical
- **Don't forget:** Initialize variables, check edge cases, use `-Wall`

---

*Generated for C++ Level 0 — C01 Problem Solving Guide*


## Key Takeaways
1. `int` for whole numbers (4 bytes typically), `double` for decimals (8 bytes), `float` for lower-precision decimals (4 bytes)
2. `char` holds a single character (1 byte), `bool` holds true/false (1 byte)
3. Use `double` over `float` unless memory is critical — more precision
4. `sizeof()` reveals actual byte sizes on your platform
5. Prefer `int` for general integers; use `double` for floating-point math

## Common Mistakes (Specific)
- Using `float` when `double` is needed — losing precision silently
- Forgetting that `char` is an integer type (can do arithmetic on it)
- Comparing `float`/`double` with `==` — precision issues
- Uninitialized variables — contain garbage values
