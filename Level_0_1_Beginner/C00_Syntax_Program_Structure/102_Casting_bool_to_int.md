# Casting bool to int

> **Level:** 0 — Absolute Beginner  
> **Category:** C00 — C++ Syntax & Program Structure  
> **Topic:** syntax

---

## Problem Statement
Understand implicit and explicit conversions between `bool` and `int`.

## What You Need to Know
- `true` converts to `1`, `false` converts to `0`.
- Non-zero integers convert to `true`, zero converts to `false`.
- These conversions happen implicitly in most contexts.

## Bool to Int
```cpp
#include <iostream>

int main() {
    bool a = true;
    bool b = false;

    int x = a;    // x = 1
    int y = b;    // y = 0

    // Useful for counting true values
    int count = (5 > 3) + (10 > 20) + (7 == 7);
    std::cout << "True count: " << count << "\n";  // 2

    return 0;
}
```

## Int to Bool
```cpp
#include <iostream>

int main() {
    bool a = 42;     // true (non-zero)
    bool b = 0;      // false
    bool c = -1;     // true (non-zero)

    std::cout << std::boolalpha;
    std::cout << a << " " << b << " " << c << "\n";
    // true false true

    return 0;
}
```

## Practical Use: Counting Conditions
```cpp
#include <iostream>
#include <vector>

int main() {
    std::vector<int> nums = {-3, 0, 5, -1, 8, 0, 2};

    int positives = 0;
    for (int n : nums) {
        positives += (n > 0);   // true = 1, false = 0
    }

    std::cout << "Positive count: " << positives << "\n";  // 3
    return 0;
}
```

## Explicit Casting
```cpp
#include <iostream>

int main() {
    int value = 42;

    // Implicit conversion (works, but less clear)
    bool b1 = value;

    // Explicit conversion (preferred — shows intent)
    bool b2 = static_cast<bool>(value);
    int i = static_cast<int>(true);

    std::cout << std::boolalpha << b2 << "\n";  // true
    std::cout << i << "\n";                       // 1
    return 0;
}
```

## Key Takeaways
1. `true` → 1, `false` → 0 (guaranteed by the standard)
2. Non-zero → `true`, zero → `false`
3. `(condition)` evaluates to 0 or 1 — useful for counting
4. Use `static_cast<bool>()` or `static_cast<int>()` for clarity
5. Implicit conversions work but can hide bugs

## Common Mistakes
- `if (x == true)` when x is 42 → `42 == 1` → false! Use `if (x)` instead
- Assuming bool stores only 0 or 1 in memory — uninitialized bool can have other values
- Narrowing: `bool b{42};` may warn with brace initialization
