# Basic struct definition

> **Level:** 0 — Absolute Beginner  
> **Category:** C00 — C++ Syntax & Program Structure  
> **Topic:** syntax

---

## Problem Statement
Define and use structs to group related data together.

## What You Need to Know
- A `struct` groups multiple variables (members) under one name.
- Members can be different types.
- In C++, structs can also have functions (methods), constructors, etc.

## Basic Definition
```cpp
#include <iostream>
#include <string>

struct Student {
    std::string name;
    int age;
    double gpa;
};    // Don't forget the semicolon!

int main() {
    Student s;
    s.name = "Viswa";
    s.age = 25;
    s.gpa = 3.85;

    std::cout << s.name << ", " << s.age << ", " << s.gpa << "\n";
    return 0;
}
```

## Initialization Methods
```cpp
#include <iostream>
#include <string>

struct Point {
    double x;
    double y;
};

int main() {
    // Method 1: Member-by-member
    Point p1;
    p1.x = 3.0;
    p1.y = 4.0;

    // Method 2: Aggregate initialization
    Point p2 = {1.0, 2.0};

    // Method 3: C++11 brace initialization
    Point p3{5.0, 6.0};

    // Method 4: Designated initializers (C++20)
    Point p4{.x = 7.0, .y = 8.0};

    return 0;
}
```

## Struct with Functions
```cpp
#include <iostream>
#include <cmath>

struct Point {
    double x;
    double y;

    double distanceTo(const Point& other) const {
        double dx = x - other.x;
        double dy = y - other.y;
        return std::sqrt(dx*dx + dy*dy);
    }

    void print() const {
        std::cout << "(" << x << ", " << y << ")\n";
    }
};

int main() {
    Point a{3.0, 0.0};
    Point b{0.0, 4.0};
    a.print();
    std::cout << "Distance: " << a.distanceTo(b) << "\n";  // 5.0
    return 0;
}
```

## Struct vs Class
```
Feature     struct (default)    class (default)
-------     ----------------    ---------------
Access      public              private
Usage       Simple data types   Complex objects
Convention  POD/data bundles    Full OOP
```
In C++, the ONLY difference is the default access level.

## Key Takeaways
1. Structs group related variables into a single type
2. Access members with `.` (dot operator)
3. Don't forget the semicolon after the closing `}`
4. Structs can have methods, constructors, and more in C++
5. Use structs for simple data aggregation

## Common Mistakes
- Forgetting `;` after struct definition → confusing compile errors
- Not initializing struct members → garbage values
- Confusing struct and class — in C++, they're almost identical
