# Static analysis basics

> **Level:** 0 — Absolute Beginner  
> **Category:** C00 — C++ Syntax & Program Structure  
> **Topic:** syntax

---

## Problem Statement
Use static analysis tools to find bugs without running your code.

## What You Need to Know
- **Static analysis** examines source code without executing it.
- Finds bugs that compilers miss: memory leaks, null dereferences, logic errors.
- Complements testing — catches bugs before they happen.

## Compiler Warnings (First Line of Defense)
```bash
# Enable maximum warnings — this IS static analysis
g++ -Wall -Wextra -Wpedantic -Wshadow -Wconversion -Werror main.cpp

# Key warnings explained:
# -Wall       : Common warnings (uninitialized vars, unused results)
# -Wextra     : Extra warnings (unused parameters, sign comparisons)
# -Wshadow    : Variable shadows another variable
# -Wconversion: Implicit narrowing conversions
# -Werror     : Treat all warnings as errors
```

## clang-tidy
```bash
# Install
sudo apt install clang-tidy

# Run on a file
clang-tidy main.cpp -- -std=c++17

# Common checks it finds:
# - Modernize: suggest auto, range-for, nullptr
# - Bugprone: suspicious constructs
# - Performance: unnecessary copies
# - Readability: naming conventions
```

## cppcheck
```bash
# Install
sudo apt install cppcheck

# Basic usage
cppcheck main.cpp

# Thorough check
cppcheck --enable=all --std=c++17 main.cpp

# Example findings:
# [main.cpp:10]: (error) Array 'arr[5]' accessed at index 10
# [main.cpp:15]: (warning) Unused variable 'x'
# [main.cpp:20]: (style) Variable 'count' is assigned but never used
```

## Example: What Static Analysis Finds
```cpp
int* getPointer(bool flag) {
    int* p = nullptr;
    if (flag) {
        p = new int(42);
    }
    return p;    // cppcheck: possible null pointer returned
}

void example() {
    int arr[5];
    for (int i = 0; i <= 5; ++i) {   // clang-tidy: off-by-one (i <= 5)
        arr[i] = i;                    // Buffer overflow when i=5
    }
}
```

## Tools Summary
```
Tool               Type         Cost      Depth
----               ----         ----      -----
g++ -Wall          Compiler     Free      Basic
clang-tidy         Linter       Free      Deep
cppcheck           Analyzer     Free      Deep
PVS-Studio         Analyzer     Paid      Very deep
SonarQube          Platform     Free/Paid Enterprise
```

## Key Takeaways
1. Always compile with `-Wall -Wextra` — free bug detection
2. `clang-tidy` modernizes code and catches subtle bugs
3. `cppcheck` finds memory errors and logic issues
4. Static analysis catches bugs BEFORE runtime — cheaper to fix
5. Use multiple tools — each catches different issues

## Common Mistakes
- Ignoring compiler warnings → missing real bugs
- Running analysis only once → should be part of CI/CD
- Blindly applying all suggestions → some may not apply to your codebase
