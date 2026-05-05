# Return value from function

> **Level:** 0 — Absolute Beginner  
> **Category:** C00 — C++ Syntax & Program Structure  
> **Topic:** syntax

---

## Problem Statement
Understand how return values work in C++ functions.

## What You Need to Know
- `return expression;` sends a value back to the caller.
- The return type is declared before the function name.
- A function can have multiple `return` statements but only one executes.

## Basic Return
```cpp
#include <iostream>

int getMax(int a, int b) {
    if (a > b) {
        return a;      // Returns here if a > b
    }
    return b;          // Returns here otherwise
}

int main() {
    int m = getMax(10, 20);
    std::cout << "Max: " << m << "\n";  // 20
    return 0;
}
```

## Return Different Types
```cpp
#include <iostream>
#include <string>

int getSquare(int n) {
    return n * n;          // Returns int
}

double getCircleArea(double r) {
    return 3.14159 * r * r;  // Returns double
}

bool isAdult(int age) {
    return age >= 18;       // Returns bool
}

std::string getGreeting(const std::string& name) {
    return "Hello, " + name + "!";  // Returns string
}

char getGrade(int score) {
    if (score >= 90) return 'A';
    if (score >= 80) return 'B';
    if (score >= 70) return 'C';
    return 'F';
}

int main() {
    std::cout << getSquare(5) << "\n";
    std::cout << getCircleArea(3.0) << "\n";
    std::cout << std::boolalpha << isAdult(20) << "\n";
    std::cout << getGreeting("Viswa") << "\n";
    std::cout << getGrade(85) << "\n";
    return 0;
}
```

## void — No Return Value
```cpp
void printBanner() {
    std::cout << "=== BANNER ===\n";
    // No return statement needed
    // But you CAN use "return;" to exit early
}

void printIfPositive(int n) {
    if (n <= 0) {
        return;   // Exit early — no value returned
    }
    std::cout << n << "\n";
}
```

## Return by Value (Copy)
```cpp
#include <iostream>
#include <vector>

std::vector<int> getNumbers() {
    std::vector<int> v = {1, 2, 3, 4, 5};
    return v;    // Returns a COPY (move semantics make this efficient)
}

int main() {
    std::vector<int> nums = getNumbers();
    for (int n : nums) std::cout << n << " ";
    std::cout << "\n";
    return 0;
}
```

## Key Takeaways
1. Return type must match (or be convertible to) what you return
2. `void` functions don't return a value — use `return;` for early exit
3. Multiple `return` statements are fine — only one executes per call
4. Returning objects (string, vector) is efficient due to move semantics
5. Every path through a non-void function should have a return statement

## Common Mistakes
- Missing return in non-void function → undefined behavior
- Not all code paths return a value → undefined behavior, compiler may warn
- Returning a reference to a local variable → dangling reference
