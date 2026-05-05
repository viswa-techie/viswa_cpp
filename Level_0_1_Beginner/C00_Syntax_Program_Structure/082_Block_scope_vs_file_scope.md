# Block scope vs file scope

> **Level:** 0 — Absolute Beginner  
> **Category:** C00 — C++ Syntax & Program Structure  
> **Topic:** syntax

---

## Problem Statement
Understand the two main scope levels: block scope (local) and file scope (global).

## What You Need to Know
- **Block scope**: variable declared inside `{}` — visible only within that block.
- **File scope**: variable declared outside all functions — visible in the entire file.
- Narrower scope = better — reduces accidental interactions.

## Block Scope
```cpp
#include <iostream>

int main() {
    int a = 1;         // Block scope: main

    if (true) {
        int b = 2;     // Block scope: if-block
        std::cout << a << " " << b << "\n";   // Both visible
    }

    for (int i = 0; i < 3; ++i) {
        int c = 3;     // Block scope: for-loop body
        // i is also block-scoped to the for statement
    }

    // b, c, i are NOT accessible here
    std::cout << a << "\n";
    return 0;
}
```

## File Scope
```cpp
#include <iostream>

// File scope — accessible everywhere in this file after declaration
int globalVar = 100;
const double PI = 3.14159;

void printGlobal() {
    std::cout << globalVar << "\n";   // Accessible
}

int main() {
    std::cout << globalVar << "\n";   // Accessible
    std::cout << PI << "\n";          // Accessible
    printGlobal();
    return 0;
}
```

## Limiting File Scope
```cpp
// Without static: visible to other files via extern
int publicVar = 10;

// With static: visible ONLY in this file
static int privateVar = 20;

// Anonymous namespace: same as static (modern C++ preferred)
namespace {
    int alsoPrivate = 30;
}
```

## Scope Comparison
```
Scope       Declared Where       Visible Where         Lifetime
-----       --------------       -------------         --------
Block       Inside {}            Only within {}        Scope duration
Function    Inside function      Entire function       Function duration
File        Outside functions    Entire file           Program duration
Global      File scope + extern  Multiple files        Program duration
```

## Best Practice: Minimize Scope
```cpp
#include <iostream>
#include <vector>

int main() {
    std::vector<int> data = {5, 3, 8, 1, 9};

    // GOOD: 'i' scoped to loop only
    for (size_t i = 0; i < data.size(); ++i) {
        std::cout << data[i] << " ";
    }
    // i doesn't exist here — can't accidentally misuse it

    // EVEN BETTER: range-for, no index variable at all
    for (int val : data) {
        std::cout << val << " ";
    }
    return 0;
}
```

## Key Takeaways
1. Block scope `{}` is the narrowest — prefer it
2. File scope is the widest within a single file
3. Use `static` or anonymous namespace to limit file-scope variables
4. Declare variables in the smallest scope possible
5. Loop variables in `for(int i = ...)` are block-scoped to the loop

## Common Mistakes
- Declaring variables at file scope when they could be local
- Expecting loop variable `i` to be accessible after the loop
- Two files with same global name → linker error (unless one is `static`)
