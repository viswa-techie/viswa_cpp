# Blank lines and readability

> **Level:** 0 — Absolute Beginner  
> **Category:** C00 — C++ Syntax & Program Structure  
> **Topic:** syntax

---

## Problem Statement
Use blank lines to make C++ code readable and well-organized.

## What You Need to Know
- Blank lines are ignored by the compiler — they are purely for humans.
- They group related statements into logical "paragraphs."
- Consistent spacing makes code easier to review and maintain.

## Mental Model
Think of blank lines like paragraph breaks in an essay — they separate ideas and give readers a visual pause.

## Example 1: Without blank lines (hard to read)
```cpp
#include <iostream>
int main() {
int x = 10;
int y = 20;
int sum = x + y;
std::cout << "Sum: " << sum << "\n";
int product = x * y;
std::cout << "Product: " << product << "\n";
return 0;
}
```

## Example 2: With blank lines (clean and readable)
```cpp
#include <iostream>

int main() {
    int x = 10;
    int y = 20;

    int sum = x + y;
    std::cout << "Sum: " << sum << "\n";

    int product = x * y;
    std::cout << "Product: " << product << "\n";

    return 0;
}
```

## Guidelines for Blank Lines
```
1. After #include blocks
2. Between function definitions
3. Between logical groups of statements
4. Before return statements (optional, aids readability)
5. Between class sections (public/private/protected)
```

## Example 3: Functions separated by blank lines
```cpp
#include <iostream>

int add(int a, int b) {
    return a + b;
}

int multiply(int a, int b) {
    return a * b;
}

int main() {
    std::cout << add(3, 4) << "\n";
    std::cout << multiply(3, 4) << "\n";
    return 0;
}
```

## Key Takeaways
1. Blank lines cost nothing — the compiler ignores them
2. Group related statements together, separate groups with blank lines
3. Always put a blank line after `#include` directives
4. Always put a blank line between function definitions
5. Don't use excessive blank lines — one is usually enough

## Common Mistakes
- No blank lines at all → "wall of text" code
- Too many blank lines (3-4 in a row) → wastes vertical space
- Inconsistent spacing → confusing to read
