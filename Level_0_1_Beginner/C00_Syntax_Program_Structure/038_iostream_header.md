# iostream header

> **Level:** 0 — Absolute Beginner  
> **Category:** C00 — C++ Syntax & Program Structure  
> **Topic:** syntax

---

## Problem Statement
Understand what `<iostream>` provides and how standard I/O works in C++.

## What You Need to Know
- `<iostream>` is the primary C++ header for input/output.
- It defines `std::cin`, `std::cout`, `std::cerr`, and `std::clog`.

## What iostream Provides
```
Object       Type              Purpose
------       ----              -------
std::cin     istream           Standard input (keyboard)
std::cout    ostream           Standard output (screen)
std::cerr    ostream           Standard error (unbuffered)
std::clog    ostream           Standard log (buffered)
std::endl    manipulator       Newline + flush
```

## Basic Usage
```cpp
#include <iostream>   // Must include this for I/O

int main() {
    int x;
    std::cout << "Enter a number: ";  // Output to screen
    std::cin >> x;                     // Input from keyboard
    std::cout << "You entered: " << x << std::endl;

    std::cerr << "This goes to stderr\n";  // Error stream
    std::clog << "This is a log message\n"; // Log stream
    return 0;
}
```

## Stream Operators
```cpp
#include <iostream>

int main() {
    // << is the insertion operator (output)
    std::cout << "Hello" << " " << "World" << "\n";

    // >> is the extraction operator (input)
    int a, b;
    std::cin >> a >> b;   // Read two integers

    return 0;
}
```

## iostream vs stdio
```
Feature         <iostream>       <cstdio>
-------         ----------       --------
Output          cout << x        printf("%d", x)
Input           cin >> x         scanf("%d", &x)
Type safety     Yes              No
Extensible      Yes              No
Performance     Good             Slightly faster
Sync with C     Yes (default)    N/A
```

## Disable sync for performance
```cpp
#include <iostream>

int main() {
    // Speeds up cin/cout by disabling sync with C stdio
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);

    // Now cin/cout are faster but can't mix with printf/scanf
    int n;
    std::cin >> n;
    std::cout << n << "\n";
    return 0;
}
```

## Key Takeaways
1. Always `#include <iostream>` for `cin`, `cout`, `cerr`, `clog`
2. `<<` for output, `>>` for input
3. `cerr` is unbuffered — use for error messages
4. `clog` is buffered — use for log messages
5. Disable sync for competitive programming speed boost

## Common Mistakes
- Forgetting `#include <iostream>` → "cout was not declared"
- Using `iostream.h` (old, non-standard) instead of `<iostream>`
- Not including `<string>` when using `std::string` with I/O
