# Calling a function

> **Level:** 0 — Absolute Beginner  
> **Category:** C00 — C++ Syntax & Program Structure  
> **Topic:** syntax

---

## Problem Statement
Understand how to call functions, pass arguments, and use return values.

## What You Need to Know
- Call a function by writing its name followed by `()` with arguments.
- Arguments are copied into the function's parameters (pass by value).
- The return value can be used in expressions, assigned, or ignored.

## Basic Function Call
```cpp
#include <iostream>

int multiply(int a, int b) {
    return a * b;
}

int main() {
    // Call and use return value
    int result = multiply(5, 3);
    std::cout << result << "\n";  // 15

    // Call directly in expression
    std::cout << multiply(4, 7) << "\n";  // 28

    // Call and ignore return value
    multiply(2, 3);  // Legal but wasteful

    return 0;
}
```

## Arguments vs Parameters
```cpp
#include <iostream>

//            Parameters (formal)
//            ↓     ↓
void greet(std::string name, int times) {
    for (int i = 0; i < times; ++i) {
        std::cout << "Hello, " << name << "!\n";
    }
}

int main() {
    //    Arguments (actual values passed)
    //    ↓         ↓
    greet("Viswa", 3);
    return 0;
}
```

## Function Call Flow
```
main()                     multiply(5, 3)
  │                            │
  │  ──── call ────►           │ a = 5, b = 3
  │                            │ return 15
  │  ◄── return 15 ──          │
  │                            │
  │ result = 15                │
```

## Chaining Function Calls
```cpp
#include <iostream>
#include <cmath>

int square(int n) { return n * n; }
int add(int a, int b) { return a + b; }

int main() {
    // Nested calls
    int result = add(square(3), square(4));
    std::cout << result << "\n";   // 9 + 16 = 25

    // Using result of one call as argument to another
    std::cout << std::sqrt(add(9, 16)) << "\n";  // sqrt(25) = 5
    return 0;
}
```

## Key Takeaways
1. Call syntax: `functionName(arg1, arg2)`
2. Arguments are copied to parameters (pass by value by default)
3. Return value can be stored, used in expressions, or ignored
4. Functions can call other functions, including themselves (recursion)
5. Number and types of arguments must match the parameters

## Common Mistakes
- Wrong number of arguments: `add(1)` when `add(int, int)` → compile error
- Wrong argument type: `add("hello", 5)` → compile error
- Forgetting `()` on a call: `add` is a function pointer, `add()` calls it
