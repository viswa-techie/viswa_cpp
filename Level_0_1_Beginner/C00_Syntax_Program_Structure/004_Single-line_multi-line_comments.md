# Single-line & multi-line comments

> **Level:** 0 — Absolute Beginner  
> **Category:** C00 — C++ Syntax & Program Structure  
> **Topic:** syntax

---

## Problem Statement
Learn how to write comments in C++ and when to use each style.

## What You Need to Know
- Comments are ignored by the compiler — they're for humans.
- Two styles: single-line (`//`) and multi-line (`/* ... */`).
- Comments explain WHY, not WHAT (good code is self-documenting for WHAT).

## Solution: Comment Styles
```cpp
// This is a single-line comment

/* This is a
   multi-line comment */

/**
 * This is a documentation comment (Doxygen style)
 * @param x The input value
 * @return The squared value
 */
int square(int x) {
    return x * x;  // inline comment
}
```

## Good vs Bad Comments
```cpp
// BAD: States the obvious
int age = 25;  // set age to 25

// GOOD: Explains WHY
int timeout = 3000;  // 3 seconds — server needs at least 2s to respond

// GOOD: Warns about non-obvious behavior
// NOTE: This function is NOT thread-safe
void updateCache() { /* ... */ }
```

## Key Takeaways
1. `//` for single lines, `/* */` for blocks
2. Comments don't nest: `/* /* inner */ outer */` breaks
3. Use comments to explain WHY, not WHAT
4. TODO/FIXME/HACK are common tags: `// TODO: optimize this`
5. Doxygen comments (`///` or `/** */`) generate documentation

## Common Mistakes
- Nested `/* */` comments cause compile errors
- Commenting out code instead of deleting it (use version control instead)
- Over-commenting obvious code
