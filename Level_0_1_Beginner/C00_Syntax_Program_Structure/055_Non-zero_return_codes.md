# Non-zero return codes

> **Level:** 0 — Absolute Beginner  
> **Category:** C00 — C++ Syntax & Program Structure  
> **Topic:** syntax

---

## Problem Statement
Use non-zero return codes to indicate different error conditions.

## What You Need to Know
- Non-zero return from `main()` tells the OS that something went wrong.
- Different values can indicate different errors.
- Return codes are used extensively in scripts and CI/CD pipelines.

## Basic Error Reporting
```cpp
#include <iostream>
#include <fstream>

int main(int argc, char* argv[]) {
    if (argc < 2) {
        std::cerr << "Error: No filename provided\n";
        return 1;   // Error code 1: missing argument
    }

    std::ifstream file(argv[1]);
    if (!file.is_open()) {
        std::cerr << "Error: Cannot open " << argv[1] << "\n";
        return 2;   // Error code 2: file not found
    }

    // Process file...
    std::cout << "File processed successfully\n";
    return 0;       // Success
}
```

## Checking in Shell
```bash
./program
echo "Exit code: $?"    # 1 (missing argument)

./program nonexistent.txt
echo "Exit code: $?"    # 2 (file not found)

./program existing.txt
echo "Exit code: $?"    # 0 (success)
```

## Using in Shell Scripts
```bash
#!/bin/bash
./program input.txt
case $? in
    0) echo "Success" ;;
    1) echo "Missing argument" ;;
    2) echo "File not found" ;;
    *) echo "Unknown error" ;;
esac
```

## Common Convention
```
Code    Meaning (convention, not enforced)
----    -------
0       Success
1       General error
2       Invalid usage / bad arguments
126     Command not executable
127     Command not found
128+N   Killed by signal N
```

## Using exit()
```cpp
#include <iostream>
#include <cstdlib>   // for exit()

void processData() {
    // If something goes wrong deep in the code:
    std::cerr << "Fatal error in processData\n";
    std::exit(1);    // Exit immediately with code 1
}

int main() {
    processData();
    return 0;   // Never reached if exit() is called
}
```

## Key Takeaways
1. Return 0 for success, 1-255 for different errors
2. Document what each return code means
3. Use `std::exit(code)` to exit from any function (not just `main`)
4. Shell scripts use `$?` to check the last program's exit code
5. CI/CD systems treat non-zero as failure

## Common Mistakes
- Using only 0 and 1 — different errors deserve different codes
- Not documenting what each code means
- Using very large return codes — only 0-255 are portable (8-bit)
