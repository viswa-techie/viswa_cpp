# cin.clear() usage

> **Level:** 0 — Absolute Beginner  
> **Category:** C00 — C++ Syntax & Program Structure  
> **Topic:** syntax

---

## Problem Statement
Use `cin.clear()` to reset error flags when input fails.

## What You Need to Know
- When `cin >>` fails (e.g., entering "abc" for an `int`), the stream enters a **fail state**.
- In fail state, ALL subsequent `cin` operations are skipped.
- `cin.clear()` resets the error flags, restoring the stream.
- You must also `cin.ignore()` to discard the bad input.

## The Problem
```cpp
#include <iostream>

int main() {
    int x;
    std::cout << "Enter a number: ";
    std::cin >> x;    // User types "hello"

    // cin is now in fail state
    std::cout << "State: " << (std::cin.good() ? "good" : "FAIL") << "\n";

    int y;
    std::cin >> y;    // This is SKIPPED — cin still in fail state
    // y is uninitialized/garbage
    return 0;
}
```

## The Fix
```cpp
#include <iostream>
#include <limits>

int main() {
    int x;
    std::cout << "Enter a number: ";

    if (!(std::cin >> x)) {
        std::cout << "Invalid input!\n";

        std::cin.clear();    // Step 1: Reset error flags
        std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
                             // Step 2: Discard bad input

        std::cout << "Try again: ";
        std::cin >> x;       // Now this works!
    }

    std::cout << "Got: " << x << "\n";
    return 0;
}
```

## Stream State Flags
```cpp
#include <iostream>

int main() {
    int x;
    std::cin >> x;

    // Check individual flags
    std::cout << "good: " << std::cin.good() << "\n";   // No errors
    std::cout << "fail: " << std::cin.fail() << "\n";   // Logic error (bad type)
    std::cout << "bad:  " << std::cin.bad() << "\n";    // I/O error (rare)
    std::cout << "eof:  " << std::cin.eof() << "\n";    // End of file reached

    return 0;
}
```

## Robust Input Loop
```cpp
#include <iostream>
#include <limits>

int main() {
    int number;

    while (true) {
        std::cout << "Enter an integer: ";
        if (std::cin >> number) {
            break;    // Success — exit loop
        }

        // Failed — recover and retry
        std::cerr << "That's not a valid integer!\n";
        std::cin.clear();                                            // Reset flags
        std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');  // Discard
    }

    std::cout << "You entered: " << number << "\n";
    return 0;
}
```

## Key Takeaways
1. `cin.clear()` resets error flags — does NOT discard bad input
2. Always pair `cin.clear()` with `cin.ignore()` for full recovery
3. Order matters: `clear()` first, then `ignore()`
4. Check stream state with `cin.fail()`, `cin.good()`, `cin.eof()`
5. Using `cin` in a boolean context checks for errors: `if (cin >> x)`

## Common Mistakes
- Using `cin.clear()` without `cin.ignore()` → bad input still in buffer
- Using `cin.ignore()` without `cin.clear()` → ignore is skipped (still in fail state)
- Not checking if `cin >>` succeeded → using garbage values
