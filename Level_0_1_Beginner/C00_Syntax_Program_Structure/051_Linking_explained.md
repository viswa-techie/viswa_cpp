# Linking explained

> **Level:** 0 — Absolute Beginner  
> **Category:** C00 — C++ Syntax & Program Structure  
> **Topic:** syntax

---

## Problem Statement
Understand what the linker does and how it combines object files into an executable.

## What You Need to Know
- The linker is the final stage of the build process.
- It combines `.o` files and resolves references between them.
- It also links the C++ standard library.

## What the Linker Does
```
1. Takes all .o files as input
2. Resolves symbols: matches function calls to function definitions
3. Combines code and data sections
4. Links standard library functions (cout, string, etc.)
5. Produces the final executable
```

## Symbol Resolution Example
```
main.o contains:
  CALLS add()        ← undefined, needs resolution
  CALLS multiply()   ← undefined, needs resolution
  DEFINES main()     ← defined here

math_utils.o contains:
  DEFINES add()      ← defined here
  DEFINES multiply() ← defined here

Linker: matches CALLS → DEFINES, produces executable
```

## Common Linker Errors
```bash
# Error: undefined reference
$ g++ main.o -o program
# undefined reference to `add(int, int)'
# Fix: include math_utils.o in the link command

$ g++ main.o math_utils.o -o program   # Fixed!
```

```bash
# Error: multiple definition
# If add() is defined in TWO .cpp files:
# multiple definition of `add(int, int)'
# Fix: define the function in only ONE .cpp file
```

## Static vs Dynamic Linking
```bash
# Static linking: copies library code into executable
g++ -static main.o -o program   # Larger binary, no dependencies

# Dynamic linking: references shared libraries (.so/.dll)
g++ main.o -o program           # Default, smaller binary
```

```
Static (.a)          Dynamic (.so / .dll)
-----------          --------------------
Code copied into exe Code loaded at runtime
Larger executable    Smaller executable
No runtime deps      Needs .so/.dll files
Faster startup       Shared across programs
```

## Linking Libraries
```bash
# Link the math library (-lm)
g++ main.o -lm -o program

# Link a custom library
g++ main.o -L./libs -lmylib -o program
# -L: library search path
# -l: library name (libmylib.a or libmylib.so)
```

## Key Takeaways
1. The linker connects function calls to function definitions
2. "Undefined reference" = linker can't find a function definition
3. "Multiple definition" = same function defined in multiple `.o` files
4. Static linking copies code; dynamic linking shares libraries
5. `-l` flag links libraries: `-lm` links `libm`

## Common Mistakes
- Forgetting to link all `.o` files → undefined reference
- Defining functions in headers without `inline` → multiple definition
- Wrong link order: libraries must come after the files that use them
