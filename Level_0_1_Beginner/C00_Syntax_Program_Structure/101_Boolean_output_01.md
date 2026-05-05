# Boolean output (0/1)

> **Level:** 0 — Absolute Beginner  
> **Category:** C00 — C++ Syntax & Program Structure  
> **Topic:** syntax

---

## Problem Statement
Control how boolean values are printed — as `0`/`1` or `true`/`false`.

## Default Output (0/1)
```cpp
#include <iostream>

int main() {
    bool a = true;
    bool b = false;

    // Default: prints 1 and 0
    std::cout << "a = " << a << "\n";   // a = 1
    std::cout << "b = " << b << "\n";   // b = 0
    return 0;
}
```

## Using boolalpha (true/false)
```cpp
#include <iostream>

int main() {
    bool a = true;
    bool b = false;

    std::cout << std::boolalpha;         // Switch to text mode
    std::cout << "a = " << a << "\n";   // a = true
    std::cout << "b = " << b << "\n";   // b = false

    std::cout << std::noboolalpha;       // Switch back to numeric
    std::cout << "a = " << a << "\n";   // a = 1
    return 0;
}
```

## Inline Usage
```cpp
#include <iostream>

int main() {
    int x = 10;
    // boolalpha as inline manipulator
    std::cout << "Is positive: " << std::boolalpha << (x > 0) << "\n";
    // Output: Is positive: true
    return 0;
}
```

## Common Pattern: Print Condition Results
```cpp
#include <iostream>

int main() {
    int score = 85;

    std::cout << std::boolalpha;
    std::cout << "Passing: " << (score >= 60) << "\n";   // true
    std::cout << "Perfect: " << (score == 100) << "\n";  // false
    std::cout << "Score > 80: " << (score > 80) << "\n"; // true
    return 0;
}
```

## Key Takeaways
1. Default: `cout << true` prints `1`, `cout << false` prints `0`
2. `std::boolalpha` makes cout print `true`/`false` as text
3. `std::noboolalpha` switches back to `0`/`1`
4. `boolalpha` is sticky — affects all subsequent bool output
5. Use `boolalpha` for human-readable output

## Common Mistakes
- Expecting `true`/`false` by default — you get `1`/`0`
- Forgetting boolalpha is persistent — it affects all subsequent output
- Printing expressions without parentheses: `cout << x > 5` is parsed as `(cout << x) > 5`
