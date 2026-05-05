# Garbage values without initialization

> **Level:** 0 — Absolute Beginner  
> **Category:** C00 — C++ Syntax & Program Structure  
> **Topic:** syntax

---

## Problem Statement
Understand why uninitialized variables contain garbage values and how to avoid this.

## What You Need to Know
- In C++, local variables are NOT automatically initialized.
- An uninitialized variable contains whatever bits were in that memory location.
- Reading an uninitialized variable is **undefined behavior**.

## The Problem
```cpp
#include <iostream>

int main() {
    int x;          // NOT initialized — contains garbage!
    std::cout << x << "\n";  // UB! Could print anything
    // Might print: 0, -858993460, 32767, or crash

    double d;       // Also garbage
    bool b;         // Also garbage (might not be true or false!)

    return 0;
}
```

## The Fix: Always Initialize
```cpp
#include <iostream>

int main() {
    int x = 0;          // Initialized to 0
    double d = 0.0;     // Initialized to 0.0
    bool b = false;     // Initialized to false
    char c = '\0';      // Initialized to null character
    int* p = nullptr;   // Initialized to null pointer

    // C++11: Brace initialization
    int y{};            // Zero-initialized (0)
    int z{42};          // Initialized to 42

    std::cout << x << " " << y << " " << z << "\n";
    return 0;
}
```

## Where Variables ARE Auto-Initialized
```cpp
#include <iostream>

int global_x;    // Global → auto-initialized to 0

void foo() {
    static int s;  // Static → auto-initialized to 0
    int local;     // Local → NOT initialized (garbage!)
}

int main() {
    std::cout << global_x << "\n";   // 0 (guaranteed)
    return 0;
}
```

## Summary Table
```
Variable Type        Auto-initialized?    Value
-------------        -----------------    -----
Global               Yes                  0
Static local         Yes                  0
Local (automatic)    No                   Garbage!
new int              No                   Garbage!
new int()            Yes                  0
new int{}            Yes                  0
```

## Compiler Warnings
```bash
# Enable warnings for uninitialized variables
g++ -Wall -Wuninitialized main.cpp
# Warning: 'x' is used uninitialized in this function
```

## Key Takeaways
1. Local variables are NOT initialized — always assign a value
2. Global and static variables are zero-initialized automatically
3. Reading uninitialized variables is undefined behavior
4. Use `{}` initialization: `int x{};` → 0, `int x{42};` → 42
5. Compile with `-Wall` to catch uninitialized variable usage

## Common Mistakes
- Declaring `int x;` and assuming it's 0
- "It worked in debug mode" → debug builds may zero-initialize, release won't
- Array members: `int arr[100];` — all 100 elements are garbage
