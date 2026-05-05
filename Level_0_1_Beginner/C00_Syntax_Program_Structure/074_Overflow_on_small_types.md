# Overflow on small types

> **Level:** 0 — Absolute Beginner  
> **Category:** C00 — C++ Syntax & Program Structure  
> **Topic:** syntax

---

## Problem Statement
Understand integer overflow — what happens when a value exceeds a type's range.

## What You Need to Know
- Each integer type has a fixed range (e.g., `int` is typically -2³¹ to 2³¹-1).
- Overflow is **undefined behavior** for signed integers.
- Unsigned integers wrap around (modular arithmetic).

## Type Ranges
```
Type              Bytes   Min                    Max
----              -----   ---                    ---
char              1       -128                   127
unsigned char     1       0                      255
short             2       -32,768                32,767
unsigned short    2       0                      65,535
int               4       -2,147,483,648         2,147,483,647
unsigned int      4       0                      4,294,967,295
long long         8       -9.2×10¹⁸              9.2×10¹⁸
```

## Overflow Example
```cpp
#include <iostream>
#include <climits>

int main() {
    // Signed overflow — UNDEFINED BEHAVIOR!
    int max_int = INT_MAX;   // 2,147,483,647
    std::cout << "INT_MAX: " << max_int << "\n";
    std::cout << "INT_MAX + 1: " << max_int + 1 << "\n";  // UB! Often wraps to INT_MIN

    // Unsigned overflow — well-defined wrapping
    unsigned int umax = UINT_MAX;  // 4,294,967,295
    std::cout << "UINT_MAX: " << umax << "\n";
    std::cout << "UINT_MAX + 1: " << umax + 1 << "\n";  // 0 (wraps around)

    return 0;
}
```

## Small Type Overflow
```cpp
#include <iostream>

int main() {
    // char: range -128 to 127
    char c = 127;
    c = c + 1;    // Overflow! Result is implementation-defined
    std::cout << static_cast<int>(c) << "\n";  // Often -128

    // short: range -32768 to 32767
    short s = 32767;
    s = s + 1;    // Overflow!
    std::cout << s << "\n";  // Often -32768

    return 0;
}
```

## Detecting Overflow Before It Happens
```cpp
#include <iostream>
#include <climits>

int safe_add(int a, int b) {
    if (b > 0 && a > INT_MAX - b) {
        std::cerr << "Overflow detected!\n";
        return INT_MAX;
    }
    if (b < 0 && a < INT_MIN - b) {
        std::cerr << "Underflow detected!\n";
        return INT_MIN;
    }
    return a + b;
}

int main() {
    std::cout << safe_add(INT_MAX, 1) << "\n";    // Overflow detected
    std::cout << safe_add(100, 200) << "\n";       // 300
    return 0;
}
```

## Key Takeaways
1. Signed integer overflow is **undefined behavior** — anything can happen
2. Unsigned integers wrap around (defined, modular arithmetic)
3. Use `<climits>` for `INT_MAX`, `INT_MIN`, etc.
4. Use larger types (`long long`) when values might exceed `int` range
5. Check before arithmetic to prevent overflow

## Common Mistakes
- Assuming signed overflow wraps like unsigned — it's UB
- Using `int` for large values (e.g., factorial of 20)
- Multiplying two ints without checking: `50000 * 50000` overflows int
- `char` arithmetic: `char + char` promotes to `int`, but storing back in `char` may overflow
