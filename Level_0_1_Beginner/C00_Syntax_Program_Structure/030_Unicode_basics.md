# Unicode basics

> **Level:** 0 — Absolute Beginner  
> **Category:** C00 — C++ Syntax & Program Structure  
> **Topic:** syntax

---

## Problem Statement
Understand Unicode character encoding and how C++ supports it.

## What You Need to Know
- **ASCII** encodes 128 characters (0–127): English letters, digits, symbols.
- **Unicode** is a universal standard that assigns a code point to every character in every language.
- **UTF-8** is the most common encoding: ASCII-compatible, variable-width (1–4 bytes).
- **UTF-16** uses 2 or 4 bytes per character. Windows uses this internally.
- **UTF-32** uses exactly 4 bytes per character.

## C++ Character Types
```cpp
char     c1 = 'A';       // 1 byte, ASCII/UTF-8
wchar_t  c2 = L'Ω';      // Wide char (platform-dependent size)
char16_t c3 = u'Ω';      // 2 bytes, UTF-16 (C++11)
char32_t c4 = U'😀';     // 4 bytes, UTF-32 (C++11)
char8_t  c5 = u8'A';     // 1 byte, UTF-8 (C++20)
```

## String Literal Prefixes
```cpp
#include <iostream>
#include <string>

int main() {
    auto s1 = "Hello";         // const char[]     — narrow (ASCII/UTF-8)
    auto s2 = L"Hello";        // const wchar_t[]  — wide
    auto s3 = u"Hello";        // const char16_t[] — UTF-16
    auto s4 = U"Hello";        // const char32_t[] — UTF-32
    auto s5 = u8"Hello";       // const char8_t[]  — UTF-8 (C++20)

    std::cout << s1 << "\n";
    return 0;
}
```

## Unicode Escape Sequences
```cpp
#include <iostream>

int main() {
    // \uNNNN — 4-digit Unicode code point
    std::cout << "\u03A9" << "\n";   // Ω (Greek capital omega)

    // \UNNNNNNNN — 8-digit Unicode code point
    std::cout << "\U0001F600" << "\n";  // 😀 (if terminal supports it)

    return 0;
}
```

## Practical: UTF-8 in std::string
```cpp
#include <iostream>
#include <string>

int main() {
    std::string greeting = "नमस्ते";   // Hindi (UTF-8 encoded)
    std::cout << greeting << "\n";
    std::cout << "Bytes: " << greeting.size() << "\n";  // More than 6!
    // Each Devanagari character takes 3 bytes in UTF-8
    return 0;
}
```

## Key Takeaways
1. Use UTF-8 (`char` / `std::string`) for most purposes
2. `\uNNNN` for 4-digit Unicode, `\UNNNNNNNN` for 8-digit
3. `std::string::size()` returns bytes, not characters for UTF-8
4. `wchar_t` is platform-dependent — avoid in portable code
5. C++20 adds `char8_t` for type-safe UTF-8

## Common Mistakes
- Assuming `std::string::length()` gives character count for non-ASCII text
- Mixing wide and narrow strings without conversion
- Assuming `wchar_t` is always 4 bytes (2 on Windows, 4 on Linux)
