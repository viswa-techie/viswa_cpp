# Chapter: Largest rectangle in histogram

> **Level:** 3 | **Category:** C31 — Stacks & Queues

---

## 1. Problem Statement
Master the topic: **Largest rectangle in histogram**.

**Examples:**
- **Normal case:** typical input demonstrating the concept.
- **Edge case:** empty / null / boundary input.
- **Large case:** stress test with N up to 10^5 or 10^6.

**Constraints:** Time O(n) or O(n log n) typical; Space O(1) or O(n).

---

## 2. Prerequisites
- C++17 syntax, references, pointers basics
- Stack/queue ADT basics
- Big-O analysis fundamentals

---

## 3. Core Concept Deep Dive
Monotonic increasing stack. For each bar, pop higher bars and compute area.

**Internal mechanics:** Stack/queue are container adaptors over `deque` by default; LIFO/FIFO semantics enforced by interface.

**Common misconception:** `std::stack::pop()` returns void — call `top()` first to read.

---

## 4. Mental Model & Intuition
Think of **Largest rectangle in histogram** as a stack of plates (LIFO) or a coffee-shop queue (FIFO).

```
ASCII state diagram:
Before: [ initial state ]
   |
   v  (apply operation)
After:  [ result state ]
```

**Pattern category:** LIFO/FIFO + Monotonic

---

## 5. Solution Approaches

### Approach 1: Brute Force / Naive
```cpp
#include <vector>
#include <stack>
#include <iostream>
int largest(std::vector<int>& h){
    std::stack<int> st;
    int n = h.size(), best = 0;
    for(int i = 0; i <= n; ++i){
        int cur = (i == n) ? 0 : h[i];
        while(!st.empty() && h[st.top()] > cur){
            int top = st.top(); st.pop();
            int width = st.empty() ? i : i - st.top() - 1;
            best = std::max(best, h[top] * width);
        }
        st.push(i);
    }
    return best;
}
int main(){
    std::vector<int> h={2,1,5,6,2,3};
    std::cout << largest(h) << "\n"; // 10
}
```
**Time:** O(n²)  
**Space:** O(1)  
**Bottleneck:** redundant work / extra memory traversals.

### Approach 2: Optimized
```cpp
// O(n) time, O(n) space — already optimal.
// Each bar pushed and popped at most once.
int main(){return 0;}
```
**Time:** O(n)  
**Space:** O(n)  
**Insight:** eliminate redundancy via monotonic structure.

### Approach 3: STL / Idiomatic C++
```cpp
#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>
// STL idiomatic template for: Largest rectangle in histogram
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
- **Cache behavior:** deque-backed = good

---

## 8. Common Mistakes at Level 3
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
`std::stack<T>` is `std::stack<T, std::deque<T>>`. Deque is segmented array → push/pop both ends O(1) amortized, no invalidation of references.

---

## 11. Pattern Recognition & Generalizations
- **Formal name:** LIFO/FIFO + Monotonic
- **Similar problems:** see other entries in this category.
- **When you see** _nearest greater/smaller_, **think** _monotonic stack_.
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
- **Core idea:** Largest rectangle in histogram — order-of-arrival/departure matters.
- **Complexity:** O(n) time, O(n) space.
- **Don't forget:** (1) null-check pointers, (2) free what you allocate, (3) handle empty input, (4) consider iterator invalidation.

---
*Compile:* `g++ -std=c++17 -Wall -Wextra -fsanitize=address main.cpp -o sol`
