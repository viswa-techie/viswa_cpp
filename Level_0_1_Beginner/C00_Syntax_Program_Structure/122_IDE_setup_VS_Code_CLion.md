# IDE setup: VS Code & CLion

> **Level:** 0 — Absolute Beginner  
> **Category:** C00 — C++ Syntax & Program Structure  
> **Topic:** syntax

---

## Problem Statement
Set up a C++ development environment in VS Code or CLion.

## VS Code Setup

### Required Extensions
```
1. C/C++ (Microsoft)           — IntelliSense, debugging, formatting
2. C/C++ Extension Pack         — Additional tools
3. CMake Tools (optional)       — CMake integration
```

### Install Compiler (Linux)
```bash
# Ubuntu/Debian
sudo apt update
sudo apt install g++ gdb make

# Verify
g++ --version
gdb --version
```

### Minimal tasks.json (Build)
```json
{
    "version": "2.0.0",
    "tasks": [{
        "label": "build",
        "type": "shell",
        "command": "g++",
        "args": ["-std=c++17", "-Wall", "-g", "${file}", "-o", "${fileDirname}/${fileBasenameNoExtension}"],
        "group": {"kind": "build", "isDefault": true}
    }]
}
```

### Minimal launch.json (Debug)
```json
{
    "version": "0.2.0",
    "configurations": [{
        "name": "Debug",
        "type": "cppdbg",
        "request": "launch",
        "program": "${fileDirname}/${fileBasenameNoExtension}",
        "args": [],
        "cwd": "${workspaceFolder}",
        "preLaunchTask": "build",
        "MIMode": "gdb"
    }]
}
```

## CLion Setup

### Key Features
```
- CMake-based project system (built-in)
- Advanced refactoring
- Integrated debugger (GDB/LLDB)
- Memory view, profiler
- Code analysis
```

### Minimal CMakeLists.txt for CLion
```cmake
cmake_minimum_required(VERSION 3.10)
project(MyProject)
set(CMAKE_CXX_STANDARD 17)
add_executable(main main.cpp)
```

## Quick Start: Command Line Only
```bash
# No IDE needed — just terminal
# Write code
nano main.cpp

# Compile
g++ -std=c++17 -Wall -g main.cpp -o main

# Run
./main

# Debug
gdb ./main
```

## Key Takeaways
1. VS Code: free, lightweight, needs extensions for C++
2. CLion: paid (free for students), full-featured C++ IDE
3. Both need a compiler installed separately (g++, clang++)
4. `-g` flag enables debugging symbols
5. Command line works perfectly for learning — IDE is optional

## Common Mistakes
- Forgetting to install g++/gdb before setting up IDE
- Not using `-g` flag → can't debug
- VS Code: forgetting to save tasks.json/launch.json in `.vscode/` folder
