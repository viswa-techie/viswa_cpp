# Multiple source files concept

> **Level:** 0 — Absolute Beginner  
> **Category:** C00 — C++ Syntax & Program Structure  
> **Topic:** syntax

---

## Problem Statement
Understand why and how to split a C++ program across multiple source files.

## What You Need to Know
- Real programs have thousands of lines — putting everything in one file is unmanageable.
- Each `.cpp` file is compiled independently into an `.o` (object) file.
- The linker combines all `.o` files into one executable.

## Project Structure
```
project/
├── main.cpp          // Entry point
├── math_utils.h      // Declarations
├── math_utils.cpp    // Definitions
├── string_utils.h    // Declarations
└── string_utils.cpp  // Definitions
```

## Step-by-Step Example

### math_utils.h — Declarations
```cpp
#pragma once

int add(int a, int b);
int multiply(int a, int b);
```

### math_utils.cpp — Definitions
```cpp
#include "math_utils.h"

int add(int a, int b) {
    return a + b;
}

int multiply(int a, int b) {
    return a * b;
}
```

### main.cpp — Uses the functions
```cpp
#include <iostream>
#include "math_utils.h"

int main() {
    std::cout << "3 + 4 = " << add(3, 4) << "\n";
    std::cout << "3 * 4 = " << multiply(3, 4) << "\n";
    return 0;
}
```

### Compilation
```bash
# Compile each file separately
g++ -c main.cpp -o main.o
g++ -c math_utils.cpp -o math_utils.o

# Link them together
g++ main.o math_utils.o -o program

# Or all at once
g++ main.cpp math_utils.cpp -o program
```

## Why Separate Files?
```
Benefit              Explanation
-------              -----------
Organization         Each file has one responsibility
Faster recompilation Only recompile changed files
Team collaboration   Multiple people work on different files
Reusability          Use math_utils in other projects
Readability          Smaller files are easier to understand
```

## Key Takeaways
1. Split code into header (`.h`) + source (`.cpp`) pairs
2. Headers contain declarations; source files contain definitions
3. `main.cpp` includes headers to use functions from other files
4. Compile each `.cpp` file, then link the `.o` files together
5. Only `main()` should appear once across all files

## Common Mistakes
- Including `.cpp` files: `#include "math.cpp"` → multiple definitions
- Forgetting to compile all `.cpp` files → "undefined reference" errors
- Putting definitions in headers → linker errors when included by multiple files
