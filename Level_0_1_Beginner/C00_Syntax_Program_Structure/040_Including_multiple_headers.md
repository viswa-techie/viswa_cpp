# Including multiple headers

> **Level:** 0 — Absolute Beginner  
> **Category:** C00 — C++ Syntax & Program Structure  
> **Topic:** syntax

---

## Problem Statement
Learn how to include multiple headers properly and understand header organization.

## What You Need to Know
- Each `#include` brings in declarations from one header file.
- Include only the headers you actually use.
- Order of includes matters for style, not usually for correctness.

## Common C++ Headers
```cpp
// I/O
#include <iostream>       // cin, cout, cerr
#include <fstream>        // File I/O
#include <sstream>        // String streams

// Strings
#include <string>         // std::string
#include <cstring>        // C-string functions (strlen, strcpy)

// Containers
#include <vector>         // Dynamic array
#include <array>          // Fixed-size array
#include <map>            // Key-value pairs
#include <set>            // Unique sorted elements
#include <unordered_map>  // Hash map

// Algorithms & Utilities
#include <algorithm>      // sort, find, etc.
#include <numeric>        // accumulate, iota
#include <cmath>          // Math functions
#include <climits>        // INT_MAX, INT_MIN
#include <cassert>        // assert macro

// C compatibility
#include <cstdio>         // printf, scanf
#include <cstdlib>        // malloc, free, exit
#include <cctype>         // isalpha, isdigit
```

## Recommended Include Order
```cpp
// 1. Corresponding header (for .cpp files)
#include "myclass.h"

// 2. C++ standard library headers
#include <iostream>
#include <string>
#include <vector>

// 3. C standard library headers (wrapped)
#include <cstdio>
#include <cmath>

// 4. Third-party library headers
#include <boost/algorithm/string.hpp>

// 5. Project-specific headers
#include "utils.h"
#include "config.h"
```

## System vs User Headers
```cpp
#include <iostream>    // Angle brackets: search system/standard paths
#include "myfile.h"    // Quotes: search current directory first, then system
```

## Example: Using Multiple Headers
```cpp
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

int main() {
    std::vector<std::string> names = {"Charlie", "Alice", "Bob"};
    std::sort(names.begin(), names.end());

    for (const auto& name : names) {
        std::cout << name << "\n";
    }
    return 0;
}
```

## Key Takeaways
1. Include only what you use — don't include everything
2. Use `<header>` for standard/system, `"header"` for your own files
3. Follow a consistent include order in your project
4. `<cXXX>` headers (e.g., `<cmath>`) are C++ versions of C headers
5. Duplicate includes are harmless (headers have include guards)

## Common Mistakes
- Including `<bits/stdc++.h>` — non-standard, GCC-only, slows compilation
- Not including `<string>` when using `std::string` (may work on some compilers but not portable)
- Including unused headers → slower compilation
