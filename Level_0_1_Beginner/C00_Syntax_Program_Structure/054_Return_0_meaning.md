# Return 0 meaning

> **Level:** 0 — Absolute Beginner  
> **Category:** C00 — C++ Syntax & Program Structure  
> **Topic:** syntax

---

## Problem Statement
Understand what `return 0` means in `main()` and why it matters.

## What You Need to Know
- `main()` returns an `int` to the operating system.
- `return 0` means "program completed successfully."
- The OS or calling script can check this value.

## Basic Example
```cpp
#include <iostream>

int main() {
    std::cout << "Hello!\n";
    return 0;   // Tell OS: "Everything went fine"
}
```

## Checking the Return Value
```bash
# Run the program
./program

# Check the exit code (bash)
echo $?    # Prints 0 if successful
```

## In Scripts
```bash
#!/bin/bash
./program
if [ $? -eq 0 ]; then
    echo "Program succeeded!"
else
    echo "Program failed with code $?"
fi
```

## C++11: Implicit return 0
```cpp
#include <iostream>

int main() {
    std::cout << "Hello!\n";
    // In C++11 and later, if you omit return in main(),
    // the compiler automatically returns 0
}
// This is equivalent to return 0; but explicit is preferred
```

## Convention
```
Return Value    Meaning
------------    -------
0               Success
Non-zero        Failure (value indicates error type)
1               General error
2               Misuse of command (convention)
```

## Key Takeaways
1. `return 0` = success, non-zero = error
2. The OS receives this value as the program's exit status
3. Check with `echo $?` in bash or `%errorlevel%` in Windows CMD
4. C++11 implicitly returns 0 from `main()` if omitted
5. Always return 0 for successful programs — it's good practice

## Common Mistakes
- Thinking `return 0` ends the OS — it only ends your program
- Forgetting return type: `void main()` is non-standard (use `int main()`)
- Returning nothing from `main()` in pre-C++11 → undefined behavior
