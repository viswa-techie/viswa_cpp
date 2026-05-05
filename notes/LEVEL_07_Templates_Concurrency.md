# Level 7 — Expert: Templates, Generic Programming & Concurrency

> **Directory:** `Level_6_7_Expert/`  
> **Categories:** `C70_Templates_Generic_Programming` · `C71_Concurrency_Multithreading`  
> **Total Files:** 120 + 120 = **240 files**  
> **Prerequisite:** Level 6 (Advanced Trees, Advanced Graphs)  
> **Leads to:** Level 8 (Advanced Algorithms, System Design)

---

## Overview

Level 7 is where you master the unique power of C++: zero-overhead abstractions through templates and safe concurrent programming. Templates let you write code that works for any type at compile time. Concurrency lets you exploit multi-core hardware. Both are mandatory for senior C++ roles.

---

## C70 — Templates & Generic Programming (120 files)

### What is Covered

| Range | Topics |
|-------|--------|
| 001–010 | Function templates, class templates, template type/non-type/template-template parameters; variadic templates; parameter pack expansion; fold expressions (C++17) |
| 011–020 | Template specialisation (full), partial specialisation; SFINAE (Substitution Failure Is Not An Error); `std::enable_if`, `void_t` |
| 021–030 | Concepts (C++20): `requires` expression, named concepts, `concept` keyword, constraining templates; `std::same_as`, `std::integral`, etc. |
| 031–040 | Type traits deep-dive: `is_integral`, `is_floating_point`, `is_class`, `is_trivially_copyable`; `remove_cv`, `decay_t`, `conditional_t`, `void_t` |
| 041–050 | Compile-time computation: `constexpr` functions, `consteval`, template metaprogramming (TMP); compile-time factorial, Fibonacci, prime sieve |
| 051–060 | `std::tuple`: `get<N>`, `tuple_size`, `tuple_element`; tuple iteration with `std::apply`; `std::integer_sequence` |
| 061–070 | Policy-based design (template policies); tag dispatching; CRTP deep-dive; expression templates |
| 071–080 | Template argument deduction (TAD), CTAD (Class Template Argument Deduction, C++17); deduction guides |
| 081–090 | Variadic templates: recursive unpacking, `sizeof...`, heterogeneous containers (type list); `std::variant` visitor |
| 091–100 | Type erasure: `std::any`, `std::function`, virtual-based type erasure, manual type erasure with vtable |
| 101–110 | `std::visit`, overloaded visitor pattern; `std::variant` as discriminated union; monostate |
| 111–120 | Reflection intro (no standard yet): `std::source_location`, `std::type_info`; `if constexpr` chains; coroutines intro (`co_yield`, `co_await`, `co_return`) |

### Key Concepts Learned
- Template instantiation happens at compile time — the compiler generates a new function/class per type
- SFINAE: if template substitution fails, it's not an error — it's just removed from overload set
- Concepts (C++20) replace SFINAE with readable constraints; error messages are far clearer
- `if constexpr` selects branch at compile time — dead branch not compiled (unlike runtime `if`)
- Expression templates avoid temporaries: `a + b + c` builds an expression tree, evaluates in one pass
- Type erasure: hide the concrete type behind a stable interface (how `std::function` works)
- Coroutines are stackless — `co_await` suspends at a specific point without a full stack frame

### Patterns Introduced
- **Policy-based design** — inject behaviour via template parameters
- **Tag dispatch** — select overload based on type property
- **Expression templates** — zero-copy chained operations (used in Eigen, BLAZE)
- **CRTP mixin** — static polymorphism for reusable behaviour
- **Overloaded visitor** — `struct Visitor : F1, F2... { using F1::operator(); ... }`

### Cross-Links
- Concepts (C70) ↔ Type traits (Level 0, C01)
- CRTP (C70) ↔ OOP/CRTP intro (Level 2, C21)
- `std::variant` visitor (C70) ↔ `std::optional/variant` (Level 0, C01)
- Coroutines (C70) ↔ Async I/O in Concurrency (C71)

---

## C71 — Concurrency & Multithreading (120 files)

### What is Covered

