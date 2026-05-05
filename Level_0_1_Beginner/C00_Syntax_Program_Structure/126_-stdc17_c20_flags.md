# -std=c++17 / c++20 flags

> **Level:** 0 — Absolute Beginner  
> **Category:** C00 — C++ Syntax & Program Structure  
> **Topic:** syntax

---

## Problem Statement
Select the C++ standard version to compile against.

## What You Need to Know
- C++ has multiple standards: C++11, C++14, C++17, C++20, C++23.
- Each adds new features.
- Use `-std=c++XX` to select which standard to compile with.

## Selecting a Standard
```bash
g++ -std=c++11 main.cpp -o main    # C++11
g++ -std=c++14 main.cpp -o main    # C++14
g++ -std=c++17 main.cpp -o main    # C++17 (recommended for learning)
g++ -std=c++20 main.cpp -o main    # C++20
g++ -std=c++23 main.cpp -o main    # C++23
```

## Key Features by Standard
```
C++11 (2011) — The "Modern C++" revolution:
  auto, range-for, lambdas, nullptr, enum class,
  move semantics, smart pointers, constexpr, threads

C++14 (2014) — Refinements:
  Generic lambdas, return type deduction,
  std::make_unique, relaxed constexpr

C++17 (2017) — Quality of life:
  Structured bindings, if constexpr, std::optional,
  std::variant, std::string_view, nested namespaces,
  filesystem library

C++20 (2020) — Major additions:
  Concepts, ranges, coroutines, modules,
  std::format, calendar/timezone, three-way comparison

C++23 (2023) — Latest:
  std::print, deducing this, std::expected,
  flat_map, improved ranges
```

## Check Which Standard Features Work
```cpp
// This requires C++17
#include <iostream>
#include <optional>

int main() {
    std::optional<int> value = 42;
    if (value) {
        std::cout << *value << "\n";
    }
    return 0;
}
```

```bash
g++ -std=c++14 optional.cpp   # ERROR — optional not available
g++ -std=c++17 optional.cpp   # OK — optional is C++17
```

## Checking Default Standard
```bash
# See what your compiler defaults to
g++ -dM -E -x c++ /dev/null | grep cplusplus
# __cplusplus 201703L  (means C++17)
```

## Key Takeaways
1. `-std=c++17` is the recommended standard for learning (2024)
2. Each standard adds features — code may not compile with older standards
3. Always specify the standard explicitly in your build system
4. GCC/Clang default standard varies by version
5. `__cplusplus` macro tells you which standard is active

## Common Mistakes
- Not specifying `-std=` → getting an old default
- Using C++20 features with `-std=c++17` → compile error
- Assuming all compilers support the latest standard
