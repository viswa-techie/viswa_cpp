# Keywords list & usage

> **Level:** 0 — Absolute Beginner  
> **Category:** C00 — C++ Syntax & Program Structure  
> **Topic:** syntax

---

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



Additional Resources:
Here’s a **clean, well‑organized categorization of the C++ keywords and related items** you listed, corrected and grouped for clarity. This matches **modern C++ (up to C++23)** usage.

***

## ✅ **1. Fundamental Types**

```cpp
bool        char        char8_t     char16_t    char32_t
wchar_t    short       int          long
float      double      void
signed     unsigned
```

***

## ✅ **2. Type Modifiers & Qualifiers**

```cpp
const          volatile       mutable
static         extern         register
thread_local  inline
```

***

## ✅ **3. Object Lifetime & Memory Management**

```cpp
new        delete
```

***

## ✅ **4. Control Flow Statements**

```cpp
if          else        switch      case       default
for         while       do
break       continue    goto
return
```

***

## ✅ **5. Functions & Function Specifiers**

```cpp
auto        noexcept    throw
constexpr  consteval   constinit
decltype
```

***

## ✅ **6. Classes, Structs & OOP**

```cpp
class       struct      union
public      private     protected
virtual     this
friend
explicit
```

***

## ✅ **7. Templates & Generic Programming**

```cpp
template
typename
concept
requires
export        // (rare, reintroduced with modules)
```

***

## ✅ **8. Casting Operators**

```cpp
static_cast
dynamic_cast
const_cast
reinterpret_cast
```

***

## ✅ **9. Operators (Symbolic & Alternative Tokens)**

### Logical / Bitwise (alternative spellings)

```cpp
and        or         not
bitand    bitor      compl
xor
```

### Assignment versions

```cpp
and_eq    or_eq      xor_eq      not_eq
```

***

## ✅ **10. Namespaces & Type Aliases**

```cpp
namespace
using
typedef
```

***

## ✅ **11. Exception Handling**

```cpp
try
catch
```

***

## ✅ **12. Enums & Type Information**

```cpp
enum
typeid
sizeof
```

***

## ✅ **13. Boolean & Null Values**

```cpp
true
false
nullptr
```

***

## ✅ **14. Coroutines (C++20+)**

```cpp
co_await
co_yield
co_return
```

***

## ✅ **15. Low‑Level / Special Purpose**

```cpp
asm
operator
```

***

## ✅ **16. Miscellaneous / Rarely Used**

```cpp
default
delete
```

***

### ✅ **Summary**

*   ✅ This list now correctly reflects **standard C++ keywords**
*   ✅ Categories match **practical learning paths**
*   ✅ Especially useful for **interview prep, compilers, or language reference**

If you want:

*   a **printable PDF**
*   a **keyword cheat‑sheet**
*   a **C++ learning roadmap based on these categories**
*   or **examples for each keyword**

Just tell me 👍
