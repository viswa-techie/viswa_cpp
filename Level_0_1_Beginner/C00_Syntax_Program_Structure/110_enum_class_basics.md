# enum class basics

> **Level:** 0 — Absolute Beginner  
> **Category:** C00 — C++ Syntax & Program Structure  
> **Topic:** syntax

---

## Problem Statement
Use `enum class` (scoped enums) — the modern, safer alternative to traditional enums.

## What You Need to Know
- `enum class` (C++11) keeps names scoped — no name collisions.
- Values don't implicitly convert to integers.
- Access values with `EnumName::Value` syntax.

## Basic enum class
```cpp
#include <iostream>

enum class Color {
    Red,
    Green,
    Blue
};

int main() {
    Color c = Color::Green;     // Must use scope: Color::

    if (c == Color::Green) {
        std::cout << "Green!\n";
    }

    // int x = c;               // ERROR! No implicit conversion
    int x = static_cast<int>(c);  // OK: explicit conversion → 1

    return 0;
}
```

## No Name Collisions
```cpp
enum class Color { Red, Green, Blue };
enum class TrafficLight { Red, Yellow, Green };  // OK! No collision

// Color::Red and TrafficLight::Red are completely separate
```

## Specifying Underlying Type
```cpp
// Default underlying type is int
enum class ErrorCode : uint8_t {   // Use uint8_t (1 byte) to save memory
    Success = 0,
    NotFound = 1,
    Timeout = 2,
    Unknown = 255
};

// Underlying type can be any integer type
enum class BigEnum : long long {
    Huge = 1000000000LL
};
```

## Switch with enum class
```cpp
#include <iostream>

enum class Season { Spring, Summer, Autumn, Winter };

void describe(Season s) {
    switch (s) {
        case Season::Spring: std::cout << "Flowers bloom\n"; break;
        case Season::Summer: std::cout << "Sun shines\n"; break;
        case Season::Autumn: std::cout << "Leaves fall\n"; break;
        case Season::Winter: std::cout << "Snow falls\n"; break;
    }
}

int main() {
    describe(Season::Summer);
    return 0;
}
```

## enum vs enum class
```
Feature              enum (unscoped)      enum class (scoped)
-------              ---------------      -------------------
Scope                Leaks to enclosing   Contained in enum
Name collision       Possible             Impossible
Implicit to int      Yes                  No (need cast)
Type safety          Weak                 Strong
Syntax               Color::Red or Red    Color::Red only
C++ version          All                  C++11+
```

## Key Takeaways
1. `enum class` scopes values — access with `Enum::Value`
2. No implicit integer conversion — prevents accidental misuse
3. No name collisions between different enum classes
4. Specify underlying type: `enum class X : uint8_t { ... }`
5. Always prefer `enum class` over plain `enum` in modern C++

## Common Mistakes
- Forgetting scope prefix: `Red` instead of `Color::Red` → error
- Trying to use enum class in arithmetic without casting
- Using plain `enum` when `enum class` is available
