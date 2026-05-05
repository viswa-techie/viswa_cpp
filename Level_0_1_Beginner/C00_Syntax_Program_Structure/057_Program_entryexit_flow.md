# Program entry/exit flow

> **Level:** 0 — Absolute Beginner  
> **Category:** C00 — C++ Syntax & Program Structure  
> **Topic:** syntax

---

## Program Statement
Understand the complete lifecycle of a C++ program from start to finish.

## Program Lifecycle
```
OS loads executable
        │
        ▼
  C++ Runtime Startup
  (initialize globals, static objects)
        │
        ▼
    main() called
        │
        ▼
  Your code executes
        │
        ▼
  main() returns (or exit() called)
        │
        ▼
  C++ Runtime Shutdown
  (destroy globals, static objects, flush buffers)
        │
        ▼
  Exit code returned to OS
```

## Before main()
```cpp
#include <iostream>

// Global variable — constructed before main()
struct Logger {
    Logger() { std::cout << "1. Logger constructed\n"; }
    ~Logger() { std::cout << "5. Logger destroyed\n"; }
};

Logger globalLogger;    // Constructed before main

int main() {
    std::cout << "2. main() starts\n";
    std::cout << "3. main() runs\n";
    std::cout << "4. main() ends\n";
    return 0;
}
// After main returns: globalLogger is destroyed
```
**Output:**
```
1. Logger constructed
2. main() starts
3. main() runs
4. main() ends
5. Logger destroyed
```

## Ways to End a Program
```cpp
#include <iostream>
#include <cstdlib>

int main() {
    // Method 1: return from main (preferred)
    return 0;    // Destructors run, buffers flushed

    // Method 2: std::exit(code) — from anywhere
    std::exit(0);   // Globals destroyed, atexit handlers run

    // Method 3: std::abort() — emergency exit
    std::abort();   // NO cleanup, generates core dump

    // Method 4: std::terminate() — called on unhandled exception
    std::terminate();  // Calls abort() by default

    // Method 5: std::quick_exit() (C++11) — minimal cleanup
    std::quick_exit(0);  // Only at_quick_exit handlers
}
```

## atexit — Register Cleanup
```cpp
#include <iostream>
#include <cstdlib>

void cleanup1() { std::cout << "Cleanup 1\n"; }
void cleanup2() { std::cout << "Cleanup 2\n"; }

int main() {
    std::atexit(cleanup1);
    std::atexit(cleanup2);
    std::cout << "Main running\n";
    return 0;
}
```
**Output:**
```
Main running
Cleanup 2
Cleanup 1
```
(atexit handlers run in reverse order)

## Key Takeaways
1. Global/static objects are constructed before `main()`, destroyed after
2. `return` from `main()` is the cleanest exit — all destructors run
3. `std::exit()` runs cleanup but skips local destructors
4. `std::abort()` terminates immediately — no cleanup at all
5. `atexit()` registers functions called during normal termination

## Common Mistakes
- Relying on global construction order across files — it's undefined
- Using `std::exit()` without realizing local destructors are skipped
- Calling `abort()` when `exit()` would suffice
