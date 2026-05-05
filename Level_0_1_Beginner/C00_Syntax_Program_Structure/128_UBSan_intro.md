# UBSan intro

> **Level:** 0 — Absolute Beginner  
> **Category:** C00 — C++ Syntax & Program Structure  
> **Topic:** syntax

---

## Problem Statement
Use UndefinedBehaviorSanitizer (UBSan) to detect undefined behavior at runtime.

## What You Need to Know
- Undefined behavior (UB) means the C++ standard doesn't define what happens.
- UB can cause crashes, wrong results, or "work fine" — unpredictably.
- UBSan instruments your code to catch UB at runtime.

## Basic Usage
```bash
# Compile with UBSan
g++ -std=c++17 -g -fsanitize=undefined main.cpp -o main

# Run — UBSan reports UB as it happens
./main
```

## What UBSan Catches
```cpp
// 1. Signed integer overflow
int x = INT_MAX;
x += 1;     // UBSan: "signed integer overflow"

// 2. Division by zero
int a = 10, b = 0;
int c = a / b;    // UBSan: "division by zero"

// 3. Null pointer dereference
int* p = nullptr;
*p = 42;    // UBSan: "null pointer dereference"

// 4. Out-of-bounds array access
int arr[5];
arr[10] = 0;    // UBSan: "index 10 out of bounds"

// 5. Shift overflow
int x = 1;
x << 33;    // UBSan: "shift exponent 33 is too large for 32-bit type"

// 6. Misaligned pointer
char buf[10];
int* p = (int*)(buf + 1);   // UBSan: "misaligned address"
```

## UBSan Output Example
```
main.cpp:8:15: runtime error: signed integer overflow:
2147483647 + 1 cannot be represented in type 'int'
SUMMARY: UndefinedBehaviorSanitizer: undefined-behavior main.cpp:8:15
```

## Combining Sanitizers
```bash
# ASan + UBSan together (recommended)
g++ -g -fsanitize=address,undefined main.cpp -o main

# All common sanitizers
g++ -g -fsanitize=address,undefined -fno-omit-frame-pointer main.cpp -o main
```

## Key Takeaways
1. `-fsanitize=undefined` catches undefined behavior at runtime
2. Catches: integer overflow, null dereference, bad shifts, division by zero
3. Combine with ASan: `-fsanitize=address,undefined`
4. Always use `-g` for readable diagnostics
5. Run tests with UBSan regularly — UB causes subtle, hard-to-find bugs

## Common Mistakes
- Assuming "it works on my machine" means no UB exists
- Not testing with UBSan → shipping code with undefined behavior
- Relying on specific UB behavior (e.g., signed overflow wrapping)
