# argc and argv basics

> **Level:** 0 — Absolute Beginner  
> **Category:** C00 — C++ Syntax & Program Structure  
> **Topic:** syntax

---

## Problem Statement
Understand command-line arguments passed to `main()` via `argc` and `argv`.

## What You Need to Know
- `argc` (argument count): number of arguments including the program name.
- `argv` (argument vector): array of C-strings containing the arguments.
- `argv[0]` is always the program name.

## Function Signature
```cpp
int main(int argc, char* argv[])
// or equivalently:
int main(int argc, char** argv)
```

## Basic Example
```cpp
#include <iostream>

int main(int argc, char* argv[]) {
    std::cout << "Number of arguments: " << argc << "\n";

    for (int i = 0; i < argc; ++i) {
        std::cout << "argv[" << i << "] = " << argv[i] << "\n";
    }

    return 0;
}
```

```bash
$ ./program hello world 42
Number of arguments: 4
argv[0] = ./program
argv[1] = hello
argv[2] = world
argv[3] = 42
```

## argc/argv Layout in Memory
```
argc = 4

argv: ┌─────────────┐
  [0] │ "./program"  │
  [1] │ "hello"      │
  [2] │ "world"      │
  [3] │ "42"         │
  [4] │ nullptr      │  ← always null-terminated
      └─────────────┘
```

## Arguments Are Always Strings
```cpp
#include <iostream>
#include <cstdlib>   // for atoi
#include <string>

int main(int argc, char* argv[]) {
    if (argc < 2) {
        std::cout << "Usage: " << argv[0] << " <number>\n";
        return 1;
    }

    // Convert string argument to integer
    int num = std::atoi(argv[1]);    // C-style
    // or: int num = std::stoi(argv[1]);  // C++ style (can throw)

    std::cout << "Number: " << num << "\n";
    return 0;
}
```

## Key Takeaways
1. `argc` is always >= 1 (program name counts)
2. `argv[0]` is the program name/path
3. All arguments are strings — convert with `stoi()`, `stod()`, etc.
4. `argv[argc]` is guaranteed to be `nullptr`
5. Check `argc` before accessing `argv[n]` to avoid out-of-bounds

## Common Mistakes
- Accessing `argv[1]` without checking `argc >= 2` → crash
- Forgetting arguments are strings: `argv[1] + argv[2]` does pointer arithmetic, not addition
- Assuming `argv[0]` is just the filename — it might include the full path
