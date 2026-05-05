# Pass by value basics

> **Level:** 0 — Absolute Beginner  
> **Category:** C00 — C++ Syntax & Program Structure  
> **Topic:** syntax

---

## Problem Statement
Understand pass by value — the default parameter passing mechanism in C++.

## What You Need to Know
- Pass by value means the function receives a **copy** of the argument.
- Modifications inside the function do NOT affect the original.
- Copies can be expensive for large objects.

## Pass by Value Demo
```cpp
#include <iostream>

void doubleIt(int x) {    // x is a copy
    x = x * 2;
    std::cout << "Inside: " << x << "\n";   // 20
}

int main() {
    int num = 10;
    doubleIt(num);
    std::cout << "Outside: " << num << "\n";  // 10 (unchanged!)
    return 0;
}
```

## Memory View
```
Before call:    num = 10
                    │
Function call:  x = 10 (copy created)
                x = 20 (copy modified)
After return:   num = 10 (original unchanged)
                x destroyed
```

## Pass by Reference (Preview)
```cpp
#include <iostream>

void doubleIt(int& x) {   // x is a REFERENCE (alias)
    x = x * 2;
}

int main() {
    int num = 10;
    doubleIt(num);
    std::cout << "num: " << num << "\n";  // 20 (modified!)
    return 0;
}
```

## When to Use Which
```
Use pass by value:              Use pass by reference:
------------------              ----------------------
Small types (int, char, bool)   Large objects (string, vector)
When you need a local copy      When you need to modify the original
When function shouldn't modify  When copying is too expensive
```

## const Reference (Best of Both)
```cpp
#include <iostream>
#include <string>

// Pass by value — copies the entire string
void printV(std::string s) {
    std::cout << s << "\n";
}

// Pass by const reference — no copy, can't modify
void printR(const std::string& s) {
    std::cout << s << "\n";
}

int main() {
    std::string text = "Hello, World!";
    printV(text);    // Makes a copy (slow for large strings)
    printR(text);    // No copy (fast, and safe — const prevents modification)
    return 0;
}
```

## Key Takeaways
1. Pass by value creates a copy — modifications don't affect the original
2. Use pass by value for small, cheap-to-copy types (int, double, char)
3. Use `const &` for read-only access to large objects (string, vector)
4. Use `&` (non-const reference) when the function needs to modify the argument
5. Pass by value is safe — the function can't accidentally modify your data

## Common Mistakes
- Passing large objects by value → unnecessary expensive copies
- Thinking value parameters modify the original → they don't
- Using `&` when `const &` would suffice → accidental modification possible
