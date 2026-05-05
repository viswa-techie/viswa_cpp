# Header file purpose

> **Level:** 0 — Absolute Beginner  
> **Category:** C00 — C++ Syntax & Program Structure  
> **Topic:** syntax

---

## Problem Statement
Understand what header files are, why they exist, and how to create your own.

## What You Need to Know
- A header file (`.h` or `.hpp`) contains **declarations** — function prototypes, class definitions, constants.
- A source file (`.cpp`) contains **definitions** — the actual implementation.
- Headers allow code to be shared across multiple source files.

## Mental Model
Think of a header file as a **menu** (lists what's available) and the `.cpp` file as the **kitchen** (where the food is actually prepared).

## Anatomy of a Header File
```cpp
// math_utils.h
#ifndef MATH_UTILS_H    // Include guard
#define MATH_UTILS_H

int add(int a, int b);          // Function declaration (prototype)
int multiply(int a, int b);     // No function body here

const double PI = 3.14159265;   // Constant

#endif // MATH_UTILS_H
```

## Corresponding Source File
```cpp
// math_utils.cpp
#include "math_utils.h"

int add(int a, int b) {         // Function definition
    return a + b;
}

int multiply(int a, int b) {
    return a * b;
}
```

## Using the Header
```cpp
// main.cpp
#include <iostream>
#include "math_utils.h"    // Include our header

int main() {
    std::cout << add(3, 4) << "\n";         // 7
    std::cout << multiply(3, 4) << "\n";    // 12
    std::cout << PI << "\n";                // 3.14159
    return 0;
}
```

## Compile Multiple Files
```bash
g++ -o program main.cpp math_utils.cpp
```

## What Goes in Headers vs Source Files
```
Header (.h/.hpp)              Source (.cpp)
-----------------             ------------
Function declarations         Function definitions
Class declarations            Method implementations
Constants                     Static variable definitions
Type aliases (typedef/using)  Main function
Template definitions          Implementation details
Inline functions              Non-inline function bodies
```

## Key Takeaways
1. Headers declare interfaces; source files define implementations
2. Always use include guards (`#ifndef` or `#pragma once`)
3. Use `"quotes"` for your own headers, `<angles>` for system headers
4. Never put `main()` in a header file
5. Never put function definitions in headers (except inline/template)

## Common Mistakes
- Putting function bodies in headers → linker errors (multiple definitions)
- Forgetting include guards → redefinition errors
- Circular includes — A.h includes B.h which includes A.h
