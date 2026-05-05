# Raw string literals R"(...)"

> **Level:** 0 — Absolute Beginner  
> **Category:** C00 — C++ Syntax & Program Structure  
> **Topic:** syntax

---

## Problem Statement
Use raw string literals to avoid escaping special characters in C++ strings.

## What You Need to Know
- Raw strings start with `R"(` and end with `)"`.
- Inside a raw string, backslashes and quotes are treated as literal characters.
- Available since C++11.

## Why Raw Strings?
```cpp
// Without raw string — many escape characters
std::string path = "C:\\Users\\Viswa\\Documents\\file.txt";
std::string regex = "\\d+\\.\\d+";

// With raw string — clean and readable
std::string path = R"(C:\Users\Viswa\Documents\file.txt)";
std::string regex = R"(\d+\.\d+)";
```

## Basic Syntax
```cpp
#include <iostream>

int main() {
    // Basic raw string
    std::cout << R"(Hello\nWorld)" << "\n";
    // Output: Hello\nWorld  (the \n is literal, not a newline)

    // Regular string for comparison
    std::cout << "Hello\nWorld" << "\n";
    // Output:
    // Hello
    // World

    return 0;
}
```

## Multi-line Raw Strings
```cpp
#include <iostream>

int main() {
    std::string json = R"({
    "name": "Viswa",
    "age": 30,
    "city": "Chennai"
})";

    std::cout << json << "\n";
    return 0;
}
```
**Output:**
```
{
    "name": "Viswa",
    "age": 30,
    "city": "Chennai"
}
```

## Custom Delimiter
```cpp
#include <iostream>

int main() {
    // If your string contains )" you need a custom delimiter
    // Syntax: R"delimiter(content)delimiter"
    std::string s = R"xyz(She said "Hello)" and left)xyz";
    std::cout << s << "\n";
    // Output: She said "Hello)" and left
    return 0;
}
```

## Key Takeaways
1. `R"(text)"` — no escaping needed inside
2. Great for regex, file paths, JSON, SQL, HTML
3. Supports multi-line strings naturally
4. Use custom delimiters `R"delim(...)delim"` if string contains `)`
5. C++11 and later only

## Common Mistakes
- Forgetting the parentheses: `R"text"` is wrong → must be `R"(text)"`
- Using raw strings in C++03 code → compilation error
- Thinking `\n` inside raw string creates a newline — it doesn't
