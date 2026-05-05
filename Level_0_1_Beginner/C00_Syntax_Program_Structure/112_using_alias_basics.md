# using alias basics

> **Level:** 0 — Absolute Beginner  
> **Category:** C00 — C++ Syntax & Program Structure  
> **Topic:** syntax

---

## Problem Statement
Use `using` to create type aliases — the modern C++ alternative to `typedef`.

## What You Need to Know
- `using NewName = ExistingType;` creates a type alias (C++11).
- Clearer syntax than `typedef`, especially for complex types.
- Can be templated (unlike `typedef`).

## Basic using Alias
```cpp
#include <iostream>
#include <string>
#include <vector>

using Integer = int;
using Real = double;
using String = std::string;
using IntVector = std::vector<int>;

int main() {
    Integer x = 42;
    Real pi = 3.14;
    String name = "Viswa";
    IntVector nums = {1, 2, 3};

    std::cout << x << " " << pi << " " << name << "\n";
    return 0;
}
```

## using vs typedef
```cpp
#include <vector>
#include <map>
#include <string>

// typedef syntax (reads right-to-left, can be confusing)
typedef std::vector<int> IntVecT;
typedef int (*FuncPtrT)(int, int);
typedef std::map<std::string, std::vector<int>> ScoreMapT;

// using syntax (reads left-to-right, clearer)
using IntVecU = std::vector<int>;
using FuncPtrU = int(*)(int, int);
using ScoreMapU = std::map<std::string, std::vector<int>>;

// Function pointers are MUCH clearer with using:
// typedef void (*Callback)(int, const std::string&);  // Hard to read
// using Callback = void(*)(int, const std::string&);  // Much clearer
```

## Template Aliases (using-only feature)
```cpp
#include <vector>
#include <map>
#include <string>

// Cannot do this with typedef!
template<typename T>
using Vec = std::vector<T>;

template<typename V>
using StringMap = std::map<std::string, V>;

int main() {
    Vec<int> numbers = {1, 2, 3};
    Vec<double> reals = {1.1, 2.2};
    StringMap<int> ages = {{"Viswa", 30}};
    return 0;
}
```

## Key Takeaways
1. `using Name = Type;` is the modern alternative to `typedef`
2. Reads left-to-right — much clearer for function pointers
3. Supports template aliases — `typedef` cannot do this
4. Prefer `using` over `typedef` in C++11 and later
5. Both create aliases, not new types

## Common Mistakes
- Using `typedef` out of habit when `using` is cleaner
- Forgetting that `using` aliases are C++11 — won't work in older compilers
- Confusing `using` alias with `using namespace` — completely different features
