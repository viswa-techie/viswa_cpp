# Chapter: Partial specialization

> **Level:** 2 | **Category:** C21 — OOP — Classes & Objects

---

## 1. Problem Statement
Master the topic: **Partial specialization**.

**Examples:**
- **Normal case:** typical input demonstrating the concept.
- **Edge case:** empty / null / boundary input.
- **Large case:** stress test with N up to 10^5 or 10^6.

**Constraints:** Time O(n) or O(n log n) typical; Space O(1) or O(n).

---

## 2. Prerequisites
- C++17 syntax, references, pointers basics
- Class basics, constructors
- Big-O analysis fundamentals

---

## 3. Core Concept Deep Dive
This problem exercises **Partial specialization** — a core concept in OOP — Classes & Objects.

**Internal mechanics:** Each polymorphic class has a vptr to its vtable. Non-virtual calls are static dispatch.

**Common misconception:** Calling virtual functions from constructors does NOT dispatch dynamically.

---

## 4. Mental Model & Intuition
Think of **Partial specialization** as a blueprint (class) producing instances (objects) sharing behavior via a vtable.

```
ASCII state diagram:
Before: [ initial state ]
   |
   v  (apply operation)
After:  [ result state ]
```

**Pattern category:** OOP / Polymorphism

---

## 5. Solution Approaches

### Approach 1: Brute Force / Naive
```cpp
#include <iostream>
#include <vector>
#include <string>
// Brute-force template for: Partial specialization
int solve_partial_specialization(std::vector<int> v) {
    int result = 0;
    for (size_t i = 0; i < v.size(); ++i)
        for (size_t j = i; j < v.size(); ++j)
            result = std::max(result, v[i] + v[j]);
    return result;
}
int main() {
    std::vector<int> v = {1,2,3,4,5};
    std::cout << solve_partial_specialization(v) << "\n";
}
```
**Time:** O(n²)  
**Space:** O(1)  
**Bottleneck:** redundant work / extra memory traversals.

### Approach 2: Optimized
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
// Optimized one-pass template for: Partial specialization
int solve_partial_specialization(const std::vector<int>& v) {
    if (v.empty()) return 0;
    int best = v[0], acc = v[0];
    for (size_t i = 1; i < v.size(); ++i) {
        acc = std::max(v[i], acc + v[i]);
        best = std::max(best, acc);
    }
    return best;
}
int main() {
    std::vector<int> v = {-2,1,-3,4,-1,2,1,-5,4};
    std::cout << solve_partial_specialization(v) << "\n";  // 6 (Kadane)
}
```
**Time:** O(n)  
**Space:** O(n)  
**Insight:** eliminate redundancy via cached lookup.

### Approach 3: STL / Idiomatic C++
```cpp
#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>
// STL idiomatic template for: Partial specialization
int main() {
    std::vector<int> v = {1,2,3,4,5};
    int sum = std::accumulate(v.begin(), v.end(), 0);
    auto mx = *std::max_element(v.begin(), v.end());
    std::cout << "sum=" << sum << " max=" << mx << "\n";
}
```
**Production preference:** STL version — well-tested, optimized, expressive.  
**Interview preference:** the manual optimal version — proves you understand the algorithm.



---

## 6. Dry Run / Step-by-Step Trace

| Step | State | Key Variables | Action |
|------|-------|---------------|--------|
| 1 | initial | inputs loaded | parse / read |
| 2 | processing | i=0, acc=0 | first iteration |
| 3 | processing | i=1, acc updated | second iteration |
| 4 | processing | i=k, partial result | mid-state |
| 5 | near-end | i=n-1 | last element |
| 6 | terminal | result computed | return |

---

## 7. Complexity Analysis
- **Time (best/avg/worst):** O(n) / O(n) / O(n)
- **Space:** stack O(1), heap O(n)
- **Amortized:** vector push_back O(1) amortized due to geometric resizing.
- **Cache behavior:** vtable lookup adds 1 cache miss

---

## 8. Common Mistakes at Level 2
1. **Memory leak** — forgetting `delete` for `new`-allocated objects.
2. **Dangling pointer** — pointer to freed/out-of-scope memory.
3. **Iterator invalidation** — modifying container while iterating.
4. **Off-by-one** — `<` vs `<=` in loop conditions.
5. **Null dereference** — not checking `if (ptr)` before `*ptr`.
6. **Slicing** — assigning derived to base by value loses the derived part.
7. **Wrong container** — using `std::list` when `std::vector` would be cache-friendlier.

---

## 9. What a Senior Engineer Would Do Differently
- **Code review:** prefer smart pointers over raw `new/delete`; mark single-arg constructors `explicit`; use `const` aggressively.
- **Production vs interview:** production adds error handling, logging, edge-case validation, and unit tests; interview focuses on correctness + complexity.
- **Tests:** empty input, single element, max size, duplicates, negatives, overflow.
- **Defense:** `[[nodiscard]]` on functions returning resources; `noexcept` where applicable.

---

## 10. C++ Internals — Under the Hood
Virtual call: load vptr from object, index vtable, indirect call. Adds 1 cache miss + indirect branch (predictable if hot). EBO can hide empty bases.

---

## 11. Pattern Recognition & Generalizations
- **Formal name:** OOP / Polymorphism
- **Similar problems:** see other entries in this category.
- **When you see** _shared interface across types_, **think** _virtual + override_.
- **Harder variants:** add concurrency, streaming input, or dynamic updates.

---

## 12. Practice Variants
- **Easy:** smaller N, no edge cases.
- **Medium:** add a constraint (in-place, O(1) extra space).
- **Hard:** combine with another structure (e.g., LRU = hash + DLL).

---

## 13. Interview Corner
- **Frequency:** Common at FAANG; appears in automotive/embedded for memory & data-structure roles.
- **Expected complexity:** O(n).
- **Follow-ups:** "What if the input doesn't fit in memory?" "How do you parallelize?" "What about thread safety?"
- **Strong vs weak answer:** strong = states approach, complexity, edge cases BEFORE coding; weak = jumps straight to code.

---

## 14. Quick Reference Card
- **Core idea:** Partial specialization — model real-world entities with state + behavior.
- **Complexity:** O(n) time, O(n) space.
- **Don't forget:** (1) null-check pointers, (2) free what you allocate, (3) handle empty input, (4) consider iterator invalidation.

---
*Compile:* `g++ -std=c++17 -Wall -Wextra -fsanitize=address main.cpp -o sol`
