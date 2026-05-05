# Function prototypes concept

> **Level:** 0 — Absolute Beginner  
> **Category:** C00 — C++ Syntax & Program Structure  
> **Topic:** syntax

---

## Problem Statement
Understand function prototypes — declarations that tell the compiler about a function's interface.

## What You Need to Know
- A prototype declares a function's return type, name, and parameter types.
- It does NOT include the function body.
- Prototypes go at the top of the file or in header files.

## Syntax
```cpp
// Prototype (declaration only — no body)
return_type function_name(param_type1 param_name1, param_type2 param_name2);

// Examples:
int add(int a, int b);
void printMessage(const std::string& msg);
double calculateArea(double radius);
bool isEven(int n);
```

## Complete Example
```cpp
#include <iostream>
#include <string>

// Prototypes (declarations)
int add(int a, int b);
void greet(const std::string& name);
bool isPositive(int n);

int main() {
    std::cout << add(3, 4) << "\n";
    greet("Viswa");
    std::cout << std::boolalpha << isPositive(-5) << "\n";
    return 0;
}

// Definitions (must match prototypes exactly)
int add(int a, int b) {
    return a + b;
}

void greet(const std::string& name) {
    std::cout << "Hello, " << name << "!\n";
}

bool isPositive(int n) {
    return n > 0;
}
```

## Parameter Names Are Optional in Prototypes
```cpp
// These are all valid prototypes:
int add(int a, int b);      // With names (preferred for documentation)
int add(int, int);           // Without names (valid but less clear)
int add(int x, int y);      // Different names from definition (valid)
```

## Prototypes in Headers
```cpp
// math_utils.h
#pragma once
int add(int a, int b);
int multiply(int a, int b);

// math_utils.cpp
#include "math_utils.h"
int add(int a, int b) { return a + b; }
int multiply(int a, int b) { return a * b; }

// main.cpp
#include "math_utils.h"    // Gets the prototypes
int main() {
    return add(1, 2);
}
```

## Key Takeaways
1. Prototypes declare the interface without the body
2. Placed at the top of `.cpp` files or in `.h` header files
3. Parameter names are optional in prototypes
4. The definition must match the prototype's return type and parameter types
5. Headers are collections of prototypes (and other declarations)

## Common Mistakes
- Prototype doesn't match definition: `int add(int, int)` vs `double add(int, int)` → error
- Missing prototype: calling a function before it's declared → compile error
- Forgetting semicolon after prototype: `int add(int a, int b)` → compile error
