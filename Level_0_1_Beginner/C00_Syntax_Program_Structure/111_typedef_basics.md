# typedef basics

> **Level:** 0 — Absolute Beginner  
> **Category:** C00 — C++ Syntax & Program Structure  
> **Topic:** syntax

---

## Problem Statement
Use `typedef` to create aliases for types, making code more readable.

## What You Need to Know
- `typedef` creates a new name for an existing type.
- It doesn't create a new type — just an alias.
- Widely used in C; in modern C++, `using` is preferred.

## Basic typedef
```cpp
#include <iostream>

typedef int Integer;
typedef double Real;
typedef unsigned long ulong;

int main() {
    Integer x = 42;        // Same as: int x = 42;
    Real pi = 3.14;        // Same as: double pi = 3.14;
    ulong big = 1000000UL;

    std::cout << x << " " << pi << " " << big << "\n";
    return 0;
}
```

## typedef with Complex Types
```cpp
#include <iostream>
#include <vector>
#include <map>
#include <string>

// Without typedef — verbose
std::map<std::string, std::vector<int>> studentScores;

// With typedef — clean
typedef std::map<std::string, std::vector<int>> ScoreMap;
ScoreMap scores;

// Function pointers
typedef int (*MathFunc)(int, int);

int add(int a, int b) { return a + b; }

int main() {
    MathFunc op = add;
    std::cout << op(3, 4) << "\n";  // 7
    return 0;
}
```

## typedef for Structs (C-style)
```cpp
// C style: need typedef to avoid writing "struct" everywhere
typedef struct {
    double x, y;
} Point;

// C++: struct name works directly (typedef not needed)
struct Point2 {
    double x, y;
};

Point p1 = {1.0, 2.0};
Point2 p2 = {3.0, 4.0};   // Both work the same in C++
```

## Key Takeaways
1. `typedef existing_type new_name;` creates an alias
2. Makes complex types readable (maps, vectors, function pointers)
3. Doesn't create a new type — just a new name
4. In modern C++, prefer `using` over `typedef`
5. Still commonly seen in C codebases and older C++ code

## Common Mistakes
- Syntax confusion: `typedef int* IntPtr;` — IntPtr is the alias, not int*
- `typedef int* A, B;` — A is `int*`, B is `int` (not `int*`!)
- Thinking typedef creates a distinct type — it doesn't (no extra type safety)
