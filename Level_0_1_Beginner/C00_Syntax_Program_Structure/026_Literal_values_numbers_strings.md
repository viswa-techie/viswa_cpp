# Literal values (numbers, strings)

> **Level:** 0 — Absolute Beginner  
> **Category:** C00 — C++ Syntax & Program Structure  
> **Topic:** syntax

---

## Problem Statement
Understand the different kinds of literal values you can write directly in C++ code.

## What You Need to Know
- A **literal** is a fixed value written directly in source code.
- The compiler determines the type of a literal from its form.

## Integer Literals
```cpp
int a = 42;            // Decimal (base 10)
int b = 052;           // Octal (base 8) — starts with 0 → equals 42
int c = 0x2A;          // Hexadecimal (base 16) — starts with 0x → equals 42
int d = 0b101010;      // Binary (base 2, C++14) — starts with 0b → equals 42

// Digit separators (C++14) for readability
long big = 1'000'000;               // one million
int mask = 0b1111'0000'1111'0000;   // binary with separators
```

## Floating-Point Literals
```cpp
double a = 3.14;       // double by default
float b = 3.14f;       // f suffix → float
long double c = 3.14L; // L suffix → long double
double d = 6.02e23;    // Scientific notation: 6.02 × 10²³
double e = 1.5e-3;     // 0.0015
```

## Character and String Literals
```cpp
char ch = 'A';                    // Single character in single quotes
const char* s = "Hello";         // C-style string in double quotes
std::string str = "World";       // std::string from string literal
```

## Boolean Literals
```cpp
bool t = true;     // 1
bool f = false;    // 0
```

## Pointer Literal
```cpp
int* p = nullptr;  // C++11 null pointer (prefer over NULL or 0)
```

## Suffix Summary
```
Suffix    Type              Example
------    ----              -------
(none)    int / double      42, 3.14
u / U     unsigned int      42u
l / L     long              42L
ll / LL   long long         42LL
ul / UL   unsigned long     42UL
f / F     float             3.14f
L         long double       3.14L
```

## Key Takeaways
1. Integer default type is `int`; floating-point default is `double`
2. Use `0x` for hex, `0b` for binary, `0` prefix for octal
3. Use `'` digit separator (C++14) for large numbers: `1'000'000`
4. Use `nullptr` instead of `NULL` or `0` for null pointers
5. Suffix `f` for float literals, `L` for long/long double

## Common Mistakes
- Writing `052` thinking it's 52 — it's actually octal 42!
- Forgetting `f` suffix: `float x = 3.14;` triggers a narrowing warning
- Using `NULL` instead of `nullptr` — `NULL` is just `0` or `(void*)0`
