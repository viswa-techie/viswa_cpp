# NULL vs nullptr

> **Level:** 0 — Absolute Beginner  
> **Category:** C00 — C++ Syntax & Program Structure  
> **Topic:** syntax

---

## Problem Statement
Understand why `nullptr` (C++11) is preferred over `NULL` and how they differ.

## What You Need to Know
- `NULL` is a C-era macro, typically defined as `0` or `((void*)0)`.
- `nullptr` is a C++11 keyword with its own type `std::nullptr_t`.
- `NULL` can be ambiguous; `nullptr` is not.

## The Ambiguity Problem
```cpp
#include <iostream>

void process(int value) {
    std::cout << "int: " << value << "\n";
}

void process(int* ptr) {
    std::cout << "pointer: " << ptr << "\n";
}

int main() {
    process(0);          // Calls process(int) — 0 is an int
    // process(NULL);    // Ambiguous! May call either version
    process(nullptr);    // Calls process(int*) — unambiguous!
    return 0;
}
```

## How NULL Is Defined
```cpp
// In C:
#define NULL ((void*)0)    // void pointer

// In C++:
#define NULL 0             // Just zero! (void* doesn't implicitly convert)
// or:
#define NULL 0L
```

## Type Comparison
```cpp
#include <iostream>
#include <type_traits>

int main() {
    // NULL is an integer (implementation-defined, usually 0)
    // nullptr has type std::nullptr_t

    std::cout << std::boolalpha;
    std::cout << std::is_same_v<decltype(NULL), int> << "\n";         // Often true
    std::cout << std::is_same_v<decltype(nullptr), std::nullptr_t> << "\n";  // true

    // nullptr converts to any pointer type
    int* ip = nullptr;     // OK
    double* dp = nullptr;  // OK
    char* cp = nullptr;    // OK

    // nullptr does NOT convert to int
    // int x = nullptr;    // ERROR!

    return 0;
}
```

## Migration Guide
```cpp
// OLD code (pre-C++11):
int* p = NULL;
if (p == NULL) { }

// NEW code (C++11+):
int* p = nullptr;
if (p == nullptr) { }
// or simply:
if (!p) { }
```

## Key Takeaways
1. `NULL` = `0` in C++ — it's an integer, not a pointer
2. `nullptr` = true null pointer constant with its own type
3. `nullptr` prevents ambiguity in overloaded functions
4. `nullptr` cannot be implicitly converted to `int`
5. Always use `nullptr` in C++11 and later

## Common Mistakes
- Mixing `NULL` and `nullptr` in the same codebase → inconsistency
- `if (ptr == NULL)` in modern C++ — prefer `if (ptr == nullptr)` or `if (!ptr)`
- Assuming `NULL` is a pointer type in C++ — it's usually just `0`
