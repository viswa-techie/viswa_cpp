# Multiple return values intro

> **Level:** 0 — Absolute Beginner  
> **Category:** C00 — C++ Syntax & Program Structure  
> **Topic:** syntax

---

## Problem Statement
Return multiple values from a function — something `return` alone can't do.

## What You Need to Know
- A function can only `return` one value directly.
- To return multiple values, use: `struct`, `std::pair`, `std::tuple`, or output parameters.

## Method 1: Using std::pair
```cpp
#include <iostream>
#include <utility>

std::pair<int, int> minMax(int a, int b) {
    if (a < b) return {a, b};
    return {b, a};
}

int main() {
    auto [lo, hi] = minMax(7, 3);   // Structured binding (C++17)
    std::cout << "Min: " << lo << ", Max: " << hi << "\n";

    // Without structured binding:
    auto result = minMax(7, 3);
    std::cout << "Min: " << result.first << ", Max: " << result.second << "\n";
    return 0;
}
```

## Method 2: Using std::tuple
```cpp
#include <iostream>
#include <tuple>
#include <string>

std::tuple<std::string, int, double> getStudentInfo() {
    return {"Viswa", 25, 3.85};
}

int main() {
    auto [name, age, gpa] = getStudentInfo();  // C++17
    std::cout << name << ", " << age << ", " << gpa << "\n";

    // Without structured binding:
    auto info = getStudentInfo();
    std::cout << std::get<0>(info) << "\n";  // "Viswa"
    return 0;
}
```

## Method 3: Using a struct
```cpp
#include <iostream>

struct DivResult {
    int quotient;
    int remainder;
};

DivResult divide(int a, int b) {
    return {a / b, a % b};
}

int main() {
    auto [q, r] = divide(17, 5);
    std::cout << "17 / 5 = " << q << " remainder " << r << "\n";
    return 0;
}
```

## Method 4: Output Parameters (older style)
```cpp
#include <iostream>

void divide(int a, int b, int& quotient, int& remainder) {
    quotient = a / b;
    remainder = a % b;
}

int main() {
    int q, r;
    divide(17, 5, q, r);
    std::cout << q << " R " << r << "\n";
    return 0;
}
```

## Recommendation
```
Method            When to Use
------            -----------
struct            Named fields, used frequently
pair              Exactly 2 values, quick
tuple             3+ values, quick
Output params     Legacy code, performance-critical
```

## Key Takeaways
1. Use `std::pair` for 2 values, `std::tuple` for 3+
2. Use structs when values have meaningful names
3. Structured bindings (C++17) make all methods clean
4. Output parameters work but are less readable
5. Prefer returning values over output parameters

## Common Mistakes
- Using output parameters when pair/tuple would be clearer
- Forgetting `#include <tuple>` or `#include <utility>`
- Not using structured bindings when available (C++17)
