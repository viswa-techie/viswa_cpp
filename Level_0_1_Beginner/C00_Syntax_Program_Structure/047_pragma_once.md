# #pragma once

> **Level:** 0 — Absolute Beginner  
> **Category:** C00 — C++ Syntax & Program Structure  
> **Topic:** syntax

---

## Problem Statement
Understand `#pragma once` and how it prevents header files from being included multiple times.

## The Problem: Multiple Inclusion
```cpp
// main.cpp
#include "math.h"
#include "physics.h"    // physics.h also includes math.h
// Now math.h is included TWICE → redefinition errors!
```

## Solution: #pragma once
```cpp
// math.h
#pragma once           // Only include this file once per translation unit

struct Point {
    double x, y;
};

double distance(Point a, Point b);
```
Now even if `math.h` is included multiple times, the preprocessor includes it only once.

## How It Works
```
First time #include "math.h" is seen:
  → Preprocessor reads the file, sees #pragma once
  → Marks this file as "already included"
  → Includes the content

Second time #include "math.h" is seen:
  → Preprocessor checks: already included? YES
  → Skips the entire file
```

## #pragma once vs Include Guards
```cpp
// Method 1: #pragma once (simpler)
#pragma once
struct Foo {};

// Method 2: Include guards (traditional, standard-conforming)
#ifndef FOO_H
#define FOO_H
struct Foo {};
#endif
```

## Comparison
```
Feature              #pragma once     Include Guards
-------              ------------     --------------
Simplicity           Simple (1 line)  3 lines needed
Standard C++?        No (but universal)  Yes
Compiler support     All major compilers  All compilers
Name collision risk  None             Possible (#define name clash)
Performance          Slightly faster  Standard
```

## Key Takeaways
1. `#pragma once` prevents multiple inclusion of the same header
2. Place it at the very top of every header file
3. Not officially in the C++ standard but supported by all major compilers
4. Simpler than traditional include guards
5. Both methods solve the same problem — pick one and be consistent

## Common Mistakes
- Putting `#pragma once` in `.cpp` files — only needed in headers
- Forgetting any inclusion guard → "redefinition" errors
- Using `#pragma once` and include guards together — redundant but harmless
