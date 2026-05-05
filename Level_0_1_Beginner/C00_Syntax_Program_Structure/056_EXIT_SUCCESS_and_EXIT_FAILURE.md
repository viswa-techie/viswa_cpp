# EXIT_SUCCESS and EXIT_FAILURE

> **Level:** 0 — Absolute Beginner  
> **Category:** C00 — C++ Syntax & Program Structure  
> **Topic:** syntax

---

## Problem Statement
Use `EXIT_SUCCESS` and `EXIT_FAILURE` constants for portable exit codes.

## What You Need to Know
- `EXIT_SUCCESS` and `EXIT_FAILURE` are defined in `<cstdlib>`.
- They are portable — guaranteed to work on all platforms.
- `EXIT_SUCCESS` is typically 0, `EXIT_FAILURE` is typically 1.

## Usage
```cpp
#include <iostream>
#include <cstdlib>    // Required for EXIT_SUCCESS, EXIT_FAILURE

int main() {
    int x;
    std::cout << "Enter a positive number: ";
    std::cin >> x;

    if (x <= 0) {
        std::cerr << "Error: not positive\n";
        return EXIT_FAILURE;   // Portable "error" code
    }

    std::cout << "You entered: " << x << "\n";
    return EXIT_SUCCESS;       // Portable "success" code
}
```

## With std::exit()
```cpp
#include <iostream>
#include <cstdlib>

void initialize() {
    bool ok = false;
    // ... initialization logic ...
    if (!ok) {
        std::cerr << "Initialization failed!\n";
        std::exit(EXIT_FAILURE);
    }
}

int main() {
    initialize();
    std::cout << "Running...\n";
    return EXIT_SUCCESS;
}
```

## Comparison
```
Expression        Value (typical)    Portable?
----------        ---------------    ---------
return 0;         0                  Yes (guaranteed)
return 1;         1                  Yes, but meaning varies
EXIT_SUCCESS      0 (usually)        Yes (defined by standard)
EXIT_FAILURE      1 (usually)        Yes (defined by standard)
```

## Key Takeaways
1. `EXIT_SUCCESS` = program succeeded (typically 0)
2. `EXIT_FAILURE` = program failed (typically 1)
3. Both are macros from `<cstdlib>`
4. More readable than raw `return 0` / `return 1`
5. `return 0` in `main()` is also guaranteed to mean success

## Common Mistakes
- Using without `#include <cstdlib>` → undefined
- Assuming `EXIT_FAILURE` is always 1 — standard only guarantees it's non-zero
- Mixing `EXIT_FAILURE` with custom error codes — pick one approach
