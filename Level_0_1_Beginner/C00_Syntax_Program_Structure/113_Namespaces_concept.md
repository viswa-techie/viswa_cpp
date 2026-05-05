# Namespaces concept

> **Level:** 0 — Absolute Beginner  
> **Category:** C00 — C++ Syntax & Program Structure  
> **Topic:** syntax

---

## Problem Statement
Understand namespaces — C++'s mechanism for organizing code and preventing name collisions.

## What You Need to Know
- A namespace groups names (functions, classes, variables) under a unique prefix.
- `std` is the standard library namespace.
- Without namespaces, two libraries with a function named `sort` would conflict.

## Why Namespaces?
```cpp
// Without namespaces:
// library1.h defines sort()
// library2.h also defines sort()
// → LINKER ERROR: multiple definitions of sort!

// With namespaces:
namespace lib1 {
    void sort() { /* ... */ }
}
namespace lib2 {
    void sort() { /* ... */ }
}
// lib1::sort() and lib2::sort() are separate — no conflict!
```

## Defining a Namespace
```cpp
#include <iostream>

namespace Math {
    const double PI = 3.14159265;

    double square(double x) {
        return x * x;
    }

    double circleArea(double r) {
        return PI * r * r;
    }
}

int main() {
    std::cout << Math::PI << "\n";
    std::cout << Math::square(5) << "\n";
    std::cout << Math::circleArea(3) << "\n";
    return 0;
}
```

## Accessing Namespace Members
```cpp
#include <iostream>

namespace Utils {
    void greet() { std::cout << "Hello!\n"; }
    int add(int a, int b) { return a + b; }
}

int main() {
    // Method 1: Fully qualified name (recommended)
    Utils::greet();

    // Method 2: using declaration (imports one name)
    using Utils::add;
    std::cout << add(3, 4) << "\n";

    // Method 3: using directive (imports everything — avoid in headers)
    using namespace Utils;
    greet();   // Works but risky in large programs

    return 0;
}
```

## Key Takeaways
1. Namespaces prevent name collisions between libraries
2. Access with `namespace::name` (scope resolution operator `::`)
3. `std` is the standard library namespace
4. `using namespace X;` is convenient but can cause collisions
5. Always use `namespace::name` in header files

## Common Mistakes
- `using namespace std;` in header files → forces it on everyone who includes the header
- Forgetting `::` → "name not declared" errors
- Creating a namespace with the same name as a standard one → confusion
