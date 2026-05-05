# clang-format intro

> **Level:** 0 — Absolute Beginner  
> **Category:** C00 — C++ Syntax & Program Structure  
> **Topic:** syntax

---

## Problem Statement
Use `clang-format` to automatically format C++ code consistently.

## What You Need to Know
- `clang-format` automatically reformats source code.
- Handles indentation, spacing, braces, line breaks.
- Ensures consistent style across a team.

## Basic Usage
```bash
# Install
sudo apt install clang-format

# Format a file (prints to stdout)
clang-format main.cpp

# Format in-place (modifies file)
clang-format -i main.cpp

# Format multiple files
clang-format -i *.cpp *.h
```

## Built-in Styles
```bash
# Use a predefined style
clang-format -style=llvm main.cpp        # LLVM style
clang-format -style=google main.cpp      # Google style
clang-format -style=chromium main.cpp    # Chromium style
clang-format -style=mozilla main.cpp     # Mozilla style
clang-format -style=webkit main.cpp      # WebKit style
clang-format -style=microsoft main.cpp   # Microsoft style
```

## Before and After
```cpp
// BEFORE: messy formatting
#include<iostream>
int main(){int x=5;
    if(x>3){std::cout<<"big"<<std::endl;
}else{
        std::cout<<"small"<<std::endl;}
return 0;}

// AFTER: clang-format -style=google
#include <iostream>
int main() {
  int x = 5;
  if (x > 3) {
    std::cout << "big" << std::endl;
  } else {
    std::cout << "small" << std::endl;
  }
  return 0;
}
```

## .clang-format Config File
```yaml
# Save as .clang-format in your project root
BasedOnStyle: Google
IndentWidth: 4
ColumnLimit: 100
AllowShortFunctionsOnASingleLine: Empty
BreakBeforeBraces: Attach
```

```bash
# Uses .clang-format from current or parent directory
clang-format -i main.cpp

# Generate a config from a style
clang-format -style=google -dump-config > .clang-format
```

## VS Code Integration
```
1. Install "C/C++" extension (Microsoft)
2. Settings → "C_Cpp: Clang_format_style" → "file" or "google"
3. Format: Shift+Alt+F (or right-click → Format Document)
4. Enable "Format On Save" in settings
```

## Key Takeaways
1. `clang-format -i file.cpp` formats code in-place
2. Use built-in styles (google, llvm, etc.) or create `.clang-format`
3. Consistent formatting prevents style debates in code reviews
4. Integrate with your editor for format-on-save
5. Add `.clang-format` to your project root for team-wide consistency

## Common Mistakes
- Formatting manually → waste of time when tools exist
- Different team members using different styles → messy diffs
- Not putting `.clang-format` in version control → inconsistent formatting
