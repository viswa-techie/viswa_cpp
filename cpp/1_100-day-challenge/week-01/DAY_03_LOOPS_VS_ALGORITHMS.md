# 🎓 Day 3: Loops vs Algorithms - Side by Side Comparison

## Why STL Algorithms Matter

This guide shows the same task implemented with manual loops vs STL algorithms.
**Spoiler:** Algorithms win on clarity, safety, and performance!

---

## Example 1: Square All Numbers

### ❌ Manual Loop (C-style)
```cpp
vector<int> nums = {1, 2, 3, 4, 5};
for (int i = 0; i < nums.size(); i++) {  // ⚠️ Signed/unsigned comparison warning
    nums[i] = nums[i] * nums[i];
}
// Problems:
// - Index management prone to off-by-one errors
// - Signed/unsigned comparison
// - Intent not immediately clear
```

### ✅ STL Algorithm
```cpp
vector<int> nums = {1, 2, 3, 4, 5};
transform(nums.begin(), nums.end(), nums.begin(),
          [](int x) { return x * x; });
// Benefits:
// ✓ Intent is crystal clear ("transform each element")
// ✓ No index management
// ✓ No type mismatch issues
// ✓ Harder to make mistakes
```

---

## Example 2: Find First Even Number

### ❌ Manual Loop
```cpp
int firstEven = -1;
for (int i = 0; i < nums.size(); i++) {
    if (nums[i] % 2 == 0) {
        firstEven = nums[i];
        break;  // Easy to forget!
    }
}
if (firstEven == -1) {
    // Not found - but what if -1 is valid?
}
// Problems:
// - Sentinel value (-1) might be valid data
// - Easy to forget break
// - Need separate "found" flag for robustness
```

### ✅ STL Algorithm
```cpp
auto it = find_if(nums.begin(), nums.end(),
                  [](int x) { return x % 2 == 0; });
if (it != nums.end()) {
    int firstEven = *it;
    // Use it
}
// Benefits:
// ✓ Clear semantics with iterator
// ✓ No sentinel value confusion
// ✓ Automatic early termination
// ✓ Type-safe
```

---

## Example 3: Count Elements Matching Condition

### ❌ Manual Loop
```cpp
int count = 0;
for (int i = 0; i < nums.size(); i++) {
    if (nums[i] > 10 && nums[i] % 2 == 0) {
        count++;
    }
}
// Problems:
// - Verbose for simple task
// - Easy to forget increment
// - More lines = more bugs
```

### ✅ STL Algorithm
```cpp
int count = count_if(nums.begin(), nums.end(),
                     [](int x) { return x > 10 && x % 2 == 0; });
// Benefits:
// ✓ One line, clear intent
// ✓ Predicate is reusable
// ✓ Impossible to forget increment
```

---

## Example 4: Remove All Negative Numbers

### ❌ Manual Loop (Incorrect!)
```cpp
// WRONG: Modifying while iterating
for (int i = 0; i < nums.size(); i++) {
    if (nums[i] < 0) {
        nums.erase(nums.begin() + i);  // ⚠️ Indices shift!
        i--;  // Ugly fix
    }
}
// Problems:
// - Index invalidation bugs
// - Inefficient: O(n²) erases
// - Error-prone logic
```

### ❌ Manual Loop (Better, but still verbose)
```cpp
vector<int> result;
for (int i = 0; i < nums.size(); i++) {
    if (nums[i] >= 0) {
        result.push_back(nums[i]);
    }
}
nums = result;  // Extra copy
// Problems:
// - Requires temporary vector
// - Extra memory allocation
// - More complex than needed
```

### ✅ STL Algorithm (Erase-Remove Idiom)
```cpp
//how the remove_if works?
nums.erase(remove_if(nums.begin(), nums.end(),
                     [](int x) { return x < 0; }),
           nums.end());
// Benefits:
// ✓ One line
// ✓ O(n) efficient
// ✓ No temporary vector
// ✓ Standard idiom
```

---

## Example 5: Sum of Squares

### ❌ Manual Loop
```cpp
int sum = 0;
for (int i = 0; i < nums.size(); i++) {
    sum += nums[i] * nums[i];
}
// Problems:
// - Mixing computation with accumulation
// - Not composable
```

### ✅ STL Algorithm (Two Ways)

