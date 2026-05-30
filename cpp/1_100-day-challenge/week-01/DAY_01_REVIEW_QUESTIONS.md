# 📊 Day 1 Review - Answer These Questions

Complete these questions to solidify your Day 1 learning. Write your answers, then check the solution guide below.

---

## ❓ Questions to Test Your Understanding

### **1. Two Sum - Multiple Solutions**
**Q:** In your `twoSum_Optimized()`, what happens with input `[3, 3, 6]` and target `9`?
- Will it find duplicate pairs `[3, 3]` twice?
- Why or why not?

**Q:** Why did you need `twoSum_Optimized_duplicate()` with a `set<pair<int,int>>`?

**Your Answer:**
```
(Write here)
```

---

### **2. Space Complexity**
**Q:** What's the space complexity of your optimized Two Sum solution?
- Best case?
- Worst case?
- When would worst case occur?

**Your Answer:**
```
(Write here)
```

---

### **3. Remove Duplicates Comparison**
**Q:** Compare these two approaches:
- `removeDuplicates()` (sorted array): Time ___, Space ___
- `removeDuplicates_unsorted()`: Time ___, Space ___
- When would you choose the unsorted version?

**Your Answer:**
```
(Write here)
```

---

### **4. Two Pointer Technique**
**Q:** In `removeDuplicates()`, why compare `nums[readPos]` with `nums[writePos - 1]` instead of `nums[writePos]`?

Draw an example: `[1, 1, 2, 2, 3]`
- Show writePos and readPos at each step
- Why does `writePos - 1` work?

**Your Answer:**
```
(Write here)
```

---

### **5. Vector Performance**
**Q:** Explain "amortized O(1)" for `push_back()`:
- When does reallocation happen?
- Why is it still considered O(1) on average?
- What growth strategy does vector use (hint: multiplicative)?

**Your Answer:**
```
(Write here)
```

---

### **6. Pass by Reference**
**Q:** What happens internally when you pass:
- `vector<int> nums` (by value)
- `const vector<int>& nums` (by const reference)

Which is better and why?

**Your Answer:**
```
(Write here)
```

---

### **7. Kadane's Algorithm**
**Q:** In `maxSubArray()`, explain this line:
```cpp
currentSum = max(nums[i], currentSum + nums[i]);
```
- What does `nums[i]` mean (starting fresh)?
- What does `currentSum + nums[i]` mean (extending)?
- When do we start fresh and why?

**Your Answer:**
```
(Write here)
```

---

### **8. Product Except Self**
**Q:** Why can't we use division in "Product Except Self"?
- What would the division approach be?
- What edge case breaks it?

**Q:** Explain the two-pass solution:
- What does the left pass compute?
- What does the right pass compute?
- How do they combine?

**Your Answer:**
```
(Write here)
```

---

## ✅ Solution Guide

<details>
<summary>Click to reveal answers</summary>

### **Answer 1: Two Sum Duplicates**
With `[3, 3, 6]` and target `9`:
- First 3 at index 0 goes into map: `{3 -> 0}`
- Second 3 at index 1: checks if `9-3=6` exists → NO
- Then adds: `{3 -> 1, ...}` (OVERWRITES previous 3!)
- Number 6 at index 2: checks if `9-6=3` exists → YES → returns `[1, 2]`

**Result:** Only finds ONE pair `[3, 6]`, misses the `[3, 3]` pair!

The `_duplicate()` version uses `set<pair<int,int>>` to track already-found pairs and avoid reporting duplicates.

---

### **Answer 2: Space Complexity**
- **Best case:** O(1) - if all elements sum to target immediately
- **Worst case:** O(n) - store all n elements in hash map
- **Average case:** O(n) - typically need to store most elements

Worst case: When solution is at the very end of array.

---

### **Answer 3: Sorted vs Unsorted**
- **Sorted:** Time O(n), Space O(1) - two pointers, in-place
- **Unsorted:** Time O(n), Space O(n) - hash set to track seen

Choose unsorted version when:
- Array cannot be sorted (preserve order)
- Space is not a concern
- Need faster random access pattern

---

