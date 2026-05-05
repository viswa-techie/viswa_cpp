# scanf vs cin

> **Level:** 0 — Absolute Beginner  
> **Category:** C00 — C++ Syntax & Program Structure  
> **Topic:** syntax

---

## Problem Statement
Compare C-style `scanf` with C++ `cin` for reading input.

## What You Need to Know
- `scanf` uses format strings to parse input (from C).
- `cin` uses `>>` stream extraction (C++).
- `cin` is type-safe; `scanf` is not.

## Side-by-Side Comparison
```cpp
#include <iostream>
#include <cstdio>

int main() {
    int age;
    double salary;

    // scanf style
    printf("Enter age and salary: ");
    scanf("%d %lf", &age, &salary);   // Note: & required for scanf
    printf("Age: %d, Salary: %.2f\n", age, salary);

    // cin style
    std::cout << "Enter age and salary: ";
    std::cin >> age >> salary;          // No & needed
    std::cout << "Age: " << age << ", Salary: " << salary << "\n";

    return 0;
}
```

## Key Differences
```
Feature          scanf                cin
-------          -----                ---
Header           <cstdio>             <iostream>
Syntax           scanf("%d", &x)      cin >> x
Address-of (&)   Required             Not needed
Type safety      No                   Yes
String input     char buf[100];       std::string s;
                 scanf("%s", buf);    cin >> s;
Buffer overflow  Possible             Not possible with std::string
Error handling   Returns count        Sets stream state flags
```

## Reading Strings
```cpp
#include <iostream>
#include <cstdio>
#include <string>

int main() {
    // scanf: buffer overflow risk!
    char name[50];
    scanf("%49s", name);  // Must limit length manually

    // cin: safe with std::string
    std::string safe_name;
    std::cin >> safe_name;  // No buffer overflow possible

    return 0;
}
```

## Error Checking
```cpp
#include <iostream>

int main() {
    int x;
    std::cout << "Enter a number: ";

    if (std::cin >> x) {
        std::cout << "Got: " << x << "\n";
    } else {
        std::cout << "Invalid input!\n";
        std::cin.clear();
        std::cin.ignore(10000, '\n');
    }

    return 0;
}
```

## Key Takeaways
1. `cin` is safer — no `&` needed, no buffer overflow with `std::string`
2. `scanf` requires exact format specifiers and `&` for variables
3. `scanf` returns number of items read; `cin` sets fail flags
4. Prefer `cin` in C++ for type safety and simplicity
5. Both skip leading whitespace by default

## Common Mistakes
- Forgetting `&` in `scanf`: `scanf("%d", x)` → crash
- Using `%f` for `double` in `scanf` — need `%lf` for double
- Buffer overflow with `scanf("%s", buf)` on long input
