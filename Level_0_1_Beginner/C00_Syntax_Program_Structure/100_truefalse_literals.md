# true/false literals

> **Level:** 0 — Absolute Beginner  
> **Category:** C00 — C++ Syntax & Program Structure  
> **Topic:** syntax

---

## Problem Statement
Understand the `true` and `false` boolean literals in C++.

## What You Need to Know
- `true` and `false` are C++ keywords of type `bool`.
- `true` converts to `1`, `false` converts to `0`.
- Any non-zero value converts to `true`, zero converts to `false`.

## Basic Usage
```cpp
#include <iostream>

int main() {
    bool isReady = true;
    bool isDone = false;

    std::cout << std::boolalpha;
    std::cout << "Ready: " << isReady << "\n";   // true
    std::cout << "Done: " << isDone << "\n";     // false

    // Without boolalpha
    std::cout << std::noboolalpha;
    std::cout << "Ready: " << isReady << "\n";   // 1
    std::cout << "Done: " << isDone << "\n";     // 0

    return 0;
}
```

## Integer ↔ Bool Conversion
```cpp
#include <iostream>

int main() {
    // Bool to int
    int a = true;    // 1
    int b = false;   // 0

    // Int to bool
    bool c = 42;     // true (any non-zero)
    bool d = 0;      // false
    bool e = -1;     // true (any non-zero)

    // Pointer to bool
    int x = 5;
    int* ptr = &x;
    bool f = ptr;        // true (non-null pointer)
    bool g = nullptr;    // false (null pointer)

    std::cout << std::boolalpha;
    std::cout << c << " " << d << " " << e << "\n";
    return 0;
}
```

## Boolean in Conditions
```cpp
#include <iostream>

int main() {
    bool loggedIn = true;

    // These are equivalent:
    if (loggedIn == true) { /* ... */ }
    if (loggedIn) { /* ... */ }         // Preferred — cleaner

    // These are equivalent:
    if (loggedIn == false) { /* ... */ }
    if (!loggedIn) { /* ... */ }        // Preferred — cleaner

    return 0;
}
```

## sizeof(bool)
```cpp
#include <iostream>

int main() {
    std::cout << "sizeof(bool): " << sizeof(bool) << "\n";  // 1 byte
    // bool uses 1 byte even though it only needs 1 bit
    // This is because the smallest addressable unit is 1 byte
    return 0;
}
```

## Key Takeaways
1. `true` = 1, `false` = 0 (when converted to int)
2. Any non-zero → `true`, zero → `false`
3. Use `std::boolalpha` to print "true"/"false"
4. Don't compare to `true`/`false` explicitly: `if (x)` not `if (x == true)`
5. `sizeof(bool)` is 1 byte (not 1 bit)

## Common Mistakes
- `if (x == true)` where x is an int ≠ `if (x)` — `42 == true` is `42 == 1` → false!
- Expecting `bool` to be 1 bit — it's 1 byte
- Using integers (0/1) instead of `true`/`false` — less readable
