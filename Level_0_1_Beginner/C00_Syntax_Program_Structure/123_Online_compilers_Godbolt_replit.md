# Online compilers: Godbolt & Replit

> **Level:** 0 — Absolute Beginner  
> **Category:** C00 — C++ Syntax & Program Structure  
> **Topic:** syntax

---

## Problem Statement
Use online compilers to write and run C++ without local setup.

## Popular Online Compilers

### 1. Compiler Explorer (Godbolt) — godbolt.org
```
Purpose:  See assembly output alongside your C++ code
Best for: Understanding what the compiler does, optimization analysis
Features:
  - Side-by-side C++ → assembly view
  - Multiple compilers (GCC, Clang, MSVC)
  - Color-coded source-to-assembly mapping
  - Compiler flags support
  - Share via URL
```

### 2. Wandbox — wandbox.org
```
Purpose:  Run C++ code quickly
Best for: Quick testing, trying different compilers/standards
Features:
  - Multiple C++ standards (C++11 to C++23)
  - GCC and Clang
  - Standard input support
  - Share via URL
```

### 3. Coliru — coliru.stacked-crooked.com
```
Purpose:  Run C++ code with full command-line control
Best for: Testing compilation commands
Features:
  - Custom compiler commands
  - Output display
```

### 4. cpp.sh — cpp.sh
```
Purpose:  Simple C++ playground
Best for: Beginners — minimal interface
Features:
  - Run C++ directly in browser
  - Basic input/output
```

## When to Use What
```
Scenario                    Tool
--------                    ----
Learn what compiler does    Godbolt
Quick code test             Wandbox or cpp.sh
Try different standards     Wandbox
Share code snippet          Any (all have URL sharing)
Serious development         Local IDE (VS Code, CLion)
```

## Godbolt Tips
```
1. Type C++ on the left
2. See assembly on the right
3. Color coding shows which source line → which assembly
4. Add compiler flags: -O2, -std=c++17
5. Add multiple compiler panels to compare GCC vs Clang
```

## Key Takeaways
1. Online compilers need zero setup — great for learning
2. Godbolt shows assembly — invaluable for understanding optimization
3. Wandbox supports multiple compilers and C++ standards
4. Always share code via URL links — no screenshots
5. For real projects, use a local development environment

## Common Mistakes
- Using online compilers for large projects — they have limits
- Not checking which C++ standard is selected
- Forgetting to provide stdin input when program uses cin
