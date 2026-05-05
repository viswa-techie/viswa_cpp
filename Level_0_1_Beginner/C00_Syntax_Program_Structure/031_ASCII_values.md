# ASCII values

> **Level:** 0 — Absolute Beginner  
> **Category:** C00 — C++ Syntax & Program Structure  
> **Topic:** syntax

---

## Problem Statement
Understand ASCII character encoding and how characters map to integer values in C++.

## What You Need to Know
- ASCII (American Standard Code for Information Interchange) maps 128 characters to numbers 0–127.
- In C++, `char` is actually a small integer type.
- You can freely convert between `char` and `int`.

## Key ASCII Ranges
```
Range     Characters          Examples
-----     ----------          --------
0-31      Control characters  \n(10), \t(9), \0(0)
32        Space
48-57     Digits '0'-'9'
65-90     Uppercase 'A'-'Z'
97-122    Lowercase 'a'-'z'
```

## Example: Print ASCII Values
```cpp
#include <iostream>

int main() {
    char ch = 'A';
    std::cout << "Character: " << ch << "\n";
    std::cout << "ASCII value: " << static_cast<int>(ch) << "\n";  // 65

    // Print ASCII table for printable characters
    for (int i = 32; i < 127; ++i) {
        std::cout << i << " = " << static_cast<char>(i) << "   ";
        if ((i - 31) % 8 == 0) std::cout << "\n";
    }
    return 0;
}
```

## Example: Character Arithmetic
```cpp
#include <iostream>

int main() {
    char ch = 'A';

    // Convert uppercase to lowercase: add 32
    char lower = ch + 32;    // 65 + 32 = 97 = 'a'
    std::cout << lower << "\n";

    // Check if a character is a digit
    char c = '5';
    if (c >= '0' && c <= '9') {
        int digit = c - '0';   // '5' - '0' = 53 - 48 = 5
        std::cout << "Digit value: " << digit << "\n";
    }

    return 0;
}
```

## Example: Convert Case
```cpp
#include <iostream>
#include <cctype>

int main() {
    char upper = 'G';
    char lower = 'g';

    // Using arithmetic
    std::cout << static_cast<char>(upper + 32) << "\n";  // 'g'
    std::cout << static_cast<char>(lower - 32) << "\n";  // 'G'

    // Using standard library (preferred)
    std::cout << static_cast<char>(std::tolower(upper)) << "\n";
    std::cout << static_cast<char>(std::toupper(lower)) << "\n";

    return 0;
}
```

## Key Takeaways
1. `char` is an integer type — `'A'` is stored as 65
2. `'0'` is 48, `'A'` is 65, `'a'` is 97
3. Uppercase to lowercase: add 32 (or use `tolower()`)
4. Digit character to integer: subtract `'0'`
5. Use `<cctype>` functions for robust character classification

## Common Mistakes
- Printing `char` as a number: `cout << ch` prints the character, not the number
- Assuming ASCII extends beyond 127 — it doesn't (use Unicode for extended)
- Forgetting that `'0'` (48) is different from `0` (null character)
