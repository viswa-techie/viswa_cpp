# Inline concept (brief)

> **Level:** 0 — Absolute Beginner  
> **Category:** C00 — C++ Syntax & Program Structure  
> **Topic:** syntax

---

## Problem Statement
Understand the `inline` keyword and its effect on function compilation.

## What You Need to Know
- `inline` suggests the compiler replace a function call with the function body.
- It's a **hint**, not a command — the compiler decides.
- Modern use: allows function definitions in headers without linker errors.

## Basic inline Function
```cpp
#include <iostream>

inline int square(int x) {
    return x * x;
}

int main() {
    // Compiler MAY replace square(5) with (5 * 5) directly
    std::cout << square(5) << "\n";  // 25
    return 0;
}
```

## Without inline vs With inline
```
Without inline:
    main() → CALL square(5) → return 25 → back to main()
    (function call overhead: push args, jump, return)

With inline (if compiler agrees):
    main() → 5 * 5 → 25
    (no function call overhead — code inserted directly)
```

## Why inline Matters for Headers
```cpp
// math.h
#pragma once

// Without inline: including in multiple .cpp files → linker error
// (multiple definition of square)

// With inline: OK — each .cpp gets its own copy
inline int square(int x) {
    return x * x;
}
```

## Modern Perspective
```
Key Points:
1. The compiler inlines functions automatically when beneficial
2. Small functions are usually inlined regardless of the keyword
3. Large functions are usually NOT inlined regardless of the keyword
4. Main modern use: allowing definitions in headers
5. -O2 and higher optimization levels enable aggressive inlining
```

## Key Takeaways
1. `inline` = hint to replace call with body (compiler may ignore)
2. Main modern use: define functions in headers without linker errors
3. Small functions are auto-inlined by the compiler at `-O2`
4. Don't inline large functions — the keyword won't help
5. Class member functions defined inside the class are implicitly inline

## Common Mistakes
- Thinking `inline` guarantees inlining — it's just a suggestion
- Putting large functions in headers with `inline` → code bloat
- Not using `inline` for header-defined functions → linker errors
