# Macro constants

> **Level:** 0 — Absolute Beginner  
> **Category:** C00 — C++ Syntax & Program Structure  
> **Topic:** syntax

---

## Problem Statement
Understand function-like macros and their pitfalls compared to inline functions.

## What You Need to Know
- Macros can take parameters like functions: `#define NAME(params) body`.
- They perform text substitution — not function calls.
- Parentheses are critical to avoid bugs.

## Object-like vs Function-like Macros
```cpp
#include <iostream>

// Object-like macro (constant)
#define PI 3.14159

// Function-like macro
#define SQUARE(x) ((x) * (x))
#define MAX(a, b) ((a) > (b) ? (a) : (b))
#define ABS(x) ((x) < 0 ? -(x) : (x))

int main() {
    std::cout << SQUARE(5) << "\n";   // 25
    std::cout << MAX(10, 20) << "\n"; // 20
    std::cout << ABS(-7) << "\n";     // 7
    return 0;
}
```

## The Parenthesis Problem
```cpp
#include <iostream>

// BAD: Missing parentheses
#define BAD_SQUARE(x) x * x

// GOOD: Proper parentheses
#define GOOD_SQUARE(x) ((x) * (x))

int main() {
    // BAD_SQUARE(2+3) expands to: 2+3 * 2+3 = 2+6+3 = 11 (WRONG!)
    std::cout << BAD_SQUARE(2+3) << "\n";   // 11, not 25!

    // GOOD_SQUARE(2+3) expands to: ((2+3) * (2+3)) = 25 (CORRECT)
    std::cout << GOOD_SQUARE(2+3) << "\n";  // 25
    return 0;
}
```

## Double Evaluation Problem
```cpp
#include <iostream>

#define MAX(a, b) ((a) > (b) ? (a) : (b))

int main() {
    int x = 5;
    // MAX(x++, 3) expands to: ((x++) > (3) ? (x++) : (3))
    // x gets incremented TWICE if x > 3!
    int result = MAX(x++, 3);  // x becomes 7, not 6!
    std::cout << result << ", x=" << x << "\n";
    return 0;
}
```

## Modern Alternative: Inline Functions
```cpp
#include <iostream>
#include <algorithm>

// Prefer this over macros
inline int square(int x) {
    return x * x;
}

int main() {
    int x = 5;
    std::cout << square(2 + 3) << "\n";   // 25 (correct!)
    std::cout << std::max(x++, 3) << "\n"; // No double evaluation
    return 0;
}
```

## Key Takeaways
1. Always wrap macro parameters and the whole body in parentheses
2. Macros evaluate arguments multiple times — beware of side effects
3. Prefer `inline` functions or `constexpr` functions over macros
4. Macros have no type checking or scope
5. Macros are still used for: include guards, `__FILE__`, `__LINE__`, conditional compilation

## Common Mistakes
- Missing parentheses: `#define SQ(x) x*x` → wrong results with expressions
- Side effects: `MAX(i++, j)` → `i` incremented twice
- Semicolons in macros: `#define FOO(x) { bar(x); }` breaks in `if` without braces
