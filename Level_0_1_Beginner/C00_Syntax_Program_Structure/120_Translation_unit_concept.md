# Translation unit concept

> **Level:** 0 — Absolute Beginner  
> **Category:** C00 — C++ Syntax & Program Structure  
> **Topic:** syntax

---

## Problem Statement
Understand translation units — the basic unit of compilation in C++.

## What You Need to Know
- A **translation unit** = one `.cpp` file + all its `#include`d headers after preprocessing.
- Each translation unit is compiled independently into one object file (`.o`).
- The linker combines all object files into the final executable.

## What Makes a Translation Unit
```
main.cpp
  + #include <iostream>     (thousands of lines from standard headers)
  + #include "utils.h"      (your header declarations)
  = One translation unit    (compiled to main.o)

utils.cpp
  + #include "utils.h"
  = Another translation unit (compiled to utils.o)
```

## Visual
```
Source files:         After preprocessing:        Compilation:

main.cpp ──┐
            ├──→ [main.cpp + all headers] ──→ main.o
iostream ──┘
utils.h ──┘

utils.cpp ──┐
             ├──→ [utils.cpp + all headers] ──→ utils.o
utils.h ───┘

                                     Linking:
                           main.o + utils.o ──→ executable
```

## Why It Matters
```
Key implications:
1. Each TU is compiled independently — can't see other .cpp files
2. Headers share declarations across TUs
3. static/anonymous namespace limits visibility to one TU
4. ODR applies: one definition per entity per TU (or per program for functions)
5. Errors in one TU don't prevent other TUs from compiling
```

## Seeing the Translation Unit
```bash
# Preprocess to see the full translation unit
g++ -E main.cpp -o main.i

# Check the size
wc -l main.i
# Even a simple "Hello World" can be 30,000+ lines after preprocessing!
```

## One TU, One Object File
```bash
# Each .cpp → one .o
g++ -c main.cpp    # → main.o
g++ -c utils.cpp   # → utils.o
g++ -c math.cpp    # → math.o

# Link all .o files
g++ main.o utils.o math.o -o program
```

## Internal Linkage (File-Private)
```cpp
// utils.cpp
static int counter = 0;      // Only visible in this translation unit
namespace {
    void helper() {}          // Only visible in this translation unit
}
```

## Key Takeaways
1. Translation unit = `.cpp` file + all included headers
2. Each TU is compiled independently into one `.o` file
3. Headers enable sharing declarations across TUs
4. `static` and anonymous namespaces limit scope to one TU
5. The linker resolves cross-TU references

## Common Mistakes
- Thinking two `.cpp` files can see each other's contents directly
- Not understanding why header definitions cause "multiple definition" errors
- `#include "file.cpp"` — never include `.cpp` files!
