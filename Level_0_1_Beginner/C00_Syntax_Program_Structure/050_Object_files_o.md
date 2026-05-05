# Object files (.o)

> **Level:** 0 — Absolute Beginner  
> **Category:** C00 — C++ Syntax & Program Structure  
> **Topic:** syntax

---

## Problem Statement
Understand what object files are and their role in the C++ build process.

## What You Need to Know
- An object file (`.o` on Linux/Mac, `.obj` on Windows) contains compiled machine code.
- It's the output of the compiler, before linking.
- Object files have unresolved references — the linker resolves them.

## Creating Object Files
```bash
# -c flag: compile only, don't link
g++ -c main.cpp          # Produces main.o
g++ -c math_utils.cpp    # Produces math_utils.o

# Now link them
g++ main.o math_utils.o -o program
```

## What's Inside an Object File?
```bash
# View symbols in an object file
nm math_utils.o
```
```
Output (simplified):
T add            # T = defined text (code) symbol
T multiply       # T = defined text (code) symbol
U cout           # U = undefined (needs to be resolved by linker)
```

## The Build Process with Object Files
```
main.cpp ──────→ main.o ──────┐
                               ├──→ Linker ──→ program (executable)
math_utils.cpp → math_utils.o ┘
                               ↑
                          Standard Library (libstdc++)
```

## Why Object Files Matter
```
Benefit              Explanation
-------              -----------
Incremental builds   Only recompile changed .cpp files
Faster builds        Don't recompile unchanged code
Library creation     Bundle .o files into .a (static lib)
Separate compilation Each .cpp is independent
```

## Practical Example
```bash
# First build: compile everything
g++ -c main.cpp -o main.o              # 2 seconds
g++ -c math_utils.cpp -o math_utils.o  # 2 seconds
g++ main.o math_utils.o -o program     # 1 second

# Change only main.cpp:
g++ -c main.cpp -o main.o              # Recompile only this (2 sec)
g++ main.o math_utils.o -o program     # Re-link (1 sec)
# Saved 2 seconds by not recompiling math_utils.cpp!
```

## Inspecting Object Files
```bash
# List symbols
nm main.o

# View section sizes
size main.o

# Disassemble
objdump -d main.o
```

## Key Takeaways
1. `g++ -c file.cpp` creates `file.o` (compile without linking)
2. Object files contain machine code with unresolved references
3. The linker combines `.o` files into the final executable
4. Incremental builds only recompile changed source files
5. `nm` shows symbols, `objdump -d` shows disassembly

## Common Mistakes
- Trying to run an object file — `.o` files are not executables
- Forgetting to re-link after recompiling → running stale executable
- Not recompiling files that depend on changed headers