| Range | Topics |
|-------|--------|
| 001–010 | `std::thread` creation, `join()`, `detach()`, thread ID, `hardware_concurrency()` |
| 011–020 | `std::mutex`, `lock_guard`, `unique_lock`, `shared_mutex` (C++17); recursive mutex; timed mutex |
| 021–030 | `std::condition_variable`: `wait`, `notify_one`, `notify_all`; spurious wakeups; producer-consumer pattern |
| 031–040 | `std::atomic<T>`: load/store/exchange/CAS; memory orders (`relaxed`, `acquire`, `release`, `acq_rel`, `seq_cst`) |
| 041–050 | Lock-free stack (CAS loop), lock-free queue; ABA problem and solutions (tagged pointers, hazard pointers) |
| 051–060 | `std::future`, `std::promise`, `std::packaged_task`; `std::async` (launch policies: `async` vs `deferred`) |
| 061–070 | Thread pool implementation: task queue + worker threads; work-stealing deque |
| 071–080 | Parallel algorithms: `std::execution::par`, `std::execution::par_unseq`; parallel sort, parallel transform |
| 081–090 | Deadlock: causes, detection, prevention (lock ordering, `std::lock`, `std::scoped_lock`) |
| 091–100 | Read-write lock patterns; seqlock; RCU (Read-Copy-Update) concept; hazard pointers |
| 101–110 | Coroutines deep-dive: `promise_type`, `coroutine_handle`, awaitable type, generator coroutine, async generator |
| 111–120 | Task coroutine type, recursive coroutine, coroutine scheduler implementation, `io_uring` with coroutines |

### Key Concepts Learned
- `std::thread` without `join()`/`detach()` → `std::terminate()` — always join or detach
- `lock_guard` is non-movable (RAII lock for a scope); `unique_lock` is movable (can unlock early)
- Memory order `seq_cst` = strongest (total order across all threads); `relaxed` = weakest (no sync)
- CAS (compare-and-swap) is the atomic primitive for lock-free programming
- ABA problem: CAS succeeds even when value cycled A→B→A; solve with version tags or hazard pointers
- `std::async(std::launch::async, ...)` guarantees a new thread; `deferred` runs lazily in calling thread
- Coroutines: `co_await expr` suspends if `expr.await_ready()` returns false; no heap frame allocation in many implementations

### Patterns Introduced
- **Producer-Consumer** with bounded queue + condition variable
- **Thread pool** — fixed worker threads, shared task queue
- **RAII Lock** — `scoped_lock` for multiple mutexes (deadlock-safe)
- **Double-checked locking** (with `atomic` for correct publication)
- **Fork-join** — parallel work with future/promise
- **Coroutine generator** — `co_yield` values lazily

---

## Level 7 — Revision Checklist

### Templates & Generic Programming
- [ ] Write a variadic `print()` function using fold expressions
- [ ] Implement a `std::tuple` iteration with `std::apply` + `std::index_sequence`
- [ ] Write a Concepts-constrained template that only accepts integral types
- [ ] Implement type erasure for a simple `Drawable` concept (without virtual)
- [ ] Use SFINAE to choose between two implementations based on `is_integral`
- [ ] Implement a CRTP base that adds `print()` to any derived class

### Concurrency
- [ ] Implement producer-consumer with `std::queue` + `std::mutex` + `std::condition_variable`
- [ ] Write a simple lock-free stack using `std::atomic` and CAS
- [ ] Implement a thread pool with 4 workers and a task queue
- [ ] Explain the difference between `memory_order_relaxed` and `memory_order_seq_cst`
- [ ] Write a coroutine generator that yields Fibonacci numbers
- [ ] Detect a deadlock scenario and fix it with `std::scoped_lock`

## Common Mistakes at Level 7

| Mistake | Correct Approach |
|---------|-----------------|
| `thread` without join/detach | Always `join()` in destructor (RAII thread wrapper) |
| `relaxed` order for publish-subscribe | Use `release` (write) + `acquire` (read) pair |
| Using `volatile` for threading | `volatile` is NOT atomic — use `std::atomic<T>` |
| Ignoring spurious wakeups in `condition_variable` | Always use predicate form: `cv.wait(lock, pred)` |
| SFINAE unreadable error messages | Migrate to Concepts (C++20) for clear diagnostics |
| Expression template storing dangling reference | Ensure all temporaries outlive the expression |

## Interview Focus (Level 7 Topics)

| Topic | Question |
|-------|---------|
| Templates | "How does SFINAE work? Show an example." |
| Concepts | "How do Concepts improve over SFINAE?" |
| Atomics | "What is memory_order_acquire and when to use it?" |
| Lock-free | "Explain the ABA problem and how to avoid it." |
| `std::async` | "What is the difference between `async` and `deferred`?" |
| Deadlock | "What are the 4 conditions for deadlock and how to break them?" |
| Coroutines | "How does `co_await` suspend a coroutine?" |
