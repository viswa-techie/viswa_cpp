# Compiler flags overview

> **Level:** 0 — Absolute Beginner  
> **Category:** C00 — C++ Syntax & Program Structure  
> **Topic:** syntax

---

## Problem Statement
Understand common compiler flags for g++ and clang++.

## What You Need to Know
- Compiler flags control warnings, optimization, debugging, and standards.
- Flags start with `-` (dash).
- More flags = more information/control.

## Essential Flags
```bash
# Warning flags (always use these!)
g++ -Wall -Wextra -Wpedantic main.cpp -o main

# -Wall     : Enable most warnings
# -Wextra   : Enable extra warnings
# -Wpedantic: Enforce strict ISO C++ compliance
```

## Flag Categories
```bash
# WARNINGS
-Wall              # Most common warnings
-Wextra            # Additional useful warnings
-Werror            # Treat warnings as errors
-Wpedantic         # Strict standard compliance
-Wshadow           # Warn when variable shadows another
-Wconversion       # Warn on implicit type conversions

# DEBUGGING
-g                 # Include debug info (for gdb)
-g3                # Maximum debug info
-O0                # No optimization (default, best for debugging)

# OPTIMIZATION
-O1                # Basic optimization
-O2                # Standard optimization (recommended for release)
-O3                # Aggressive optimization
-Os                # Optimize for size

# STANDARD SELECTION
-std=c++11         # C++11 standard
-std=c++14         # C++14 standard
-std=c++17         # C++17 standard (recommended)
-std=c++20         # C++20 standard
-std=c++23         # C++23 standard

# OUTPUT CONTROL
-o name            # Set output filename
-c                 # Compile only (no linking) → .o file
-E                 # Preprocess only → stdout
-S                 # Compile to assembly → .s file
```

## Recommended Combinations
```bash
# Learning/Development
g++ -std=c++17 -Wall -Wextra -g -O0 main.cpp -o main

# Release build
g++ -std=c++17 -Wall -Wextra -O2 -DNDEBUG main.cpp -o main

# Maximum safety during development
g++ -std=c++17 -Wall -Wextra -Wpedantic -Werror -Wshadow \
    -Wconversion -g -O0 main.cpp -o main
```

## Key Takeaways
1. `-Wall -Wextra` — always use these for better code quality
2. `-g` — essential for debugging with gdb
3. `-std=c++17` — explicitly set the C++ standard
4. `-O2` — good optimization for release builds
5. `-Werror` — treat warnings as errors (use during development)

## Common Mistakes
- Compiling without any warnings → missing bugs
- Using `-O2` while debugging → variables optimized away
- Not specifying `-std=c++17` → getting old default standard
- Forgetting `-g` → "no debugging symbols" when using gdb
