# Build systems intro — Makefile basics

> **Level:** 0 — Absolute Beginner  
> **Category:** C00 — C++ Syntax & Program Structure  
> **Topic:** syntax

---

## Problem Statement
Understand build systems and write a basic Makefile to compile C++ projects.

## What You Need to Know
- Typing `g++ file1.cpp file2.cpp ...` gets tedious for large projects.
- A **Makefile** automates compilation — just type `make`.
- `make` only recompiles files that changed (incremental builds).

## Simplest Makefile
```makefile
# Makefile — save as "Makefile" (no extension)

program: main.cpp
g++ -o program main.cpp
```

**IMPORTANT**: Makefile indentation must use TABS, not spaces.

```bash
$ make           # Compiles main.cpp → program
$ ./program      # Run it
```

## Multi-File Makefile
```makefile
CXX = g++
CXXFLAGS = -std=c++17 -Wall -Wextra

program: main.o utils.o math.o
$(CXX) $(CXXFLAGS) -o program main.o utils.o math.o

main.o: main.cpp utils.h math.h
$(CXX) $(CXXFLAGS) -c main.cpp

utils.o: utils.cpp utils.h
$(CXX) $(CXXFLAGS) -c utils.cpp

math.o: math.cpp math.h
$(CXX) $(CXXFLAGS) -c math.cpp

clean:
rm -f *.o program
```

```bash
$ make           # Build all
$ make clean     # Remove build artifacts
```

## How Makefile Works
```
target: dependencies
command (TAB-indented)

1. make checks if "target" is older than "dependencies"
2. If yes (or target doesn't exist), runs the command
3. Only recompiles what changed — saves time
```

## Modern Build Systems
```
Tool           Description                   Complexity
----           -----------                   ----------
Makefile       Manual, low-level             Simple projects
CMake          Generate Makefiles/projects   Medium-large projects
Meson          Modern, fast                  Medium-large
Bazel          Google's build system         Very large projects
```

## Minimal CMakeLists.txt
```cmake
cmake_minimum_required(VERSION 3.10)
project(MyProject)
set(CMAKE_CXX_STANDARD 17)
add_executable(program main.cpp utils.cpp math.cpp)
```

```bash
mkdir build && cd build
cmake ..
make
```

## Key Takeaways
1. Makefiles automate `g++` commands — type `make` instead of long commands
2. Rules: `target: dependencies` → TAB-indented command
3. `make` only rebuilds what changed — fast incremental builds
4. CMake is the industry standard for larger C++ projects
5. Variables (`CXX`, `CXXFLAGS`) keep Makefiles maintainable

## Common Mistakes
- Using spaces instead of tabs → "missing separator" error
- Forgetting dependencies → changes don't trigger recompilation
- Not using `-Wall -Wextra` → missing important warnings
