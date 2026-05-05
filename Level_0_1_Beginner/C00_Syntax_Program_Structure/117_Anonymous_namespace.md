# Anonymous namespace

> **Level:** 0 — Absolute Beginner  
> **Category:** C00 — C++ Syntax & Program Structure  
> **Topic:** syntax

---

## Problem Statement
Use anonymous (unnamed) namespaces to make symbols file-local.

## What You Need to Know
- An anonymous namespace has no name: `namespace { ... }`.
- Everything inside is visible only within the current translation unit (file).
- It's the modern C++ replacement for `static` at file scope.

## Basic Usage
```cpp
// helpers.cpp

namespace {
    // These are only visible in this file
    int helperCounter = 0;

    void internalProcess() {
        ++helperCounter;
    }
}

void publicFunction() {
    internalProcess();     // Can use within this file
    // helperCounter and internalProcess are hidden from other files
}
```

## Comparison with static
```cpp
// C-style: using static for file-local
static int fileLocalVar = 42;
static void fileLocalFunc() { /* ... */ }

// Modern C++: using anonymous namespace
namespace {
    int fileLocalVar = 42;
    void fileLocalFunc() { /* ... */ }
}

// Both achieve the same result — anonymous namespace is preferred in C++
```

## Why Anonymous Namespace?
```cpp
// Without anonymous namespace or static:
// helper.cpp
int counter = 0;        // Visible to ALL files via extern
void reset() { counter = 0; }  // Also visible externally

// other.cpp
extern int counter;     // Can access helper.cpp's counter!

// With anonymous namespace:
// helper.cpp
namespace {
    int counter = 0;         // Only visible in helper.cpp
    void reset() { counter = 0; }
}
// other.cpp
// extern int counter;   // LINKER ERROR — counter doesn't exist externally
```

## What Goes in Anonymous Namespaces
```
Good candidates:              Don't put here:
- Helper functions            - Functions needed by other files
- File-local constants        - Public API
- Internal state variables    - Types used in headers
- Implementation details      
```

## Key Takeaways
1. `namespace { ... }` makes everything inside file-local
2. Preferred over `static` for file-scoped variables/functions in C++
3. Prevents linker conflicts — no other file can see these symbols
4. Use for implementation details that shouldn't be exposed
5. Works for variables, functions, classes, and types

## Common Mistakes
- Putting types in anonymous namespace that are used in headers → ODR violation
- Using `static` when anonymous namespace is more idiomatic in C++
- Forgetting that anonymous namespace symbols still have external linkage (technically)
