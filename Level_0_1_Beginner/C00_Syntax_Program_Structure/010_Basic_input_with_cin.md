# Basic input with cin

> **Level:** 0 — Absolute Beginner  
> **Category:** C00 — C++ Syntax & Program Structure  
> **Topic:** syntax

---

## Problem Statement
Read user input from the keyboard using `std::cin`.

## What You Need to Know
- `std::cin` reads from standard input (keyboard by default).
- `>>` is the stream extraction operator.
- `cin` skips leading whitespace by default.
- `cin` stops reading at whitespace for strings.

## Solution 1: Read a single integer
```cpp
#include <iostream>

int main() {
    int age;
    std::cout << "Enter your age: ";
    std::cin >> age;
    std::cout << "You are " << age << " years old.\n";
    return 0;
}
```

## Solution 2: Read multiple values
```cpp
#include <iostream>

int main() {
    int x, y;
    std::cout << "Enter two numbers: ";
    std::cin >> x >> y;  // Chained extraction
    std::cout << "Sum: " << (x + y) << "\n";
    return 0;
}
```

## Solution 3: Read a string (single word)
```cpp
#include <iostream>
#include <string>

int main() {
    std::string name;
    std::cout << "Enter your name: ";
    std::cin >> name;  // Reads only ONE word (stops at space)
    std::cout << "Hello, " << name << "\n";
    return 0;
}
```

## Solution 4: Read an entire line
```cpp
#include <iostream>
#include <string>

int main() {
    std::string fullName;
    std::cout << "Enter your full name: ";
    std::getline(std::cin, fullName);  // Reads entire line including spaces
    std::cout << "Hello, " << fullName << "\n";
    return 0;
}
```

## Input Validation
```cpp
#include <iostream>

int main() {
    int num;
    std::cout << "Enter a number: ";
    if (std::cin >> num) {
        std::cout << "You entered: " << num << "\n";
    } else {
        std::cout << "Invalid input!\n";
        std::cin.clear();             // Clear error flags
        std::cin.ignore(10000, '\n'); // Discard bad input
    }
    return 0;
}
```

## Key Takeaways
1. `cin >> var` reads one token (stops at whitespace)
2. `getline(cin, str)` reads entire line
3. Always validate input: check if `cin >>` succeeded
4. After failed input, call `cin.clear()` then `cin.ignore()`
5. Mixing `cin >>` and `getline` requires `cin.ignore()` between them

## Common Mistakes
- Reading a string with `cin >>` when input has spaces → only first word captured
- Not handling invalid input → program enters infinite loop or reads garbage
- Mixing `cin >>` and `getline` without `cin.ignore()` → getline reads empty string
