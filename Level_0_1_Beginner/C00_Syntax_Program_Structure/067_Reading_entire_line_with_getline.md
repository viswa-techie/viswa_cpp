# Reading entire line with getline

> **Level:** 0 — Absolute Beginner  
> **Category:** C00 — C++ Syntax & Program Structure  
> **Topic:** syntax

---

## Problem Statement
Use `std::getline()` to read an entire line of input including spaces.

## What You Need to Know
- `cin >>` stops at whitespace — can't read "Hello World" as one input.
- `std::getline(cin, str)` reads the entire line until newline.
- Requires `#include <string>`.

## cin >> vs getline
```cpp
#include <iostream>
#include <string>

int main() {
    std::string input;

    // cin >> reads only ONE word
    std::cout << "Enter with cin>>: ";
    std::cin >> input;
    std::cout << "Got: '" << input << "'\n";
    // Input "Hello World" → Got: 'Hello'

    std::cin.ignore();  // Discard leftover newline

    // getline reads the ENTIRE line
    std::cout << "Enter with getline: ";
    std::getline(std::cin, input);
    std::cout << "Got: '" << input << "'\n";
    // Input "Hello World" → Got: 'Hello World'

    return 0;
}
```

## Basic getline Usage
```cpp
#include <iostream>
#include <string>

int main() {
    std::string name;
    std::string city;

    std::cout << "Enter your full name: ";
    std::getline(std::cin, name);

    std::cout << "Enter your city: ";
    std::getline(std::cin, city);

    std::cout << name << " lives in " << city << "\n";
    return 0;
}
```

## getline with Custom Delimiter
```cpp
#include <iostream>
#include <string>

int main() {
    std::string token;

    // Read until semicolon instead of newline
    std::cout << "Enter data (semicolon-separated): ";
    while (std::getline(std::cin, token, ';')) {
        std::cout << "Token: " << token << "\n";
    }
    // Input: "apple;banana;cherry"
    // Output: Token: apple, Token: banana, Token: cherry
    return 0;
}
```

## Reading Multiple Lines
```cpp
#include <iostream>
#include <string>

int main() {
    std::string line;
    std::cout << "Enter lines (Ctrl+D to stop):\n";

    while (std::getline(std::cin, line)) {
        std::cout << "Read: " << line << "\n";
    }
    return 0;
}
```

## Key Takeaways
1. `std::getline(cin, str)` reads the entire line including spaces
2. The newline character is consumed but not stored
3. Third parameter changes delimiter: `getline(cin, str, ';')`
4. Returns a reference to the stream — can be used in `while`/`if`
5. Requires `#include <string>`

## Common Mistakes
- Using `cin >>` when input has spaces → only first word captured
- Mixing `cin >>` and `getline` without `cin.ignore()` → getline reads empty string
- Forgetting to `#include <string>`
