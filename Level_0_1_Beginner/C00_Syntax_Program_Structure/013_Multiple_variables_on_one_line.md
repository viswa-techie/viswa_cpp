# Multiple variables on one line

> **Level:** 0 — Absolute Beginner  
> **Category:** C00 — C++ Syntax & Program Structure  
> **Topic:** syntax

---

## Problem Statement
Declare and initialize multiple variables on a single line.

## Solutions
```cpp
int a, b, c;           // Three uninitialized ints
int x = 1, y = 2, z = 3;  // Three initialized ints
double pi = 3.14, e = 2.71;

// DANGER: pointer declaration trap
int* p, q;   // p is int*, but q is just int! NOT int*
int *p, *q;  // Both are int* — asterisk binds to the variable name

// BETTER: one declaration per line for clarity
int* p = nullptr;
int* q = nullptr;
```

## Key Takeaways
1. Comma separates variables of the same type
2. Pointer `*` binds to the variable name, not the type
3. Best practice: one variable per line for clarity, especially with pointers
