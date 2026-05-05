# Undefined behavior intro

> **Level:** 0 — Absolute Beginner  
> **Category:** C00 — C++ Syntax & Program Structure  
> **Topic:** syntax

---

## Problem Statement
Understand undefined behavior (UB) in C++ — the most dangerous concept for beginners.

## What You Need to Know
- **Undefined Behavior** means the C++ standard says "anything can happen."
- The program might work, crash, produce wrong results, or do something completely unexpected.
- Compilers are allowed to assume UB never happens — this enables aggressive optimizations.

## Common Sources of Undefined Behavior
```cpp
#include <iostream>

int main() {
    // 1. Signed integer overflow
    int x = 2147483647;
    x = x + 1;    // UB!

    // 2. Reading uninitialized variables
    int y;
    std::cout << y;  // UB!

    // 3. Null pointer dereference
    int* p = nullptr;
    *p = 42;        // UB!

    // 4. Array out of bounds
    int arr[5];
    arr[10] = 99;   // UB!

    // 5. Division by zero
    int z = 42 / 0;  // UB!

    // 6. Use after free (will learn later)
    // 7. Data races in multithreaded programs

    return 0;
}
```

## Why UB Is Dangerous
```cpp
#include <iostream>

int main() {
    // This code has UB — signed overflow
    // The compiler may REMOVE the check entirely!
    int x = 100;
    for (int i = 0; i < 10; ++i) {
        x += 1000000000;
    }

    // Compiler thinks: "x can't overflow (that would be UB),
    // so this condition is always true/false" → removes code!
    if (x > 0) {
        std::cout << "Positive\n";
    }
    return 0;
}
```

## UB vs Implementation-Defined vs Unspecified
```
Category               Meaning                         Example
--------               -------                         -------
Undefined              Anything can happen              Null deref, signed overflow
Implementation-defined Compiler chooses, must document  sizeof(int), char signedness
Unspecified            Compiler chooses, need not doc    Order of function arg evaluation
Well-defined           Standard guarantees behavior     unsigned overflow wraps
```

## Detecting UB
```bash
# Compile with sanitizers
g++ -fsanitize=undefined -g main.cpp -o program
./program
# Runtime error: signed integer overflow

# Also useful:
g++ -fsanitize=address -g main.cpp -o program  # Memory errors
```

## Key Takeaways
1. UB means "anything can happen" — your program is broken
2. Common UB: overflow, uninitialized reads, null deref, out-of-bounds
3. UB might "work" today and break tomorrow with a different compiler
4. Compilers optimize assuming no UB — this can remove your safety checks!
5. Use `-fsanitize=undefined` to detect UB at runtime

## Common Mistakes
- "It works on my machine" → UB can appear to work but is still broken
- Relying on signed overflow wrapping → the compiler may optimize it away
- Not using sanitizers → UB silently corrupts data
