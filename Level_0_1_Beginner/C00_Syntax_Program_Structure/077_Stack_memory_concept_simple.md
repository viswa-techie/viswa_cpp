# Stack memory concept (simple)

> **Level:** 0 — Absolute Beginner  
> **Category:** C00 — C++ Syntax & Program Structure  
> **Topic:** syntax

---

## Problem Statement
Understand the stack — where local variables live in C++.

## What You Need to Know
- The **stack** is a region of memory used for local variables and function calls.
- It works like a stack of plates: last in, first out (LIFO).
- Memory is allocated when entering a function, freed when leaving.

## How the Stack Works
```
When main() calls foo():

        ┌──────────────┐
        │ foo() locals  │ ← Stack top (grows downward)
        ├──────────────┤
        │ main() locals │
        ├──────────────┤
        │ ... (OS/CRT)  │
        └──────────────┘ ← Stack bottom

When foo() returns:

        ┌──────────────┐
        │ main() locals │ ← Stack top
        ├──────────────┤
        │ ... (OS/CRT)  │
        └──────────────┘
```

## Example
```cpp
#include <iostream>

void greet() {
    int y = 20;    // y is on the stack (inside greet's frame)
    std::cout << "y = " << y << "\n";
}   // y is destroyed here (stack frame popped)

int main() {
    int x = 10;    // x is on the stack (inside main's frame)
    greet();       // Push greet's frame, execute, pop
    // y no longer exists here
    std::cout << "x = " << x << "\n";
    return 0;
}   // x is destroyed here
```

## Stack Properties
```
Property          Description
--------          -----------
Allocation        Automatic (entering scope)
Deallocation      Automatic (leaving scope)
Speed             Very fast (just move stack pointer)
Size              Limited (typically 1-8 MB)
Growth            Downward (high → low addresses)
Lifetime          Tied to scope/function
Order             LIFO (last allocated, first freed)
```

## Stack Overflow
```cpp
#include <iostream>

void infinite_recursion() {
    int arr[1000];  // Each call uses ~4KB of stack
    infinite_recursion();  // Never stops → stack overflow!
}

int main() {
    infinite_recursion();  // Crash: stack overflow / segfault
    return 0;
}
```

## Key Takeaways
1. Local variables live on the stack — fast, automatic management
2. Stack memory is freed when the function/scope exits
3. Stack is limited in size (1-8 MB typical) — don't put huge arrays there
4. Infinite recursion causes stack overflow
5. No need to manually free stack memory — it happens automatically

## Common Mistakes
- Returning a pointer to a local variable → dangling pointer (stack memory freed)
- Allocating huge arrays on the stack: `int arr[10000000];` → crash
- Infinite or deep recursion → stack overflow
