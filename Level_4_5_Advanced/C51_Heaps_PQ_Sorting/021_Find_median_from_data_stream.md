# Chapter: Find median from data stream

> **Level:** 5 | **Category:** C51 — Heaps, Priority Queues & Advanced Sorting

---

## 1. Problem Statement
Master the topic: **Find median from data stream**.

**Examples:**
- **Simple:** small, unambiguous input.
- **Tricky:** edge case (empty / cycle / single node / overflow).
- **Maximum-constraint:** N up to 10^5 or 10^6 — must hit optimal complexity.

**Follow-ups:** What if the input is a stream? What if updates are interleaved with queries?

---

## 2. Category & Difficulty
- **Category:** Heaps, Priority Queues & Advanced Sorting
- **Sub-category:** Heap / Priority Queue + Sorting
- **Difficulty:** Medium → Hard
- **Interview frequency:** Common at FAANG; appears in system-design and on-site rounds.
- **Estimated solve time:** 20–35 min for a prepared candidate.

---

## 3. Prerequisites
- Heap property, comparators, std::priority_queue
- Big-O analysis; understanding of amortized cost
- Earlier problems in this category

---

## 4. Core Algorithmic Concept
Two heaps: max-heap of lower half, min-heap of upper. Balance sizes.

**Why it works:** the algorithm maintains an invariant — at each step the partial solution is provably optimal/correct given the inputs seen so far.

**Mental model:** a partial-order data structure where you always extract the extreme element fast.

```
Visual:
  initial state  ──>  iteration  ──>  iteration  ──>  final
```

---

## 5. Recurrence / State Definition
Not a DP problem — see algorithm in section 4.

---

## 6. Solution Approaches

### Approach 1: Brute Force
```cpp
#include <queue>
class MedianFinder {
    std::priority_queue<int> lo;            // max-heap
    std::priority_queue<int,std::vector<int>,std::greater<int>> hi;  // min-heap
public:
    void addNum(int x){
        lo.push(x);
        hi.push(lo.top()); lo.pop();
        if(hi.size() > lo.size()){ lo.push(hi.top()); hi.pop(); }
    }
    double findMedian(){
        return lo.size()>hi.size() ? lo.top() : (lo.top()+hi.top())/2.0;
    }
};
int main(){return 0;}
```
**Time:** O(n²) or worse.  
**Space:** O(n).  
**Why it TLEs:** redundant recomputation.

### Approach 2: Optimal
```cpp
// O(log n) per add, O(1) per median query.
int main(){return 0;}
```
**Time:** O(n log n) or O(n).  
**Space:** O(n) typical, often reducible to O(1) per state.  
**Insight:** use the right data structure (heap/queue/DSU).

---

## 7. Trace Through Example

| Step | State | Key Variables | Observation |
|------|-------|---------------|-------------|
| 1 | start | inputs loaded | initialize structures |
| 2 | iter 1 | first element | base case applied |
| 3 | iter 2 | partial result | recurrence/transition fires |
| 4 | mid | accumulating | invariant holds |
| 5 | near-end | almost done | final updates |
| 6 | end | answer ready | return |

---

## 8. Complexity Deep Dive
- **Time:** O(V+E) graph / O(n log n) sort/heap
- **Space:** O(V) visited / O(n) heap
- **Hidden constants:** hash collisions, cache misses, allocator overhead.
- **Cache:** Heap is array-based binary tree. Sort algorithms have different cache + constant-factor profiles.

| Approach | Time | Space |
|----------|------|-------|
| Brute | O(n²) or worse | O(n) |
| Optimal | O(n log n) or O(n) | O(n) or O(1) |

---

## 9. Edge Cases & Gotchas
1. Empty input / single element
2. All identical values
3. Already-sorted / reverse-sorted input
4. Integer overflow on sums or products
5. Heap with duplicate keys
6. Maximum N where naive recursion blows the stack
7. Concurrency: not thread-safe by default

---

## 10. Optimization Techniques
- **Space:** rolling array (DP), implicit tree pointers (Morris).
- **Time:** monotonic queue, binary search, segment/Fenwick tree.
- **Early termination:** stop when answer is provably found.
- **Pruning:** skip impossible branches in backtracking.

---

## 11. Code Quality & Production
- Replace raw `new`/`delete` with smart pointers in production trees/graphs.
- Avoid magic numbers; use `constexpr`.
- Unit tests: empty, single, two, large random, adversarial.
- Embedded: avoid recursion (stack-limited) — use iterative + explicit stack.

---

## 12. Pattern Recognition
- **Pattern:** Heap / Priority Queue + Sorting
- **When you see** k-th / median / top-k, **think** heap (priority_queue)
- 5 similar problems: see neighboring entries in this category.

---

## 13. Practice Variants
- **Easy:** smaller bounds, no edge cases.
- **Medium:** add a constraint (no extra space, online queries).
- **Hard:** multi-dimensional state, parallel edges, weighted variants.
- **Competition:** N up to 10^6, 1-second TL.

---

## 14. Interview Playbook
- **First 2 min:** restate problem, ask about constraints (size, range, ties), give 1–2 examples.
- **Brute → optimal:** state brute, complexity, then identify bottleneck and remove it.
- **If stuck:** try smaller examples, consider what data structure gives O(1)/O(log n) for the operation needed.
- **Strong verbal:** "I'll use Heap / Priority Queue + Sorting. The invariant is X. Time O(?), space O(?). Edge cases: empty, single, max-N."

---

## 15. Quick Reference Card
- **Core idea:** Find median from data stream — Heap / Priority Queue + Sorting.
- **Algorithm:** heap-driven greedy
- **Complexity:** O(n log n)
- **Don't forget:** (1) base cases, (2) edge cases, (3) overflow, (4) recursion depth, (5) cache friendliness.

---
*Compile:* `g++ -std=c++17 -O2 -Wall -Wextra main.cpp -o sol`
