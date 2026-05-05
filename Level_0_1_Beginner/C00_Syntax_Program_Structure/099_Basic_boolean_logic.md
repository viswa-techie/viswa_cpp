# Basic boolean logic

> **Level:** 0 — Absolute Beginner  
> **Category:** C00 — C++ Syntax & Program Structure  
> **Topic:** syntax

---

## Problem Statement
Understand boolean operators and logic in C++.

## What You Need to Know
- `bool` type has two values: `true` (1) and `false` (0).
- Logical operators: `&&` (AND), `||` (OR), `!` (NOT).
- Comparison operators return `bool`: `==`, `!=`, `<`, `>`, `<=`, `>=`.

## Logical Operators
```cpp
#include <iostream>

int main() {
    bool a = true, b = false;

    std::cout << std::boolalpha;    // Print true/false instead of 1/0

    std::cout << "AND: " << (a && b) << "\n";   // false
    std::cout << "OR:  " << (a || b) << "\n";   // true
    std::cout << "NOT: " << (!a) << "\n";        // false

    return 0;
}
```

## Truth Tables
```
AND (&&)        OR (||)         NOT (!)
A     B  Result A     B  Result A    Result
true  true  true   true  true  true   true  false
true  false false  true  false true   false true
false true  false  false true  true
false false false  false false false
```

## Comparison Operators
```cpp
#include <iostream>

int main() {
    int x = 10, y = 20;

    std::cout << std::boolalpha;
    std::cout << (x == y) << "\n";   // false (equal)
    std::cout << (x != y) << "\n";   // true  (not equal)
    std::cout << (x < y)  << "\n";   // true  (less than)
    std::cout << (x > y)  << "\n";   // false (greater than)
    std::cout << (x <= y) << "\n";   // true  (less or equal)
    std::cout << (x >= y) << "\n";   // false (greater or equal)

    return 0;
}
```

## Combining Conditions
```cpp
#include <iostream>

int main() {
    int age = 25;
    bool hasLicense = true;

    // AND — both must be true
    if (age >= 18 && hasLicense) {
        std::cout << "Can drive\n";
    }

    // OR — at least one must be true
    int day = 6;
    if (day == 6 || day == 7) {
        std::cout << "Weekend\n";
    }

    // NOT — inverts
    bool isRaining = false;
    if (!isRaining) {
        std::cout << "Go outside\n";
    }

    return 0;
}
```

## Short-Circuit Evaluation
```cpp
#include <iostream>

int main() {
    int* ptr = nullptr;

    // AND short-circuits: if first is false, second is NOT evaluated
    if (ptr != nullptr && *ptr > 0) {
        // Safe — *ptr is never reached if ptr is null
    }

    // OR short-circuits: if first is true, second is NOT evaluated
    bool found = true;
    if (found || expensiveSearch()) {
        // expensiveSearch() is never called
    }

    return 0;
}
```

## Key Takeaways
1. `&&` = AND, `||` = OR, `!` = NOT
2. Short-circuit: `&&` stops on first false, `||` stops on first true
3. Use `std::boolalpha` to print "true"/"false" instead of "1"/"0"
4. Non-zero integers are `true`, zero is `false`
5. Parenthesize complex conditions for clarity

## Common Mistakes
- Using `=` (assignment) instead of `==` (comparison) in conditions
- Not understanding short-circuit → dereferencing null pointer
- `if (x = 5)` — always true! Use `if (x == 5)`
