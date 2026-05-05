# Local variables basics

> **Level:** 0 — Absolute Beginner  
> **Category:** C00 — C++ Syntax & Program Structure  
> **Topic:** syntax

---

## Problem Statement
Understand local variables — scope, lifetime, and best practices.

## What You Need to Know
- A local variable is declared inside a function or block `{}`.
- It only exists within that block — not accessible outside.
- It's created when the block is entered and destroyed when it exits.

## Basic Local Variables
```cpp
#include <iostream>

void greet() {
    std::string message = "Hello!";   // Local to greet()
    std::cout << message << "\n";
}   // message is destroyed here

int main() {
    int x = 10;    // Local to main()
    greet();
    // std::cout << message;  // ERROR: message not in scope
    return 0;
}
```

## Block Scope
```cpp
#include <iostream>

int main() {
    int x = 10;

    {   // New block
        int y = 20;        // Local to this block
        std::cout << x << "\n";   // OK — x is in outer scope
        std::cout << y << "\n";   // OK — y is in scope
    }
    // std::cout << y;    // ERROR: y is out of scope

    if (x > 5) {
        int z = 30;        // Local to if-block
        std::cout << z << "\n";
    }
    // std::cout << z;    // ERROR: z is out of scope

    return 0;
}
```

## Variable Shadowing
```cpp
#include <iostream>

int main() {
    int x = 10;
    std::cout << "Outer x: " << x << "\n";   // 10

    {
        int x = 20;   // Shadows outer x (same name, different variable)
        std::cout << "Inner x: " << x << "\n";   // 20
    }

    std::cout << "Outer x: " << x << "\n";   // 10 (unchanged)
    return 0;
}
```

## Declare Close to First Use
```cpp
#include <iostream>
#include <vector>

int main() {
    // BAD: Declare everything at top (C style)
    // int x, y, z;
    // ... 50 lines later ...
    // x = computeX();

    // GOOD: Declare where first used
    std::vector<int> data = {1, 2, 3, 4, 5};

    int sum = 0;
    for (int val : data) {
        sum += val;
    }

    double average = static_cast<double>(sum) / data.size();
    std::cout << "Average: " << average << "\n";
    return 0;
}
```

## Key Takeaways
1. Local variables exist only within their enclosing `{}`
2. They're created on the stack, destroyed when scope exits
3. Declare variables close to where they're first used
4. Inner variables can shadow outer ones (same name)
5. Local variables are NOT automatically initialized — always initialize

## Common Mistakes
- Trying to use a variable outside its scope
- Variable shadowing (same name in inner/outer scope) → confusing bugs
- Forgetting to initialize: `int x;` → garbage value
- Returning a reference/pointer to a local variable → dangling reference
