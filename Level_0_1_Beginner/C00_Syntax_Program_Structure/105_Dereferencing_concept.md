# Dereferencing concept

> **Level:** 0 — Absolute Beginner  
> **Category:** C00 — C++ Syntax & Program Structure  
> **Topic:** syntax

---

## Problem Statement
Understand pointer dereferencing — accessing the value a pointer points to.

## What You Need to Know
- `*ptr` (dereference) accesses the value at the address stored in `ptr`.
- `&var` (address-of) gets the address of a variable.
- These are inverse operations: `*(&x)` is `x`.

## Basic Dereferencing
```cpp
#include <iostream>

int main() {
    int x = 42;
    int* ptr = &x;     // ptr points to x

    // Read through pointer
    std::cout << *ptr << "\n";   // 42

    // Write through pointer
    *ptr = 100;
    std::cout << x << "\n";     // 100 (x changed through ptr!)

    return 0;
}
```

## Step by Step
```
int x = 42;
int* ptr = &x;

ptr  → stores address of x (e.g., 0x1000)
*ptr → goes to address 0x1000, reads/writes value there (42)

      ptr          x
    ┌──────┐    ┌──────┐
    │0x1000│───>│  42  │
    └──────┘    └──────┘
     *ptr = 42
```

## Multiple Pointers
```cpp
#include <iostream>

int main() {
    int a = 10, b = 20;
    int* p = &a;

    std::cout << *p << "\n";   // 10 (points to a)

    p = &b;                    // Reassign pointer to b
    std::cout << *p << "\n";   // 20 (now points to b)

    *p = 99;                   // Modify through pointer
    std::cout << b << "\n";   // 99

    return 0;
}
```

## Null Pointer Danger
```cpp
#include <iostream>

int main() {
    int* ptr = nullptr;

    // NEVER dereference a null pointer!
    // *ptr = 42;   // CRASH! Undefined behavior — segfault

    // Always check first
    if (ptr != nullptr) {
        std::cout << *ptr << "\n";
    } else {
        std::cout << "Null pointer — cannot dereference\n";
    }

    return 0;
}
```

## Key Takeaways
1. `*ptr` reads or writes the value at the address ptr holds
2. `&x` and `*ptr` are inverses: `*(&x) == x`
3. Changing `*ptr` changes the original variable
4. Never dereference `nullptr` — it's undefined behavior (crash)
5. Always check for null before dereferencing

## Common Mistakes
- Dereferencing nullptr → segfault / crash
- Dereferencing uninitialized pointer → undefined behavior
- Confusing `*` in declaration (`int* p`) vs `*` in expression (`*p`)
