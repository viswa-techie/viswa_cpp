# Tab stops with \t

> **Level:** 0 — Absolute Beginner  
> **Category:** C00 — C++ Syntax & Program Structure  
> **Topic:** syntax

---

## Problem Statement
Use tab characters (`\t`) to align output in columns.

## What You Need to Know
- `\t` inserts a horizontal tab character.
- Tabs advance to the next tab stop (typically every 8 characters).
- Tab alignment can be unpredictable with varying text widths.

## Basic Tab Usage
```cpp
#include <iostream>

int main() {
    std::cout << "Name\tAge\tCity\n";
    std::cout << "Viswa\t30\tChennai\n";
    std::cout << "Bob\t25\tDelhi\n";
    return 0;
}
```
**Output:**
```
Name    Age     City
Viswa   30      Chennai
Bob     25      Delhi
```

## Tab Alignment Problem
```cpp
#include <iostream>

int main() {
    // When text lengths vary, tabs may misalign
    std::cout << "Name\tScore\n";
    std::cout << "Al\t95\n";           // Short name — tab works
    std::cout << "Christopher\t88\n";  // Long name — pushed to next tab stop
    return 0;
}
```
**Output (may misalign):**
```
Name        Score
Al          95
Christopher 88
```

## Better Alternative: setw()
```cpp
#include <iostream>
#include <iomanip>

int main() {
    std::cout << std::left;
    std::cout << std::setw(15) << "Name"
              << std::setw(8)  << "Age"
              << std::setw(15) << "City" << "\n";
    std::cout << std::setw(15) << "Viswa"
              << std::setw(8)  << 30
              << std::setw(15) << "Chennai" << "\n";
    std::cout << std::setw(15) << "Christopher"
              << std::setw(8)  << 25
              << std::setw(15) << "New York" << "\n";
    return 0;
}
```
**Output (perfectly aligned):**
```
Name           Age     City
Viswa          30      Chennai
Christopher    25      New York
```

## Key Takeaways
1. `\t` moves to the next tab stop (usually every 8 chars)
2. Tabs are simple but can misalign with varying text widths
3. Use `std::setw()` from `<iomanip>` for precise column alignment
4. `std::left` left-aligns within the field width
5. Tab width depends on the terminal — not guaranteed to be 8

## Common Mistakes
- Relying on `\t` for precise alignment → breaks with long strings
- Assuming tab width is consistent across all terminals/editors
- Using multiple `\t\t` to "fix" alignment — fragile solution
