# Linker errors vs compile errors

> **Level:** 0 — Absolute Beginner  
> **Category:** C00 — C++ Syntax & Program Structure  
> **Topic:** syntax

---

## Problem Statement
Understand the difference between compilation errors and linker errors.

## Compile Errors (Caught During Compilation)
```cpp
// Syntax error — compiler catches this
int x = ;  // ERROR: expected expression

// Type error — compiler catches this
int x = "hello";  // ERROR: cannot initialize int with string
```
**Pattern:** Error message says "error:" with source file and line number.

## Linker Errors (Caught During Linking)
```cpp
// file1.cpp
void doSomething();  // Declaration only — no definition anywhere

int main() {
    doSomething();  // Compiles fine! But linker can't find the definition
    return 0;
}
// LINKER ERROR: undefined reference to 'doSomething()'
```
**Pattern:** Error message says "undefined reference to" or "unresolved external symbol".

## How to Tell the Difference
| Compile Error | Linker Error |
|--------------|-------------|
| Shows source file + line number | Shows function/symbol name |
| Says "error:" | Says "undefined reference" |
| Syntax/type problem | Missing implementation |
| Fix: correct the code | Fix: add missing implementation or library |

## Common Linker Error Fixes
```bash
# Missing library
g++ main.cpp -lm          # Link math library
g++ main.cpp -lpthread    # Link pthread library

# Missing source file
g++ main.cpp utils.cpp    # Include ALL source files
```

## Key Takeaways
1. Compile errors = language mistakes (syntax, types)
2. Linker errors = missing implementations (function body, library)
3. Fix compile errors first, then linker errors
