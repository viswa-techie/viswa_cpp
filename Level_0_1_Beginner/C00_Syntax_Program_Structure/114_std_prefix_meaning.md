# std:: prefix meaning

> **Level:** 0 — Absolute Beginner  
> **Category:** C00 — C++ Syntax & Program Structure  
> **Topic:** syntax

---

## Problem Statement
Understand what `std::` means and why it appears everywhere in C++ code.

## What You Need to Know
- `std` is the namespace containing the entire C++ Standard Library.
- `std::` is the scope resolution operator telling the compiler "look in the std namespace."
- `cout`, `string`, `vector`, `sort` — all live in `std`.

## What's in std?
```cpp
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>

int main() {
    // All of these are in the std namespace:
    std::cout << "Hello\n";                    // I/O
    std::string name = "Viswa";                // Strings
    std::vector<int> nums = {3, 1, 4};         // Containers
    std::sort(nums.begin(), nums.end());       // Algorithms
    std::map<std::string, int> m;              // Containers

    return 0;
}
```

## Without std::
```cpp
#include <iostream>
using namespace std;   // Import everything from std

int main() {
    cout << "Hello\n";        // No std:: needed
    string name = "Viswa";    // No std:: needed
    return 0;
}
```

## Why Use std:: Explicitly?
```cpp
// Scenario: name collision
#include <iostream>
#include <algorithm>

// Your own sort function
void sort(int* arr, int n) {
    // custom implementation
}

int main() {
    int data[] = {3, 1, 4};

    sort(data, 3);           // Calls YOUR sort
    std::sort(data, data+3); // Calls STANDARD sort

    // With "using namespace std;" — which sort is called?
    // Ambiguous! Compile error or wrong function called.
    return 0;
}
```

## Best Practice
```
Context                  Recommendation
-------                  --------------
Header files (.h)        Always use std::
Source files (.cpp)       Prefer std::, or "using" for specific names
Quick prototypes         "using namespace std;" is OK
Production code          Always use std::
Competitive programming  "using namespace std;" is fine
```

## Key Takeaways
1. `std::` means "from the standard library namespace"
2. It prevents name collisions with your own code
3. Always use `std::` in headers — never `using namespace std;`
4. Using specific imports is OK: `using std::cout; using std::endl;`
5. Every standard library symbol lives in `std`

## Common Mistakes
- Forgetting `std::` without `using namespace std;` → compile error
- `using namespace std;` in headers → pollutes everyone's namespace
- Not realizing `cout`, `string`, `vector` are all `std::` prefixed
