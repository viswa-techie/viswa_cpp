# flush output buffer

> **Level:** 0 — Absolute Beginner  
> **Category:** C00 — C++ Syntax & Program Structure  
> **Topic:** syntax

---

## Problem Statement
Understand output buffering and how to manually flush the buffer.

## What You Need to Know
- Output is **buffered**: data is collected in memory before being sent to the screen.
- The buffer is flushed (written to screen) when: it's full, `\n` is printed (line-buffered), `endl` is used, `flush` is called, or the program ends.
- Flushing too often hurts performance. Not flushing can lose output on crash.

## What Is Buffering?
```
Your code:          cout << "Hello" << "World" << ...
                         ↓
Buffer (memory):    [H][e][l][l][o][W][o][r][l][d]...
                         ↓   (flush)
Screen/File:        HelloWorld...
```

## Ways to Flush
```cpp
#include <iostream>

int main() {
    // Method 1: std::endl (newline + flush)
    std::cout << "Hello" << std::endl;

    // Method 2: std::flush (flush without newline)
    std::cout << "Processing..." << std::flush;

    // Method 3: Manual flush call
    std::cout << "Data";
    std::cout.flush();

    // Method 4: \n (usually flushes on terminals, not files)
    std::cout << "Done\n";

    return 0;
}
```

## When Flushing Matters
```cpp
#include <iostream>
#include <chrono>
#include <thread>

int main() {
    // Progress indicator — needs flush to show immediately
    for (int i = 0; i < 10; ++i) {
        std::cout << "." << std::flush;   // Without flush, dots appear all at once
        // simulate work
    }
    std::cout << " Done!\n";

    // Prompt before input — needs flush
    std::cout << "Enter name: " << std::flush;
    std::string name;
    std::getline(std::cin, name);

    return 0;
}
```

## Performance Impact
```cpp
#include <iostream>

int main() {
    // SLOW: endl flushes every line
    for (int i = 0; i < 100000; ++i) {
        std::cout << i << std::endl;     // Flush on every iteration!
    }

    // FAST: \n doesn't force a flush
    for (int i = 0; i < 100000; ++i) {
        std::cout << i << "\n";          // Buffer handles flushing
    }

    return 0;
}
```

## Key Takeaways
1. Buffering collects output in memory before writing — it's an optimization
2. Use `\n` instead of `endl` for better performance
3. Use `std::flush` when you need output to appear immediately
4. `endl` = `"\n" + flush`
5. `cerr` is unbuffered (auto-flushes), `cout` and `clog` are buffered

## Common Mistakes
- Using `endl` everywhere → significantly slower I/O
- Not flushing before input prompts → prompt appears after user types
- Expecting debug output to appear before crash without flushing
