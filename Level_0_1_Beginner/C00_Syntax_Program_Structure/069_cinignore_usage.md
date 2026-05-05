# cin.ignore() usage

> **Level:** 0 — Absolute Beginner  
> **Category:** C00 — C++ Syntax & Program Structure  
> **Topic:** syntax

---

## Problem Statement
Use `cin.ignore()` to discard unwanted characters from the input buffer.

## What You Need to Know
- `cin.ignore(n, ch)` discards up to `n` characters or until `ch` is found.
- Most common use: `cin.ignore(numeric_limits<streamsize>::max(), '\n')`.
- This clears the entire line from the buffer.

## Syntax
```cpp
cin.ignore();                    // Ignore 1 character
cin.ignore(n);                   // Ignore up to n characters
cin.ignore(n, delim);            // Ignore up to n chars or until delim found

// The "clear entire line" pattern:
#include <limits>
std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
```

## Common Use Cases

### After cin >> before getline
```cpp
#include <iostream>
#include <string>
#include <limits>

int main() {
    int num;
    std::string line;

    std::cout << "Enter number: ";
    std::cin >> num;
    std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');

    std::cout << "Enter text: ";
    std::getline(std::cin, line);

    std::cout << num << " / " << line << "\n";
    return 0;
}
```

### After failed input
```cpp
#include <iostream>
#include <limits>

int main() {
    int x;
    while (true) {
        std::cout << "Enter a number: ";
        if (std::cin >> x) {
            break;  // Valid input
        }
        // Invalid input — clear error and discard bad data
        std::cin.clear();
        std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
        std::cout << "Invalid! Try again.\n";
    }
    std::cout << "Got: " << x << "\n";
    return 0;
}
```

### Discard extra input
```cpp
#include <iostream>
#include <limits>

int main() {
    char ch;
    std::cout << "Enter a character: ";
    std::cin >> ch;
    // User might type "hello" — discard "ello\n"
    std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
    std::cout << "First char: " << ch << "\n";
    return 0;
}
```

## Key Takeaways
1. `cin.ignore()` discards characters from the input buffer
2. Use `numeric_limits<streamsize>::max()` to clear the entire line
3. Always use after `cin >>` if `getline()` follows
4. Pair with `cin.clear()` to recover from input errors
5. Without the second argument `'\n'`, it doesn't know where to stop

## Common Mistakes
- `cin.ignore()` alone ignores only 1 character — might not be enough
- Forgetting `#include <limits>` for `numeric_limits`
- Using `cin.ignore()` before any input → discards user's first character
