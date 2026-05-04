# Whitespace and indentation rules

> **Level:** 0 — Absolute Beginner  
> **Category:** C00 — C++ Syntax & Program Structure  
> **Topic:** syntax

---

## Problem Statement
Understand how C++ treats whitespace and learn consistent indentation practices.

## What You Need to Know
- C++ is a **free-form language** — whitespace (spaces, tabs, newlines) is ignored by the compiler between tokens.
- Indentation is purely for human readability.
- String literals preserve whitespace: `"hello world"` keeps the space.
- Preprocessor directives (`#include`, `#define`) must start at the beginning of a line.

## Examples
```cpp
// All of these compile identically:
int x=5;
int x = 5;
int
    x
        =
            5
                ;

// But readable code uses consistent style:
int x = 5;
```

## Common Indentation Styles
```cpp
// K&R / "One True Brace Style" (most common in C++)
if (condition) {
    doSomething();
} else {
    doOther();
}

// Allman style
if (condition)
{
    doSomething();
}
else
{
    doOther();
}

// Google C++ Style: 2 spaces, K&R braces
// LLVM Style: 2 spaces, K&R braces
// Linux Kernel Style: 8-space tabs (C, not C++)
```

## Tool: clang-format
```bash
# Auto-format your code
clang-format -i myfile.cpp            # in-place format
clang-format -style=google myfile.cpp  # Google style
```

## Key Takeaways
1. Compiler ignores whitespace between tokens
2. Pick ONE style and be consistent
3. Use `clang-format` to auto-format
4. 2 or 4 spaces per indent level is standard
5. Never mix tabs and spaces