**Option 1: Explicit Transform**
```cpp
vector<int> squares(nums.size());
transform(nums.begin(), nums.end(), squares.begin(),
          [](int x) { return x * x; });
int sum = accumulate(squares.begin(), squares.end(), 0);
```

**Option 2: Single Pass**
```cpp
int sum = accumulate(nums.begin(), nums.end(), 0,
                     [](int acc, int x) { return acc + x * x; });
// Benefits:
// ✓ Functional composition
// ✓ Clear separation of concerns
// ✓ Reusable lambdas
```

---

## Example 6: Partition (Evens before Odds)

### ❌ Manual Loop
```cpp
vector<int> evens, odds;
for (int x : nums) {
    if (x % 2 == 0) {
        evens.push_back(x);
    } else {
        odds.push_back(x);
    }
}
nums.clear();
nums.insert(nums.end(), evens.begin(), evens.end());
nums.insert(nums.end(), odds.begin(), odds.end());
// Problems:
// - Two temporary vectors
// - Multiple passes
// - O(n) extra space
// - Slow due to allocations
```

### ✅ STL Algorithm
```cpp
partition(nums.begin(), nums.end(),
          [](int x) { return x % 2 == 0; });
// Benefits:
// ✓ In-place: O(1) extra space
// ✓ Single pass: O(n) time
// ✓ Optimized implementation
// ✓ Clear intent
```

---

## Example 7: Find Kth Largest Element

### ❌ Manual Approach (Sort Everything)
```cpp
sort(nums.begin(), nums.end(), greater<>());
int kthLargest = nums[k - 1];
// Problems:
// - O(n log n) - overkill!
// - Sorts entire array when only need one element
// - Wasteful for large arrays
```

### ✅ STL Algorithm (nth_element)
```cpp
nth_element(nums.begin(), nums.begin() + k - 1, nums.end(),
            greater<>());
int kthLargest = nums[k - 1];
// Benefits:
// ✓ O(n) average time - much faster!
// ✓ Only partitions, doesn't fully sort
// ✓ Optimal for this problem
```

---

## Example 8: Check If All Elements Are Positive

### ❌ Manual Loop
```cpp
bool allPositive = true;
for (int x : nums) {
    if (x <= 0) {
        allPositive = false;
        break;
    }
}
// Problems:
// - Need flag variable
// - Must remember break
// - Verbose for simple check
```

### ✅ STL Algorithm
```cpp
bool allPositive = all_of(nums.begin(), nums.end(),
                          [](int x) { return x > 0; });
// Benefits:
// ✓ Self-documenting
// ✓ No flag needed
// ✓ Automatic short-circuit
// ✓ Also: any_of, none_of
```

---

## Example 9: Copy Strings Longer Than 5 Characters

### ❌ Manual Loop
```cpp
vector<string> longWords;
for (const auto& word : words) {  // At least used range-for!
    if (word.length() > 5) {
        longWords.push_back(word);
    }
}
// Problems:
// - Boilerplate for filtering
// - Easy to forget const& (copies!)
```

### ✅ STL Algorithm
```cpp
vector<string> longWords;
copy_if(words.begin(), words.end(), back_inserter(longWords),
        [](const auto& w) { return w.length() > 5; });
// Benefits:
// ✓ Clear filtering intent
// ✓ Predicate is reusable
// ✓ Composable with other algorithms
```

---

## Example 10: Generate Fibonacci Sequence

### ❌ Manual Loop
```cpp
vector<int> fib(10);
int a = 0, b = 1;
for (int i = 0; i < 10; i++) {
    fib[i] = a;
    int temp = a;
    a = b;
    b = temp + b;
}
// Problems:
// - Index management
// - Mixing generation with storage
```

### ✅ STL Algorithm
```cpp
vector<int> fib(10);
int a = 0, b = 1;
generate(fib.begin(), fib.end(), [&]() {
    int temp = a;
    a = b;
    b = temp + b;
    return temp;
});
// Benefits:
// ✓ Separation: generate logic vs storage
// ✓ No index management
// ✓ Lambda captures state cleanly
```

---

## 📊 Performance Comparison

