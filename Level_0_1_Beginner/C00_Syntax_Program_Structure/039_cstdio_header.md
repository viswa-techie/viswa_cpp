# cstdio header

> **Level:** 0 — Absolute Beginner  
> **Category:** C00 — C++ Syntax & Program Structure  
> **Topic:** syntax

---

## Problem Statement
Understand the `<cstdio>` header and C-style I/O functions available in C++.

## What You Need to Know
- `<cstdio>` is the C++ version of C's `<stdio.h>`.
- It provides `printf`, `scanf`, `fprintf`, `fopen`, `fclose`, etc.
- Functions are placed in the `std` namespace (though often also in global scope).

## Key Functions
```
Function         Purpose
--------         -------
printf()         Formatted output to stdout
scanf()          Formatted input from stdin
fprintf()        Formatted output to a file
fscanf()         Formatted input from a file
sprintf()        Formatted output to a string (buffer overflow risk)
snprintf()       Safe formatted output to a string
fopen()          Open a file
fclose()         Close a file
fgets()          Read a line from a file/stdin
fputs()          Write a string to a file/stdout
puts()           Write a string + newline to stdout
```

## Common Usage
```cpp
#include <cstdio>

int main() {
    // Output
    std::printf("Hello, %s! You are %d years old.\n", "Viswa", 30);

    // Input
    int x;
    std::printf("Enter a number: ");
    std::scanf("%d", &x);
    std::printf("You entered: %d\n", x);

    return 0;
}
```

## File I/O with cstdio
```cpp
#include <cstdio>

int main() {
    FILE* fp = std::fopen("output.txt", "w");
    if (fp) {
        std::fprintf(fp, "Hello from file!\n");
        std::fclose(fp);
    }
    return 0;
}
```

## snprintf — Safe String Formatting
```cpp
#include <cstdio>
#include <iostream>

int main() {
    char buffer[50];
    int n = std::snprintf(buffer, sizeof(buffer),
                          "Score: %d/%d", 85, 100);
    std::printf("%s (wrote %d chars)\n", buffer, n);
    return 0;
}
```

## Key Takeaways
1. `<cstdio>` wraps C's `<stdio.h>` in the `std` namespace
2. Prefer `<cstdio>` over `<stdio.h>` in C++ code
3. `printf/scanf` lack type safety — use `cout/cin` when possible
4. Use `snprintf` instead of `sprintf` to prevent buffer overflow
5. File operations: `fopen` → `fprintf/fgets` → `fclose`

## Common Mistakes
- Using `<stdio.h>` instead of `<cstdio>` in C++ — works but not standard
- `sprintf` buffer overflow — always use `snprintf` with a size limit
- Forgetting `&` in `scanf`: `scanf("%d", x)` → undefined behavior
