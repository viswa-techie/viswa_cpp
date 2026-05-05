# One-definition rule basics

> **Level:** 0 — Absolute Beginner  
> **Category:** C00 — C++ Syntax & Program Structure  
> **Topic:** syntax

---

## Problem Statement
Understand the One Definition Rule (ODR) — a fundamental C++ rule that governs definitions.

## What You Need to Know
- **ODR**: Each entity (function, variable, class) can be **defined** only once in the entire program.
- **Declarations** (prototypes) can appear multiple times.
- **Definitions** (with body/value) must appear exactly once (with exceptions).

## Declaration vs Definition
```cpp
// DECLARATIONS (can appear multiple times)
int add(int a, int b);          // Function declaration
extern int globalVar;            // Variable declaration
class MyClass;                   // Class forward declaration

// DEFINITIONS (must appear exactly once)
int add(int a, int b) {         // Function definition (has body)
    return a + b;
}
int globalVar = 42;              // Variable definition (has value)
class MyClass {                  // Class definition (has body)
    int x;
};
```

## ODR Violation Example
```cpp
// file1.cpp
int add(int a, int b) { return a + b; }

// file2.cpp
int add(int a, int b) { return a + b; }  // ODR VIOLATION!
// Linker error: multiple definition of `add`
```

## Exceptions to ODR
```cpp
// These CAN appear in multiple translation units (must be identical):

// 1. Inline functions
inline int square(int x) { return x * x; }

// 2. constexpr functions
constexpr int cube(int x) { return x * x * x; }

// 3. Class definitions (in headers — same definition everywhere)
struct Point { int x, y; };

// 4. Template definitions
template<typename T>
T getMax(T a, T b) { return (a > b) ? a : b; }
```

## The Header Problem
```cpp
// math.h (BAD — violates ODR when included by multiple .cpp files)
int add(int a, int b) { return a + b; }  // Definition in header!

// math.h (GOOD — declaration only)
int add(int a, int b);  // Declaration

// math.h (GOOD — inline makes it ODR-safe)
inline int add(int a, int b) { return a + b; }
```

## Key Takeaways
1. ONE definition per function/variable across the entire program
2. Multiple declarations are OK (and normal — headers contain declarations)
3. `inline`, `constexpr`, templates, and class definitions are exceptions
4. Violating ODR = linker error ("multiple definition of...")
5. Headers should contain declarations, not definitions (unless inline/template)

## Common Mistakes
- Defining functions in headers without `inline` → linker error
- Defining global variables in headers → multiple definitions
- Two different definitions of the same entity → undefined behavior
