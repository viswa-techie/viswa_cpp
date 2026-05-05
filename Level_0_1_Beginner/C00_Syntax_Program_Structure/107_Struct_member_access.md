# Struct member access

> **Level:** 0 — Absolute Beginner  
> **Category:** C00 — C++ Syntax & Program Structure  
> **Topic:** syntax

---

## Problem Statement
Access and modify struct members using the dot (`.`) and arrow (`->`) operators.

## What You Need to Know
- Use `.` to access members of a struct variable.
- Use `->` to access members through a pointer to a struct.
- `ptr->member` is shorthand for `(*ptr).member`.

## Dot Operator (.)
```cpp
#include <iostream>
#include <string>

struct Person {
    std::string name;
    int age;
};

int main() {
    Person p;
    p.name = "Viswa";    // Set member
    p.age = 30;

    std::cout << p.name << " is " << p.age << " years old\n";

    // Read and modify
    p.age += 1;
    std::cout << "Next year: " << p.age << "\n";  // 31

    return 0;
}
```

## Arrow Operator (->)
```cpp
#include <iostream>
#include <string>

struct Point {
    double x, y;
};

int main() {
    Point p = {3.0, 4.0};
    Point* ptr = &p;

    // Access through pointer
    std::cout << ptr->x << ", " << ptr->y << "\n";  // 3, 4

    // Equivalent but verbose:
    std::cout << (*ptr).x << ", " << (*ptr).y << "\n";

    // Modify through pointer
    ptr->x = 10.0;
    std::cout << p.x << "\n";  // 10 (modified through pointer)

    return 0;
}
```

## Passing Structs to Functions
```cpp
#include <iostream>
#include <string>

struct Rectangle {
    double width, height;
};

// By value (copy)
double area(Rectangle r) {
    return r.width * r.height;
}

// By const reference (no copy, read-only)
void print(const Rectangle& r) {
    std::cout << r.width << " x " << r.height << "\n";
}

// By reference (can modify)
void scale(Rectangle& r, double factor) {
    r.width *= factor;
    r.height *= factor;
}

int main() {
    Rectangle r = {5.0, 3.0};
    print(r);                      // 5 x 3
    std::cout << area(r) << "\n";  // 15
    scale(r, 2.0);
    print(r);                      // 10 x 6
    return 0;
}
```

## Key Takeaways
1. `.` accesses members of an object: `obj.member`
2. `->` accesses members through a pointer: `ptr->member`
3. `ptr->x` is equivalent to `(*ptr).x`
4. Pass structs by `const&` to avoid copies
5. Members can be read, written, and used in expressions

## Common Mistakes
- Using `->` on a non-pointer: `obj->member` → compile error
- Using `.` on a pointer: `ptr.member` → compile error
- Forgetting `const` when passing struct by reference (allows unwanted modification)
