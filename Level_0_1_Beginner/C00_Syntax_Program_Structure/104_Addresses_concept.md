# Addresses concept

> **Level:** 0 — Absolute Beginner  
> **Category:** C00 — C++ Syntax & Program Structure  
> **Topic:** syntax

---

## Problem Statement
Understand memory addresses — every variable has a location in memory.

## What You Need to Know
- Every variable occupies a location in memory, identified by an **address**.
- The `&` operator (address-of) gives you the address of a variable.
- Addresses are stored in **pointers**.

## Getting an Address
```cpp
#include <iostream>

int main() {
    int x = 42;

    std::cout << "Value: " << x << "\n";
    std::cout << "Address: " << &x << "\n";  // Something like 0x7ffd4a3b2c4c

    double pi = 3.14;
    std::cout << "pi address: " << &pi << "\n";

    return 0;
}
```

## Storing Addresses in Pointers
```cpp
#include <iostream>

int main() {
    int x = 42;
    int* ptr = &x;   // ptr stores the address of x

    std::cout << "x value: " << x << "\n";      // 42
    std::cout << "x address: " << &x << "\n";    // 0x7fff...
    std::cout << "ptr value: " << ptr << "\n";   // Same address as &x
    std::cout << "ptr points to: " << *ptr << "\n"; // 42 (dereference)

    return 0;
}
```

## Memory Layout Visualization
```
Address        Content     Variable
---------      -------     --------
0x1000         42          x (int, 4 bytes)
0x1004         ...
...
0x1008         3.14        pi (double, 8 bytes)
...
0x1010         0x1000      ptr (points to x)
```

## Multiple Variables
```cpp
#include <iostream>

int main() {
    int a = 10, b = 20, c = 30;

    std::cout << "a at " << &a << "\n";
    std::cout << "b at " << &b << "\n";
    std::cout << "c at " << &c << "\n";
    // Addresses are typically 4 bytes apart (sizeof(int))
    // Stack grows downward, so addresses may decrease

    return 0;
}
```

## Key Takeaways
1. Every variable has an address in memory — use `&var` to get it
2. Addresses are hexadecimal numbers (like `0x7ffd4a3b2c4c`)
3. Pointers store addresses: `int* ptr = &x;`
4. `*ptr` dereferences the pointer — gives the value at that address
5. Understanding addresses is fundamental to C++ pointers and references

## Common Mistakes
- Confusing `&` (address-of) with `&` (reference) — context matters
- Printing `&char_var` — cout treats `char*` as a string, use `(void*)&c`
- Assuming addresses are predictable — ASLR randomizes them
