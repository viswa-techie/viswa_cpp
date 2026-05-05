# Parameters vs arguments

> **Level:** 0 — Absolute Beginner  
> **Category:** C00 — C++ Syntax & Program Structure  
> **Topic:** syntax

---

## Problem Statement
Understand the difference between parameters (formal) and arguments (actual).

## What You Need to Know
- **Parameter**: the variable in the function declaration — a placeholder.
- **Argument**: the actual value passed when calling the function.
- Parameters are like empty boxes; arguments are what you put in them.

## Visual Explanation
```cpp
//        Parameters (formal parameters)
//        ↓         ↓
int add(int a, int b) {
    return a + b;
}

int main() {
    //     Arguments (actual arguments)
    //     ↓    ↓
    add(3, 4);
    
    int x = 10, y = 20;
    add(x, y);     // x and y are arguments
    add(x+1, y*2); // Expressions can be arguments
    return 0;
}
```

## Terminology
```
Term                 Also Called            Where
----                 ----------            -----
Parameter            Formal parameter       In function definition
Argument             Actual parameter       In function call
```

## Default Parameters
```cpp
#include <iostream>

// Default values in parameters
void greet(const std::string& name, const std::string& greeting = "Hello") {
    std::cout << greeting << ", " << name << "!\n";
}

int main() {
    greet("Viswa");                // Uses default: "Hello, Viswa!"
    greet("Viswa", "Good morning"); // Override: "Good morning, Viswa!"
    return 0;
}
```

## Parameter Passing (by Value)
```cpp
#include <iostream>

void tryToModify(int x) {   // x is a COPY of the argument
    x = 999;
    std::cout << "Inside: " << x << "\n";  // 999
}

int main() {
    int num = 42;
    tryToModify(num);
    std::cout << "Outside: " << num << "\n";  // 42 (unchanged!)
    return 0;
}
```

## Number of Arguments Must Match
```cpp
int add(int a, int b);

add(1);        // ERROR: too few arguments
add(1, 2);     // OK
add(1, 2, 3);  // ERROR: too many arguments
```

## Key Takeaways
1. Parameters are in the definition, arguments are in the call
2. By default, arguments are **copied** to parameters (pass by value)
3. Default parameters must be rightmost: `foo(int a, int b = 5)`
4. Number and types of arguments must match parameters
5. Arguments can be literals, variables, or expressions

## Common Mistakes
- Modifying a parameter expecting the argument to change — pass by value makes a copy
- Default parameters in wrong position: `foo(int a = 0, int b)` → error
- Confusing "parameter" and "argument" in technical discussions
