# Address sanitizer (-fsanitize=address)

> **Level:** 0 — Absolute Beginner  
> **Category:** C00 — C++ Syntax & Program Structure  
> **Topic:** syntax

---

## Problem Statement
Use AddressSanitizer (ASan) to detect memory errors at runtime.

## What You Need to Know
- ASan detects bugs like buffer overflows, use-after-free, memory leaks.
- Just add `-fsanitize=address` when compiling.
- It's a runtime tool — your program runs and ASan reports errors as they happen.

## Basic Usage
```bash
# Compile with ASan
g++ -std=c++17 -g -fsanitize=address main.cpp -o main

# Run — ASan will report any memory errors
./main
```

## What ASan Catches
```cpp
// 1. Buffer overflow
int arr[5];
arr[10] = 42;    // ASan: "heap/stack-buffer-overflow"

// 2. Use after free
int* p = new int(42);
delete p;
*p = 10;          // ASan: "heap-use-after-free"

// 3. Memory leak
int* leaked = new int(42);
// Never deleted → ASan: "detected memory leaks"

// 4. Stack use after return
int* dangling() {
    int x = 42;
    return &x;    // ASan: "stack-use-after-return"
}

// 5. Double free
int* p = new int;
delete p;
delete p;          // ASan: "double-free"
```

## ASan Output Example
```
=================================================================
==12345==ERROR: AddressSanitizer: stack-buffer-overflow on address 0x7fff...
READ of size 4 at 0x7fff... thread T0
    #0 0x400abc in main main.cpp:10
    #1 0x7f... in __libc_start_main

Address 0x7fff... is located in stack of thread T0 at offset 48
  This frame has 1 object(s):
    [32, 52) 'arr' (line 8)    <== Memory access at offset 72 overflows this variable
=================================================================
```

## Compile Flags
```bash
# ASan only
g++ -g -fsanitize=address main.cpp -o main

# ASan + leak detection (default on Linux)
g++ -g -fsanitize=address -fno-omit-frame-pointer main.cpp -o main

# Disable leak detection if not needed
ASAN_OPTIONS=detect_leaks=0 ./main
```

## Key Takeaways
1. `-fsanitize=address` catches memory bugs at runtime
2. Always compile with `-g` for readable error messages
3. Catches: overflows, use-after-free, leaks, double-free
4. ~2x slowdown and ~3x memory overhead — use for testing, not production
5. Fix ALL ASan errors — they indicate real bugs

## Common Mistakes
- Forgetting `-g` flag → ASan output lacks file/line info
- Not running tests with ASan → missing memory bugs
- Ignoring ASan output → bugs will crash in production
