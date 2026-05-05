# Include guards

> **Level:** 0 — Absolute Beginner  
> **Category:** C00 — C++ Syntax & Program Structure  
> **Topic:** syntax

---

## Problem Statement
Understand include guards — the traditional way to prevent multiple header inclusion.

## What You Need to Know
- Include guards use `#ifndef` / `#define` / `#endif` to wrap the entire header.
- The macro name must be unique across the entire project.
- This is the C++ standard-compliant way to prevent multiple inclusion.

## Basic Pattern
```cpp
// my_header.h

#ifndef MY_HEADER_H    // If MY_HEADER_H is NOT defined...
#define MY_HEADER_H    // ...define it now

// Header content goes here
struct Point {
    double x, y;
};

void printPoint(Point p);

#endif // MY_HEADER_H  // End of guard
```

## How It Works
```
First #include "my_header.h":
  → Is MY_HEADER_H defined? NO
  → Define MY_HEADER_H
  → Include all content between #ifndef and #endif

Second #include "my_header.h":
  → Is MY_HEADER_H defined? YES
  → Skip everything until #endif
  → Nothing is included
```

## Naming Convention
```cpp
// Common patterns for guard names:
#ifndef FILENAME_H           // Simple
#ifndef PROJECT_FILENAME_H   // With project prefix
#ifndef MY_PROJECT_SRC_UTILS_MATH_H  // Full path
#ifndef MATH_UTILS_HPP_      // With extension
```

## Complete Example
```cpp
// rectangle.h
#ifndef RECTANGLE_H
#define RECTANGLE_H

struct Rectangle {
    double width;
    double height;
};

double area(Rectangle r);
double perimeter(Rectangle r);

#endif // RECTANGLE_H
```

```cpp
// rectangle.cpp
#include "rectangle.h"

double area(Rectangle r) {
    return r.width * r.height;
}

double perimeter(Rectangle r) {
    return 2 * (r.width + r.height);
}
```

```cpp
// main.cpp
#include <iostream>
#include "rectangle.h"   // Safe to include — has include guard

int main() {
    Rectangle r = {5.0, 3.0};
    std::cout << "Area: " << area(r) << "\n";
    return 0;
}
```

## Key Takeaways
1. Pattern: `#ifndef GUARD` → `#define GUARD` → content → `#endif`
2. Guard name must be unique — use filename + project name
3. This is the standard, portable method (unlike `#pragma once`)
4. Place the guard around ALL header content
5. Comment `#endif` with the guard name for clarity

## Common Mistakes
- Duplicate guard names across different headers → one header silently excluded
- Placing code outside the guard (before `#ifndef` or after `#endif`)
- Forgetting `#endif` → everything after this header is conditionally excluded
