# Simple enum definition

> **Level:** 0 — Absolute Beginner  
> **Category:** C00 — C++ Syntax & Program Structure  
> **Topic:** syntax

---

## Problem Statement
Use enumerations to define a type with a fixed set of named values.

## What You Need to Know
- An `enum` defines a set of named integer constants.
- Makes code more readable than raw numbers.
- Traditional (unscoped) enums leak names into the enclosing scope.

## Basic Enum
```cpp
#include <iostream>

enum Color {
    RED,      // 0
    GREEN,    // 1
    BLUE      // 2
};

int main() {
    Color c = GREEN;

    if (c == GREEN) {
        std::cout << "Color is green\n";
    }

    std::cout << "Value: " << c << "\n";  // 1
    return 0;
}
```

## Custom Values
```cpp
enum HttpStatus {
    OK = 200,
    NOT_FOUND = 404,
    SERVER_ERROR = 500
};

enum Weekday {
    MONDAY = 1,     // Start from 1 instead of 0
    TUESDAY,        // 2 (auto-increments)
    WEDNESDAY,      // 3
    THURSDAY,       // 4
    FRIDAY,         // 5
    SATURDAY,       // 6
    SUNDAY          // 7
};
```

## Using Enums in Switch
```cpp
#include <iostream>

enum Direction { NORTH, SOUTH, EAST, WEST };

void move(Direction dir) {
    switch (dir) {
        case NORTH: std::cout << "Moving north\n"; break;
        case SOUTH: std::cout << "Moving south\n"; break;
        case EAST:  std::cout << "Moving east\n";  break;
        case WEST:  std::cout << "Moving west\n";  break;
    }
}

int main() {
    move(NORTH);
    move(EAST);
    return 0;
}
```

## Problem with Unscoped Enums
```cpp
enum Color { RED, GREEN, BLUE };
enum TrafficLight { RED, YELLOW, GREEN };  // ERROR! RED and GREEN already defined!

// Solution: use enum class (next topic)
```

## Key Takeaways
1. Enums define named integer constants
2. Default values start at 0 and auto-increment
3. Use enums instead of magic numbers (0, 1, 2)
4. Great with switch statements
5. Unscoped enums leak names — prefer `enum class` (C++11)

## Common Mistakes
- Name collisions: two enums with same value names → error
- Implicit conversion to int can hide bugs
- Forgetting `break` in switch → fall-through
