# Using -Wall flag

> **Level:** 0 — Absolute Beginner  
> **Category:** C00 — C++ Syntax & Program Structure  
> **Topic:** syntax

---

## Problem Statement
Understand the `-Wall` compiler flag and related warning flags.

## Flag Overview
```bash
g++ -Wall main.cpp         # Common warnings
g++ -Wall -Wextra main.cpp # More warnings
g++ -Wall -Wextra -Wpedantic main.cpp  # Strict standard compliance
g++ -Wall -Werror main.cpp # Treat all warnings as errors
```

## What -Wall Enables (partial list)
- `-Wunused-variable`: unused variables
- `-Wuninitialized`: potentially uninitialized variables
- `-Wreturn-type`: missing return in non-void function
- `-Wparentheses`: ambiguous expressions that need parentheses
- `-Wsign-compare`: signed/unsigned comparison
- `-Wformat`: printf format string mismatches

## What -Wextra Adds
- `-Wunused-parameter`: unused function parameters
- `-Wmissing-field-initializers`: missing struct initializers

## Recommended Compile Command
```bash
g++ -std=c++17 -Wall -Wextra -Wpedantic -Wshadow -Wconversion -g main.cpp -o prog
```

## Key Takeaways
1. `-Wall` doesn't enable ALL warnings (misleading name)
2. `-Wextra` adds important additional warnings
3. Use `-Werror` in CI/CD to prevent warning accumulation
4. `-Wshadow` catches variable shadowing bugs
5. `-Wconversion` catches implicit narrowing conversions
