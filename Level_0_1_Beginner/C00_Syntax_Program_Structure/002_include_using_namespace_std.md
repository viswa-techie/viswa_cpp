# #include, using namespace std

> **Level:** 0 — Absolute Beginner  
> **Category:** C00 — C++ Syntax & Program Structure  
> **Topic:** syntax

---

## Problem Statement
Understand what `#include` and `using namespace std` do in a C++ program.

## What You Need to Know
- `#include` is a **preprocessor directive** — it copies the contents of a header file into your source file before compilation.
- `<iostream>` is a **header file** that declares `cout`, `cin`, `endl`, etc.
- `std` is a **namespace** — a container that groups all standard library names.
- `using namespace std;` makes everything in `std` available without the `std::` prefix.

## Mental Model
Think of `#include` as importing a toolbox. The tools are labeled "std::hammer", "std::screwdriver". `using namespace std;` removes the "std::" label so you can just say "hammer".

## How It Works (Under the Hood)
```
Step 1: You write:   #include <iostream>
Step 2: Preprocessor replaces this line with ~20,000+ lines from iostream header
Step 3: Compiler now knows about std::cout, std::cin, etc.
```

## Solution 1: With `using namespace std`
```cpp
#include <iostream>
using namespace std;

int main() {
    cout << "Hello" << endl;  // No std:: needed
    return 0;
}
```

## Solution 2: Without `using namespace std` (Best Practice)
```cpp
#include <iostream>

int main() {
    std::cout << "Hello" << std::endl;
    return 0;
}
```

## Solution 3: Selective `using` declarations
```cpp
#include <iostream>
using std::cout;
using std::endl;

int main() {
    cout << "Hello" << endl;
    return 0;
}
```
**Best of both worlds:** Only imports what you need.

## Why `using namespace std` Is Risky
```cpp
#include <iostream>
#include <algorithm>
using namespace std;

int count = 5;  // PROBLEM: std::count also exists!
// This causes ambiguity or silent bugs
```

## Key Takeaways
1. `#include` literally pastes header content into your file
2. `<>` for system headers, `""` for your own headers
3. `std::` prefix is verbose but safe
4. `using namespace std;` is OK for small programs, risky for large ones
5. In header files, NEVER use `using namespace std;`

## Common Mistakes
- `#include "iostream"` — works but wrong convention (use `<>` for standard headers)
- Forgetting the semicolon after `using namespace std`
- Using `#include <iostream.h>` — this is pre-standard C++ and doesn't exist in modern compilers

## Pattern
**Header inclusion pattern** — include what you use, no more.
