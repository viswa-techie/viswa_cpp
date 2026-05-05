# #define basics

> **Level:** 0 — Absolute Beginner  
> **Category:** C00 — C++ Syntax & Program Structure  
> **Topic:** syntax

---

## Problem Statement
Understand `#define` for creating macros and constants, and when to avoid it in modern C++.

## What You Need to Know
- `#define NAME value` creates a text substitution rule.
- The preprocessor replaces every `NAME` with `value` before compilation.
- No type checking — it's just text replacement.

## Simple Constants
```cpp
#include <iostream>

#define PI 3.14159
#define MAX_STUDENTS 30
#define GREETING "Hello, World!"

int main() {
    double area = PI * 5 * 5;
    std::cout << GREETING << "\n";
    std::cout << "Area: " << area << "\n";
    std::cout << "Max students: " << MAX_STUDENTS << "\n";
    return 0;
}
```

## Modern C++ Alternative (Preferred)
```cpp
#include <iostream>

// Use constexpr instead of #define for typed constants
constexpr double PI = 3.14159;
constexpr int MAX_STUDENTS = 30;
const char* GREETING = "Hello, World!";

int main() {
    double area = PI * 5 * 5;
    std::cout << area << "\n";
    return 0;
}
```

## Why constexpr is Better
```
Feature          #define         constexpr/const
-------          -------         ---------------
Type checking    No              Yes
Scope            Global          Respects scope
Debuggable       No (replaced)   Yes (visible)
Namespace        No              Yes
Errors           Confusing       Clear
```

## #undef
```cpp
#define TEMP 100
// ... use TEMP ...
#undef TEMP       // Remove the macro
// TEMP is no longer defined
```

## Multi-line #define
```cpp
#define PRINT_HEADER()      \
    std::cout << "========" \
              << "\n"       \
              << "REPORT"   \
              << "\n"       \
              << "========" \
              << "\n"

int main() {
    PRINT_HEADER();
    return 0;
}
```

## Key Takeaways
1. `#define` does text replacement — no types, no scope
2. Prefer `constexpr` (C++11) for constants in modern C++
3. Prefer `const` for string literals
4. `#define` is still useful for include guards and conditional compilation
5. Use `\` for multi-line macros

## Common Mistakes
- `#define MAX 100;` — the `;` becomes part of the value
- No `=` sign: `#define X = 5` means X is replaced by `= 5`
- `#define` doesn't respect scope — it's global from point of definition
