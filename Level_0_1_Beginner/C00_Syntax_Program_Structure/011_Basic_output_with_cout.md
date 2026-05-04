# Basic output with cout

> **Level:** 0 — Absolute Beginner  
> **Category:** C00 — C++ Syntax & Program Structure  
> **Topic:** syntax

---

## Problem Statement
Display output to the console using `std::cout`.

## Solutions
```cpp
#include <iostream>

int main() {
    // String output
    std::cout << "Hello, World!\n";

    // Variable output
    int x = 42;
    std::cout << "x = " << x << "\n";

    // Chained output
    std::cout << "a=" << 1 << " b=" << 2.5 << " c=" << 'Z' << "\n";

    // Formatted output
    double pi = 3.14159;
    std::cout << std::fixed;          // fixed-point notation
    std::cout.precision(2);           // 2 decimal places
    std::cout << "Pi = " << pi << "\n";  // Pi = 3.14

    return 0;
}
```

## Key Takeaways
1. `<<` chains multiple values
2. `\n` for newline (faster than `endl`)
3. `std::fixed` + `precision()` for decimal formatting
4. `cout` buffers output — use `endl` or `flush` to force immediate display
