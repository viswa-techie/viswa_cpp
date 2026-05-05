# std::endl flushing

> **Level:** 0 — Absolute Beginner  
> **Category:** C00 — C++ Syntax & Program Structure  
> **Topic:** syntax

---

## Problem Statement
Understand what `std::endl` does, why it's slower than `\n`, and when to use each.

## What You Need to Know
- `std::endl` does TWO things: outputs `\n` AND flushes the buffer.
- `\n` only outputs a newline character — no flush.
- Flushing after every line is usually unnecessary and slow.

## endl vs \n
```cpp
#include <iostream>

int main() {
    // These produce the same visible output:
    std::cout << "Hello" << std::endl;   // Newline + flush
    std::cout << "Hello" << "\n";        // Newline only (faster)
    std::cout << "Hello\n";             // Same as above
    return 0;
}
```

## Performance Difference
```cpp
#include <iostream>
#include <chrono>

int main() {
    auto start = std::chrono::steady_clock::now();

    for (int i = 0; i < 100000; ++i) {
        std::cout << i << std::endl;    // Slow! Flushes 100,000 times
    }

    auto end = std::chrono::steady_clock::now();
    auto ms = std::chrono::duration_cast<std::chrono::milliseconds>(end - start);
    std::cerr << "endl: " << ms.count() << " ms\n";

    // Now with \n:
    start = std::chrono::steady_clock::now();
    for (int i = 0; i < 100000; ++i) {
        std::cout << i << "\n";         // Fast! Buffer handles flushing
    }
    end = std::chrono::steady_clock::now();
    ms = std::chrono::duration_cast<std::chrono::milliseconds>(end - start);
    std::cerr << "\\n: " << ms.count() << " ms\n";

    return 0;
}
```
Typical result: `endl` can be 5-10x slower than `\n`.

## When to Use endl
```cpp
// USE endl when you need guaranteed immediate output:

// 1. Before a crash-prone section
std::cout << "About to do risky operation" << std::endl;

// 2. Interactive prompts (though cout << flush also works)
std::cout << "Enter value: " << std::endl;

// 3. Logging critical events
std::cout << "CRITICAL: System shutting down" << std::endl;
```

## When to Use \n
```cpp
// USE \n for everything else (the vast majority of cases):
for (const auto& item : items) {
    std::cout << item << "\n";
}
```

## Key Takeaways
1. `std::endl` = `\n` + `flush` — use sparingly
2. `\n` is faster — use for normal output
3. `endl` can be 5-10x slower in loops
4. Only use `endl` when you need immediate, guaranteed output
5. In competitive programming, always use `\n`

## Common Mistakes
- Using `endl` in every output statement → massive slowdown
- Thinking `\n` and `endl` are identical — they're not
- Using `endl` in tight loops processing millions of lines
