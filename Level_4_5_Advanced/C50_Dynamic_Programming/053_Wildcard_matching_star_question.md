# Chapter: Wildcard matching star question

> **Level:** 5 | **Category:** C50 — Dynamic Programming

---

## 1. Problem Statement
Master the topic: **Wildcard matching star question**.

**Examples:**
- **Simple:** small, unambiguous input.
- **Tricky:** edge case (empty / cycle / single node / overflow).
- **Maximum-constraint:** N up to 10^5 or 10^6 — must hit optimal complexity.

**Follow-ups:** What if the input is a stream? What if updates are interleaved with queries?

---

## 2. Category & Difficulty
- **Category:** Dynamic Programming
- **Sub-category:** Dynamic Programming
- **Difficulty:** Medium → Hard
- **Interview frequency:** Common at FAANG; appears in system-design and on-site rounds.
- **Estimated solve time:** 20–35 min for a prepared candidate.

---

## 3. Prerequisites
- Recursion, memoization, table reasoning
- Big-O analysis; understanding of amortized cost
- Earlier problems in this category

---

## 4. Core Algorithmic Concept
dp[i][j] = match s[0..i-1] vs p[0..j-1]. '*' matches empty or extend.

**Why it works:** the algorithm maintains an invariant — at each step the partial solution is provably optimal/correct given the inputs seen so far.

**Mental model:** break problem into overlapping subproblems and cache results.

```
Visual:
  initial state  ──>  iteration  ──>  iteration  ──>  final
```

---

## 5. Recurrence / State Definition
`dp[i][j]` = optimal value for first i items using state j. Transition: dp[i][j] = best of taking vs skipping option.

---

## 6. Solution Approaches

### Approach 1: Brute Force
```cpp
#include <string>
#include <vector>
bool isMatch(const std::string& s, const std::string& p){
    int m=s.size(), n=p.size();
    std::vector<std::vector<bool>> dp(m+1, std::vector<bool>(n+1,false));
    dp[0][0]=true;
    for(int j=1;j<=n;++j) if(p[j-1]=='*') dp[0][j]=dp[0][j-1];
    for(int i=1;i<=m;++i)
        for(int j=1;j<=n;++j){
            if(p[j-1]=='*') dp[i][j] = dp[i-1][j] || dp[i][j-1];
            else if(p[j-1]=='?' || p[j-1]==s[i-1]) dp[i][j]=dp[i-1][j-1];
        }
    return dp[m][n];
}
int main(){return 0;}
```
**Time:** O(n²) or worse.  
**Space:** O(n).  
**Why it TLEs:** redundant recomputation.

### Approach 2: Optimal
```cpp
// O(m*n).
int main(){return 0;}
```
**Time:** O(n log n) or O(n).  
**Space:** O(n) typical, often reducible to O(1) per state.  
**Insight:** memoize subproblems / use rolling array.

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
- **Time:** O(n²) DP / O(n log n) optimized
- **Space:** O(n²) table → O(n) rolling
- **Hidden constants:** hash collisions, cache misses, allocator overhead.
- **Cache:** DP table is contiguous memory — cache-friendly. Memoization adds hash/map overhead.

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
5. Subproblem dimension > expected
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
- **Pattern:** Dynamic Programming
- **When you see** optimal subproblem with overlap, **think** DP recurrence + memoize
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
- **Strong verbal:** "I'll use Dynamic Programming. The invariant is X. Time O(?), space O(?). Edge cases: empty, single, max-N."

---

## 15. Quick Reference Card
- **Core idea:** Wildcard matching star question — Dynamic Programming.
- **Algorithm:** DP table fill
- **Complexity:** O(n²) or O(n)
- **Don't forget:** (1) base cases, (2) edge cases, (3) overflow, (4) recursion depth, (5) cache friendliness.

---
*Compile:* `g++ -std=c++17 -O2 -Wall -Wextra main.cpp -o sol`
