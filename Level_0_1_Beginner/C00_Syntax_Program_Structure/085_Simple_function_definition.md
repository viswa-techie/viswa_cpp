# Simple function definition

> **Level:** 0 — Absolute Beginner  
> **Category:** C00 — C++ Syntax & Program Structure  
> **Topic:** syntax

---

## Problem Statement
Define and use simple functions in C++.

## What You Need to Know
- A function groups reusable code under a name.
- Syntax: `return_type name(parameters) { body }`
- Every function (except `void`) must return a value.

## Basic Function
```cpp
#include <iostream>

// Function definition
int add(int a, int b) {
    return a + b;
}

int main() {
    int result = add(3, 4);
    std::cout << result << "\n";  // 7
    return 0;
}
```

## Function Anatomy
```cpp
int add(int a, int b) {
//│   │   │         │
//│   │   └─────────┘── Parameters (input)
//│   └── Function name
//└── Return type

    return a + b;
//  └── Return statement (output)
}
```

## Multiple Functions
```cpp
#include <iostream>

int square(int n) {
    return n * n;
}

double average(int a, int b) {
    return static_cast<double>(a + b) / 2;
}

bool isEven(int n) {
    return n % 2 == 0;
}

int main() {
    std::cout << "5² = " << square(5) << "\n";
    std::cout << "Avg(3,7) = " << average(3, 7) << "\n";
    std::cout << "4 is even? " << std::boolalpha << isEven(4) << "\n";
    return 0;
}
```

## void Functions (No Return Value)
```cpp
#include <iostream>

void printLine() {
    std::cout << "================\n";
}

void printHeader(const std::string& title) {
    printLine();
    std::cout << title << "\n";
    printLine();
}

int main() {
    printHeader("REPORT");
    return 0;
}
```

## Key Takeaways
1. Functions have: return type, name, parameters, body
2. Use `return` to send a value back to the caller
3. `void` functions don't return a value (no `return` needed)
4. Functions should do ONE thing and do it well
5. Name functions with verbs: `calculateArea`, `printReport`, `isValid`

## Common Mistakes
- Forgetting `return` in a non-void function → undefined behavior
- Wrong return type: `int add(...)` but returning a `double` → truncation
- Defining a function inside another function → not allowed in standard C++
