# Whitespace in getline

> **Level:** 0 — Absolute Beginner  
> **Category:** C00 — C++ Syntax & Program Structure  
> **Topic:** syntax

---

## Problem Statement
Handle whitespace correctly when using `getline`, especially after `cin >>`.

## The Classic Problem
```cpp
#include <iostream>
#include <string>

int main() {
    int age;
    std::string name;

    std::cout << "Enter age: ";
    std::cin >> age;          // Reads "25", leaves '\n' in buffer

    std::cout << "Enter name: ";
    std::getline(std::cin, name);  // Reads the leftover '\n' immediately!
    // name is now "" (empty string)!

    std::cout << "Age: " << age << ", Name: '" << name << "'\n";
    return 0;
}
```

## The Fix: cin.ignore()
```cpp
#include <iostream>
#include <string>
#include <limits>

int main() {
    int age;
    std::string name;

    std::cout << "Enter age: ";
    std::cin >> age;

    // Discard leftover newline from cin >>
    std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');

    std::cout << "Enter name: ";
    std::getline(std::cin, name);  // Now works correctly!

    std::cout << "Age: " << age << ", Name: '" << name << "'\n";
    return 0;
}
```

## Why This Happens
```
Input buffer after "cin >> age":

User types: 25↵ (25 followed by Enter)
cin >> reads: 25
Buffer still has: ↵ (\n remains!)

getline reads: ↵ (the leftover newline)
Result: empty string
```

## Alternative Fixes
```cpp
#include <iostream>
#include <string>

int main() {
    int age;
    std::string name;

    // Fix 1: Use getline for everything
    std::string age_str;
    std::cout << "Enter age: ";
    std::getline(std::cin, age_str);
    age = std::stoi(age_str);

    std::cout << "Enter name: ";
    std::getline(std::cin, name);

    // Fix 2: cin.ignore() after each cin >>
    // (shown above)

    // Fix 3: ws manipulator
    std::cin >> age;
    std::getline(std::cin >> std::ws, name);
    // std::ws consumes whitespace including the leftover \n

    return 0;
}
```

## Key Takeaways
1. `cin >>` leaves the newline in the buffer
2. `getline` reads that leftover newline → empty string
3. Fix: `cin.ignore()` between `cin >>` and `getline`
4. Alternative: use `getline` for all input, convert with `stoi()`
5. `std::ws` manipulator also skips leading whitespace

## Common Mistakes
- Not using `cin.ignore()` → mysterious empty strings
- Using `cin.ignore()` without proper arguments → only ignores 1 char
- Mixing `cin >>` and `getline` throughout the program without care
