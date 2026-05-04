# Case sensitivity

> **Level:** 0 — Absolute Beginner  
> **Category:** C00 — C++ Syntax & Program Structure  
> **Topic:** syntax

---

## Problem Statement
Understand that C++ is case-sensitive and how this affects your code.

## What You Need to Know
- `myVar`, `MyVar`, `MYVAR`, and `myvar` are FOUR DIFFERENT identifiers.
- Keywords are lowercase: `int`, `if`, `return` (NOT `Int`, `IF`, `Return`).
- Standard library names follow conventions: `std::cout`, `std::vector`.

## Examples
```cpp
int count = 5;
int Count = 10;
int COUNT = 15;
// These are three separate variables!

// This is WRONG:
Int x = 5;     // Error: 'Int' is not a type
Return 0;      // Error: 'Return' is not a keyword

// Conventions:
int myVariable;        // camelCase (common in C++)
int my_variable;       // snake_case (common in C++ STL style)
const int MAX_SIZE = 100;  // UPPER_SNAKE_CASE for constants
class MyClass {};      // PascalCase for classes
```

## Key Takeaways
1. C++ is fully case-sensitive
2. Keywords are always lowercase
3. Follow your project's naming convention consistently
4. Common: `camelCase` for variables, `PascalCase` for classes, `UPPER_CASE` for constants
