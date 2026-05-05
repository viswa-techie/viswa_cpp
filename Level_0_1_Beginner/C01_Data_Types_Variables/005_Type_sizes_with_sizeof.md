# Type sizes with sizeof

> **Level:** 0 — Absolute Beginner  
> **Category:** C01  
> **Topic:** types

---

## Problem Statement

Master the use of Type sizes with sizeof in C++ programs. Understand when and why to use it.

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
Type sizes with sizeof is a technique in C++ that appears frequently in interviews and real projects.

### Why Does It Matter?
- Used extensively in production C++ code
- Commonly asked in technical interviews
- Helps write clean, maintainable code

### Mental Model
Think of type sizes with sizeof as a tool in your toolbox — know when to reach for it.

---

## Solution Approaches

### Approach 1: Direct / Straightforward
```cpp
#include <iostream>

struct Example {
    char c;    // 1 byte + 3 padding
    int i;     // 4 bytes
    double d;  // 8 bytes
};

int main() {
    std::cout << "Fundamental types:
";
    std::cout << "  char: " << sizeof(char) << "
";
    std::cout << "  short: " << sizeof(short) << "
";
    std::cout << "  int: " << sizeof(int) << "
";
    std::cout << "  long: " << sizeof(long) << "
";
    std::cout << "  long long: " << sizeof(long long) << "
";
    std::cout << "  float: " << sizeof(float) << "
";
    std::cout << "  double: " << sizeof(double) << "
";
    std::cout << "  pointer: " << sizeof(void*) << "
";
    std::cout << "  Example struct: " << sizeof(Example) << " (with padding)
";

    int arr[10];
    std::cout << "  arr[10]: " << sizeof(arr) << " bytes, "
              << sizeof(arr)/sizeof(arr[0]) << " elements
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
#include <string>
#include <array>

int main() {
    std::cout << "STL container object sizes:
";
    std::cout << "  std::string: " << sizeof(std::string) << "
";
    std::cout << "  std::vector<int>: " << sizeof(std::vector<int>) << "
";
    std::cout << "  std::array<int,10>: " << sizeof(std::array<int,10>) << "
";

    // Note: sizeof gives object size, not content size
    std::string s = "Hello World";
    std::cout << "  sizeof(s)=" << sizeof(s) << " vs s.size()=" << s.size() << "
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
#include <type_traits>

template<typename T>
void printSize(const char* name) {
    std::cout << name << ": " << sizeof(T) << " bytes, "
              << "aligned to " << alignof(T) << "
";
}

int main() {
    printSize<char>("char");
    printSize<int>("int");
    printSize<double>("double");
    printSize<long double>("long double");
    printSize<void*>("void*");

    // constexpr sizeof — available at compile time
    constexpr size_t intSize = sizeof(int);
    static_assert(intSize >= 2, "int must be at least 2 bytes");
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
- Type sizes with sizeof demonstrates proper C++ idioms and best practices

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
- **Core idea:** Type sizes with sizeof
- **Key construct:** STL / Standard Library
- **Complexity:** O(n) typical
- **Don't forget:** Initialize variables, check edge cases, use `-Wall`

---

*Generated for C++ Level 0 — C01 Problem Solving Guide*


## Key Takeaways
1. `sizeof` is a compile-time operator — zero runtime cost
2. `sizeof(char)` is ALWAYS 1 by definition
3. Struct sizes include padding for alignment
4. `sizeof(array)` gives total bytes; `sizeof(pointer)` gives pointer size only
5. Use `sizeof(arr)/sizeof(arr[0])` for C-array element count

## Common Mistakes (Specific)
- `sizeof(pointer)` gives pointer size (4 or 8), not pointed-to data size
- `sizeof(std::string)` gives object overhead, not string content length
- Array decays to pointer in functions — sizeof then gives pointer size
- Assuming sizes are same across platforms — they vary
