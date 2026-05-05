# Level 2 — Intermediate: Pointers, Memory & Object-Oriented Programming

> **Directory:** `Level_2_3_Intermediate/`  
> **Categories:** `C20_Pointers_Memory` · `C21_OOP_Classes`  
> **Total Files:** 125 + 120 = **245 files**  
> **Prerequisite:** Level 1 (Control Flow, Functions, Arrays)  
> **Leads to:** Level 3 (STL, Linked Lists, Hashing)

---

## Overview

Level 2 is the most conceptually dense beginner-to-intermediate transition. Pointers unlock direct memory manipulation — mandatory for embedded, systems, and performance work. OOP teaches you to model real-world entities as self-contained objects with invariants. Together they form the complete C++ object model.

---

## C20 — Pointers & Memory (125 files)

### What is Covered

| Range | Topics |
|-------|--------|
| 001–010 | Pointer declaration, address-of `&`, dereference `*`, null pointer / `nullptr`, pointer arithmetic, pointer to array |
| 011–020 | Array name as pointer, pointer-to-pointer (`**`), pointer to function, `const T*` / `T* const` / `const T* const` variants |
| 021–030 | `void*` pointer, pointer casting, dangling pointer, wild pointer, pointer aliasing, `restrict` keyword |
| 031–040 | Pointer comparison, pointer subtraction, pointer to struct member, arrow operator `->` |
| 041–050 | `new` / `delete`, `new[]` / `delete[]`; placement `new`; stack vs heap allocation; RAII intro |
| 051–060 | `unique_ptr<T>`: ownership, `make_unique`, `move()`, custom deleters; cannot copy `unique_ptr` |
| 061–070 | `shared_ptr<T>`: reference counting, `make_shared`, `weak_ptr`, cyclic reference problem |
| 071–080 | `weak_ptr`: `lock()`, `expired()`, breaking cycles; custom deleters; `enable_shared_from_this` |
| 081–090 | `std::allocator<T>`, custom allocators, pool allocator pattern, arena allocator |
| 091–100 | `std::mem_fn`, pointer-to-member function (`T::*`), `std::invoke`; type-erased callable |
| 101–110 | Pimpl idiom, opaque pointer, hidden implementation, ABI stability, forward declaration for pimpl, `unique_ptr` in pimpl |
| 111–125 | Memory model basics, sequenced-before, observable side effects, sequence points; UB catalog; sanitiser workflows (ASan, MSan, LSan, UBSan); Valgrind memcheck/massif; cache-friendly access, false sharing, SoA vs AoS |

### Key Concepts Learned
- Stack memory is automatically managed (LIFO, fixed size); heap needs explicit `new`/`delete`
- Dangling pointer → reading freed memory → UB (program may appear to work)
- Smart pointers implement RAII — destructor automatically calls `delete`
- `unique_ptr` = sole owner; `shared_ptr` = shared ownership; `weak_ptr` = non-owning observer
- False sharing: two threads writing adjacent cache lines cause cache coherency traffic
- Valgrind/ASan catch memory bugs that don't immediately crash

### Patterns Introduced
- **RAII** — Resource Acquisition Is Initialisation (constructor acquires, destructor releases)
- **Pimpl** — pointer-to-implementation for ABI stability
- **Owner / Observer split** — `shared_ptr` owner + `weak_ptr` observer
- **Arena / Pool allocator** — batch-allocate, batch-free for performance

### Cross-Links
- Pointer-to-function (C20) ↔ callbacks / `std::function` (C11)
- Smart pointers (C20) ↔ class destructors / rule-of-five (C21)
- Memory model / atomics (C20) ↔ Concurrency (Level 7, C71)
- Cache line / false sharing (C20) ↔ Lock-free data structures (C71)

---

## C21 — OOP & Classes (120 files)

### What is Covered

