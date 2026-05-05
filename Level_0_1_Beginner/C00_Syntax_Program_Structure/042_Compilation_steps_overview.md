# Compilation steps overview

> **Level:** 0 — Absolute Beginner  
> **Category:** C00 — C++ Syntax & Program Structure  
> **Topic:** syntax

---

## Problem Statement
Understand the four stages of C++ compilation: preprocessing, compilation, assembly, and linking.

## The Four Stages
```
Source Code (.cpp)
      │
      ▼
┌─────────────┐
│ Preprocessor │  (#include, #define, #ifdef)
└──────┬──────┘
       │  Translation Unit (.i)
       ▼
┌──────────────┐
│   Compiler   │  (C++ → Assembly)
└──────┬───────┘
       │  Assembly (.s)
       ▼
┌──────────────┐
│  Assembler   │  (Assembly → Machine Code)
└──────┬───────┘
       │  Object File (.o)
       ▼
┌──────────────┐
│    Linker    │  (Combine .o files + libraries)
└──────┬───────┘
       │
       ▼
  Executable (a.out / program)
```

## Stage 1: Preprocessing
```bash
g++ -E main.cpp -o main.i    # Stop after preprocessing
```
- Expands `#include` (copies header content)
- Replaces `#define` macros
- Processes `#ifdef` / `#endif` conditionally
- Strips comments

## Stage 2: Compilation
```bash
g++ -S main.cpp -o main.s    # Stop after compilation
```
- Converts C++ into assembly language
- Performs syntax checking, type checking
- Generates compiler errors and warnings here

## Stage 3: Assembly
```bash
g++ -c main.cpp -o main.o    # Stop after assembly
```
- Converts assembly to machine code (object file)
- Object file contains binary code but unresolved references

## Stage 4: Linking
```bash
g++ main.o utils.o -o program   # Link object files
```
- Combines object files into final executable
- Resolves function calls across files
- Links standard library functions
- Generates linker errors (undefined reference)

## One-Step Command
```bash
g++ -o program main.cpp utils.cpp   # All 4 stages at once
```

## Key Takeaways
1. Preprocessing → `#include` expansion, macro substitution
2. Compilation → C++ to assembly, catches syntax/type errors
3. Assembly → assembly to machine code (`.o` files)
4. Linking → combines `.o` files, resolves cross-file references
5. Each stage produces specific error types

## Common Mistakes
- Confusing compiler errors (stage 2) with linker errors (stage 4)
- Forgetting to link all `.o` files → "undefined reference" errors
- Not understanding that `#include` literally copies file contents
