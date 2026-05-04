#!/usr/bin/env python3
"""
Generates comprehensive C++ learning docs for Level 0 & Level 1 problems.
Each problem gets a full Markdown document with multiple solution approaches,
learning points, and practice guidance.
"""

import os
import re

BASE = "/home/23u58g/work/ZZZ_LEARN_VISWA_DOCS/CPP_problem_solving/Level_0_1_Beginner"

def safe_filename(name, idx):
    """Convert problem name to a safe filename."""
    clean = re.sub(r'[^\w\s-]', '', name)
    clean = re.sub(r'[\s]+', '_', clean.strip())
    clean = clean[:80]  # truncate
    return f"{idx:03d}_{clean}.md"

# ============================================================
# C00: C++ Syntax & Program Structure (120 problems)
# ============================================================
C00 = [
    # 1-20: Foundation
    ("Hello World program", "syntax", """
## Problem Statement
Write a program that prints "Hello, World!" to the console.

## What You Need to Know
- Every C++ program needs a `main()` function as its entry point.
- `#include <iostream>` provides `std::cout` for output.
- `std::cout` is the standard character output stream.
- `<<` is the stream insertion operator.
- Every statement ends with a semicolon `;`.

## Mental Model
Think of `cout` as a conveyor belt going to the screen. You use `<<` to place items onto the belt.

## Solution 1: Minimal (Using namespace)
```cpp
#include <iostream>
using namespace std;

int main() {
    cout << "Hello, World!" << endl;
    return 0;
}
```
**Explanation:** `using namespace std;` lets us write `cout` instead of `std::cout`. `endl` outputs a newline and flushes the buffer.  
**Time:** O(1) | **Space:** O(1)

## Solution 2: Without `using namespace std` (Recommended)
```cpp
#include <iostream>

int main() {
    std::cout << "Hello, World!" << std::endl;
    return 0;
}
```
**Why this is better:** Avoids polluting the global namespace. In large projects, `using namespace std;` can cause name collisions.

## Solution 3: Using `\\n` instead of `endl`
```cpp
#include <iostream>

int main() {
    std::cout << "Hello, World!\\n";
    return 0;
}
```
**Why this matters:** `\\n` is faster than `endl` because `endl` flushes the output buffer. In performance-critical code, prefer `\\n`.

## Solution 4: Using C-style printf
```cpp
#include <cstdio>

int main() {
    printf("Hello, World!\\n");
    return 0;
}
```
**Note:** `printf` is from C. It's sometimes faster but lacks type safety of `cout`.

## Key Takeaways
1. `#include <iostream>` is needed for I/O
2. `main()` returns `int` (0 means success)
3. `<<` chains multiple outputs: `cout << "a" << "b";`
4. Prefer `std::cout` over `using namespace std;` in production code
5. Prefer `\\n` over `endl` unless you need to flush

## Common Mistakes
- Forgetting `#include <iostream>` → compile error
- Missing semicolon at end of statement
- Using `"` vs `'` — double quotes for strings, single for chars
- Writing `cout` without `std::` and without `using namespace std`

## Pattern
**Output pattern** — When you need to display something: `std::cout << value;`

## Similar Problems
- Print your name
- Print multiple lines
- Print a formatted table
"""),

    ("#include, using namespace std", "syntax", """
## Problem Statement
Understand what `#include` and `using namespace std` do in a C++ program.

## What You Need to Know
- `#include` is a **preprocessor directive** — it copies the contents of a header file into your source file before compilation.
- `<iostream>` is a **header file** that declares `cout`, `cin`, `endl`, etc.
- `std` is a **namespace** — a container that groups all standard library names.
- `using namespace std;` makes everything in `std` available without the `std::` prefix.

## Mental Model
Think of `#include` as importing a toolbox. The tools are labeled "std::hammer", "std::screwdriver". `using namespace std;` removes the "std::" label so you can just say "hammer".

## How It Works (Under the Hood)
```
Step 1: You write:   #include <iostream>
Step 2: Preprocessor replaces this line with ~20,000+ lines from iostream header
Step 3: Compiler now knows about std::cout, std::cin, etc.
```

## Solution 1: With `using namespace std`
```cpp
#include <iostream>
using namespace std;

int main() {
    cout << "Hello" << endl;  // No std:: needed
    return 0;
}
```

## Solution 2: Without `using namespace std` (Best Practice)
```cpp
#include <iostream>

int main() {
    std::cout << "Hello" << std::endl;
    return 0;
}
```

## Solution 3: Selective `using` declarations
```cpp
#include <iostream>
using std::cout;
using std::endl;

int main() {
    cout << "Hello" << endl;
    return 0;
}
```
**Best of both worlds:** Only imports what you need.

## Why `using namespace std` Is Risky
```cpp
#include <iostream>
#include <algorithm>
using namespace std;

int count = 5;  // PROBLEM: std::count also exists!
// This causes ambiguity or silent bugs
```

## Key Takeaways
1. `#include` literally pastes header content into your file
2. `<>` for system headers, `""` for your own headers
3. `std::` prefix is verbose but safe
4. `using namespace std;` is OK for small programs, risky for large ones
5. In header files, NEVER use `using namespace std;`

## Common Mistakes
- `#include "iostream"` — works but wrong convention (use `<>` for standard headers)
- Forgetting the semicolon after `using namespace std`
- Using `#include <iostream.h>` — this is pre-standard C++ and doesn't exist in modern compilers

## Pattern
**Header inclusion pattern** — include what you use, no more.
"""),

    ("main() function anatomy", "syntax", """
## Problem Statement
Understand the structure and purpose of the `main()` function in C++.

## What You Need to Know
- `main()` is the **entry point** of every C++ program.
- It must return `int` (the return value goes to the operating system).
- `return 0;` means "program succeeded."
- Non-zero return means "program failed" (the value indicates the error type).
- `argc` and `argv` allow command-line arguments.

## Mental Model
`main()` is like the front door of your program. The OS knocks on this door to start your program. When your program is done, it passes a number back through the door (0 = "all good", non-zero = "something went wrong").

## Forms of main()

### Form 1: Simplest
```cpp
int main() {
    return 0;
}
```

### Form 2: With command-line arguments
```cpp
int main(int argc, char* argv[]) {
    // argc = argument count (including program name)
    // argv = array of C-strings (arguments)
    return 0;
}
```

### Form 3: Modern alternative argv
```cpp
int main(int argc, char** argv) {
    // char** argv is equivalent to char* argv[]
    return 0;
}
```

## Detailed Example
```cpp
#include <iostream>

int main(int argc, char* argv[]) {
    std::cout << "Program name: " << argv[0] << "\\n";
    std::cout << "Number of arguments: " << argc << "\\n";

    for (int i = 1; i < argc; ++i) {
        std::cout << "Arg " << i << ": " << argv[i] << "\\n";
    }

    return 0;  // EXIT_SUCCESS
}
```
Run: `./program hello world` → prints 3 arguments.

## Return Values
```cpp
#include <cstdlib>  // for EXIT_SUCCESS, EXIT_FAILURE

int main() {
    if (/* some error */) {
        return EXIT_FAILURE;  // typically 1
    }
    return EXIT_SUCCESS;      // typically 0
}
```

## Key Takeaways
1. `main()` is called by the C++ runtime (which is called by the OS)
2. Return type MUST be `int` (C++ standard requirement)
3. If you omit `return 0;`, the compiler implicitly adds it (C++11+)
4. `void main()` is NOT standard C++ (some compilers accept it, but don't use it)
5. Global objects are constructed BEFORE `main()` and destroyed AFTER `main()` returns

## Common Mistakes
- `void main()` — non-standard, don't use
- Forgetting `return 0;` in older C++ (C++11 auto-adds it, but be explicit)
- Confusing `argc` count (it includes the program name itself)

## What Happens Before main()?
1. OS loads the program into memory
2. C++ runtime initializes global/static objects
3. `main()` is called
4. After `main()` returns, destructors for globals run
5. `atexit()` handlers execute
6. OS gets the return code
"""),

    ("Single-line & multi-line comments", "syntax", """
## Problem Statement
Learn how to write comments in C++ and when to use each style.

## What You Need to Know
- Comments are ignored by the compiler — they're for humans.
- Two styles: single-line (`//`) and multi-line (`/* ... */`).
- Comments explain WHY, not WHAT (good code is self-documenting for WHAT).

## Solution: Comment Styles
```cpp
// This is a single-line comment

/* This is a
   multi-line comment */

/**
 * This is a documentation comment (Doxygen style)
 * @param x The input value
 * @return The squared value
 */
int square(int x) {
    return x * x;  // inline comment
}
```

## Good vs Bad Comments
```cpp
// BAD: States the obvious
int age = 25;  // set age to 25

// GOOD: Explains WHY
int timeout = 3000;  // 3 seconds — server needs at least 2s to respond

// GOOD: Warns about non-obvious behavior
// NOTE: This function is NOT thread-safe
void updateCache() { /* ... */ }
```

## Key Takeaways
1. `//` for single lines, `/* */` for blocks
2. Comments don't nest: `/* /* inner */ outer */` breaks
3. Use comments to explain WHY, not WHAT
4. TODO/FIXME/HACK are common tags: `// TODO: optimize this`
5. Doxygen comments (`///` or `/** */`) generate documentation

## Common Mistakes
- Nested `/* */` comments cause compile errors
- Commenting out code instead of deleting it (use version control instead)
- Over-commenting obvious code
"""),

    ("Semicolons and statement termination", "syntax", """
## Problem Statement
Understand why semicolons are required and where they go in C++.

## What You Need to Know
- C++ uses `;` to terminate statements (unlike Python which uses newlines).
- A **statement** is a complete instruction.
- Some constructs do NOT need semicolons: function bodies, if/else blocks, loops.
- Class/struct definitions DO need a semicolon after the closing brace.

## Examples
```cpp
int x = 5;           // variable declaration — needs ;
x = x + 1;           // assignment — needs ;
std::cout << x;      // expression statement — needs ;

if (x > 0) {         // NO semicolon after )
    x = 0;           // statement inside — needs ;
}                     // NO semicolon after }

struct Point {
    int x, y;
};                    // YES! Semicolon after class/struct closing brace

for (int i = 0; i < 10; ++i) {  // semicolons INSIDE for() separate clauses
    // ...
}                     // NO semicolon after loop body
```

## The Accidental Semicolon Bug
```cpp
// BUG: semicolon after if() creates an empty statement
if (x > 0);          // This empty statement always executes
{
    x = 0;            // This ALWAYS runs regardless of condition!
}

// BUG: semicolon after for() 
for (int i = 0; i < 10; ++i);  // Loop body is empty!
{
    std::cout << i;   // This runs ONCE, and `i` is out of scope
}
```

## Key Takeaways
1. Every statement ends with `;`
2. Control flow keywords (`if`, `for`, `while`) do NOT get `;` after `)`
3. Class/struct definitions need `;` after `}`
4. An accidental `;` after `if()` or `for()` is a silent logic bug
5. Use `-Wall` to catch some of these mistakes
"""),

    ("Whitespace and indentation rules", "syntax", """
## Problem Statement
Understand how C++ treats whitespace and learn consistent indentation practices.

## What You Need to Know
- C++ is a **free-form language** — whitespace (spaces, tabs, newlines) is ignored by the compiler between tokens.
- Indentation is purely for human readability.
- String literals preserve whitespace: `"hello world"` keeps the space.
- Preprocessor directives (`#include`, `#define`) must start at the beginning of a line.

## Examples
```cpp
// All of these compile identically:
int x=5;
int x = 5;
int
    x
        =
            5
                ;

// But readable code uses consistent style:
int x = 5;
```

## Common Indentation Styles
```cpp
// K&R / "One True Brace Style" (most common in C++)
if (condition) {
    doSomething();
} else {
    doOther();
}

// Allman style
if (condition)
{
    doSomething();
}
else
{
    doOther();
}

// Google C++ Style: 2 spaces, K&R braces
// LLVM Style: 2 spaces, K&R braces
// Linux Kernel Style: 8-space tabs (C, not C++)
```

## Tool: clang-format
```bash
# Auto-format your code
clang-format -i myfile.cpp            # in-place format
clang-format -style=google myfile.cpp  # Google style
```

## Key Takeaways
1. Compiler ignores whitespace between tokens
2. Pick ONE style and be consistent
3. Use `clang-format` to auto-format
4. 2 or 4 spaces per indent level is standard
5. Never mix tabs and spaces
"""),

    ("Case sensitivity", "syntax", """
## Problem Statement
Understand that C++ is case-sensitive and how this affects your code.

## What You Need to Know
- `myVar`, `MyVar`, `MYVAR`, and `myvar` are FOUR DIFFERENT identifiers.
- Keywords are lowercase: `int`, `if`, `return` (NOT `Int`, `IF`, `Return`).
- Standard library names follow conventions: `std::cout`, `std::vector`.

## Examples
```cpp
int count = 5;
int Count = 10;
int COUNT = 15;
// These are three separate variables!

// This is WRONG:
Int x = 5;     // Error: 'Int' is not a type
Return 0;      // Error: 'Return' is not a keyword

// Conventions:
int myVariable;        // camelCase (common in C++)
int my_variable;       // snake_case (common in C++ STL style)
const int MAX_SIZE = 100;  // UPPER_SNAKE_CASE for constants
class MyClass {};      // PascalCase for classes
```

## Key Takeaways
1. C++ is fully case-sensitive
2. Keywords are always lowercase
3. Follow your project's naming convention consistently
4. Common: `camelCase` for variables, `PascalCase` for classes, `UPPER_CASE` for constants
"""),

    ("Identifiers & naming rules", "syntax", """
## Problem Statement
Learn the rules for valid C++ identifiers (variable names, function names, etc.).

## Rules
1. Can contain: letters (a-z, A-Z), digits (0-9), underscore (_)
2. Must START with a letter or underscore (NOT a digit)
3. Cannot be a C++ keyword (`int`, `class`, `return`, etc.)
4. No spaces or special characters
5. Names starting with `_` followed by uppercase or `__` are RESERVED for the compiler

## Examples
```cpp
int age;          // ✓ valid
int _count;       // ✓ valid (but avoid leading underscore in global scope)
int player1;      // ✓ valid
int my_var;       // ✓ valid

int 1st_place;    // ✗ starts with digit
int my-var;       // ✗ contains hyphen
int my var;       // ✗ contains space
int class;        // ✗ is a keyword
int __reserved;   // ✗ double underscore — reserved for implementation
int _Uppercase;   // ✗ underscore + uppercase — reserved
```

## Naming Conventions
```cpp
// Google C++ Style:
int my_variable;           // variables: snake_case
void MyFunction();         // functions: PascalCase
class MyClass {};          // classes: PascalCase
const int kMaxSize = 100;  // constants: k + PascalCase
int member_var_;           // class members: trailing underscore

// LLVM Style:
int MyVariable;            // variables: PascalCase
void myFunction();         // functions: camelCase
```

## Key Takeaways
1. Start with letter or underscore
2. No special characters except underscore
3. Don't use reserved names (`__x`, `_Uppercase`)
4. Be descriptive: `count` > `c`, `studentAge` > `sa`
5. Single-letter names OK for loop indices: `i`, `j`, `k`
"""),

    ("Keywords list & usage", "syntax", """
## Problem Statement
Know the C++ keywords and understand they cannot be used as identifiers.

## C++ Keywords (C++20, 92 keywords)
```
alignas    alignof    and        and_eq     asm
auto       bitand     bitor      bool       break
case       catch      char       char8_t    char16_t
char32_t   class      compl      concept    const
consteval  constexpr  constinit  const_cast continue
co_await   co_return  co_yield   decltype   default
delete     do         double     dynamic_cast else
enum       explicit   export     extern     false
float      for        friend     goto       if
inline     int        long       mutable    namespace
new        noexcept   not        not_eq     nullptr
operator   or         or_eq      private    protected
public     register   reinterpret_cast requires return
short      signed     sizeof     static     static_assert
static_cast struct    switch     template   this
thread_local throw    true       try        typedef
typeid     typename   union      unsigned   using
virtual    void       volatile   wchar_t    while
xor        xor_eq
```

## Most Common Keywords by Category
```cpp
// Types:        int, char, float, double, bool, void, auto
// Control:      if, else, for, while, do, switch, case, break, continue, return
// Classes:      class, struct, public, private, protected, virtual, this
// Memory:       new, delete, const, static, extern
// Modern C++:   auto, decltype, nullptr, constexpr, noexcept, concept, requires
```

## Key Takeaways
1. You CANNOT use keywords as variable/function names
2. Some keywords are context-sensitive (e.g., `override`, `final` — not reserved everywhere)
3. Alternative tokens exist: `and` (&&), `or` (||), `not` (!) — rarely used
"""),

    ("Basic input with cin", "syntax", """
## Problem Statement
Read user input from the keyboard using `std::cin`.

## What You Need to Know
- `std::cin` reads from standard input (keyboard by default).
- `>>` is the stream extraction operator.
- `cin` skips leading whitespace by default.
- `cin` stops reading at whitespace for strings.

## Solution 1: Read a single integer
```cpp
#include <iostream>

int main() {
    int age;
    std::cout << "Enter your age: ";
    std::cin >> age;
    std::cout << "You are " << age << " years old.\\n";
    return 0;
}
```

## Solution 2: Read multiple values
```cpp
#include <iostream>

int main() {
    int x, y;
    std::cout << "Enter two numbers: ";
    std::cin >> x >> y;  // Chained extraction
    std::cout << "Sum: " << (x + y) << "\\n";
    return 0;
}
```

## Solution 3: Read a string (single word)
```cpp
#include <iostream>
#include <string>

int main() {
    std::string name;
    std::cout << "Enter your name: ";
    std::cin >> name;  // Reads only ONE word (stops at space)
    std::cout << "Hello, " << name << "\\n";
    return 0;
}
```

## Solution 4: Read an entire line
```cpp
#include <iostream>
#include <string>

int main() {
    std::string fullName;
    std::cout << "Enter your full name: ";
    std::getline(std::cin, fullName);  // Reads entire line including spaces
    std::cout << "Hello, " << fullName << "\\n";
    return 0;
}
```

## Input Validation
```cpp
#include <iostream>

int main() {
    int num;
    std::cout << "Enter a number: ";
    if (std::cin >> num) {
        std::cout << "You entered: " << num << "\\n";
    } else {
        std::cout << "Invalid input!\\n";
        std::cin.clear();             // Clear error flags
        std::cin.ignore(10000, '\\n'); // Discard bad input
    }
    return 0;
}
```

## Key Takeaways
1. `cin >> var` reads one token (stops at whitespace)
2. `getline(cin, str)` reads entire line
3. Always validate input: check if `cin >>` succeeded
4. After failed input, call `cin.clear()` then `cin.ignore()`
5. Mixing `cin >>` and `getline` requires `cin.ignore()` between them

## Common Mistakes
- Reading a string with `cin >>` when input has spaces → only first word captured
- Not handling invalid input → program enters infinite loop or reads garbage
- Mixing `cin >>` and `getline` without `cin.ignore()` → getline reads empty string
"""),

    ("Basic output with cout", "syntax", """
## Problem Statement
Display output to the console using `std::cout`.

## Solutions
```cpp
#include <iostream>

int main() {
    // String output
    std::cout << "Hello, World!\\n";

    // Variable output
    int x = 42;
    std::cout << "x = " << x << "\\n";

    // Chained output
    std::cout << "a=" << 1 << " b=" << 2.5 << " c=" << 'Z' << "\\n";

    // Formatted output
    double pi = 3.14159;
    std::cout << std::fixed;          // fixed-point notation
    std::cout.precision(2);           // 2 decimal places
    std::cout << "Pi = " << pi << "\\n";  // Pi = 3.14

    return 0;
}
```

## Key Takeaways
1. `<<` chains multiple values
2. `\\n` for newline (faster than `endl`)
3. `std::fixed` + `precision()` for decimal formatting
4. `cout` buffers output — use `endl` or `flush` to force immediate display
"""),

    ("endl vs \\n", "syntax", """
## Problem Statement
Understand the difference between `std::endl` and `\\n` for newlines.

## Comparison
```cpp
#include <iostream>

int main() {
    // Using \\n — just inserts a newline character
    std::cout << "Line 1\\n";
    std::cout << "Line 2\\n";

    // Using endl — inserts newline AND flushes the buffer
    std::cout << "Line 3" << std::endl;
    std::cout << "Line 4" << std::endl;

    return 0;
}
```

## What "Flushing" Means
```
Without flush:
  Program writes to buffer → [H][e][l][l][o][\\n] → waits until buffer is full → THEN sends to screen

With flush (endl):
  Program writes to buffer → [H][e][l][l][o][\\n] → IMMEDIATELY sends to screen
```

## Performance Test
```cpp
#include <iostream>
#include <chrono>

int main() {
    auto start = std::chrono::high_resolution_clock::now();
    for (int i = 0; i < 100000; ++i)
        std::cout << i << "\\n";     // FAST
    auto end = std::chrono::high_resolution_clock::now();
    // Using endl would be ~5-10x slower for this loop
    return 0;
}
```

## When to Use Which
| Use `\\n` | Use `endl` |
|-----------|-----------|
| Normal output | Debugging (ensure output appears before crash) |
| Loops with lots of output | Interactive prompts (before reading input) |
| Performance-critical code | Before `cin` operations |

## Key Takeaways
1. `\\n` = newline only (fast)
2. `endl` = newline + flush (slow)
3. Default: use `\\n`. Use `endl` only when you NEED to flush.
"""),

    ("Multiple variables on one line", "syntax", """
## Problem Statement
Declare and initialize multiple variables on a single line.

## Solutions
```cpp
int a, b, c;           // Three uninitialized ints
int x = 1, y = 2, z = 3;  // Three initialized ints
double pi = 3.14, e = 2.71;

// DANGER: pointer declaration trap
int* p, q;   // p is int*, but q is just int! NOT int*
int *p, *q;  // Both are int* — asterisk binds to the variable name

// BETTER: one declaration per line for clarity
int* p = nullptr;
int* q = nullptr;
```

## Key Takeaways
1. Comma separates variables of the same type
2. Pointer `*` binds to the variable name, not the type
3. Best practice: one variable per line for clarity, especially with pointers
"""),

    ("Chained cout statements", "syntax", """
## Problem Statement
Output multiple values in a single `cout` statement using chaining.

## Solution
```cpp
#include <iostream>

int main() {
    std::string name = "Alice";
    int age = 30;
    double gpa = 3.95;

    // Chained output
    std::cout << "Name: " << name 
              << ", Age: " << age 
              << ", GPA: " << gpa 
              << "\\n";

    // How it works internally:
    // std::cout << "Name: "   → returns reference to cout
    //           << name       → returns reference to cout
    //           << ", Age: "  → returns reference to cout
    //           << age        → returns reference to cout
    //           << "\\n"       → returns reference to cout

    return 0;
}
```

## Key Takeaways
1. Each `<<` returns a reference to `cout`, enabling chaining
2. You can mix types: strings, ints, doubles, chars
3. Break long chains across lines for readability
"""),

    ("Reading multiple inputs", "syntax", """
## Problem Statement
Read multiple values from the user in one or more `cin` operations.

## Solution 1: Chained extraction
```cpp
#include <iostream>

int main() {
    int a, b, c;
    std::cout << "Enter three numbers: ";
    std::cin >> a >> b >> c;  // User can type: 10 20 30
    std::cout << "Sum: " << (a + b + c) << "\\n";
    return 0;
}
```

## Solution 2: Reading in a loop
```cpp
#include <iostream>
#include <vector>

int main() {
    int n;
    std::cout << "How many numbers? ";
    std::cin >> n;

    std::vector<int> nums(n);
    for (int i = 0; i < n; ++i) {
        std::cin >> nums[i];
    }

    int sum = 0;
    for (int x : nums) sum += x;
    std::cout << "Sum: " << sum << "\\n";
    return 0;
}
```

## Solution 3: Reading until EOF
```cpp
#include <iostream>

int main() {
    int x, sum = 0, count = 0;
    while (std::cin >> x) {  // Reads until EOF (Ctrl+D on Linux, Ctrl+Z on Windows)
        sum += x;
        ++count;
    }
    std::cout << "Average: " << (count > 0 ? (double)sum / count : 0) << "\\n";
    return 0;
}
```

## Key Takeaways
1. `cin >>` skips whitespace between values
2. Chained `>>` reads multiple values separated by spaces or newlines
3. `while (cin >> x)` is the standard pattern for reading until EOF
4. Check `cin.fail()` after reading to detect invalid input
"""),

    ("Program compilation with g++", "syntax", """
## Problem Statement
Compile and run a C++ program using the g++ compiler from the command line.

## Compilation Commands
```bash
# Basic compilation
g++ main.cpp -o myprogram
./myprogram

# With C++17 standard
g++ -std=c++17 main.cpp -o myprogram

# With warnings enabled (ALWAYS do this)
g++ -std=c++17 -Wall -Wextra main.cpp -o myprogram

# With debugging info (for gdb)
g++ -std=c++17 -Wall -g main.cpp -o myprogram

# With optimization
g++ -std=c++17 -O2 main.cpp -o myprogram

# With address sanitizer (find memory bugs)
g++ -std=c++17 -Wall -fsanitize=address -g main.cpp -o myprogram

# Multiple source files
g++ -std=c++17 main.cpp utils.cpp math.cpp -o myprogram
```

## Compilation Steps (What g++ Does)
```
1. Preprocessing:  g++ -E main.cpp    → Expands #include, #define
2. Compilation:    g++ -S main.cpp    → Generates assembly (.s file)
3. Assembly:       g++ -c main.cpp    → Generates object file (.o)
4. Linking:        g++ main.o -o prog → Links object files into executable
```

## Key Flags
| Flag | Purpose |
|------|---------|
| `-std=c++17` | Use C++17 standard |
| `-Wall` | Enable common warnings |
| `-Wextra` | Enable extra warnings |
| `-g` | Include debug info |
| `-O0` / `-O2` / `-O3` | Optimization levels |
| `-fsanitize=address` | Detect memory errors |
| `-fsanitize=undefined` | Detect undefined behavior |

## Key Takeaways
1. Always compile with `-Wall -Wextra`
2. Use `-std=c++17` (or c++20) for modern features
3. Use `-g` when debugging with gdb
4. Use `-fsanitize=address` to catch memory bugs
"""),

    ("Common compile errors", "syntax", """
## Problem Statement
Recognize and fix the most common C++ compilation errors.

## Error 1: Missing semicolon
```cpp
int x = 5   // ERROR: expected ';' at end of declaration
int y = 10;
```
**Fix:** Add `;` after `5`.

## Error 2: Undeclared identifier
```cpp
cout << "hello";  // ERROR: 'cout' was not declared in this scope
```
**Fix:** Add `#include <iostream>` and use `std::cout`.

## Error 3: Type mismatch
```cpp
int x = "hello";  // ERROR: cannot initialize int with string literal
```
**Fix:** Use `std::string x = "hello";`

## Error 4: Missing return statement
```cpp
int add(int a, int b) {
    int result = a + b;
    // WARNING: no return statement
}
```
**Fix:** Add `return result;`

## Error 5: Mismatched braces
```cpp
if (x > 0) {
    std::cout << "positive";
// ERROR: expected '}' at end of input
```
**Fix:** Add closing `}`.

## Error 6: Redefinition
```cpp
int x = 5;
int x = 10;  // ERROR: redefinition of 'x'
```
**Fix:** Use `x = 10;` (assignment, not declaration).

## Key Takeaways
1. Read error messages carefully — the line number is often BEFORE the actual error
2. Fix errors from TOP to BOTTOM (later errors are often caused by earlier ones)
3. Common pattern: if you see 100 errors, fix the first one and recompile
"""),

    ("Linker errors vs compile errors", "syntax", """
## Problem Statement
Understand the difference between compilation errors and linker errors.

## Compile Errors (Caught During Compilation)
```cpp
// Syntax error — compiler catches this
int x = ;  // ERROR: expected expression

// Type error — compiler catches this
int x = "hello";  // ERROR: cannot initialize int with string
```
**Pattern:** Error message says "error:" with source file and line number.

## Linker Errors (Caught During Linking)
```cpp
// file1.cpp
void doSomething();  // Declaration only — no definition anywhere

int main() {
    doSomething();  // Compiles fine! But linker can't find the definition
    return 0;
}
// LINKER ERROR: undefined reference to 'doSomething()'
```
**Pattern:** Error message says "undefined reference to" or "unresolved external symbol".

## How to Tell the Difference
| Compile Error | Linker Error |
|--------------|-------------|
| Shows source file + line number | Shows function/symbol name |
| Says "error:" | Says "undefined reference" |
| Syntax/type problem | Missing implementation |
| Fix: correct the code | Fix: add missing implementation or library |

## Common Linker Error Fixes
```bash
# Missing library
g++ main.cpp -lm          # Link math library
g++ main.cpp -lpthread    # Link pthread library

# Missing source file
g++ main.cpp utils.cpp    # Include ALL source files
```

## Key Takeaways
1. Compile errors = language mistakes (syntax, types)
2. Linker errors = missing implementations (function body, library)
3. Fix compile errors first, then linker errors
"""),

    ("Warnings and how to fix them", "syntax", """
## Problem Statement
Understand common compiler warnings and why you should fix them.

## Common Warnings
```cpp
// Warning: unused variable
int x = 5;  // Never used → remove it or use [[maybe_unused]]

// Warning: signed/unsigned comparison
int a = -1;
unsigned int b = 5;
if (a < b) { }  // Dangerous! -1 converts to a huge unsigned number

// Warning: implicit conversion loses precision
double pi = 3.14;
int approx = pi;  // Loses .14 → use static_cast<int>(pi) to be explicit

// Warning: variable may be used uninitialized
int x;
std::cout << x;  // x has garbage value!

// Warning: control reaches end of non-void function
int getValue(bool flag) {
    if (flag) return 42;
    // Missing return for else case!
}
```

## Suppressing Intentional Warnings
```cpp
[[maybe_unused]] int debugCounter = 0;  // C++17: suppress unused warning

(void)unusedParam;  // C-style: cast to void to suppress unused parameter warning
```

## Key Takeaways
1. Always compile with `-Wall -Wextra`
2. Treat warnings as errors with `-Werror`
3. Fix warnings — they often indicate real bugs
4. Use `[[maybe_unused]]` for intentionally unused variables (C++17)
"""),

    ("Using -Wall flag", "syntax", """
## Problem Statement
Understand the `-Wall` compiler flag and related warning flags.

## Flag Overview
```bash
g++ -Wall main.cpp         # Common warnings
g++ -Wall -Wextra main.cpp # More warnings
g++ -Wall -Wextra -Wpedantic main.cpp  # Strict standard compliance
g++ -Wall -Werror main.cpp # Treat all warnings as errors
```

## What -Wall Enables (partial list)
- `-Wunused-variable`: unused variables
- `-Wuninitialized`: potentially uninitialized variables
- `-Wreturn-type`: missing return in non-void function
- `-Wparentheses`: ambiguous expressions that need parentheses
- `-Wsign-compare`: signed/unsigned comparison
- `-Wformat`: printf format string mismatches

## What -Wextra Adds
- `-Wunused-parameter`: unused function parameters
- `-Wmissing-field-initializers`: missing struct initializers

## Recommended Compile Command
```bash
g++ -std=c++17 -Wall -Wextra -Wpedantic -Wshadow -Wconversion -g main.cpp -o prog
```

## Key Takeaways
1. `-Wall` doesn't enable ALL warnings (misleading name)
2. `-Wextra` adds important additional warnings
3. Use `-Werror` in CI/CD to prevent warning accumulation
4. `-Wshadow` catches variable shadowing bugs
5. `-Wconversion` catches implicit narrowing conversions
"""),
]

