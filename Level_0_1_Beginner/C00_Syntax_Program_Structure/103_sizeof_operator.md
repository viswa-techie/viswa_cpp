# sizeof operator

> **Level:** 0 — Absolute Beginner  
> **Category:** C00 — C++ Syntax & Program Structure  
> **Topic:** syntax

---

## Problem Statement
Use `sizeof` to determine the size (in bytes) of types and variables.

## What You Need to Know
- `sizeof` returns the size in bytes at compile time.
- Works on types and expressions.
- `sizeof(char)` is always 1 byte (by definition).

## Basic Usage
```cpp
#include <iostream>

int main() {
    std::cout << "char:        " << sizeof(char)        << " bytes\n";
    std::cout << "short:       " << sizeof(short)       << " bytes\n";
    std::cout << "int:         " << sizeof(int)         << " bytes\n";
    std::cout << "long:        " << sizeof(long)        << " bytes\n";
    std::cout << "long long:   " << sizeof(long long)   << " bytes\n";
    std::cout << "float:       " << sizeof(float)       << " bytes\n";
    std::cout << "double:      " << sizeof(double)      << " bytes\n";
    std::cout << "bool:        " << sizeof(bool)        << " bytes\n";
    std::cout << "pointer:     " << sizeof(int*)        << " bytes\n";
    return 0;
}
```

Typical output (64-bit Linux):
```
char:        1 bytes
short:       2 bytes
int:         4 bytes
long:        8 bytes
long long:   8 bytes
float:       4 bytes
double:      8 bytes
bool:        1 bytes
pointer:     8 bytes
```

## sizeof on Variables
```cpp
#include <iostream>
#include <string>
#include <vector>

int main() {
    int x = 42;
    double pi = 3.14;
    char c = 'A';
    int arr[10];

    std::cout << "x:     " << sizeof(x) << "\n";    // 4
    std::cout << "pi:    " << sizeof(pi) << "\n";    // 8
    std::cout << "c:     " << sizeof(c) << "\n";     // 1
    std::cout << "arr:   " << sizeof(arr) << "\n";   // 40 (10 * 4)

    // Array element count
    std::cout << "arr elements: " << sizeof(arr) / sizeof(arr[0]) << "\n";  // 10

    return 0;
}
```

## sizeof with Structs
```cpp
#include <iostream>

struct Point {
    double x;    // 8 bytes
    double y;    // 8 bytes
};

struct Padded {
    char a;      // 1 byte + 3 padding
    int b;       // 4 bytes
    char c;      // 1 byte + 3 padding
};

int main() {
    std::cout << "Point:  " << sizeof(Point) << "\n";   // 16
    std::cout << "Padded: " << sizeof(Padded) << "\n";  // 12 (not 6!)
    return 0;
}
```

## Key Takeaways
1. `sizeof` is a compile-time operator — no runtime cost
2. `sizeof(char)` is always 1 (by definition)
3. Pointer sizes are platform-dependent (4 on 32-bit, 8 on 64-bit)
4. Struct sizes may include padding for alignment
5. Array length: `sizeof(arr) / sizeof(arr[0])`

## Common Mistakes
- `sizeof(pointer)` gives pointer size, not what it points to
- `sizeof(std::string)` gives the object size, not the string content length
- Array decays to pointer in function args: `sizeof(arr)` gives pointer size, not array size
