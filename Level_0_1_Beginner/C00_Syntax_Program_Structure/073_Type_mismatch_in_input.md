# Type mismatch in input

> **Level:** 0 — Absolute Beginner  
> **Category:** C00 — C++ Syntax & Program Structure  
> **Topic:** syntax

---

## Problem Statement
Understand what happens when user input doesn't match the expected type.

## What You Need to Know
- `cin >> int_var` expects numeric input. Entering "hello" causes a failure.
- The stream enters fail state and stops processing further input.
- The mismatched input remains in the buffer.

## What Happens on Type Mismatch
```cpp
#include <iostream>

int main() {
    int x = -1;  // Initialize to see if it changes

    std::cout << "Enter a number: ";
    std::cin >> x;

    // If user enters "hello":
    // - x remains -1 (unchanged)
    // - cin is now in fail state
    // - "hello\n" is still in the buffer

    std::cout << "x = " << x << "\n";
    std::cout << "Stream good? " << std::cin.good() << "\n";
    return 0;
}
```

## Partial Reads
```cpp
#include <iostream>

int main() {
    int x;
    std::cout << "Enter a number: ";
    std::cin >> x;

    // Input: "42abc"
    // x = 42 (reads valid part)
    // "abc\n" remains in buffer
    // No failure! cin is still good

    // Input: "abc42"
    // x = unchanged (garbage)
    // Failure! "abc42\n" remains in buffer

    std::cout << "x = " << x << "\n";
    return 0;
}
```

## Multiple Variables
```cpp
#include <iostream>

int main() {
    int a, b, c;
    std::cout << "Enter three numbers: ";
    std::cin >> a >> b >> c;

    // Input: "10 hello 30"
    // a = 10 (OK)
    // b = read fails on "hello" → failbit set
    // c = skipped (stream already failed)
    // "hello 30\n" remains in buffer

    if (std::cin.fail()) {
        std::cerr << "Failed to read all three numbers\n";
    }
    return 0;
}
```

## Recovery
```cpp
#include <iostream>
#include <limits>
#include <string>

int main() {
    int num;

    while (true) {
        std::cout << "Enter an integer: ";

        if (std::cin >> num) {
            break;
        }

        // Show what was entered
        std::cin.clear();
        std::string bad;
        std::cin >> bad;
        std::cerr << "'" << bad << "' is not an integer. Try again.\n";
    }

    std::cout << "Got: " << num << "\n";
    return 0;
}
```

## Key Takeaways
1. Type mismatch sets failbit — variable is not modified
2. Partial match (e.g., "42abc") reads 42 successfully, leaves "abc"
3. Once failed, all subsequent `cin >>` operations are skipped
4. Recovery: `clear()` then `ignore()` or read the bad data
5. Always initialize variables before `cin >>` to detect unchanged values

## Common Mistakes
- Assuming `cin >> x` sets x to 0 on failure — it leaves x unchanged
- Not noticing partial reads: "42abc" reads 42 with no error
- Forgetting that failure cascades: one bad read blocks all subsequent reads
