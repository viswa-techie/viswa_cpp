# cerr for error output

> **Level:** 0 — Absolute Beginner  
> **Category:** C00 — C++ Syntax & Program Structure  
> **Topic:** syntax

---

## Problem Statement
Use `std::cerr` to write error messages to the standard error stream.

## What You Need to Know
- `std::cerr` writes to **stderr** (file descriptor 2).
- `std::cout` writes to **stdout** (file descriptor 1).
- `cerr` is **unbuffered** — output appears immediately.
- Separating errors from normal output enables clean pipelines.

## Basic Usage
```cpp
#include <iostream>
#include <fstream>

int main(int argc, char* argv[]) {
    if (argc < 2) {
        std::cerr << "Error: Missing filename argument\n";
        return 1;
    }

    std::ifstream file(argv[1]);
    if (!file.is_open()) {
        std::cerr << "Error: Cannot open '" << argv[1] << "'\n";
        return 2;
    }

    // Normal output to stdout
    std::string line;
    while (std::getline(file, line)) {
        std::cout << line << "\n";
    }

    return 0;
}
```

## Redirecting stderr
```bash
# Normal run — both go to terminal
./program input.txt

# Redirect stdout only
./program input.txt > output.txt    # errors still show on screen

# Redirect stderr only
./program input.txt 2> errors.txt   # output shows on screen

# Redirect both separately
./program input.txt > output.txt 2> errors.txt

# Redirect both to same file
./program input.txt > all.txt 2>&1
```

## cout vs cerr
```
Feature        std::cout          std::cerr
-------        ---------          ---------
Stream         stdout (fd 1)      stderr (fd 2)
Buffering      Buffered           Unbuffered
Purpose        Program output     Error messages
Flushing       On \n or flush     Every << operation
Performance    Faster             Slower (flushes always)
```

## Key Takeaways
1. Use `cerr` for error messages, `cout` for normal output
2. `cerr` is unbuffered — output appears even if program crashes
3. Users can redirect `stdout` and `stderr` independently
4. `cerr` goes to fd 2, `cout` goes to fd 1
5. Use `cerr` for diagnostics so they don't pollute piped output

## Common Mistakes
- Using `cout` for errors → error messages get piped to next program
- Forgetting that `cerr` is slower due to unbuffered I/O
- Not using `cerr` for crash-related diagnostics → message lost in buffer
