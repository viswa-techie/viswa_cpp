# String literals with quotes

> **Level:** 0 — Absolute Beginner  
> **Category:** C00 — C++ Syntax & Program Structure  
> **Topic:** syntax

---

## Problem Statement
Understand how string literals work in C++ and how to include quotes inside strings.

## What You Need to Know
- String literals are enclosed in double quotes `" "`.
- Character literals use single quotes `' '`.
- To include a quote character inside a string, you must escape it.

## Basic String Literals
```cpp
#include <iostream>
#include <string>

int main() {
    // C-style string literal (const char*)
    const char* greeting = "Hello, World!";

    // std::string from a literal
    std::string name = "Viswa";

    std::cout << greeting << "\n";
    std::cout << name << "\n";
    return 0;
}
```

## Including Quotes Inside Strings
```cpp
#include <iostream>

int main() {
    // Use \" to include a double quote in a string
    std::cout << "She said \"Hello!\"\n";

    // Use \' for single quote (optional — works without escape too)
    std::cout << "It\'s a beautiful day\n";
    std::cout << "It's a beautiful day\n";  // Also valid — no escape needed

    return 0;
}
```
**Output:**
```
She said "Hello!"
It's a beautiful day
It's a beautiful day
```

## Empty Strings
```cpp
#include <iostream>
#include <string>

int main() {
    std::string empty = "";         // Empty string
    const char* also_empty = "";    // Empty C-string

    std::cout << "Length: " << empty.length() << "\n";  // 0
    return 0;
}
```

## String Literal Concatenation
```cpp
#include <iostream>

int main() {
    // Adjacent string literals are automatically concatenated
    const char* msg = "Hello, "
                      "World!";       // Becomes "Hello, World!"
    std::cout << msg << "\n";
    return 0;
}
```

## Key Takeaways
1. String literals use double quotes: `"text"`
2. Character literals use single quotes: `'c'`
3. Escape double quotes inside strings with `\"`
4. Adjacent string literals auto-concatenate at compile time
5. Empty string `""` is valid and has length 0

## Common Mistakes
- Using single quotes for strings: `'hello'` — this is NOT a string
- Forgetting to escape quotes: `"She said "Hi""` → compile error
- Confusing `char` and `string`: `'A'` is a char, `"A"` is a string (2 bytes: A + null)
