# Static vs automatic storage basics

> **Level:** 0 — Absolute Beginner  
> **Category:** C00 — C++ Syntax & Program Structure  
> **Topic:** syntax

---

## Problem Statement
Understand the difference between automatic (stack) and static storage duration.

## What You Need to Know
- **Automatic storage**: local variables — created when scope is entered, destroyed when scope exits.
- **Static storage**: `static` and global variables — exist for the entire program lifetime.

## Automatic Storage (Default)
```cpp
#include <iostream>

void count() {
    int x = 0;    // Created each call, destroyed at end
    ++x;
    std::cout << "x = " << x << "\n";
}

int main() {
    count();   // x = 1
    count();   // x = 1  (x is re-created each time)
    count();   // x = 1
    return 0;
}
```

## Static Storage
```cpp
#include <iostream>

void count() {
    static int x = 0;   // Created ONCE, persists between calls
    ++x;
    std::cout << "x = " << x << "\n";
}

int main() {
    count();   // x = 1
    count();   // x = 2  (x persists!)
    count();   // x = 3
    return 0;
}
```

## Global Variables (Static Storage)
```cpp
#include <iostream>

int globalCounter = 0;   // Static storage duration

void increment() {
    ++globalCounter;
}

int main() {
    increment();
    increment();
    std::cout << globalCounter << "\n";  // 2
    return 0;
}
```

## Comparison
```
Feature          Automatic (local)        Static
-------          -----------------        ------
Keyword          (none)                   static / global
Lifetime         Scope entry → exit       Program start → end
Initialization   Every time               Once (first call for local static)
Default value    Garbage                  Zero
Memory           Stack                    Data segment
```

## static Local Variable Use Case
```cpp
#include <iostream>

int getId() {
    static int nextId = 0;    // Initialized once
    return ++nextId;          // Returns 1, 2, 3, ...
}

int main() {
    std::cout << getId() << "\n";  // 1
    std::cout << getId() << "\n";  // 2
    std::cout << getId() << "\n";  // 3
    return 0;
}
```

## Key Takeaways
1. Automatic variables live on the stack, re-created each time
2. Static local variables are initialized once, persist across calls
3. Global variables have static storage — exist for program lifetime
4. Static and global variables are zero-initialized by default
5. Use `static` local variables for persistent counters, caches, etc.

## Common Mistakes
- Expecting local variables to remember values between calls
- Overusing globals → makes code hard to test and maintain
- Forgetting that static initialization happens only once
