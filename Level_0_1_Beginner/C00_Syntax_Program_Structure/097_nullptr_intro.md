# nullptr intro

> **Level:** 0 — Absolute Beginner  
> **Category:** C00 — C++ Syntax & Program Structure  
> **Topic:** syntax

---

## Problem Statement
Understand `nullptr` — the modern C++ null pointer constant.

## What You Need to Know
- `nullptr` represents a null pointer — a pointer that points to nothing.
- Introduced in C++11 to replace `NULL` and `0`.
- It has its own type: `std::nullptr_t`.

## Basic Usage
```cpp
#include <iostream>

int main() {
    int* ptr = nullptr;    // ptr points to nothing

    if (ptr == nullptr) {
        std::cout << "ptr is null\n";
    }

    // Short form (pointer in boolean context)
    if (!ptr) {
        std::cout << "ptr is null\n";
    }

    return 0;
}
```

## Why nullptr Instead of NULL or 0
```cpp
#include <iostream>

void foo(int x)    { std::cout << "int version\n"; }
void foo(int* ptr) { std::cout << "pointer version\n"; }

int main() {
    foo(0);          // Calls foo(int) — 0 is an integer!
    // foo(NULL);    // Ambiguous! NULL is often defined as 0
    foo(nullptr);    // Calls foo(int*) — unambiguous!
    return 0;
}
```

## Null Check Before Use
```cpp
#include <iostream>

void printValue(int* ptr) {
    if (ptr != nullptr) {
        std::cout << "Value: " << *ptr << "\n";
    } else {
        std::cout << "Null pointer!\n";
    }
}

int main() {
    int x = 42;
    printValue(&x);       // Value: 42
    printValue(nullptr);  // Null pointer!
    return 0;
}
```

## Comparison
```
Constant     Type           Safe?      C++ Standard
--------     ----           -----      ------------
0            int            No         All
NULL         int/void*      No         All (C compat)
nullptr      std::nullptr_t Yes        C++11+
```

## Key Takeaways
1. Use `nullptr` instead of `NULL` or `0` for null pointers
2. `nullptr` is type-safe — won't be confused with integer 0
3. Always check for null before dereferencing a pointer
4. `if (ptr)` is true when not null, `if (!ptr)` when null
5. Dereferencing nullptr is undefined behavior → crash

## Common Mistakes
- Using `NULL` in C++ — use `nullptr` instead
- Dereferencing without null check: `*ptr` when ptr is nullptr → crash
- Comparing with `0` instead of `nullptr` — works but less clear