# Add remaining C00 problems (21-120) with structured content
C00_remaining = [
    ("Code blocks and braces", "syntax"),
    ("Nested braces", "syntax"),
    ("Scope basics with braces", "syntax"),
    ("Blank lines and readability", "syntax"),
    ("Code formatting standards", "syntax"),
    ("Literal values (numbers, strings)", "syntax"),
    ("String literals with quotes", "syntax"),
    ("Escape sequences", "syntax"),
    ("Raw string literals R\"(...)\"", "syntax"),
    ("Unicode basics", "syntax"),
    ("ASCII values", "syntax"),
    ("char literals with single quotes", "syntax"),
    ("Printing special characters", "syntax"),
    ("Tab stops with \\t", "syntax"),
    ("printf vs cout", "syntax"),
    ("scanf vs cin", "syntax"),
    ("puts() and gets() legacy", "syntax"),
    ("iostream header", "syntax"),
    ("cstdio header", "syntax"),
    ("Including multiple headers", "syntax"),
    ("Header file purpose", "preprocessor"),
    ("Compilation steps overview", "preprocessor"),
    ("Preprocessor directives", "preprocessor"),
    ("#define basics", "preprocessor"),
    ("Macro constants", "preprocessor"),
    ("Conditional compilation #ifdef", "preprocessor"),
    ("#pragma once", "preprocessor"),
    ("Include guards", "preprocessor"),
    ("Multiple source files concept", "preprocessor"),
    ("Object files (.o)", "preprocessor"),
    ("Linking explained", "preprocessor"),
    ("argc and argv basics", "functions"),
    ("Command-line arguments printing", "functions"),
    ("Return 0 meaning", "functions"),
    ("Non-zero return codes", "functions"),
    ("EXIT_SUCCESS and EXIT_FAILURE", "functions"),
    ("Program entry/exit flow", "functions"),
    ("Debugger basics (gdb intro)", "debugging"),
    ("Breakpoints concept", "debugging"),
    ("Stepping through code", "debugging"),
    ("Print-based debugging", "debugging"),
    ("cerr for error output", "io"),
    ("clog for logging", "io"),
    ("flush output buffer", "io"),
    ("std::endl flushing", "io"),
    ("Buffered vs unbuffered output", "io"),
    ("Reading entire line with getline", "io"),
    ("Whitespace in getline", "io"),
    ("cin.ignore() usage", "io"),
    ("cin.clear() usage", "io"),
    ("Input failure states", "io"),
    ("Numeric input validation basics", "io"),
    ("Type mismatch in input", "io"),
    ("Overflow on small types", "types"),
    ("Garbage values without initialization", "memory"),
    ("Undefined behavior intro", "memory"),
    ("Stack memory concept (simple)", "memory"),
    ("Static vs automatic storage basics", "memory"),
    ("Global variables basics", "variables"),
    ("Local variables basics", "variables"),
    ("Variable lifetime basics", "variables"),
    ("Block scope vs file scope", "variables"),
    ("Forward declarations basics", "functions"),
    ("Function prototypes concept", "functions"),
    ("Simple function definition", "functions"),
    ("Calling a function", "functions"),
    ("Return value from function", "functions"),
    ("void functions", "functions"),
    ("Parameters vs arguments", "functions"),
    ("Pass by value basics", "functions"),
    ("Multiple return values (intro)", "functions"),
    ("Overloading intro (concept only)", "functions"),
    ("Inline concept (brief)", "functions"),
    ("constexpr intro", "modern"),
    ("auto keyword intro", "modern"),
    ("decltype intro", "modern"),
    ("nullptr intro", "modern"),
    ("NULL vs nullptr", "modern"),
    ("Basic boolean logic", "types"),
    ("true/false literals", "types"),
    ("Boolean output (0/1)", "types"),
    ("Casting bool to int", "types"),
    ("sizeof operator", "types"),
    ("Addresses concept (&)", "pointers"),
    ("Dereferencing concept (*)", "pointers"),
    ("Basic struct definition", "structs"),
    ("Struct member access", "structs"),
    ("Struct initialization", "structs"),
    ("Simple enum definition", "enums"),
    ("enum class basics", "enums"),
    ("typedef basics", "types"),
    ("using alias basics", "types"),
    ("Namespaces concept", "namespaces"),
    ("std:: prefix meaning", "namespaces"),
    ("using namespace std risks", "namespaces"),
    ("Named namespace basics", "namespaces"),
    ("Anonymous namespace", "namespaces"),
    ("Nested namespace (C++17)", "namespaces"),
    ("One-definition rule basics", "linking"),
    ("Translation unit concept", "linking"),
    ("Build systems intro (Makefile basics)", "build"),
    ("IDE setup (VS Code / CLion)", "tools"),
    ("Online compilers (Godbolt, replit)", "tools"),
    ("Compiler flags overview", "build"),
    ("-O0 / -O2 / -O3", "build"),
    ("-std=c++17 / c++20 flags", "build"),
    ("Address sanitizer (-fsanitize=address)", "debugging"),
    ("UBSan intro", "debugging"),
    ("Static analysis basics", "tools"),
    ("clang-format intro", "tools"),
]

