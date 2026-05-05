# Breakpoints concept

> **Level:** 0 — Absolute Beginner  
> **Category:** C00 — C++ Syntax & Program Structure  
> **Topic:** syntax

---

## Problem Statement
Understand breakpoints — the most important debugging concept.

## What You Need to Know
- A breakpoint pauses program execution at a specific line.
- The debugger stops BEFORE executing that line.
- You can then inspect variables, step through code, or continue.

## Setting Breakpoints in GDB
```bash
(gdb) break main              # At function start
(gdb) break 25                # At line 25
(gdb) break file.cpp:25       # At line 25 of specific file
(gdb) break add               # At function add()
```

## Conditional Breakpoints
```bash
# Only stop when condition is true
(gdb) break 15 if i == 100
(gdb) break 15 if x > 0 && y < 10
```

## Managing Breakpoints
```bash
(gdb) info breakpoints         # List all breakpoints
(gdb) delete 2                 # Delete breakpoint #2
(gdb) delete                   # Delete ALL breakpoints
(gdb) disable 1                # Temporarily disable #1
(gdb) enable 1                 # Re-enable #1
```

## Practical Example
```cpp
#include <iostream>

int main() {
    int sum = 0;
    for (int i = 0; i < 1000; ++i) {    // Line 5
        sum += i;                         // Line 6
    }
    std::cout << "Sum: " << sum << "\n"; // Line 8
    return 0;
}
```

```bash
(gdb) break 6 if i == 500    # Stop only when i reaches 500
(gdb) run
# Stopped at line 6 when i == 500
(gdb) print sum               # Sum at iteration 500
(gdb) print i                 # 500
(gdb) continue                # Run to end
```

## VS Code Breakpoints
```
In VS Code (with C/C++ extension):
- Click in the gutter (left of line numbers) to set a breakpoint (red dot)
- Right-click the dot for conditional breakpoints
- F5 to start debugging
- F10 = Step Over, F11 = Step Into, Shift+F11 = Step Out
```

## Key Takeaways
1. Breakpoints pause execution so you can inspect program state
2. Conditional breakpoints save time in loops
3. Breakpoints stop BEFORE the marked line executes
4. Use `info breakpoints` to list, `delete`/`disable` to manage
5. VS Code provides visual breakpoint support with the C++ extension

## Common Mistakes
- Setting breakpoints in optimized code — lines may be reordered/removed
- Too many breakpoints — hard to track, use conditional ones instead
- Breaking in headers — confusing, break in `.cpp` files instead
