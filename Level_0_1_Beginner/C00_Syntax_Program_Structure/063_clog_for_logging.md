# clog for logging

> **Level:** 0 — Absolute Beginner  
> **Category:** C00 — C++ Syntax & Program Structure  
> **Topic:** syntax

---

## Problem Statement
Use `std::clog` for log messages — a buffered alternative to `cerr`.

## What You Need to Know
- `std::clog` writes to **stderr**, like `cerr`.
- Unlike `cerr`, `clog` is **buffered** — more efficient for logging.
- Use `clog` for non-critical log messages, `cerr` for errors.

## Comparison
```
Stream       Destination    Buffered    Use For
------       -----------    --------    -------
std::cout    stdout         Yes         Program output
std::cerr    stderr         No          Error messages
std::clog    stderr         Yes         Log messages
```

## Basic Usage
```cpp
#include <iostream>

int main() {
    std::clog << "[INFO] Program started\n";

    for (int i = 0; i < 5; ++i) {
        std::clog << "[INFO] Processing item " << i << "\n";
    }

    std::cerr << "[ERROR] Something went wrong!\n";  // Immediate
    std::clog << "[INFO] Program ending\n";

    return 0;
}
```

## When to Use Each
```cpp
#include <iostream>

int main() {
    // cout → user-facing output
    std::cout << "Hello, User!\n";

    // clog → developer-facing log (non-critical)
    std::clog << "[LOG] Processing request\n";

    // cerr → urgent error (must appear immediately)
    std::cerr << "[ERROR] Database connection failed!\n";

    return 0;
}
```

## Redirect Logging to File
```bash
# Both clog and cerr go to stderr
./program 2> log.txt
```

## Key Takeaways
1. `clog` writes to stderr but is buffered (unlike `cerr`)
2. Use `clog` for verbose logging — it's more efficient than `cerr`
3. Use `cerr` for critical errors that must appear immediately
4. Both go to stderr — they can be redirected together
5. In production, consider a proper logging library instead

## Common Mistakes
- Using `cerr` for all logging — inefficient due to no buffering
- Expecting `clog` and `cerr` to go to different destinations — both go to stderr
- Not flushing `clog` before program crash — log messages may be lost