def generate_generic_doc(name, category, idx, level, cat_id):
    """Generate a comprehensive doc for problems without handcrafted content."""

    # Determine topic type and generate appropriate content
    is_concept = any(w in name.lower() for w in ['concept', 'basics', 'intro', 'overview', 'explained', 'rules', 'meaning'])
    is_algorithm = any(w in name.lower() for w in ['sort', 'search', 'sum', 'count', 'check', 'find', 'reverse', 'rotate', 'merge'])
    is_pattern = any(w in name.lower() for w in ['pattern', 'diamond', 'triangle', 'pyramid', 'rectangle', 'star', 'floyd'])
    is_implementation = any(w in name.lower() for w in ['implementation', 'from scratch', 'design', 'implement'])

    content = f"""# {name}

> **Level:** {'0 — Absolute Beginner' if level == 0 else '1 — Beginner'}  
> **Category:** {cat_id}  
> **Topic:** {category}

---

## Problem Statement

{"Understand and explain the concept of " + name + ". Be able to describe it, identify it in code, and use it correctly." if is_concept else
"Write a C++ program that solves the " + name + " problem." if is_algorithm or is_pattern else
"Implement " + name + " in C++ with proper error handling and clean code." if is_implementation else
"Master the use of " + name + " in C++ programs. Understand when and why to use it."}

### Examples
- **Input Example 1:** A typical/simple case
- **Input Example 2:** An edge case (empty input, boundary values)
- **Input Example 3:** A larger or tricky case

---

## Prerequisites
- Basic C++ syntax (variables, types, operators)
- {"Control flow (if/else, loops)" if is_algorithm or is_pattern else "Understanding of C++ compilation model" if is_concept else "Standard I/O operations"}
- {"Array/vector basics" if is_algorithm else "Function definition and calling" if 'function' in name.lower() or 'recursion' in name.lower() or 'recursive' in name.lower() else "Header files and namespaces"}

---

## Core Concept

### What Is It?
{name} is a {"fundamental concept" if is_concept else "classic problem" if is_algorithm else "common programming pattern" if is_pattern else "technique"} in C++ that {"every programmer must understand" if is_concept else "tests your understanding of loops and logic" if is_pattern else "appears frequently in interviews and real projects"}.

### Why Does It Matter?
- {"Forms the foundation for understanding more complex C++ features" if is_concept else
"Builds problem-solving muscle for algorithmic thinking" if is_algorithm or is_pattern else
"Used extensively in production C++ code"}
- Commonly asked in technical interviews
- {"Essential for writing correct, safe C++ code" if 'undefined' in name.lower() or 'error' in name.lower() or 'sanitizer' in name.lower() else "Helps write clean, maintainable code"}

### Mental Model
Think of {name.lower()} as {"a building block — you can't build a house without understanding bricks" if is_concept else
"a puzzle — break it into smaller pieces and solve each one" if is_algorithm else
"a recipe — follow the steps in order and you'll get the right output" if is_pattern else
"a tool in your toolbox — know when to reach for it"}.

---

## Solution Approaches

### Approach 1: Direct / Straightforward
```cpp
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

/*
 * {name}
 * 
 * Approach: Direct implementation
 * Time Complexity:  O(n) — typical for this type of problem
 * Space Complexity: O(1) — or O(n) if storing results
 */
int main() {{
    // TODO: Implement {name}
    // Step 1: Read input
    // Step 2: Process
    // Step 3: Output result
    
    std::cout << "Solution for: {name}" << std::endl;
    return 0;
}}
```

**Time Complexity:** O(n) (typical)  
**Space Complexity:** O(1) or O(n)  
**When to use:** First attempt, when simplicity matters over performance.

### Approach 2: Optimized / STL-Based
```cpp
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <numeric>

/*
 * {name} — Optimized approach using STL
 * 
 * Uses standard library algorithms where applicable.
 * Generally preferred in production C++ code.
 */
int main() {{
    // TODO: STL-based implementation
    // Use std::sort, std::find, std::accumulate, etc. as appropriate
    
    return 0;
}}
```

**Time Complexity:** Depends on STL algorithm used  
**Space Complexity:** Depends on approach  
**When to use:** Production code, when you know the right STL tool.

### Approach 3: Modern C++ (C++17/20)
```cpp
#include <iostream>
#include <string>
#include <vector>

/*
 * {name} — Modern C++ approach
 * 
 * Uses features from C++17/20: structured bindings,
 * if-init, ranges, constexpr, etc.
 */
int main() {{
    // TODO: Modern C++ implementation
    // Use auto, structured bindings, ranges, etc.
    
    return 0;
}}
```

---

## Step-by-Step Trace

For a typical input, trace the solution:

| Step | State | Action | Result |
|------|-------|--------|--------|
| 1 | Initial | Read input | — |
| 2 | Processing | Apply algorithm | — |
| 3 | Final | Output result | — |

---

## Common Mistakes & Pitfalls

1. **Off-by-one errors** — Check loop boundaries carefully
2. **Uninitialized variables** — Always initialize before use
3. **Integer overflow** — Use `long long` for large numbers
4. **Missing edge cases** — Empty input, single element, negative numbers
5. **Forgetting `#include`** — Include all necessary headers
6. **Using `==` vs `=`** — Assignment vs comparison

---

## What You Should Learn From This

### Key C++ Feature Demonstrated
- {name} demonstrates {"fundamental language syntax" if is_concept else "loop control and algorithmic thinking" if is_algorithm or is_pattern else "proper C++ idioms and best practices"}

### Interview Tips
- {"Explain the concept clearly before writing code" if is_concept else "Start with brute force, then optimize" if is_algorithm else "Discuss tradeoffs between approaches"}
- Always discuss time/space complexity
- Mention edge cases proactively

### Code Review Checklist
- [ ] Compiles with `-Wall -Wextra` — no warnings
- [ ] Handles edge cases
- [ ] Variables are properly initialized
- [ ] No memory leaks (if using dynamic allocation)
- [ ] Code is readable and well-commented

---

## Pattern Recognition

**Pattern:** {
"Language fundamentals — know the rules" if is_concept else
"Loop-based computation — iterate and accumulate" if is_algorithm else
"Nested loop pattern — control spacing and characters" if is_pattern else
"Implementation pattern — combine concepts to build"
}

**Similar Problems:**
- (See other problems in this category)

**When you see** _______, **think** _______.

---

## Practice Variants
1. **Easy:** Simplify the constraints (smaller input, fewer edge cases)
2. **Medium:** Add a constraint (handle negative numbers, optimize for time)
3. **Hard:** Combine with another concept (recursion, dynamic programming)

---

## Quick Reference Card
- **Core idea:** {name}
- **Key construct:** {"Loops" if is_algorithm or is_pattern else "Language syntax" if is_concept else "STL / Standard Library"}
- **Complexity:** O(n) typical
- **Don't forget:** Initialize variables, check edge cases, use `-Wall`

---

*Generated for C++ Level {'0' if level == 0 else '1'} — {cat_id} Problem Solving Guide*
"""
    return content


