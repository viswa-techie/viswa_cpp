# Debugger basics (gdb intro)

> **Level:** 0 — Absolute Beginner  
> **Category:** C00 — C++ Syntax & Program Structure  
> **Topic:** syntax

---

## Problem Statement
Learn the basics of using GDB (GNU Debugger) to debug C++ programs.

## What You Need to Know
- A debugger lets you run your program step by step and inspect variables.
- GDB is the standard debugger for C/C++ on Linux.
- You must compile with `-g` flag to include debug information.

## Compile for Debugging
```bash
g++ -g -o program main.cpp     # -g adds debug symbols
# Also useful:
g++ -g -O0 -o program main.cpp  # -O0 disables optimization for clearer debugging
```

## Basic GDB Commands
```
Command          Short    Action
-------          -----    ------
run              r        Start the program
break main       b main   Set breakpoint at main()
break 15         b 15     Set breakpoint at line 15
next             n        Execute next line (step over)
step             s        Step into function call
continue         c        Continue to next breakpoint
print x          p x      Print value of variable x
backtrace        bt       Show call stack
quit             q        Exit GDB
list             l        Show source code around current line
info locals               Show all local variables
watch x                   Break when x changes
```

## Example Session
```cpp
// example.cpp
#include <iostream>

int add(int a, int b) {
    return a + b;    // Line 4
}

int main() {
    int x = 10;     // Line 8
    int y = 20;     // Line 9
    int sum = add(x, y);  // Line 10
    std::cout << sum << "\n";
    return 0;
}
```

```bash
$ g++ -g -o example example.cpp
$ gdb ./example

(gdb) break main        # Set breakpoint at main
(gdb) run               # Start program
# Stopped at main
(gdb) next              # Execute: int x = 10
(gdb) next              # Execute: int y = 20
(gdb) print x           # $1 = 10
(gdb) print y           # $2 = 20
(gdb) step              # Step INTO add() function
(gdb) print a           # $3 = 10
(gdb) print b           # $4 = 20
(gdb) continue          # Run to end
(gdb) quit              # Exit GDB
```

## GDB with Arguments
```bash
gdb --args ./program arg1 arg2
# or inside GDB:
(gdb) run arg1 arg2
```

## Key Takeaways
1. Always compile with `-g` for debugging
2. `break` sets a breakpoint, `run` starts the program
3. `next` steps over, `step` steps into functions
4. `print` shows variable values at the current point
5. `backtrace` shows the call stack when you crash

## Common Mistakes
- Compiling without `-g` → GDB shows assembly instead of source
- Compiling with `-O2` → optimizer rearranges code, confusing stepping
- Not using `run` after starting GDB → program never executes
