# Overloading intro (concept only)

> **Level:** 0 — Absolute Beginner  
> **Category:** C00 — C++ Syntax & Program Structure  
> **Topic:** syntax

---

## Problem Statement
Understand function overloading — having multiple functions with the same name but different parameters.

## What You Need to Know
- **Overloading**: same function name, different parameter types or count.
- The compiler chooses the correct version based on the arguments.
- Return type alone does NOT distinguish overloads.

## Basic Overloading
```cpp
#include <iostream>
#include <string>

// Three functions, same name, different parameters
void print(int x) {
    std::cout << "Integer: " << x << "\n";
}

void print(double x) {
    std::cout << "Double: " << x << "\n";
}

void print(const std::string& x) {
    std::cout << "String: " << x << "\n";
}

int main() {
    print(42);          // Calls print(int)
    print(3.14);        // Calls print(double)
    print("Hello");     // Calls print(string) - implicit conversion
    return 0;
}
```

## Overloading by Parameter Count
```cpp
#include <iostream>

int add(int a, int b) {
    return a + b;
}

int add(int a, int b, int c) {
    return a + b + c;
}

int main() {
    std::cout << add(1, 2) << "\n";      // Calls 2-param version: 3
    std::cout << add(1, 2, 3) << "\n";   // Calls 3-param version: 6
    return 0;
}
```

## What Distinguishes Overloads
```
CAN distinguish:              CANNOT distinguish:
-----------------              -------------------
Different parameter types      Different return type only
Different parameter count      Different parameter names
const vs non-const ref         
```

```cpp
// INVALID — return type alone doesn't distinguish
int getValue();
double getValue();    // ERROR: cannot overload by return type
```

## How the Compiler Chooses
```
1. Exact match
2. Promotion (char → int, float → double)
3. Standard conversion (int → double, int → long)
4. User-defined conversion
5. If ambiguous → compile error
```

## Key Takeaways
1. Same name, different parameters = overloading
2. The compiler picks the best match automatically
3. Return type alone cannot distinguish overloads
4. Overloading makes APIs more intuitive: `print(42)`, `print("hi")`
5. Too many overloads can cause ambiguity errors

## Common Mistakes
- Trying to overload by return type only → compile error
- Ambiguous overloads: `foo(int)` and `foo(double)` — calling `foo(42L)` may be ambiguous
- Confusing overloading (same scope) with overriding (inheritance)
