# printf vs cout

> **Level:** 0 — Absolute Beginner  
> **Category:** C00 — C++ Syntax & Program Structure  
> **Topic:** syntax

---

## Problem Statement
Compare C-style `printf` with C++ `cout` and understand when to use each.

## What You Need to Know
- `printf` is from C (`<cstdio>`), uses format strings with `%` specifiers.
- `cout` is from C++ (`<iostream>`), uses the `<<` stream operator.
- Both produce the same output but have different trade-offs.

## Side-by-Side Comparison
```cpp
#include <iostream>
#include <cstdio>

int main() {
    int age = 30;
    double gpa = 3.85;
    const char* name = "Viswa";

    // printf style
    printf("Name: %s, Age: %d, GPA: %.2f\n", name, age, gpa);

    // cout style
    std::cout << "Name: " << name << ", Age: " << age
              << ", GPA: " << gpa << "\n";

    return 0;
}
```

## Format Specifiers (printf)
```
%d    int
%f    double/float
%s    C-string (char*)
%c    char
%x    hex
%o    octal
%p    pointer
%ld   long
%lld  long long
%u    unsigned int
%%    literal %
```

## Formatting Width and Precision
```cpp
#include <iostream>
#include <iomanip>
#include <cstdio>

int main() {
    double pi = 3.14159265;

    // printf: width 10, 4 decimal places
    printf("%10.4f\n", pi);    //     3.1416

    // cout: equivalent
    std::cout << std::setw(10) << std::fixed
              << std::setprecision(4) << pi << "\n";

    return 0;
}
```

## Comparison Table
```
Feature          printf              cout
-------          ------              ----
Header           <cstdio>            <iostream>
Type safety      No (runtime crash)  Yes (compile-time)
Extensible       No                  Yes (operator<<)
Format strings   Yes (%d, %s, ...)   No (use manipulators)
Performance      Generally faster    Slightly slower
Custom types     Not supported       Overload operator<<
```

## Key Takeaways
1. `cout` is type-safe — wrong type = compile error (not crash)
2. `printf` is more compact for formatted output
3. `cout` is extensible — works with user-defined types
4. In modern C++, prefer `cout` (or `std::format` in C++20)
5. `printf` can crash if format string doesn't match arguments

## Common Mistakes
- `printf("%d", 3.14)` — wrong specifier, undefined behavior
- Mixing `printf` and `cout` without syncing → output order issues
- Forgetting `\n` with `printf` (no `endl` equivalent)
