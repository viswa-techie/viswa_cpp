# Warnings and how to fix them

> **Level:** 0 — Absolute Beginner  
> **Category:** C00 — C++ Syntax & Program Structure  
> **Topic:** syntax

---

## Problem Statement
Understand common compiler warnings and why you should fix them.

## Common Warnings
```cpp
// Warning: unused variable
int x = 5;  // Never used → remove it or use [[maybe_unused]]

// Warning: signed/unsigned comparison
int a = -1;
unsigned int b = 5;
if (a < b) { }  // Dangerous! -1 converts to a huge unsigned number

// Warning: implicit conversion loses precision
double pi = 3.14;
int approx = pi;  // Loses .14 → use static_cast<int>(pi) to be explicit

// Warning: variable may be used uninitialized
int x;
std::cout << x;  // x has garbage value!

// Warning: control reaches end of non-void function
int getValue(bool flag) {
    if (flag) return 42;
    // Missing return for else case!
}
```

## Suppressing Intentional Warnings
```cpp
[[maybe_unused]] int debugCounter = 0;  // C++17: suppress unused warning

(void)unusedParam;  // C-style: cast to void to suppress unused parameter warning
```

## Key Takeaways
1. Always compile with `-Wall -Wextra`
2. Treat warnings as errors with `-Werror`
3. Fix warnings — they often indicate real bugs
4. Use `[[maybe_unused]]` for intentionally unused variables (C++17)
