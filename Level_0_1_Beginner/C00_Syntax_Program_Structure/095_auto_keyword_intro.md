# auto keyword intro

> **Level:** 0 — Absolute Beginner  
> **Category:** C00 — C++ Syntax & Program Structure  
> **Topic:** syntax

---

## Problem Statement
Use the `auto` keyword to let the compiler deduce variable types automatically.

## What You Need to Know
- `auto` tells the compiler to figure out the type from the initializer.
- Available since C++11.
- The type is still fixed at compile time — C++ is NOT dynamically typed.

## Basic Usage
```cpp
#include <iostream>
#include <vector>
#include <string>

int main() {
    auto x = 42;            // int
    auto pi = 3.14;         // double
    auto name = std::string("Viswa");  // std::string
    auto flag = true;       // bool
    auto ch = 'A';          // char

    std::cout << x << " " << pi << " " << name << "\n";
    return 0;
}
```

## Where auto Shines
```cpp
#include <iostream>
#include <vector>
#include <map>

int main() {
    std::vector<int> nums = {1, 2, 3, 4, 5};
    std::map<std::string, int> scores = {{"Alice", 95}, {"Bob", 87}};

    // Without auto — verbose
    for (std::vector<int>::iterator it = nums.begin(); it != nums.end(); ++it) {
        std::cout << *it << " ";
    }

    // With auto — clean
    for (auto it = nums.begin(); it != nums.end(); ++it) {
        std::cout << *it << " ";
    }

    // Even better — range-for with auto
    for (const auto& [name, score] : scores) {
        std::cout << name << ": " << score << "\n";
    }

    return 0;
}
```

## auto with Functions (C++14)
```cpp
// C++14: auto return type deduction
auto add(int a, int b) {
    return a + b;   // Compiler deduces return type as int
}

// C++11: trailing return type
auto multiply(int a, int b) -> int {
    return a * b;
}
```

## When NOT to Use auto
```cpp
// AVOID when type is not obvious
auto result = compute();     // What type is result? Unclear!

// PREFER explicit type when it aids readability
int count = getItemCount();  // Clear: count is an int
```

## Key Takeaways
1. `auto` deduces type from the initializer — must always initialize
2. Use for iterators, complex template types, lambdas
3. Avoid when the type isn't obvious from context
4. `auto` is compile-time — NOT like Python/JS dynamic typing
5. `const auto&` for read-only references, `auto&` for mutable references

## Common Mistakes
- `auto x;` without initializer → compile error (can't deduce type)
- `auto` drops references and const: `auto x = ref` makes a copy
- Overusing auto makes code hard to read: `auto x = foo(bar(baz()));`
