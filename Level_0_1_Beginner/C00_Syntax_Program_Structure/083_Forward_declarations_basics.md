# Forward declarations basics

> **Level:** 0 — Absolute Beginner  
> **Category:** C00 — C++ Syntax & Program Structure  
> **Topic:** syntax

---

## Problem Statement
Use forward declarations to tell the compiler about a function or class before its full definition.

## What You Need to Know
- C++ requires a declaration before use — the compiler reads top to bottom.
- A **forward declaration** tells the compiler "this exists" without providing the body.
- Function prototypes are the most common form of forward declaration.

## The Problem Without Forward Declarations
```cpp
#include <iostream>

int main() {
    greet();   // ERROR: 'greet' was not declared in this scope
    return 0;
}

void greet() {
    std::cout << "Hello!\n";
}
```

## The Fix: Forward Declaration
```cpp
#include <iostream>

// Forward declaration (prototype)
void greet();    // Tells compiler: greet exists, takes no args, returns void

int main() {
    greet();   // OK — compiler knows about greet()
    return 0;
}

// Full definition (can come later)
void greet() {
    std::cout << "Hello!\n";
}
```

## Forward Declaration for Classes
```cpp
// Forward declare a class — only says "this class exists"
class Player;

// Can use Player* and Player& but NOT Player objects
void processPlayer(Player& p);   // OK — reference

class Player {
public:
    std::string name;
    int score;
};

void processPlayer(Player& p) {
    std::cout << p.name << ": " << p.score << "\n";
}
```

## When Forward Declarations Are Needed
```cpp
// Mutual references — A uses B and B uses A
class B;   // Forward declaration

class A {
    B* partner;    // OK — pointer to forward-declared class
};

class B {
    A* partner;    // OK — A is already fully defined
};
```

## What You CAN and CAN'T Do
```
With forward declaration ONLY:    With full definition:
------------------------------    ---------------------
Declare pointer/reference         Create objects
Use in function parameter list    Access members
sizeof is NOT available           sizeof works
```

## Key Takeaways
1. Forward declarations let you use names before their full definition
2. Function prototypes are forward declarations: `void foo(int x);`
3. Class forward declarations: `class Foo;` — only allows pointers/references
4. Headers contain forward declarations; `.cpp` files contain definitions
5. Required for mutual/circular dependencies

## Common Mistakes
- Trying to create an object of a forward-declared class → incomplete type error
- Accessing members of a forward-declared class → incomplete type error
- Prototype doesn't match definition → linker error or compile error
