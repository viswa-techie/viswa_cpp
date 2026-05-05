# Stepping through code

> **Level:** 0 — Absolute Beginner  
> **Category:** C00 — C++ Syntax & Program Structure  
> **Topic:** syntax

---

## Problem Statement
Learn the different stepping commands to navigate through code in a debugger.

## What You Need to Know
- **Step Over** (`next`): Execute the current line; if it's a function call, run the entire function.
- **Step Into** (`step`): If current line is a function call, enter that function.
- **Step Out** (`finish`): Run until the current function returns.
- **Continue** (`continue`): Run until the next breakpoint.

## Visual Explanation
```cpp
int multiply(int a, int b) {   // ← step INTO goes here
    return a * b;               //   step over this
}                               //   step OUT returns here

int main() {
    int x = 5;                  // ← next (step over)
    int y = multiply(x, 3);    // ← step into → goes inside multiply()
                                //   step over → runs multiply, stays in main
    std::cout << y << "\n";    // ← next
    return 0;
}
```

## GDB Stepping Commands
```
Command      Short    Description
-------      -----    -----------
next         n        Step over (stay in current function)
step         s        Step into (enter function calls)
finish       fin      Step out (run until current function returns)
continue     c        Continue to next breakpoint
until 30     u 30     Run until line 30
nexti        ni       Step one machine instruction (over)
stepi        si       Step one machine instruction (into)
```

## Example Session
```cpp
// program.cpp
#include <iostream>

int square(int n) {
    int result = n * n;    // Line 4
    return result;          // Line 5
}

int main() {
    int a = 5;             // Line 9
    int b = square(a);     // Line 10
    int c = b + 1;         // Line 11
    std::cout << c << "\n"; // Line 12
    return 0;
}
```

```bash
(gdb) break main
(gdb) run
# Stopped at line 9
(gdb) next              # Execute line 9 (int a = 5)
(gdb) step              # Step INTO square() at line 10
# Now inside square(), at line 4
(gdb) print n            # 5
(gdb) next              # Execute line 4 (result = 25)
(gdb) print result       # 25
(gdb) finish            # Run until square() returns
# Back in main at line 11
(gdb) print b            # 25
(gdb) continue          # Run to end
```

## VS Code Equivalents
```
GDB         VS Code        Shortcut
---         -------        --------
next        Step Over      F10
step        Step Into      F11
finish      Step Out       Shift+F11
continue    Continue       F5
```

## Key Takeaways
1. `next` stays in the current function — use to skip function internals
2. `step` enters function calls — use to debug a specific function
3. `finish` returns from the current function — use when you've seen enough
4. `continue` runs to the next breakpoint — use to skip ahead
5. These are the most-used debugging commands — practice them

## Common Mistakes
- Using `step` on standard library functions (`cout`) → entering STL code by accident
- Using `next` when you need to debug inside a function → skips the bug
- Forgetting to set breakpoints before `continue` → program runs to end
