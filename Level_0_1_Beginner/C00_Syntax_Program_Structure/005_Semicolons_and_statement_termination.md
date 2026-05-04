# Semicolons and statement termination

> **Level:** 0 — Absolute Beginner  
> **Category:** C00 — C++ Syntax & Program Structure  
> **Topic:** syntax

---

## Problem Statement
Understand why semicolons are required and where they go in C++.

## What You Need to Know
- C++ uses `;` to terminate statements (unlike Python which uses newlines).
- A **statement** is a complete instruction.
- Some constructs do NOT need semicolons: function bodies, if/else blocks, loops.
- Class/struct definitions DO need a semicolon after the closing brace.

## Examples
```cpp
int x = 5;           // variable declaration — needs ;
x = x + 1;           // assignment — needs ;
std::cout << x;      // expression statement — needs ;

if (x > 0) {         // NO semicolon after )
    x = 0;           // statement inside — needs ;
}                     // NO semicolon after }

struct Point {
    int x, y;
};                    // YES! Semicolon after class/struct closing brace

for (int i = 0; i < 10; ++i) {  // semicolons INSIDE for() separate clauses
    // ...
}                     // NO semicolon after loop body
```

## The Accidental Semicolon Bug
```cpp
// BUG: semicolon after if() creates an empty statement
if (x > 0);          // This empty statement always executes
{
    x = 0;            // This ALWAYS runs regardless of condition!
}

// BUG: semicolon after for() 
for (int i = 0; i < 10; ++i);  // Loop body is empty!
{
    std::cout << i;   // This runs ONCE, and `i` is out of scope
}
```

## Key Takeaways
1. Every statement ends with `;`
2. Control flow keywords (`if`, `for`, `while`) do NOT get `;` after `)`
3. Class/struct definitions need `;` after `}`
4. An accidental `;` after `if()` or `for()` is a silent logic bug
5. Use `-Wall` to catch some of these mistakes
