# Common compile errors

> **Level:** 0 — Absolute Beginner  
> **Category:** C00 — C++ Syntax & Program Structure  
> **Topic:** syntax

---

## Problem Statement
Recognize and fix the most common C++ compilation errors.

## Error 1: Missing semicolon
```cpp
int x = 5   // ERROR: expected ';' at end of declaration
int y = 10;
```
**Fix:** Add `;` after `5`.

## Error 2: Undeclared identifier
```cpp
cout << "hello";  // ERROR: 'cout' was not declared in this scope
```
**Fix:** Add `#include <iostream>` and use `std::cout`.

## Error 3: Type mismatch
```cpp
int x = "hello";  // ERROR: cannot initialize int with string literal
```
**Fix:** Use `std::string x = "hello";`

## Error 4: Missing return statement
```cpp
int add(int a, int b) {
    int result = a + b;
    // WARNING: no return statement
}
```
**Fix:** Add `return result;`

## Error 5: Mismatched braces
```cpp
if (x > 0) {
    std::cout << "positive";
// ERROR: expected '}' at end of input
```
**Fix:** Add closing `}`.

## Error 6: Redefinition
```cpp
int x = 5;
int x = 10;  // ERROR: redefinition of 'x'
```
**Fix:** Use `x = 10;` (assignment, not declaration).

## Key Takeaways
1. Read error messages carefully — the line number is often BEFORE the actual error
2. Fix errors from TOP to BOTTOM (later errors are often caused by earlier ones)
3. Common pattern: if you see 100 errors, fix the first one and recompile
