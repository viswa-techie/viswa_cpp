# Conditional compilation (#ifdef)

> **Level:** 0 — Absolute Beginner  
> **Category:** C00 — C++ Syntax & Program Structure  
> **Topic:** syntax

---

## Problem Statement
Use `#ifdef`, `#ifndef`, `#if`, `#elif`, `#else`, `#endif` for conditional compilation.

## What You Need to Know
- Conditional directives include/exclude code at preprocessing time.
- The excluded code is completely removed — never compiled.
- Used for: debug mode, platform-specific code, feature flags.

## #ifdef / #ifndef
```cpp
#include <iostream>

#define DEBUG

int main() {
    #ifdef DEBUG
        std::cout << "Debug mode is ON\n";
    #endif

    #ifndef RELEASE
        std::cout << "Not in release mode\n";
    #endif

    std::cout << "Always printed\n";
    return 0;
}
```

## #if / #elif / #else
```cpp
#include <iostream>

#define VERSION 2

int main() {
    #if VERSION == 1
        std::cout << "Version 1\n";
    #elif VERSION == 2
        std::cout << "Version 2\n";
    #else
        std::cout << "Unknown version\n";
    #endif
    return 0;
}
```

## Platform-Specific Code
```cpp
#include <iostream>

int main() {
    #if defined(_WIN32)
        std::cout << "Windows\n";
    #elif defined(__linux__)
        std::cout << "Linux\n";
    #elif defined(__APPLE__)
        std::cout << "macOS\n";
    #else
        std::cout << "Unknown platform\n";
    #endif
    return 0;
}
```

## Define from Command Line
```bash
# Compile with DEBUG defined
g++ -DDEBUG main.cpp -o program

# Compile with VERSION=3
g++ -DVERSION=3 main.cpp -o program
```

## Debug Logging Pattern
```cpp
#include <iostream>

#ifdef DEBUG
    #define LOG(msg) std::cerr << "[DEBUG] " << __FILE__ << ":" << __LINE__ << " " << msg << "\n"
#else
    #define LOG(msg)   // Compiles to nothing in release
#endif

int main() {
    LOG("Starting program");
    int x = 42;
    LOG("x = " << x);
    return 0;
}
```

## Key Takeaways
1. `#ifdef X` — true if `X` is defined (any value, even empty)
2. `#ifndef X` — true if `X` is NOT defined
3. `#if` evaluates integer expressions
4. Use `-DNAME` on the command line to define macros
5. Always close with `#endif`

## Common Mistakes
- Forgetting `#endif` → cascading compilation errors
- `#ifdef 0` is always true (0 is defined as the identifier) — use `#if 0` instead
- `#if DEBUG` when DEBUG isn't defined → treated as 0 (false), no error
