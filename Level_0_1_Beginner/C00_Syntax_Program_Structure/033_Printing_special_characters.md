# Printing special characters

> **Level:** 0 — Absolute Beginner  
> **Category:** C00 — C++ Syntax & Program Structure  
> **Topic:** syntax

---

## Problem Statement
Print special characters like quotes, backslashes, tabs, and newlines in C++ output.

## What You Need to Know
- Special characters require escape sequences (backslash + character).
- These work in both `cout` output and string/char literals.

## Printing Quotes
```cpp
#include <iostream>

int main() {
    // Double quote inside a string
    std::cout << "He said \"Hello!\"\n";

    // Single quote
    std::cout << "It\'s working\n";

    // Using raw string to avoid escaping
    std::cout << R"(She said "Goodbye!")" << "\n";

    return 0;
}
```
**Output:**
```
He said "Hello!"
It's working
She said "Goodbye!"
```

## Printing Backslashes
```cpp
#include <iostream>

int main() {
    std::cout << "Path: C:\\Users\\Viswa\n";
    std::cout << R"(Path: C:\Users\Viswa)" << "\n";
    return 0;
}
```

## Printing Tabs and Alignment
```cpp
#include <iostream>

int main() {
    std::cout << "Name\tAge\tCity\n";
    std::cout << "Viswa\t30\tChennai\n";
    std::cout << "John\t25\tNew York\n";
    return 0;
}
```
**Output:**
```
Name    Age     City
Viswa   30      Chennai
John    25      New York
```

## Printing Non-Printable Characters
```cpp
#include <iostream>

int main() {
    // Bell/alert sound
    std::cout << "\a";

    // Carriage return — overwrites from start of line
    std::cout << "ABCDEF\rXY\n";
    // Output: XYCDEF (XY overwrites AB)

    // Backspace
    std::cout << "Hello\b\b!!!\n";
    // Output: Hel!!!

    return 0;
}
```

## Printing Unicode Characters
```cpp
#include <iostream>

int main() {
    std::cout << "\u2603\n";       // ☃ Snowman
    std::cout << "\u2764\n";       // ❤ Heart
    std::cout << "\u03C0\n";       // π Pi
    std::cout << "\u00B0" << "C\n"; // °C
    return 0;
}
```

## Key Takeaways
1. `\"` for double quote, `\\` for backslash, `\t` for tab
2. `\r` returns cursor to start of line (overwrites)
3. `\b` moves cursor back one position
4. `\uNNNN` prints Unicode characters
5. Raw strings `R"(...)"` avoid all escaping

## Common Mistakes
- Forgetting double backslash: `"\n"` is newline but `"\\n"` prints literal \n
- Expecting `\a` to always beep — depends on terminal
- Using `\r` expecting newline behavior — it's NOT a newline
