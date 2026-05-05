# Command-line arguments printing

> **Level:** 0 — Absolute Beginner  
> **Category:** C00 — C++ Syntax & Program Structure  
> **Topic:** syntax

---

## Problem Statement
Print and process command-line arguments in various useful ways.

## What You Need to Know
- Command-line arguments let users customize program behavior without recompiling.
- Arguments are separated by spaces on the command line.
- Quoted strings count as a single argument.

## Print All Arguments
```cpp
#include <iostream>

int main(int argc, char* argv[]) {
    for (int i = 0; i < argc; ++i) {
        std::cout << "[" << i << "] " << argv[i] << "\n";
    }
    return 0;
}
```

```bash
$ ./program "hello world" 42 --verbose
[0] ./program
[1] hello world
[2] 42
[3] --verbose
```

## Process Arguments with std::string
```cpp
#include <iostream>
#include <string>
#include <vector>

int main(int argc, char* argv[]) {
    // Convert to vector of strings for easier handling
    std::vector<std::string> args(argv, argv + argc);

    for (size_t i = 1; i < args.size(); ++i) {
        std::cout << "Arg " << i << ": " << args[i] << "\n";
    }
    return 0;
}
```

## Simple Flag Detection
```cpp
#include <iostream>
#include <string>

int main(int argc, char* argv[]) {
    bool verbose = false;
    std::string filename;

    for (int i = 1; i < argc; ++i) {
        std::string arg = argv[i];

        if (arg == "--verbose" || arg == "-v") {
            verbose = true;
        } else {
            filename = arg;
        }
    }

    if (verbose) {
        std::cout << "Verbose mode ON\n";
    }
    if (!filename.empty()) {
        std::cout << "File: " << filename << "\n";
    }

    return 0;
}
```

```bash
$ ./program -v myfile.txt
Verbose mode ON
File: myfile.txt
```

## Usage Message
```cpp
#include <iostream>

int main(int argc, char* argv[]) {
    if (argc < 3) {
        std::cerr << "Usage: " << argv[0] << " <input> <output>\n";
        std::cerr << "Example: " << argv[0] << " data.csv result.txt\n";
        return 1;
    }

    std::cout << "Input: " << argv[1] << "\n";
    std::cout << "Output: " << argv[2] << "\n";
    return 0;
}
```

## Key Takeaways
1. Loop through `argv[1]` to `argv[argc-1]` to process user arguments
2. Convert `argv` to `std::vector<std::string>` for easier manipulation
3. Compare with `==` for flag detection (using `std::string`)
4. Always print a usage message when required arguments are missing
5. Return non-zero from `main()` to indicate error

## Common Mistakes
- Comparing C-strings with `==`: `argv[1] == "--help"` compares pointers, not content
  - Fix: convert to `std::string` first, or use `strcmp()`
- Not quoting arguments with spaces: `./program hello world` is 3 args, not 2
- Forgetting to skip `argv[0]` (the program name) when processing user args
