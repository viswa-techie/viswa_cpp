# Preprocessor directives

> **Level:** 0 — Absolute Beginner  
> **Category:** C00 — C++ Syntax & Program Structure  
> **Topic:** syntax

---

## Problem Statement
Understand preprocessor directives — commands processed before compilation.

## What You Need to Know
- Preprocessor directives start with `#`.
- They are processed **before** the compiler sees the code.
- They do NOT end with a semicolon.
- They operate on text substitution, not C++ syntax.

## Common Directives
```
Directive         Purpose
---------         -------
#include          Include a header file
#define           Define a macro/constant
#undef            Undefine a macro
#ifdef            If macro is defined
#ifndef           If macro is NOT defined
#if               Conditional compilation
#elif             Else if
#else             Else
#endif            End conditional
#pragma           Compiler-specific instruction
#error            Generate a compile error
#warning          Generate a compile warning (GCC)
#line             Change line number/filename
```

## Examples
```cpp
#include <iostream>         // Include header

#define MAX_SIZE 100        // Define constant
#define SQUARE(x) ((x)*(x))  // Define macro

#ifdef DEBUG
    #define LOG(msg) std::cerr << msg << "\n"
#else
    #define LOG(msg)        // Does nothing in release
#endif

#if __cplusplus >= 201703L
    // C++17 or later code
#elif __cplusplus >= 201402L
    // C++14 code
#else
    // Older C++ code
#endif

#pragma once               // Include guard (non-standard but universal)

#error "This platform is not supported"  // Stop compilation with message
```

## Predefined Macros
```cpp
#include <iostream>

int main() {
    std::cout << "File: " << __FILE__ << "\n";
    std::cout << "Line: " << __LINE__ << "\n";
    std::cout << "Date: " << __DATE__ << "\n";
    std::cout << "Time: " << __TIME__ << "\n";
    std::cout << "C++ Standard: " << __cplusplus << "\n";
    return 0;
}
```

## Key Takeaways
1. Preprocessor runs before the compiler — it's text manipulation
2. No semicolons on `#` directives
3. `#define` constants are replaced literally — no type checking
4. Prefer `const` / `constexpr` over `#define` for constants in C++
5. Use `__cplusplus` to check the C++ standard version

## Common Mistakes
- Adding `;` after `#define MAX 100;` → the semicolon becomes part of the value
- Macro side effects: `SQUARE(x++)` expands to `((x++)*(x++))` — increments twice
- Forgetting `#endif` → confusing compilation errors
