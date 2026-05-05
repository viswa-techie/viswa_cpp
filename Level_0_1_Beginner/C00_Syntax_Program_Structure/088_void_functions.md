# void functions

> **Level:** 0 — Absolute Beginner  
> **Category:** C00 — C++ Syntax & Program Structure  
> **Topic:** syntax

---

## Problem Statement
Understand `void` functions — functions that perform an action without returning a value.

## What You Need to Know
- `void` means "no return value."
- Used when the function performs a side effect (printing, modifying data).
- You can use `return;` (without a value) for early exit.

## Basic void Function
```cpp
#include <iostream>

void sayHello() {
    std::cout << "Hello, World!\n";
}

void printSum(int a, int b) {
    std::cout << "Sum: " << (a + b) << "\n";
}

int main() {
    sayHello();          // Hello, World!
    printSum(3, 4);      // Sum: 7
    return 0;
}
```

## Early Return
```cpp
#include <iostream>

void printPositive(int n) {
    if (n <= 0) {
        std::cout << "Not positive!\n";
        return;    // Exit early — nothing more to do
    }
    std::cout << "Value: " << n << "\n";
}

int main() {
    printPositive(5);    // Value: 5
    printPositive(-3);   // Not positive!
    return 0;
}
```

## void Functions That Modify Data
```cpp
#include <iostream>
#include <vector>

void fillWithZeros(std::vector<int>& vec) {
    for (int& val : vec) {
        val = 0;
    }
}

void printVector(const std::vector<int>& vec) {
    for (int val : vec) {
        std::cout << val << " ";
    }
    std::cout << "\n";
}

int main() {
    std::vector<int> data = {1, 2, 3, 4, 5};
    printVector(data);     // 1 2 3 4 5
    fillWithZeros(data);
    printVector(data);     // 0 0 0 0 0
    return 0;
}
```

## When to Use void vs Return Value
```
Use void when:                   Use return when:
-----------------                ----------------
Printing output                  Computing a result
Modifying a reference parameter  Answering a question (bool)
Logging/debugging                Creating/building data
Setting state                    Transforming input
```

## Key Takeaways
1. `void` = "returns nothing"
2. Call void functions for their side effects (output, modifications)
3. Use `return;` (no value) for early exit from void functions
4. You CANNOT use a void function in an expression: `int x = sayHello();` → error
5. `void foo(void)` is valid C but just use `void foo()` in C++

## Common Mistakes
- Trying to return a value from void function: `return 42;` → error
- Using void function as an expression: `cout << sayHello()` → error
- Forgetting that void functions still execute code — just don't return a value
