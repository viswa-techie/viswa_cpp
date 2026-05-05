# Code formatting standards

> **Level:** 0 — Absolute Beginner  
> **Category:** C00 — C++ Syntax & Program Structure  
> **Topic:** syntax

---

## Problem Statement
Understand common C++ code formatting conventions and why consistency matters.

## What You Need to Know
- Formatting doesn't affect compilation but hugely affects readability.
- Teams agree on a style guide and enforce it with tools.
- Popular styles: Google C++ Style, LLVM, Mozilla, WebKit.

## Common Formatting Rules

### Indentation
```cpp
// Use 4 spaces (or 2 spaces) — be consistent, never mix tabs and spaces
if (x > 0) {
    std::cout << "Positive\n";   // 4-space indent
}
```

### Brace placement
```cpp
// Style 1: K&R / "Egyptian" braces (most common in C++)
if (x > 0) {
    doSomething();
}

// Style 2: Allman braces (each brace on its own line)
if (x > 0)
{
    doSomething();
}
```

### Line length
```
Keep lines under 80-120 characters.
Break long lines at logical points:

std::cout << "Name: " << firstName
          << " " << lastName
          << ", Age: " << age << "\n";
```

### Naming conventions
```cpp
int myVariable;       // camelCase (Google style)
int my_variable;      // snake_case (STL style)
const int MAX_SIZE;   // UPPER_CASE for constants
class MyClass {};     // PascalCase for types/classes
void doSomething();   // camelCase or snake_case for functions
```

### Spacing around operators
```cpp
int x = 10;           // ✓ spaces around =
int y = x + 5;        // ✓ spaces around +
int z = x*y + 3;      // ✗ inconsistent spacing
if (x == 10) {}       // ✓ spaces around ==
```

## Key Takeaways
1. Pick one style and stick with it across the entire project
2. Use automated formatters: `clang-format`, IDE auto-format
3. Indentation: 2 or 4 spaces, never tabs (or configure tabs = spaces)
4. Braces: K&R or Allman — either is fine if consistent
5. Naming: match your team/project convention

## Common Mistakes
- Mixing tabs and spaces → alignment breaks on different editors
- Inconsistent brace style within the same file
- Very long lines with no breaks → hard to read, hard to review
