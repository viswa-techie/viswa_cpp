# Identifiers & naming rules

> **Level:** 0 — Absolute Beginner  
> **Category:** C00 — C++ Syntax & Program Structure  
> **Topic:** syntax

---

## Problem Statement
Learn the rules for valid C++ identifiers (variable names, function names, etc.).

## Rules
1. Can contain: letters (a-z, A-Z), digits (0-9), underscore (_)
2. Must START with a letter or underscore (NOT a digit)
3. Cannot be a C++ keyword (`int`, `class`, `return`, etc.)
4. No spaces or special characters
5. Names starting with `_` followed by uppercase or `__` are RESERVED for the compiler

## Examples
```cpp
int age;          // ✓ valid
int _count;       // ✓ valid (but avoid leading underscore in global scope)
int player1;      // ✓ valid
int my_var;       // ✓ valid

int 1st_place;    // ✗ starts with digit
int my-var;       // ✗ contains hyphen
int my var;       // ✗ contains space
int class;        // ✗ is a keyword
int __reserved;   // ✗ double underscore — reserved for implementation
int _Uppercase;   // ✗ underscore + uppercase — reserved
```

## Naming Conventions
```cpp
// Google C++ Style:
int my_variable;           // variables: snake_case
void MyFunction();         // functions: PascalCase
class MyClass {};          // classes: PascalCase
const int kMaxSize = 100;  // constants: k + PascalCase
int member_var_;           // class members: trailing underscore

// LLVM Style:
int MyVariable;            // variables: PascalCase
void myFunction();         // functions: camelCase
```

## Key Takeaways
1. Start with letter or underscore
2. No special characters except underscore
3. Don't use reserved names (`__x`, `_Uppercase`)
4. Be descriptive: `count` > `c`, `studentAge` > `sa`
5. Single-letter names OK for loop indices: `i`, `j`, `k`