| Task | Manual Loop | STL Algorithm | Winner |
|------|-------------|---------------|--------|
| Transform | O(n) | O(n) | **Tie** (clarity to algorithm) |
| Find | O(n) | O(n) | **Tie** (safety to algorithm) |
| Sort | O(n²) | O(n log n) | **Algorithm** |
| Kth element | O(n log n) | O(n) | **Algorithm** ⚡ |
| Partition | O(n) + O(n) space | O(n) in-place | **Algorithm** ⚡ |
| Remove | O(n²) | O(n) | **Algorithm** ⚡ |

---

## 🎯 When to Use Which?

### **Use STL Algorithms When:**
✅ Task matches standard algorithm (transform, find, sort, etc.)  
✅ Want clear, self-documenting code  
✅ Need guaranteed performance characteristics  
✅ Working with containers/iterators  
✅ Want to avoid index management bugs  

### **Use Manual Loops When:**
✅ Complex, non-standard logic that doesn't fit algorithms  
✅ Need multiple operations per iteration (can't compose)  
✅ Early exit with complex conditions  
✅ Performance-critical tight loops (measure first!)  
✅ Code would be clearer with explicit loop  

### **Rule of Thumb:**
**Try algorithm first. Use manual loop only if algorithm is awkward.**

---

## 💡 Real-World Example: Data Pipeline

### ❌ Manual Loop Approach
```cpp
// Filter, transform, and sum positive squares > 10
vector<int> data = {-5, 3, -2, 7, 1, -8, 4, 9};
int result = 0;

for (int i = 0; i < data.size(); i++) {
    if (data[i] > 0) {
        int square = data[i] * data[i];
        if (square > 10) {
            result += square;
        }
    }
}
// Problems:
// - Nested conditions
// - Mixed concerns (filter, transform, sum)
// - Hard to modify or reuse parts
```

### ✅ Algorithm Composition
```cpp
vector<int> data = {-5, 3, -2, 7, 1, -8, 4, 9};

// Option 1: Step by step
vector<int> positives;
copy_if(data.begin(), data.end(), back_inserter(positives),
        [](int x) { return x > 0; });

vector<int> squares(positives.size());
transform(positives.begin(), positives.end(), squares.begin(),
          [](int x) { return x * x; });

vector<int> large;
copy_if(squares.begin(), squares.end(), back_inserter(large),
        [](int x) { return x > 10; });

int result = accumulate(large.begin(), large.end(), 0);

// Option 2: One-liner (functional style)
int result = accumulate(data.begin(), data.end(), 0,
    [](int sum, int x) {
        if (x > 0) {
            int sq = x * x;
            if (sq > 10) return sum + sq;
        }
        return sum;
    });
// Benefits:
// ✓ Each step is clear
// ✓ Easy to debug individual steps
// ✓ Parts are reusable
// ✓ Functional pipeline pattern
```

---

## 🎓 Key Takeaways

1. **Clarity:** Algorithms express WHAT, loops express HOW
2. **Safety:** Less manual index management = fewer bugs
3. **Performance:** STL implementations are highly optimized
4. **Composability:** Algorithms chain naturally
5. **Maintainability:** Intent is clear, changes are localized

---

## 🚀 Practice Exercise

**Challenge:** Rewrite these manual loops using STL algorithms:

```cpp
// 1. Find maximum element
int max_val = nums[0];
for (int x : nums) {
    if (x > max_val) max_val = x;
}

// 2. Reverse array in-place
for (int i = 0; i < nums.size() / 2; i++) {
    swap(nums[i], nums[nums.size() - 1 - i]);
}

// 3. Check if contains duplicate
bool hasDup = false;
for (int i = 0; i < nums.size() && !hasDup; i++) {
    for (int j = i + 1; j < nums.size(); j++) {
        if (nums[i] == nums[j]) {
            hasDup = true;
            break;
        }
    }
}
```

**Answers:**
```cpp
// 1. Find maximum
int max_val = *max_element(nums.begin(), nums.end());

// 2. Reverse in-place
reverse(nums.begin(), nums.end());

// 3. Has duplicate
sort(nums.begin(), nums.end());
bool hasDup = adjacent_find(nums.begin(), nums.end()) != nums.end();
// Or with set: nums.size() != unordered_set(nums.begin(), nums.end()).size()
```

---

**Master algorithms, write less code, fewer bugs, clearer intent! 💪**
