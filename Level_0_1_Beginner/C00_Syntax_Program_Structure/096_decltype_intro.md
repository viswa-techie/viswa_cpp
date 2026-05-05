# decltype intro

> **Level:** 0 — Absolute Beginner  
> **Category:** C00 — C++ Syntax & Program Structure  
> **Topic:** syntax

---

## Problem Statement
Use `decltype` to get the type of an expression at compile time.

## What You Need to Know
- `decltype(expr)` gives you the type of `expr` without evaluating it.
- Useful when you need a type but don't want to spell it out.
- Available since C++11.

## Basic Usage
```cpp
#include <iostream>

int main() {
    int x = 42;
    decltype(x) y = 100;     // y is int (same type as x)

    double pi = 3.14;
    decltype(pi) e = 2.71;   // e is double

    std::cout << y << " " << e << "\n";
    return 0;
}
```

## decltype vs auto
```cpp
#include <iostream>

int main() {
    int x = 42;
    int& ref = x;

    auto a = ref;           // a is int (auto drops reference)
    decltype(ref) b = x;    // b is int& (decltype preserves reference)

    b = 100;
    std::cout << x << "\n";  // 100 (b is a reference to x)
    return 0;
}
```

## decltype with Expressions
```cpp
#include <iostream>

int main() {
    int x = 5;

    decltype(x + 1) result = 0;     // int (x+1 is an int expression)
    decltype(x * 1.5) pi = 3.14;    // double (int * double = double)

    return 0;
}
```

## Practical Use: Template Functions
```cpp
#include <iostream>

template<typename A, typename B>
auto add(A a, B b) -> decltype(a + b) {
    return a + b;
}

int main() {
    auto r1 = add(3, 4);       // int
    auto r2 = add(3, 4.5);     // double
    std::cout << r1 << " " << r2 << "\n";
    return 0;
}
```

## Key Takeaways
1. `decltype(expr)` gives the exact type of the expression
2. Unlike `auto`, `decltype` preserves references and const
3. The expression is NOT evaluated — only its type is inspected
4. Useful in templates to deduce return types
5. Rarely needed in simple code — `auto` is usually sufficient

## Common Mistakes
- Confusing `auto` (drops references) with `decltype` (preserves them)
- `decltype(x)` vs `decltype((x))` — with parentheses, it becomes a reference!
- Overusing `decltype` when `auto` would be simpler
