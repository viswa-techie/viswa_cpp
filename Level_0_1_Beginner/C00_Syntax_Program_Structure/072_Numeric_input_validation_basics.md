# Numeric input validation basics

> **Level:** 0 — Absolute Beginner  
> **Category:** C00 — C++ Syntax & Program Structure  
> **Topic:** syntax

---

## Problem Statement
Validate that user input is a valid number within an expected range.

## What You Need to Know
- `cin >> int_var` fails silently if user enters non-numeric text.
- You must check the stream state after every input.
- Range checking is your responsibility — C++ doesn't do it automatically.

## Basic Validation
```cpp
#include <iostream>
#include <limits>

int main() {
    int age;

    std::cout << "Enter your age (1-120): ";
    if (!(std::cin >> age)) {
        std::cerr << "Error: Not a number\n";
        return 1;
    }

    if (age < 1 || age > 120) {
        std::cerr << "Error: Age must be between 1 and 120\n";
        return 1;
    }

    std::cout << "Your age: " << age << "\n";
    return 0;
}
```

## Robust Input Loop
```cpp
#include <iostream>
#include <limits>

int getValidInt(int min, int max) {
    int value;
    while (true) {
        std::cout << "Enter a number (" << min << "-" << max << "): ";

        if (std::cin >> value) {
            if (value >= min && value <= max) {
                return value;
            }
            std::cerr << "Out of range!\n";
        } else {
            std::cerr << "Not a valid number!\n";
            std::cin.clear();
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
        }
    }
}

int main() {
    int score = getValidInt(0, 100);
    std::cout << "Score: " << score << "\n";
    return 0;
}
```

## String-Based Validation
```cpp
#include <iostream>
#include <string>
#include <sstream>

int main() {
    std::string input;
    int number;

    std::cout << "Enter a number: ";
    std::getline(std::cin, input);

    std::istringstream iss(input);
    if (iss >> number && iss.eof()) {
        std::cout << "Valid number: " << number << "\n";
    } else {
        std::cerr << "Invalid: '" << input << "' is not a pure number\n";
    }
    // "42" → valid, "42abc" → invalid, "abc" → invalid

    return 0;
}
```

## Key Takeaways
1. Always check `if (cin >> x)` before using `x`
2. Validate range after successful read
3. Use a loop for retry logic
4. String-based approach (getline + stringstream) gives more control
5. `stoi()` / `stod()` with try-catch is another option

## Common Mistakes
- Not validating input → program continues with garbage values
- Accepting `42abc` as valid 42 — use stringstream + eof check to reject
- Forgetting `cin.clear()` + `cin.ignore()` in the retry loop → infinite loop
