# using namespace std risks

> **Level:** 0 — Absolute Beginner  
> **Category:** C00 — C++ Syntax & Program Structure  
> **Topic:** syntax

---

## Problem Statement
Understand why `using namespace std;` is considered bad practice in production code.

## What You Need to Know
- `using namespace std;` dumps ALL names from `std` into the global scope.
- This can cause name collisions — especially as the standard library grows.
- It's particularly dangerous in header files.

## The Problem: Name Collisions
```cpp
#include <iostream>
#include <algorithm>
using namespace std;

// Your own function named 'count'
int count(int arr[], int n) {
    int total = 0;
    for (int i = 0; i < n; ++i) total += arr[i];
    return total;
}

int main() {
    int data[] = {1, 2, 3};
    // Which count? std::count or yours?
    // Ambiguous call — compile error or wrong function!
    cout << count(data, 3) << "\n";
    return 0;
}
```

## In Headers: Even Worse
```cpp
// utils.h
#pragma once
#include <string>
using namespace std;   // BAD! Everyone who includes this gets it

// Now EVERY file that includes utils.h has std:: polluted
// They can't opt out!
```

## Safe Alternatives
```cpp
#include <iostream>
#include <string>
#include <vector>

// Option 1: Always use std:: (recommended)
int main() {
    std::cout << "Hello\n";
    std::string name = "Viswa";
    return 0;
}

// Option 2: Import specific names only
using std::cout;
using std::string;
using std::vector;

int main() {
    cout << "Hello\n";       // OK
    string name = "Viswa";   // OK
    // sort still needs std::sort
    return 0;
}

// Option 3: using inside a function (limited scope)
int main() {
    using namespace std;   // Only affects this function
    cout << "Hello\n";
    return 0;
}
```

## Risk Summary
```
Location                 Risk Level    Recommendation
--------                 ----------    --------------
Header file              CRITICAL      Never use
Source file (global)      HIGH          Avoid
Source file (function)    LOW           Acceptable for small programs
Competitive programming  NONE          Fine — no maintenance concerns
```

## Key Takeaways
1. `using namespace std;` in headers affects ALL users of that header
2. Name collisions can cause hard-to-debug errors
3. The `std` namespace has hundreds of names — any could clash
4. Use `std::` prefix or import specific names with `using std::cout;`
5. Acceptable ONLY in small, isolated source files or competitive programming

## Common Mistakes
- Using it in headers → forces pollution on every includer
- "It works now" → breaks when upgrading compiler or adding includes
- Not realizing how many names are in `std` (count, find, sort, distance, size, ...)
