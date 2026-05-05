# constexpr intro

> **Level:** 0 — Absolute Beginner  
> **Category:** C00 — C++ Syntax & Program Structure  
> **Topic:** syntax

---

## Problem Statement
Understand `constexpr` — compile-time constant expressions in C++11 and later.

## What You Need to Know
- `constexpr` means "can be evaluated at compile time."
- Better than `#define` — it's typed, scoped, and debuggable.
- Available since C++11, significantly improved in C++14/17/20.

## constexpr Variables
```cpp
#include <iostream>

constexpr int MAX_SIZE = 100;        // Compile-time constant
constexpr double PI = 3.14159265;    // Compile-time constant

int main() {
    constexpr int N = 10;
    int arr[N];    // OK — N is known at compile time

    // constexpr int x = rand();  // ERROR — rand() is not constexpr
    std::cout << MAX_SIZE << " " << PI << "\n";
    return 0;
}
```

## constexpr Functions
```cpp
#include <iostream>

constexpr int square(int x) {
    return x * x;
}

constexpr int factorial(int n) {
    return (n <= 1) ? 1 : n * factorial(n - 1);
}

int main() {
    constexpr int s = square(5);     // Computed at COMPILE time
    constexpr int f = factorial(5);   // Computed at COMPILE time

    std::cout << "5² = " << s << "\n";   // 25
    std::cout << "5! = " << f << "\n";   // 120

    // Can also be called at runtime
    int x;
    std::cin >> x;
    std::cout << square(x) << "\n";  // Computed at runtime
    return 0;
}
```

## constexpr vs const vs #define
```
Feature        #define          const              constexpr
-------        -------          -----              ---------
Type safety    No               Yes                Yes
Scoped         No (global)      Yes                Yes
Debuggable     No               Yes                Yes
Compile-time   Text replace     Maybe              Guaranteed (if possible)
Functions      Macros only      No                 Yes
```

## constexpr with if (C++17)
```cpp
#include <iostream>

template<typename T>
void process(T value) {
    if constexpr (std::is_integral_v<T>) {
        std::cout << "Integer: " << value << "\n";
    } else {
        std::cout << "Not integer: " << value << "\n";
    }
}

int main() {
    process(42);      // Integer: 42
    process(3.14);    // Not integer: 3.14
    return 0;
}
```

## Key Takeaways
1. `constexpr` variables are guaranteed compile-time constants
2. `constexpr` functions CAN run at compile time (if args are constexpr)
3. Prefer `constexpr` over `#define` for constants
4. Use for array sizes, template arguments, compile-time computation
5. `constexpr` implies `inline` for functions

## Common Mistakes
- `constexpr int x = non_constexpr_func();` → compile error
- Confusing `const` (runtime constant) with `constexpr` (compile-time constant)
- Overly complex constexpr functions in C++11 (only one return statement allowed)
