# char literals with single quotes

> **Level:** 0 — Absolute Beginner  
> **Category:** C00 — C++ Syntax & Program Structure  
> **Topic:** syntax

---

## Problem Statement
Understand character literals and the difference between single and double quotes in C++.

## What You Need to Know
- Single quotes `' '` define a character literal (`char`).
- Double quotes `" "` define a string literal (`const char*`).
- A `char` holds exactly one character (1 byte).

## Basic Character Literals
```cpp
#include <iostream>

int main() {
    char letter = 'A';
    char digit = '7';
    char space = ' ';
    char newline = '\n';

    std::cout << letter << "\n";    // A
    std::cout << digit << "\n";     // 7
    std::cout << "ASCII: " << static_cast<int>(letter) << "\n";  // 65
    return 0;
}
```

## char vs string: Critical Difference
```cpp
#include <iostream>

int main() {
    char   c = 'A';     // Single character, 1 byte
    // char   c2 = "A"; // ERROR! "A" is a string (const char*), not char

    const char* s = "A"; // String: 'A' + '\0' = 2 bytes
    std::cout << sizeof(c) << "\n";  // 1
    // sizeof(s) gives pointer size (4 or 8), not string length
    return 0;
}
```

## Special Character Literals
```cpp
#include <iostream>

int main() {
    char tab = '\t';        // Tab
    char nl = '\n';         // Newline
    char backslash = '\\';  // Backslash
    char quote = '\'';      // Single quote
    char dquote = '\"';     // Double quote
    char null = '\0';       // Null character

    std::cout << "Tab:" << tab << "here\n";
    std::cout << "Quote: " << quote << "\n";
    return 0;
}
```

## Character Comparisons
```cpp
#include <iostream>

int main() {
    char ch = 'B';

    if (ch >= 'A' && ch <= 'Z') {
        std::cout << ch << " is uppercase\n";
    }

    if (ch >= '0' && ch <= '9') {
        std::cout << ch << " is a digit\n";
    }

    return 0;
}
```

## Key Takeaways
1. `'A'` is a char (1 byte), `"A"` is a string (2 bytes: A + null)
2. `char` is an integer type — you can do arithmetic on it
3. Use escape sequences for special characters: `'\n'`, `'\t'`, `'\\'`
4. `'\0'` is the null character with value 0
5. Character comparisons use ASCII ordering

## Common Mistakes
- `'AB'` — multi-character literal, implementation-defined, avoid it
- Confusing `'0'` (char, value 48) with `0` (int, value zero)
- Assigning a string to a char: `char c = "x";` → compile error
