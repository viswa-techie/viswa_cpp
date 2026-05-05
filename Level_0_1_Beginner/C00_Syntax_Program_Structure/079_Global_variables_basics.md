# Global variables basics

> **Level:** 0 — Absolute Beginner  
> **Category:** C00 — C++ Syntax & Program Structure  
> **Topic:** syntax

---

## Problem Statement
Understand global variables — their behavior, uses, and why they should be avoided.

## What You Need to Know
- A global variable is declared outside all functions.
- It's accessible from any function in the same file (and across files with `extern`).
- It has static storage duration — exists for the entire program.

## Basic Example
```cpp
#include <iostream>

int count = 0;    // Global variable

void increment() {
    ++count;      // Can access global directly
}

void print() {
    std::cout << "Count: " << count << "\n";
}

int main() {
    increment();
    increment();
    print();      // Count: 2
    return 0;
}
```

## Global vs Local
```cpp
#include <iostream>

int x = 100;    // Global x

int main() {
    int x = 42;  // Local x — shadows the global
    std::cout << x << "\n";     // 42 (local)
    std::cout << ::x << "\n";   // 100 (global, using scope resolution)
    return 0;
}
```

## Across Files (extern)
```cpp
// config.cpp
int maxRetries = 3;    // Definition

// main.cpp
extern int maxRetries;  // Declaration (no memory allocated)
// Now main.cpp can use maxRetries
```

## Why Globals Are Discouraged
```
Problem              Description
-------              -----------
Hidden dependencies  Functions secretly depend on global state
Hard to test         Can't test functions in isolation
Thread safety        Multiple threads can corrupt shared data
Name collisions      Two globals with same name → linker error
Initialization order Globals in different files: undefined init order
```

## Better Alternatives
```cpp
// Instead of global:
// int config_value = 42;

// Option 1: Pass as parameter
void process(int config) { /* ... */ }

// Option 2: Use a namespace
namespace Config {
    const int value = 42;
}

// Option 3: Use a function (lazy initialization, thread-safe)
int getConfig() {
    static int value = 42;
    return value;
}
```

## Key Takeaways
1. Global variables are declared outside all functions
2. They're zero-initialized automatically
3. Use `extern` to share across files
4. **Avoid globals** — pass data through parameters instead
5. If you must use globals, make them `const`

## Common Mistakes
- Overusing globals → spaghetti code with hidden dependencies
- Name shadowing: local variable hides global → confusing bugs
- `static` global ≠ regular global: `static` limits scope to the file
