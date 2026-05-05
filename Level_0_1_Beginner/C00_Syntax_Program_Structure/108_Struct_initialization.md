# Struct initialization

> **Level:** 0 — Absolute Beginner  
> **Category:** C00 — C++ Syntax & Program Structure  
> **Topic:** syntax

---

## Problem Statement
Learn the different ways to initialize structs in C++.

## What You Need to Know
- Structs can be initialized in multiple ways depending on the C++ standard.
- Uninitialized struct members contain garbage values.
- Default member initializers (C++11) provide default values.

## Method 1: Aggregate Initialization
```cpp
struct Point {
    double x;
    double y;
};

Point p1 = {3.0, 4.0};     // C-style
Point p2{3.0, 4.0};        // C++11 brace init
Point p3 = {};              // Zero-initialized: {0.0, 0.0}
Point p4{};                 // Same as above
```

## Method 2: Default Member Initializers (C++11)
```cpp
#include <iostream>
#include <string>

struct Config {
    int width = 800;
    int height = 600;
    bool fullscreen = false;
    std::string title = "My App";
};

int main() {
    Config c1;    // Uses all defaults: 800, 600, false, "My App"
    Config c2{1920, 1080, true, "Game"};  // Override all
    Config c3{1024, 768};  // Override first two, rest default

    std::cout << c1.title << ": " << c1.width << "x" << c1.height << "\n";
    return 0;
}
```

## Method 3: Designated Initializers (C++20)
```cpp
struct Color {
    int r, g, b;
    int alpha = 255;
};

Color red{.r = 255, .g = 0, .b = 0};              // alpha = 255 (default)
Color semiBlue{.r = 0, .g = 0, .b = 255, .alpha = 128};
```

## Method 4: Constructor
```cpp
#include <iostream>
#include <string>

struct Student {
    std::string name;
    int age;
    double gpa;

    Student(const std::string& n, int a, double g)
        : name(n), age(a), gpa(g) {}
};

int main() {
    Student s("Viswa", 25, 3.85);
    std::cout << s.name << "\n";
    return 0;
}
```

## Comparison
```
Method                    Syntax              C++ Version
------                    ------              -----------
Aggregate init            {val1, val2}        C++11
Default member init       int x = 5;          C++11
Designated init           {.x = 5}            C++20
Constructor               Type(args)          Always
```

## Key Takeaways
1. Use `{}` for aggregate initialization — clean and safe
2. Default member initializers provide fallback values
3. Designated initializers (C++20) make code self-documenting
4. Constructors give full control over initialization logic
5. `Type{}` zero-initializes all members

## Common Mistakes
- Not initializing: `Point p;` leaves x and y as garbage
- Wrong order in designated initializers: must match declaration order
- Mixing designated and positional initializers → not allowed
