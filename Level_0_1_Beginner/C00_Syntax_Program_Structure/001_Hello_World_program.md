# Hello World program

> **Level:** 0 — Absolute Beginner  
> **Category:** C00 — C++ Syntax & Program Structure  
> **Topic:** syntax

---

## Problem Statement
Write a program that prints "Hello, World!" to the console.

## What You Need to Know
- Every C++ program needs a `main()` function as its entry point.
- `#include <iostream>` provides `std::cout` for output.
- `std::cout` is the standard character output stream.
- `<<` is the stream insertion operator.
- Every statement ends with a semicolon `;`.

## Mental Model
Think of `cout` as a conveyor belt going to the screen. You use `<<` to place items onto the belt.

## Solution 1: Minimal (Using namespace)
```cpp
#include <iostream>
using namespace std;

int main() {
    cout << "Hello, World!" << endl;
    return 0;
}
```
**Explanation:** `using namespace std;` lets us write `cout` instead of `std::cout`. `endl` outputs a newline and flushes the buffer.  
**Time:** O(1) | **Space:** O(1)

## Solution 2: Without `using namespace std` (Recommended)
```cpp
#include <iostream>

int main() {
    std::cout << "Hello, World!" << std::endl;
    return 0;
}
```
**Why this is better:** Avoids polluting the global namespace. In large projects, `using namespace std;` can cause name collisions.

## Solution 3: Using `\n` instead of `endl`
```cpp
#include <iostream>

int main() {
    std::cout << "Hello, World!\n";
    return 0;
}
```
**Why this matters:** `\n` is faster than `endl` because `endl` flushes the output buffer. In performance-critical code, prefer `\n`.

## Solution 4: Using C-style printf
```cpp
#include <cstdio>

int main() {
    printf("Hello, World!\n");
    return 0;
}
```
**Note:** `printf` is from C. It's sometimes faster but lacks type safety of `cout`.

## Key Takeaways
1. `#include <iostream>` is needed for I/O
2. `main()` returns `int` (0 means success)
3. `<<` chains multiple outputs: `cout << "a" << "b";`
4. Prefer `std::cout` over `using namespace std;` in production code
5. Prefer `\n` over `endl` unless you need to flush

## Common Mistakes
- Forgetting `#include <iostream>` → compile error
- Missing semicolon at end of statement
- Using `"` vs `'` — double quotes for strings, single for chars
- Writing `cout` without `std::` and without `using namespace std`

## Pattern
**Output pattern** — When you need to display something: `std::cout << value;`

## Similar Problems
- Print your name
- Print multiple lines
- Print a formatted table
