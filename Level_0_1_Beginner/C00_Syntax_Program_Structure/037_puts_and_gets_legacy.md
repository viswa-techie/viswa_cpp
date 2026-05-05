# puts and gets (legacy)

> **Level:** 0 — Absolute Beginner  
> **Category:** C00 — C++ Syntax & Program Structure  
> **Topic:** syntax

---

## Problem Statement
Understand the legacy C functions `puts` and `gets`, and why `gets` must never be used.

## What You Need to Know
- `puts()` outputs a string followed by a newline — simpler than `printf`.
- `gets()` reads a line from stdin — **removed from C11 and C++14** due to buffer overflow.
- Use `fgets()` or `std::getline()` instead of `gets()`.

## puts() — Simple String Output
```cpp
#include <cstdio>

int main() {
    puts("Hello, World!");    // Prints string + newline
    puts("Second line");

    // Equivalent to:
    printf("Hello, World!\n");
    return 0;
}
```

## gets() — NEVER USE THIS
```cpp
// DANGEROUS — DO NOT USE
#include <cstdio>

int main() {
    char buffer[10];
    gets(buffer);   // No bounds checking! Buffer overflow!
    // If user types more than 9 chars → memory corruption
    return 0;
}
```

## Safe Alternatives
```cpp
#include <iostream>
#include <string>
#include <cstdio>

int main() {
    // Option 1: fgets (C-style, safe)
    char buf[100];
    fgets(buf, sizeof(buf), stdin);  // Reads at most 99 chars

    // Option 2: std::getline (C++ style, preferred)
    std::string line;
    std::getline(std::cin, line);    // No buffer overflow possible
    std::cout << line << "\n";

    return 0;
}
```

## Comparison
```
Function    Header     Safe?    Notes
--------    ------     -----    -----
puts()      <cstdio>   Yes      Output only, adds \n
gets()      <cstdio>   NO!      REMOVED in C11/C++14
fgets()     <cstdio>   Yes      C-style safe input
getline()   <string>   Yes      C++ preferred input
```

## Key Takeaways
1. `puts(str)` is a simpler alternative to `printf("%s\n", str)`
2. **Never use `gets()`** — it was removed from the standard for safety
3. Use `fgets()` for C-style safe input, `std::getline()` for C++
4. `fgets()` keeps the trailing newline; you may need to strip it
5. Modern compilers warn or error on `gets()` usage

## Common Mistakes
- Using `gets()` at all — instant security vulnerability
- Forgetting that `fgets()` includes the trailing `\n`
- Confusing `puts()` with `printf()` — `puts` always adds a newline