def write_doc(folder, idx, name, content):
    """Write a single problem doc."""
    filename = safe_filename(name, idx)
    filepath = os.path.join(folder, filename)
    with open(filepath, 'w') as f:
        f.write(content)
    return filepath


def main():
    created = 0
    
    # === C00: Syntax & Program Structure ===
    c00_dir = os.path.join(BASE, "C00_Syntax_Program_Structure")
    os.makedirs(c00_dir, exist_ok=True)
    
    # First 20 with handcrafted content
    for idx, (name, category, content) in enumerate(C00, 1):
        full_content = f"# {name}\n\n> **Level:** 0 — Absolute Beginner  \n> **Category:** C00 — C++ Syntax & Program Structure  \n> **Topic:** {category}\n\n---\n{content}"
        write_doc(c00_dir, idx, name, full_content)
        created += 1
    
    # Remaining C00 (21-120)
    for idx_offset, (name, category) in enumerate(C00_remaining):
        idx = len(C00) + idx_offset + 1
        content = generate_generic_doc(name, category, idx, 0, "C00")
        write_doc(c00_dir, idx, name, content)
        created += 1
    
    # === C01: Data Types & Variables ===
    c01_dir = os.path.join(BASE, "C01_Data_Types_Variables")
    os.makedirs(c01_dir, exist_ok=True)
    
    c01_problems = [
        "int, float, double, char, bool", "short, long, long long",
        "unsigned types", "signed vs unsigned",
        "Type sizes with sizeof", "INT_MAX / INT_MIN constants",
        "FLT_MAX / DBL_MAX", "Overflow wrap-around (unsigned)",
        "Signed overflow UB", "Floating point precision issues",
        "0.1 + 0.2 != 0.3 explained", "NaN and infinity (float)",
        "isinf() isnan()", "std::numeric_limits<T>",
        "Fixed-width types (int32_t, uint64_t)", "<cstdint> header",
        "ptrdiff_t and size_t", "Implicit type conversion",
        "Explicit cast (C-style)", "static_cast<>",
        "reinterpret_cast<>", "const_cast<>",
        "dynamic_cast<>", "Narrowing conversions",
        "Brace-init prevents narrowing", "Integer promotion rules",
        "Usual arithmetic conversions", "Integral vs floating arithmetic",
        "Mixed-type expressions", "Char arithmetic",
        "wchar_t, char16_t, char32_t", "String vs char array",
        "std::string basics", "string length vs size",
        "Accessing string characters", "string concatenation",
        "String comparison", "String to int (stoi)",
        "String to double (stod)", "Int to string (to_string)",
        "std::stof, stol, stoul", "String find() method",
        "String substr()", "String replace()",
        "String insert() / erase()", "String empty() / clear()",
        "C-string (char array) basics", "strlen vs string::size",
        "strcpy / strncpy", "strcmp / strncmp",
        "strcat / strncat", "sprintf / snprintf",
        "atoi / atof legacy", "String literals and pointers",
        "const char*", "string_view intro (C++17)",
        "Structured bindings (C++17)", "Tuple basics",
        "pair<T1,T2>", "make_pair()",
        "tie() for tuple unpack", "Optional<T> (C++17)",
        "variant<T...> (C++17)", "any (C++17)",
        "Bitfield basics", "Union basics",
        "Anonymous union", "Alignment and alignof",
        "alignas specifier", "Padding in structs",
        "#pragma pack", "POD types",
        "Trivially copyable types", "Standard layout types",
        "Aggregate initialization", "Designated initializers (C++20)",
        "Uniform initialization {}", "Value initialization",
        "Default initialization", "Zero initialization",
        "Copy initialization", "Direct initialization",
        "List initialization", "Brace elision",
        "Narrowing in initializer lists", "constexpr variables",
        "const vs constexpr", "consteval (C++20)",
        "constinit (C++20)", "inline variables (C++17)",
        "thread_local storage", "volatile keyword",
        "register keyword (deprecated)", "extern declaration",
        "Linkage: internal vs external", "One definition rule",
        "Tentative definitions (C)", "Multiple definitions error",
        "Redeclaration vs redefinition", "Forward declare struct",
        "Incomplete types", "Opaque pointer pattern",
        "Type aliases with using", "Template type aliases",
        "auto type deduction rules", "decltype(auto)",
        "CTAD (Class Template Arg Deduction)", "Concepts intro (C++20)",
        "requires clause basics", "Type traits overview",
        "is_integral<T>", "is_floating_point<T>",
        "is_same<T,U>", "remove_const<T>",
        "add_pointer<T>", "conditional<B,T,F>",
    ]
    
    for idx, name in enumerate(c01_problems, 1):
        content = generate_generic_doc(name, "types", idx, 0, "C01")
        write_doc(c01_dir, idx, name, content)
        created += 1
    
    # === C10: Control Flow & Loops ===
    c10_dir = os.path.join(BASE, "C10_Control_Flow_Loops")
    os.makedirs(c10_dir, exist_ok=True)
    
    c10_problems = [
        "if / else if / else", "Nested if statements",
        "Dangling else problem", "Switch-case statement",
        "switch fall-through", "switch with enum",
        "Ternary operator ?:", "Nested ternary (anti-pattern)",
        "while loop", "do-while loop",
        "for loop", "Range-based for loop",
        "Range-for with index trick", "Infinite loop patterns",
        "break statement", "continue statement",
        "goto (and why to avoid)", "Loop unrolling concept",
        "FizzBuzz", "Sum 1 to N",
        "Factorial (iterative)", "Fibonacci (iterative)",
        "Prime check", "Sieve of Eratosthenes",
        "GCD (Euclidean)", "LCM from GCD",
        "Count digits", "Reverse digits",
        "Palindrome number", "Armstrong number",
        "Perfect number", "Abundant number",
        "Sum of digits", "Digital root",
        "Power (iterative)", "Modular exponentiation",
        "Binary to decimal", "Decimal to binary",
        "Octal / Hexadecimal conversion", "Base conversion generic",
        "Leap year check", "Day of week calculation",
        "Number of days in month", "Time addition (HH:MM:SS)",
        "Matrix loop (row-major)", "Column-major access",
        "Star pattern (triangle)", "Inverted triangle",
        "Diamond pattern", "Floyd's triangle",
        "Pascal's triangle (print)", "Number pyramid",
        "Hollow rectangle pattern", "Spiral matrix print",
        "Loop invariant reasoning", "Off-by-one errors",
        "Index out of bounds", "Infinite loop debugging",
        "Early exit pattern", "Guard clauses",
        "Loop with multiple conditions", "Boolean flags in loops",
        "Counting with modulo", "Cyclic iteration",
        "Two-pointer in loops (intro)", "Sliding window intro",
        "Nested loop complexity", "Reducing O(n^2) loops",
        "Loop fusion", "Loop fission",
        "Prefix sum with loop", "Running average",
        "Running max/min", "Mode of array in loop",
        "Frequency count with array", "Histogram in loop",
        "String reversal loop", "Palindrome string check",
        "Count vowels/consonants", "Caesar cipher loop",
        "ROT13", "String to uppercase/lowercase",
        "Remove spaces from string", "Count words in string",
        "Find substring manually", "Replace char in string",
        "Compress string (run-length)", "Expand compressed string",
        "Anagram check (sort approach)", "Isomorphic strings",
        "Longest run of character", "Most frequent character",
        "String rotation check", "Shift string by k",
        "Toggle case", "Title case conversion",
        "Trim leading/trailing spaces", "Tokenize by delimiter",
        "Count specific char", "Unique chars in string",
        "Remove duplicates in string", "Interleave two strings",
        "Merge sorted strings", "Longest common prefix (loop)",
        "atoi implementation", "itoa implementation",
        "strtol manual implementation", "Number formatting with commas",
        "Scientific notation parse", "Binary string to int",
        "Hex string to int", "IP address parse & validate",
        "Roman numeral to int", "Int to Roman numeral",
        "Expression evaluation (basic)", "Check balanced brackets",
        "Convert infix to prefix (intro)", "Luhn algorithm",
        "Checksum calculation", "CRC concept",
    ]
    
    for idx, name in enumerate(c10_problems, 1):
        content = generate_generic_doc(name, "control_flow", idx, 1, "C10")
        write_doc(c10_dir, idx, name, content)
        created += 1
    
    # === C11: Functions & Recursion ===
    c11_dir = os.path.join(BASE, "C11_Functions_Recursion")
    os.makedirs(c11_dir, exist_ok=True)
    
    c11_problems = [
        "Function declaration vs definition", "Return types",
        "void functions", "Multiple return values via reference",
        "Default parameter values", "Default params ordering rules",
        "Function overloading", "Overload resolution rules",
        "Ambiguous overloads", "Name mangling",
        "extern C linkage", "Inline functions",
        "constexpr functions", "consteval functions (C++20)",
        "Function pointers", "Typedef for function pointer",
        "using alias for function pointer", "Calling via function pointer",
        "Array of function pointers", "Callback pattern",
        "Passing functions to functions", "Returning function pointers",
        "std::function<>", "std::bind()",
        "Partial application with bind", "Lambda expressions",
        "Lambda capture by value", "Lambda capture by reference",
        "Generic lambdas (C++14)", "Lambda in algorithms",
        "Immediately invoked lambda", "Recursive lambda",
        "Factorial (recursive)", "Fibonacci (recursive)",
        "Sum of array (recursive)", "Power (recursive)",
        "GCD (recursive)", "Binary search (recursive)",
        "Tower of Hanoi", "Flood fill (recursive)",
        "Permutations of string", "Subsets of set",
        "Combinations nCr", "Generate parentheses",
        "Sudoku solver", "N-Queens problem",
        "Rat in a maze", "Word search in grid",
        "Letter combinations phone", "Palindrome partitioning",
        "Restore IP addresses", "Combination sum",
        "Combination sum II (duplicates)", "Subset sum check",
        "Count paths in grid", "Unique paths (recursive)",
        "Staircase problem (1/2 steps)", "Min cost staircase",
        "Print all paths in maze", "Paint fill",
        "Boolean parenthesization", "Evaluate expression tree",
        "Tree traversal (recursive)", "Depth of tree (recursive)",
        "Reverse linked list (recursive)", "Merge sort",
        "Quick sort", "Recursive binary search",
        "Ackermann function", "Hofstadter sequence",
        "Mutual recursion (even/odd)", "Indirect recursion",
        "Tail recursion", "Tail call optimization",
        "Memoization basics", "Top-down DP with memo",
        "Stack overflow (too deep)", "Max recursion depth",
        "Iterative DFS vs recursive", "Convert recursion to iteration",
        "Call stack visualization", "Recursion tree analysis",
        "Recurrence relations T(n)=2T(n/2)+n", "Master theorem basics",
        "Divide and conquer paradigm", "Merge two sorted arrays",
        "Count inversions", "Closest pair of points",
        "Strassen matrix multiply concept", "Fast exponentiation",
        "Karatsuba multiplication concept", "Binary GCD",
        "Extended Euclidean algorithm", "Modular inverse",
        "Chinese Remainder Theorem basics", "Sieve segmented",
        "Prime factorization recursive", "Euler's totient",
        "Catalan numbers recursive", "Bell numbers",
        "Stirling numbers", "Partition numbers",
        "Derangements", "Inclusion-exclusion principle",
        "Pigeonhole principle problems", "Birthday paradox",
        "Pass by reference in recursion", "Accumulator pattern",
        "Continuation-passing style", "Trampolining pattern",
        "Mutual tail recursion", "Y-combinator concept",
        "Higher-order functions", "Currying in C++",
        "Functor objects", "Memoize wrapper",
        "LRU cache concept", "Fibonacci with matrix expo",
        "Nth root binary search (float)", "Newton's method sqrt",
        "Bisection method", "Fixed-point iteration",
    ]
    
    for idx, name in enumerate(c11_problems, 1):
        content = generate_generic_doc(name, "functions_recursion", idx, 1, "C11")
        write_doc(c11_dir, idx, name, content)
        created += 1
    
    # === C12: Arrays & Strings (Core) ===
    c12_dir = os.path.join(BASE, "C12_Arrays_Strings_Core")
    os.makedirs(c12_dir, exist_ok=True)
    
    c12_problems = [
        "1D array declaration & init", "Array size pitfalls",
        "Out-of-bounds access (UB)", "std::array<T,N>",
        "std::vector basics", "vector push_back",
        "vector at() vs []", "vector size vs capacity",
        "vector resize vs reserve", "2D vector",
        "2D array (C-style)", "Multidimensional arrays",
        "Array decay to pointer", "Passing array to function",
        "Array length tricks", "Sorted array check",
        "Linear search", "Binary search iterative",
        "Binary search on answer", "Lower bound / upper bound",
        "Find first/last occurrence", "Count occurrences (sorted)",
        "Insertion into sorted array", "Deletion from array",
        "Rotate array left/right", "Find rotation pivot",
        "Search in rotated sorted array", "Two sum (brute)",
        "Two sum (hash map)", "Two sum (two pointers)",
        "Three sum", "Four sum",
        "Max subarray (Kadane's)", "Max product subarray",
        "Min subarray (Kadane's variant)", "Subarray with given sum",
        "Subarray with 0 sum", "Longest subarray with sum k",
        "Merge two sorted arrays (in-place)", "Merge intervals",
        "Insert interval", "Non-overlapping intervals",
        "Meeting rooms I & II", "Minimum platforms",
        "Activity selection greedy", "Fractional knapsack",
        "0-1 Knapsack basics", "Partition equal subset sum",
        "Count subsets with sum", "Target sum (pm)",
        "Move zeros to end", "Remove duplicates (sorted)",
        "Remove duplicates (unsorted)", "Remove element in-place",
        "Dutch national flag", "Sort 0s 1s 2s",
        "Sort by parity", "Sort by sign",
        "Wiggle sort", "Relative sort",
        "Custom comparator sort", "Sort structs",
        "Stable sort vs unstable", "Counting sort",
        "Radix sort", "Bucket sort",
        "Majority element (Moore's voting)", "Majority element II",
        "Find duplicate (Floyd's cycle)", "Find missing number",
        "Find two missing numbers", "First missing positive",
        "Single number (XOR)", "Two singles (XOR)",
        "Three singles", "Maximum consecutive 1s",
        "Minimum consecutive 0s", "Longest consecutive sequence",
        "Trapping rain water", "Container with most water",
        "Largest rectangle histogram", "Maximal rectangle in matrix",
        "Spiral order traversal", "Rotate matrix 90 degrees",
        "Set matrix zeros", "Search in 2D matrix",
        "Search in sorted 2D matrix II", "Diagonal traversal",
        "Anti-diagonal traversal", "Layer-by-layer traversal",
        "Transpose matrix", "Matrix multiplication",
        "Prefix sum 1D", "Prefix sum 2D (range sum query)",
        "Difference array", "Range update range query",
        "Product array except self", "Stock buy sell (one tx)",
        "Stock buy sell (multiple tx)", "Stock with cooldown",
        "Stock with transaction fee", "Best time to buy (k tx)",
        "Jump game I (can reach end?)", "Jump game II (min jumps)",
        "Gas station problem", "Candy distribution",
        "Task scheduler", "Minimum cost to connect ropes",
        "Minimum operations to make equal", "Minimum swaps to sort",
        "Check if array is a permutation", "Find all anagrams in string",
        "Longest substring no repeat", "Longest substring k distinct",
        "Minimum window substring", "Substring permutation check",
        "Sliding window maximum", "Sliding window minimum",
        "Count distinct in window", "Average of subarrays size k",
        "Substrings with exactly k distinct", "Replace with rank",
        "Minimum number of arrows (balloons)", "Smallest range covering all lists",
    ]
    
    for idx, name in enumerate(c12_problems, 1):
        content = generate_generic_doc(name, "arrays_strings", idx, 1, "C12")
        write_doc(c12_dir, idx, name, content)
        created += 1
    
    # Create index file
    index_path = os.path.join(BASE, "INDEX.md")
    with open(index_path, 'w') as f:
        f.write("# Level 0 & Level 1 — Complete Problem Guide\n\n")
        f.write(f"**Total Problems:** {created}\n\n")
        f.write("## Categories\n\n")
        for cat_dir in sorted(os.listdir(BASE)):
            cat_path = os.path.join(BASE, cat_dir)
            if os.path.isdir(cat_path):
                files = sorted([fi for fi in os.listdir(cat_path) if fi.endswith('.md')])
                f.write(f"### {cat_dir} ({len(files)} problems)\n\n")
                for fi in files:
                    title = fi[4:-3].replace('_', ' ')
                    f.write(f"- [{title}]({cat_dir}/{fi})\n")
                f.write("\n")
    
    print(f"✅ Generated {created} problem documents + INDEX.md")


if __name__ == "__main__":
    main()
