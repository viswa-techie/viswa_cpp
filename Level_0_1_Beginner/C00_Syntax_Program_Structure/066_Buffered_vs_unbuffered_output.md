# Buffered vs unbuffered output

> **Level:** 0 — Absolute Beginner  
> **Category:** C00 — C++ Syntax & Program Structure  
> **Topic:** syntax

---

## Problem Statement
Understand the difference between buffered and unbuffered output streams.

## What You Need to Know
- **Buffered**: Output is collected in memory, written in batches (faster).
- **Unbuffered**: Output is written immediately, one operation at a time (slower but reliable).
- `cout` and `clog` are buffered. `cerr` is unbuffered.

## How Buffering Works
```
Buffered (cout):
  cout << "A"  → Buffer: [A]        (not written yet)
  cout << "B"  → Buffer: [A][B]     (not written yet)
  cout << "C"  → Buffer: [A][B][C]  (not written yet)
  cout << "\n" → Buffer flushed → "ABC\n" appears on screen

Unbuffered (cerr):
  cerr << "A"  → "A" appears immediately
  cerr << "B"  → "B" appears immediately
  cerr << "C"  → "C" appears immediately
```

## When Buffers Flush
```
Event                    cout (buffered)    cerr (unbuffered)
-----                    ---------------    -----------------
Every << operation       No                 Yes
On newline (\n)          Usually (terminal)  N/A (always)
When buffer is full      Yes                N/A
On endl / flush          Yes                N/A
Program ends normally    Yes                N/A
cin is used              Yes (tied)         No
```

## Demonstrating the Difference
```cpp
#include <iostream>

int main() {
    // cout is buffered — may not appear before crash
    std::cout << "Before crash (cout)";

    // cerr is unbuffered — guaranteed to appear
    std::cerr << "Before crash (cerr)";

    // Simulate crash
    int* p = nullptr;
    *p = 42;    // CRASH! Segmentation fault

    // cout message may be lost, cerr message will appear
    return 0;
}
```

## cin/cout Tie
```cpp
#include <iostream>

int main() {
    // cout is "tied" to cin — cout flushes before cin reads
    std::cout << "Enter value: ";    // Auto-flushed because cin is about to read
    int x;
    std::cin >> x;

    // You can untie them for performance:
    std::cin.tie(nullptr);
    // Now cout won't auto-flush before cin reads
    return 0;
}
```

## Comparison Summary
```
Stream       Destination    Buffered    Speed     Reliability
------       -----------    --------    -----     -----------
cout         stdout         Yes         Fast      May lose data on crash
cerr         stderr         No          Slow      Guaranteed output
clog         stderr         Yes         Fast      May lose data on crash
```

## Key Takeaways
1. Buffered I/O is faster — fewer system calls
2. Unbuffered I/O is more reliable — data can't be lost in a buffer
3. `cout` is buffered (fast), `cerr` is unbuffered (reliable)
4. `cout` auto-flushes before `cin` reads (they're tied)
5. Use `cerr` for debug/error messages, `cout` for normal output

## Common Mistakes
- Using `cout` for crash diagnostics → message may be lost
- Untying `cin`/`cout` then expecting prompts to appear before input
- Assuming `\n` always flushes — it only does on terminals (not files)
