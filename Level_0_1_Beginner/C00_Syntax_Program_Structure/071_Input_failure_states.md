# Input failure states

> **Level:** 0 — Absolute Beginner  
> **Category:** C00 — C++ Syntax & Program Structure  
> **Topic:** syntax

---

## Problem Statement
Understand the different input stream states and how to detect and handle failures.

## Stream State Flags
```
Flag         Method         Meaning
----         ------         -------
goodbit      good()         No errors, ready for I/O
failbit      fail()         Logical error (wrong type, format error)
badbit       bad()          I/O error (hardware/system failure)
eofbit       eof()          End of file/input reached
```

## Checking Stream State
```cpp
#include <iostream>

int main() {
    int x;
    std::cout << "Enter a number: ";
    std::cin >> x;

    if (std::cin.good()) {
        std::cout << "Success: " << x << "\n";
    } else if (std::cin.eof()) {
        std::cout << "End of input (Ctrl+D)\n";
    } else if (std::cin.fail()) {
        std::cout << "Format error (not a number)\n";
    } else if (std::cin.bad()) {
        std::cout << "I/O error (hardware problem)\n";
    }

    return 0;
}
```

## Using Stream as Boolean
```cpp
#include <iostream>

int main() {
    int x;

    // The stream converts to bool — true if good
    if (std::cin >> x) {
        std::cout << "Got: " << x << "\n";
    } else {
        std::cout << "Input failed\n";
    }

    // Useful in loops
    while (std::cin >> x) {
        std::cout << "Read: " << x << "\n";
    }
    // Loop ends on EOF (Ctrl+D) or bad input

    return 0;
}
```

## Common Failure Scenarios
```cpp
#include <iostream>
#include <limits>

int main() {
    int x;

    // Scenario 1: Type mismatch
    // User enters "hello" for int → failbit set
    std::cin >> x;
    if (std::cin.fail()) {
        std::cerr << "Not a number!\n";
        std::cin.clear();
        std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
    }

    // Scenario 2: EOF
    // User presses Ctrl+D → eofbit set
    std::cin >> x;
    if (std::cin.eof()) {
        std::cerr << "End of input\n";
    }

    // Scenario 3: Overflow
    // User enters 99999999999999 for int → failbit set (on some implementations)

    return 0;
}
```

## Recovery Pattern
```cpp
#include <iostream>
#include <limits>
#include <string>

int readInt(const std::string& prompt) {
    int value;
    while (true) {
        std::cout << prompt;
        if (std::cin >> value) {
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
            return value;
        }
        std::cerr << "Invalid input. Try again.\n";
        std::cin.clear();
        std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
    }
}

int main() {
    int age = readInt("Enter your age: ");
    std::cout << "Age: " << age << "\n";
    return 0;
}
```

## Key Takeaways
1. `fail()` = format/type error, `bad()` = I/O error, `eof()` = end of input
2. Use stream in boolean context: `if (cin >> x)` checks for success
3. Always clear + ignore after a failure before reading again
4. `while (cin >> x)` reads until EOF or error — very idiomatic
5. `good()` returns true only when no flags are set

## Common Mistakes
- Not checking stream state → using garbage values from failed reads
- Only checking `eof()` — `fail()` is more common
- Forgetting that after failure, ALL reads are skipped until `clear()`
