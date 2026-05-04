# endl vs \n

> **Level:** 0 — Absolute Beginner  
> **Category:** C00 — C++ Syntax & Program Structure  
> **Topic:** syntax

---

## Problem Statement
Understand the difference between `std::endl` and `\n` for newlines.

## Comparison
```cpp
#include <iostream>

int main() {
    // Using \n — just inserts a newline character
    std::cout << "Line 1\n";
    std::cout << "Line 2\n";

    // Using endl — inserts newline AND flushes the buffer
    std::cout << "Line 3" << std::endl;
    std::cout << "Line 4" << std::endl;

    return 0;
}
```

## What "Flushing" Means
```
Without flush:
  Program writes to buffer → [H][e][l][l][o][\n] → waits until buffer is full → THEN sends to screen

With flush (endl):
  Program writes to buffer → [H][e][l][l][o][\n] → IMMEDIATELY sends to screen
```

## Performance Test
```cpp
#include <iostream>
#include <chrono>

int main() {
    auto start = std::chrono::high_resolution_clock::now();
    for (int i = 0; i < 100000; ++i)
        std::cout << i << "\n";     // FAST
    auto end = std::chrono::high_resolution_clock::now();
    // Using endl would be ~5-10x slower for this loop
    return 0;
}
```

## When to Use Which
| Use `\n` | Use `endl` |
|-----------|-----------|
| Normal output | Debugging (ensure output appears before crash) |
| Loops with lots of output | Interactive prompts (before reading input) |
| Performance-critical code | Before `cin` operations |

## Key Takeaways
1. `\n` = newline only (fast)
2. `endl` = newline + flush (slow)
3. Default: use `\n`. Use `endl` only when you NEED to flush.