| Range | Topics |
|-------|--------|
| 001–015 | `class` vs `struct` (access default), member variables, member functions, `this` pointer, access specifiers (`public/protected/private`), encapsulation, getters/setters, `const` member functions, `mutable`, `static` members, `friend` functions/classes, nested classes, local classes |
| 016–030 | Constructors: default, parameterised, copy, move, delegating, converting; `explicit` keyword; initialiser list order |
| 031–045 | Destructor, Rule of 3, Rule of 5, Rule of 0; copy semantics vs move semantics; `= delete` / `= default` |
| 046–060 | Operator overloading: `+`, `-`, `*`, `/`, `==`, `<`, `<<`, `>>`, `[]`, `()`, `->`, `++`/`--`, conversion operators |
| 061–075 | Inheritance: single, multiple, diamond problem, virtual inheritance; `public/protected/private` inheritance |
| 076–090 | Virtual functions, vtable, pure virtual, abstract class, override, final; virtual destructor necessity |
| 091–100 | CRTP (Curiously Recurring Template Pattern), static polymorphism, mixin pattern |
| 101–110 | Memory layout: padding, Empty Base Optimisation, `[[no_unique_address]]`; class templates, member templates |
| 111–120 | Template specialisation, partial specialisation, variable templates, concepts in class, `if constexpr` in methods, `static_assert`; serialisation (JSON/binary); comparison operators (`<=>` spaceship, total order); custom hash; class in `unordered_map`/`std::set`; Pimpl in class design; ABI-stable class design |

### Key Concepts Learned
- `class` and `struct` are identical except default access (`private` vs `public`)
- Initialiser list initialises — assignment body re-assigns; initialiser list is always preferred
- Copy constructor deep-copies; if you manage raw memory, you must write it yourself (Rule of 3/5)
- Move semantics: steal resources from rvalue, leave it in valid-but-unspecified state
- `virtual` dispatch works via vtable pointer added to each object; costs one indirection
- Abstract base class with pure virtual = interface definition
- CRTP enables zero-cost static polymorphism (no vtable)

### Patterns Introduced
- **Rule of 0 / 3 / 5** — choose one, be consistent
- **Abstract Factory / Strategy via virtual** — OOP design patterns
- **CRTP Static Polymorphism** — compile-time dispatch without vtable
- **Operator Overloading** — make user-defined types behave like built-ins
- **Spaceship Operator (`<=>`)** — auto-generates all comparison operators (C++20)

### Cross-Links
- Destructors / RAII (C21) ↔ Smart pointers (C20)
- `shared_ptr` with custom deleter (C20) ↔ Pimpl in class design (C21)
- Virtual functions (C21) ↔ Type erasure / `std::any` / `std::function` (advanced, Level 7)
- Class templates (C21) ↔ Full templates chapter (Level 7, C70)

---

## Level 2 — Revision Checklist

### Pointers & Memory
- [ ] Draw memory layout for `int x = 5; int* p = &x;`
- [ ] Explain difference: `delete` vs `delete[]`
- [ ] Convert a raw-pointer class to use `unique_ptr` (no manual `delete`)
- [ ] Identify why `weak_ptr` breaks reference cycles
- [ ] Detect a use-after-free bug using ASan flags
- [ ] Explain false sharing and how to fix it with padding or `alignas`

### OOP & Classes
- [ ] Write a class with proper Rule-of-5 (copy ctor, copy assign, move ctor, move assign, dtor)
- [ ] Implement operator `<<` for a custom class
- [ ] Explain why virtual destructor is mandatory in polymorphic base classes
- [ ] Implement CRTP-based mixin for reusable `print()` method
- [ ] Use `override` and `final` correctly; explain what `final` does to vtable optimisation

## Common Mistakes at Level 2

| Mistake | Correct Approach |
|---------|-----------------|
| `delete` on stack memory | Only `delete` heap-allocated (`new`) memory |
| Forgetting `virtual` destructor | Always add `virtual ~Base() = default;` |
| Self-assignment in copy operator | Check `if (this != &rhs)` first |
| Initialiser list order vs declaration order | Initialise in declaration order, not list order |
| `shared_ptr` cycles causing memory leaks | Use `weak_ptr` for back/observer references |
| Overloading `operator=` without copy-and-swap | Use copy-and-swap idiom for exception safety |

## Interview Focus (Level 2 Topics)

| Topic | Common Question |
|-------|----------------|
| Smart Pointers | "When to use `unique_ptr` vs `shared_ptr`?" |
| Rule of 5 | "What breaks if you only define a copy constructor?" |
| Virtual Functions | "How does vtable work? What is the cost?" |
| RAII | "How does RAII prevent resource leaks?" |
| Move Semantics | "What is `std::move`? Does it actually move anything?" |
| Memory Leaks | "How do you detect and fix a memory leak?" |
