# Chained cout statements

> **Level:** 0 — Absolute Beginner  
> **Category:** C00 — C++ Syntax & Program Structure  
> **Topic:** syntax

---

## Problem Statement
Output multiple values in a single `cout` statement using chaining.

## Solution
```cpp
#include <iostream>

int main() {
    std::string name = "Alice";
    int age = 30;
    double gpa = 3.95;

    // Chained output
    std::cout << "Name: " << name 
              << ", Age: " << age 
              << ", GPA: " << gpa 
              << "\n";

    // How it works internally:
    // std::cout << "Name: "   → returns reference to cout
    //           << name       → returns reference to cout
    //           << ", Age: "  → returns reference to cout
    //           << age        → returns reference to cout
    //           << "\n"       → returns reference to cout

    return 0;
}
```

## Key Takeaways
1. Each `<<` returns a reference to `cout`, enabling chaining
2. You can mix types: strings, ints, doubles, chars
3. Break long chains across lines for readability
