# Print-based debugging

> **Level:** 0 — Absolute Beginner  
> **Category:** C00 — C++ Syntax & Program Structure  
> **Topic:** syntax

---

## Problem Statement
Use print statements to debug C++ programs — the simplest debugging technique.

## What You Need to Know
- Print debugging (printf debugging) means adding output statements to trace program flow.
- Quick and easy — no debugger setup required.
- Works everywhere, including embedded systems and remote servers.

## Basic Print Debugging
```cpp
#include <iostream>

int factorial(int n) {
    std::cerr << "[DEBUG] factorial(" << n << ") called\n";
    if (n <= 1) return 1;
    int result = n * factorial(n - 1);
    std::cerr << "[DEBUG] factorial(" << n << ") = " << result << "\n";
    return result;
}

int main() {
    std::cerr << "[DEBUG] Starting program\n";
    int result = factorial(5);
    std::cout << "5! = " << result << "\n";
    return 0;
}
```

## Why Use cerr Instead of cout?
```cpp
// cerr is unbuffered — output appears immediately
std::cerr << "Debug: x = " << x << "\n";   // Goes to stderr

// cout is buffered — might not appear before a crash
std::cout << "Debug: x = " << x << "\n";   // Goes to stdout
```

```bash
# Separate debug output from program output
./program 2> debug.log    # stderr → file, stdout → screen
./program > output.txt 2> debug.log   # Both separated
```

## Debug Macro
```cpp
#include <iostream>

#ifdef DEBUG
    #define DBG(msg) std::cerr << "[" << __FILE__ << ":" << __LINE__ << "] " << msg << "\n"
#else
    #define DBG(msg)    // Compiles to nothing in release
#endif

int main() {
    int x = 42;
    DBG("x = " << x);            // [main.cpp:12] x = 42
    DBG("Starting processing");   // [main.cpp:13] Starting processing
    return 0;
}
```

```bash
g++ -DDEBUG main.cpp -o program    # Debug output enabled
g++ main.cpp -o program            # Debug output disabled
```

## Useful Debug Patterns
```cpp
#include <iostream>
#include <vector>

int main() {
    // Pattern 1: Trace function entry/exit
    std::cerr << ">>> Entering main()\n";

    // Pattern 2: Print variable values
    int x = 42;
    std::cerr << "x = " << x << "\n";

    // Pattern 3: Print container contents
    std::vector<int> v = {1, 2, 3, 4, 5};
    std::cerr << "v = [";
    for (size_t i = 0; i < v.size(); ++i) {
        if (i > 0) std::cerr << ", ";
        std::cerr << v[i];
    }
    std::cerr << "]\n";

    // Pattern 4: Checkpoint messages
    std::cerr << "--- Checkpoint A reached ---\n";

    std::cerr << "<<< Exiting main()\n";
    return 0;
}
```

## Key Takeaways
1. Use `std::cerr` for debug output (unbuffered, goes to stderr)
2. Use `__FILE__` and `__LINE__` to auto-include location info
3. Wrap debug prints in `#ifdef DEBUG` to easily disable them
4. Redirect stderr to a file: `./program 2> debug.log`
5. Remove or disable debug prints before releasing code

## Common Mistakes
- Using `cout` for debug output — may not appear before a crash (buffered)
- Leaving debug prints in production code
- Not including newlines → output gets jumbled
