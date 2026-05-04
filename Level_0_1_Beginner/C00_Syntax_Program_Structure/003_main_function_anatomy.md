# main() function anatomy

> **Level:** 0 — Absolute Beginner  
> **Category:** C00 — C++ Syntax & Program Structure  
> **Topic:** syntax

---

## Problem Statement
Understand the structure and purpose of the `main()` function in C++.

## What You Need to Know
- `main()` is the **entry point** of every C++ program.
- It must return `int` (the return value goes to the operating system).
- `return 0;` means "program succeeded."
- Non-zero return means "program failed" (the value indicates the error type).
- `argc` and `argv` allow command-line arguments.

## Mental Model
`main()` is like the front door of your program. The OS knocks on this door to start your program. When your program is done, it passes a number back through the door (0 = "all good", non-zero = "something went wrong").

## Forms of main()

### Form 1: Simplest
```cpp
int main() {
    return 0;
}
```

### Form 2: With command-line arguments
```cpp
int main(int argc, char* argv[]) {
    // argc = argument count (including program name)
    // argv = array of C-strings (arguments)
    return 0;
}
```

### Form 3: Modern alternative argv
```cpp
int main(int argc, char** argv) {
    // char** argv is equivalent to char* argv[]
    return 0;
}
```

## Detailed Example
```cpp
#include <iostream>

int main(int argc, char* argv[]) {
    std::cout << "Program name: " << argv[0] << "\n";
    std::cout << "Number of arguments: " << argc << "\n";

    for (int i = 1; i < argc; ++i) {
        std::cout << "Arg " << i << ": " << argv[i] << "\n";
    }

    return 0;  // EXIT_SUCCESS
}
```
Run: `./program hello world` → prints 3 arguments.

## Return Values
```cpp
#include <cstdlib>  // for EXIT_SUCCESS, EXIT_FAILURE

int main() {
    if (/* some error */) {
        return EXIT_FAILURE;  // typically 1
    }
    return EXIT_SUCCESS;      // typically 0
}
```

## Key Takeaways
1. `main()` is called by the C++ runtime (which is called by the OS)
2. Return type MUST be `int` (C++ standard requirement)
3. If you omit `return 0;`, the compiler implicitly adds it (C++11+)
4. `void main()` is NOT standard C++ (some compilers accept it, but don't use it)
5. Global objects are constructed BEFORE `main()` and destroyed AFTER `main()` returns

## Common Mistakes
- `void main()` — non-standard, don't use
- Forgetting `return 0;` in older C++ (C++11 auto-adds it, but be explicit)
- Confusing `argc` count (it includes the program name itself)

## What Happens Before main()?
1. OS loads the program into memory
2. C++ runtime initializes global/static objects
3. `main()` is called
4. After `main()` returns, destructors for globals run
5. `atexit()` handlers execute
6. OS gets the return code
