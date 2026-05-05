# Escape sequences

> **Level:** 0 — Absolute Beginner  
> **Category:** C00 — C++ Syntax & Program Structure  
> **Topic:** syntax

---

## Problem Statement
Learn all common escape sequences in C++ and when to use each one.

## What You Need to Know
- An escape sequence starts with a backslash `\` followed by a character.
- It represents a special character that can't be typed directly.
- Works in both character literals and string literals.

## Complete Escape Sequence Table
```
Sequence   Meaning                  Example Output
--------   -------                  --------------
\n         Newline                  Moves to next line
\t         Horizontal tab           Inserts a tab
\\         Backslash                Prints \
\"         Double quote             Prints "
\'         Single quote             Prints '
\0         Null character           String terminator
\a         Alert (bell)             System beep
\b         Backspace                Moves cursor back
\r         Carriage return          Moves to line start
\f         Form feed                Page break (printers)
\v         Vertical tab             Vertical spacing
\?         Question mark            Prints ?
\xHH       Hex value                \x41 = 'A'
\ooo       Octal value              \101 = 'A'
```

## Example: Common Escape Sequences
```cpp
#include <iostream>

int main() {
    std::cout << "Line 1\nLine 2\n";            // Newline
    std::cout << "Col1\tCol2\tCol3\n";          // Tab
    std::cout << "Path: C:\\Users\\Viswa\n";    // Backslash
    std::cout << "She said \"Hi\"\n";           // Double quote
    std::cout << "It\'s fine\n";                // Single quote
    return 0;
}
```
**Output:**
```
Line 1
Line 2
Col1Col2Col3
Path: C:\Users\Viswa
She said "Hi"
It's fine
```

## Example: Hex and Octal Escape
```cpp
#include <iostream>

int main() {
    std::cout << "\x48\x65\x6C\x6C\x6F\n";  // "Hello" in hex
    std::cout << "\110\145\154\154\157\n";    // "Hello" in octal
    return 0;
}
```

## Example: Null terminator
```cpp
#include <iostream>
#include <cstring>

int main() {
    char str[] = "Hello\0World";
    std::cout << str << "\n";              // Prints only "Hello"
    std::cout << strlen(str) << "\n";      // 5, not 11
    return 0;
}
```

## Key Takeaways
1. `\n` (newline) and `\t` (tab) are the most commonly used
2. `\\` to print a literal backslash
3. `\"` to include quotes inside strings
4. `\0` is the null terminator — it ends C-strings
5. Hex (`\xHH`) and octal (`\ooo`) can encode any character

## Common Mistakes
- Writing `\` alone in a string → compile error (expects an escape character after it)
- Forgetting `\\` for Windows paths: `"C:\new"` prints C + newline + ew
- Confusing `\n` (newline) with `\0` (null)
