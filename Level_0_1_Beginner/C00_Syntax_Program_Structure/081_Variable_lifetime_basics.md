# Variable lifetime basics

> **Level:** 0 — Absolute Beginner  
> **Category:** C00 — C++ Syntax & Program Structure  
> **Topic:** syntax

---

## Problem Statement
Understand variable lifetime — when a variable is created and destroyed in C++.

## What You Need to Know
- **Lifetime** = the period during which a variable exists in memory.
- **Scope** = where in the code a variable can be accessed by name.
- A variable can be "alive" but out of scope (e.g., outer variable during inner scope).

## Storage Duration Types
```
Duration         Created              Destroyed            Examples
--------         -------              ---------            --------
Automatic        Entering scope       Leaving scope        Local variables
Static           Program start        Program end          Globals, static locals
Dynamic          new expression       delete expression    Heap allocations
Thread           Thread start         Thread end           thread_local vars
```

## Automatic Lifetime
```cpp
#include <iostream>

int main() {
    // x created here
    int x = 10;
    {
        // y created here
        int y = 20;
        std::cout << x + y << "\n";
    }
    // y destroyed here

    // x is still alive
    std::cout << x << "\n";
    return 0;
}
// x destroyed here
```

## Static Lifetime
```cpp
#include <iostream>

void counter() {
    static int n = 0;   // Created once (first call), destroyed at program end
    ++n;
    std::cout << "Call #" << n << "\n";
}

int main() {
    counter();   // Call #1
    counter();   // Call #2
    counter();   // Call #3
    return 0;
}
// static n destroyed here (program end)
```

## Destructor Timing
```cpp
#include <iostream>
#include <string>

struct Widget {
    std::string name;
    Widget(const std::string& n) : name(n) {
        std::cout << name << " created\n";
    }
    ~Widget() {
        std::cout << name << " destroyed\n";
    }
};

int main() {
    Widget a("A");
    {
        Widget b("B");
        Widget c("C");
    }   // C destroyed, then B (reverse order!)
    Widget d("D");
    return 0;
}   // D destroyed, then A (reverse order!)
```
**Output:**
```
A created
B created
C created
C destroyed
B destroyed
D created
D destroyed
A destroyed
```

## Key Takeaways
1. Local variables: lifetime = scope (entering `{` to leaving `}`)
2. Static variables: lifetime = entire program
3. Destruction happens in reverse order of construction
4. Lifetime ≠ scope: a variable can exist but be inaccessible (shadowed)
5. Understanding lifetime prevents dangling references and use-after-destroy bugs

## Common Mistakes
- Returning a reference to a local variable → dangling reference (destroyed)
- Assuming static local variables are recreated each call
- Not understanding reverse destruction order → resource cleanup issues
