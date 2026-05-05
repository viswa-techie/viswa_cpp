# Level 0 — Beginner: Syntax, Program Structure & Data Types

> **Directory:** `Level_0_1_Beginner/`  
> **Categories:** `C00_Syntax_Program_Structure` · `C01_Data_Types_Variables`  
> **Total Files:** 130 + 116 = **246 files**  
> **Prerequisite:** None — absolute start  
> **Leads to:** Level 1 (Control Flow, Functions, Arrays)

---

## Overview

Level 0 establishes the bedrock of every C++ program. You learn to write, compile, and understand any syntactically valid C++ file before touching algorithms. Every concept in Levels 1–10 assumes mastery of these fundamentals.

---

## C00 — Syntax & Program Structure (130 files)

### What is Covered

| Range | Topics |
|-------|--------|
| 001–010 | `main()`, `#include`, `std::cout/cin`, `endl` vs `\n`, comments, `return 0`, whitespace rules, first Hello-World |
| 011–020 | Integer literals, float literals, string literals, char literals, bool literals, binary/octal/hex notation, `auto` type deduction intro |
| 021–030 | Operators: arithmetic, relational, logical, bitwise, assignment, compound assignment, ternary, comma, precedence & associativity |
| 031–040 | Expressions vs statements, lvalue vs rvalue, sequence points, undefined behaviour (UB) intro, side effects |
| 041–050 | `#include` mechanics, header guards (`#ifndef`/`#pragma once`), forward declarations, `.h` vs `.hpp`, include order |
| 051–060 | Preprocessor: `#define`, `#undef`, `#if`/`#ifdef`/`#endif`, `#error`, `#pragma`, token-pasting (`##`), stringification (`#`) |
| 061–070 | Scope: block, function, file, namespace scope; shadowing; RAII first look; `.cin.ignore()` pitfalls |
| 071–080 | Storage classes: `auto`, `register` (deprecated), `static` local, `extern`; linkage: internal vs external |
| 081–090 | `const`, `constexpr`, `consteval`, `constinit`; compile-time vs runtime; `volatile` |
| 091–100 | Type system basics: implicit conversions, integral promotions, usual arithmetic conversions, narrowing, `static_cast` |
| 101–110 | `bool` output/casting, `sizeof`, address-of `&`, dereference `*`, `struct` definition/access/initialization, `enum`, `enum class` |
| 111–120 | `typedef`, `using` alias, namespaces, `std::`, `using namespace` risks, named/anonymous/nested namespaces, ODR, translation units |
| 121–130 | Build systems: Makefile basics, IDE setup, online compilers, `-Wall -Wextra -O0/-O2/-O3`, `-std=c++17/20`, ASan, UBSan, static analysis, `clang-format` |

### Key Concepts Learned
- Anatomy of a C++ translation unit (preprocessor → compiler → linker)
- How the compiler sees your code (tokens, AST)
- Difference between declaration and definition
- Why undefined behaviour is catastrophic (not just "wrong output")
- How to compile with safety flags and use sanitisers from day one

### Cross-Links Inside Level 0
- `#include` guards (C00) ↔ separate compilation / ODR (C00 111-120)
- `const`/`constexpr` (C00 081-090) ↔ `constexpr` variables (C01)
- `struct` basics (C00 101-110) ↔ class/struct in OOP (Level 2, C21)

---

## C01 — Data Types & Variables (116 files)

### What is Covered

| Range | Topics |
|-------|--------|
| 001–010 | `int`, `char`, `float`, `double`, `bool`, `long`, `unsigned`; integer overflow demo; floating-point precision & epsilon |
| 011–020 | Fixed-width types (`int8_t`→`uint64_t`), `<cstdint>`, `size_t`, `ptrdiff_t`; when to use each |
| 021–030 | Casts: `static_cast`, `dynamic_cast`, `reinterpret_cast`, `const_cast`; C-cast dangers; narrowing conversion |
| 031–040 | `std::string` basics: construction, `length()`, concatenation, `substr`, `find`, comparison; `char` arrays vs `std::string` |
| 041–050 | `std::string_view` (read-only window); `std::tuple`, `std::pair`; structured bindings (`auto [a,b] = ...`) |
| 051–060 | `std::optional<T>`, `std::variant<T...>`, `std::any`; null-safety patterns; `std::monostate` |
| 061–070 | Bitfields, unnamed bitfields, `union` and active-member rule; type-punning with `memcpy`; `std::bit_cast` (C++20) |
| 071–080 | Alignment: `alignof`, `alignas`, `std::aligned_storage`; struct padding; `__attribute__((packed))` tradeoffs |
| 081–090 | Initialisation forms: value-init, zero-init, default-init, copy-init, direct-init, aggregate-init, brace-init |
| 091–100 | `const` correctness; `constexpr` variables; `inline` variables; linkage details (`extern`, internal linkage) |
| 101–110 | Type aliases (`using T = …`); `auto` in declarations; `decltype(expr)`, `decltype(auto)`; `std::declval` |
| 111–116 | CTAD (Class Template Argument Deduction); Concepts intro (`requires`); type traits: `is_integral`, `is_same`, `decay_t` |

### Key Concepts Learned
- Why overflow wraps for unsigned but is UB for signed
- When floating-point comparison with `==` is wrong
- How `std::optional` eliminates sentinel values (-1, nullptr)
- Difference between value-initialization and default-initialization
- Type traits as compile-time introspection

### Cross-Links Inside Level 0
- `static_cast` (C01) ↔ explicit cast in operators (C00)
- `std::string` (C01) ↔ string operations in arrays (Level 1, C12)
- Type traits (C01 111-116) ↔ Templates (Level 7, C70)

---

## Level 0 — Revision Checklist

- [ ] Can write, compile and run a multi-file C++ project with Makefile
- [ ] Understand every implicit conversion that happens in `int x = 3.9;`
- [ ] Know difference: `const int*` vs `int* const` vs `const int* const`
- [ ] Can use `constexpr` functions and variables correctly
- [ ] Know when to prefer `std::string_view` over `const std::string&`
- [ ] Can use `std::optional` instead of "magic" return codes
- [ ] Know 5 different initialisation syntaxes and when each fires
- [ ] Can explain what a translation unit is and what the linker does

## Common Mistakes at Level 0

| Mistake | Correct Approach |
|---------|-----------------|
| `using namespace std;` in headers | Never — causes name collisions |
| `float` for money/precise values | Use `double` or `std::decimal` |
| `sizeof(arr)` inside a function | Pointer size — pass size separately or use `std::array` |
| Comparing floats with `==` | Use `std::abs(a - b) < epsilon` |
| Integer overflow on `int` | Use `long long` or detect before operation |
| Including `.cpp` files | Only include headers; link `.cpp` separately |

## Interview Focus (Level 0 Topics)

- Explain integer overflow vs floating-point imprecision
- What is UB and give 3 examples
- `#pragma once` vs include guards — which is better?
- Difference between `constexpr` and `const`
- Why is `std::optional` better than returning `-1`?