### **Answer 4: Two Pointer Logic**
```
[1, 1, 2, 2, 3]
 w  r              writePos=1, readPos=1: nums[1]==nums[0], skip
 w     r           writePos=1, readPos=2: nums[2]!=nums[0], write
    w     r        writePos=2, readPos=3: nums[3]==nums[1], skip
    w        r     writePos=2, readPos=4: nums[4]!=nums[1], write
       w

Result: [1, 2, 3, ?, ?]
```

We compare with `writePos - 1` because that's the **last unique element written**. `writePos` points to the **next position to write**.

---

### **Answer 5: Amortized O(1)**
- **Reallocation:** When `size() == capacity()`
- **Growth strategy:** Typically doubles capacity (1 → 2 → 4 → 8 → 16...)
- **Why O(1) amortized:**
  - Most push_back operations: O(1) - just increment size
  - Occasional reallocation: O(n) - copy all elements
  - Total cost for n insertions: n + (1 + 2 + 4 + ... + n/2) ≈ 2n
  - Average per insertion: 2n/n = O(1)

**reserve()** eliminates reallocations when size is known!

---

### **Answer 6: Pass by Value vs Reference**
**By value** `vector<int> nums`:
- Creates **full copy** of entire vector
- O(n) time and space
- Modifications don't affect original
- Use when: need independent copy

**By const reference** `const vector<int>& nums`:
- No copy, just passes pointer/reference
- O(1) time and space
- Cannot modify (const)
- Use when: read-only access (most cases!)

---

### **Answer 7: Kadane's Algorithm**
```cpp
currentSum = max(nums[i], currentSum + nums[i]);
```

- `nums[i]`: Start fresh from current element
- `currentSum + nums[i]`: Extend previous subarray

**Decision:** If `currentSum` is negative, better to start fresh!

Example: `[-2, 1, -3, 4]`
- At 1: max(1, -2+1) = max(1, -1) = 1 → start fresh
- At -3: max(-3, 1-3) = max(-3, -2) = -2 → extend
- At 4: max(4, -2+4) = max(4, 2) = 4 → start fresh!

---

### **Answer 8: Product Except Self**
**Why not division:**
- Approach: `product of all / nums[i]`
- **Edge case:** Division by zero when `nums[i] = 0`!
- Even if handled, what if multiple zeros?

**Two-pass solution:**
```
nums:   [1,  2,  3,  4]
left:   [1,  1,  2,  6]  (product of all to the left)
right:  [24, 12, 4,  1]  (product of all to the right)
result: [24, 12, 8,  6]  (left[i] * right[i])
```

**Elegant!** Each position = left product × right product

</details>

---

## 🎯 Self-Assessment Checklist

After reviewing your answers, check what you've mastered:

### Day 1 Concepts:
- [ ] I understand when vector reallocates
- [ ] I can explain amortized O(1)
- [ ] I know when to use reserve()
- [ ] I understand pass by const reference
- [ ] I can implement two pointer technique
- [ ] I understand Kadane's algorithm intuition
- [ ] I can explain prefix/suffix products
- [ ] I know time/space complexity of all solutions

### Coding Skills:
- [ ] I can identify O(n²) solutions and optimize to O(n)
- [ ] I know when to use hash map vs set vs vector
- [ ] I can trace through algorithms step-by-step
- [ ] I test edge cases (empty, single element, duplicates)
- [ ] I write clean, commented code

---

## 📝 If You Struggled:

**Too hard?** That's normal! These are interview-level problems. Review:
1. BEST_PRACTICES.md (vectors, pass by reference)
2. Day 1 code comments line by line
3. Trace examples on paper

**Too easy?** Great! Try these challenges:
1. 3Sum problem (find three numbers that sum to target)
2. Container With Most Water (two pointers)
3. Merge Intervals
4. Implement your own dynamic array class

---

## 🚀 Ready for Day 2?

Once you can answer most questions above, you're ready!

**Day 2 Focus:** Maps, Sets, Hash Tables
- unordered_map vs map
- Frequency counting patterns
- Sliding window technique
- Anagram detection

Compile and run:
```bash
cd /home/23u58g/work/viswa/cpp/1_100-day-challenge/week-01
g++ -std=c++17 -Wall -Wextra -O2 day02_maps_sets.cpp -o day02
./day02
```

**Good luck! 💪**
