# 📋 Day 3 Quick Reference - STL Algorithms

## 🎯 Core Philosophy: Think in Algorithms, Not Loops!

---

## 📚 Algorithm Categories

### **1. Non-Modifying Algorithms**

| Algorithm | Purpose | Complexity | Example |
|-----------|---------|------------|---------|
| `find(first, last, val)` | Find value | O(n) | Find 42 |
| `find_if(first, last, pred)` | Find by condition | O(n) | Find first even |
| `count(first, last, val)` | Count occurrences | O(n) | Count 'a's |
| `count_if(first, last, pred)` | Count by condition | O(n) | Count odds |
| `all_of(first, last, pred)` | Check all match | O(n) | All positive? |
| `any_of(first, last, pred)` | Check any match | O(n) | Any negative? |
| `none_of(first, last, pred)` | Check none match | O(n) | No zeros? |

---

### **2. Modifying Algorithms**

| Algorithm | Purpose | Complexity | Example |
|-----------|---------|------------|---------|
| `transform(first, last, result, op)` | Apply function | O(n) | Square all |
| `fill(first, last, val)` | Fill with value | O(n) | Fill with 0 |
| `generate(first, last, gen)` | Fill with generator | O(n) | Random nums |
| `iota(first, last, start)` | Fill sequence | O(n) | 1,2,3,4,5... |
| `replace(first, last, old, new)` | Replace value | O(n) | 0 → 1 |
| `replace_if(first, last, pred, new)` | Replace conditional | O(n) | Even → 0 |

---

### **3. Removing Algorithms** (⚠️ Don't actually delete!)

| Algorithm | Purpose | Complexity | Example |
|-----------|---------|------------|---------|
| `remove(first, last, val)` | "Remove" value | O(n) | Remove 0s |
| `remove_if(first, last, pred)` | "Remove" conditional | O(n) | Remove evens |
| `unique(first, last)` | Remove consecutive dups | O(n) | 1,1,2→1,2 |

**⚠️ ERASE-REMOVE IDIOM:**
```cpp
// WRONG: remove_if doesn't delete!
remove_if(vec.begin(), vec.end(), pred);

// CORRECT: Use erase after remove!
auto newEnd = remove_if(vec.begin(), vec.end(), pred);
vec.erase(newEnd, vec.end());

// ONE-LINER:
vec.erase(remove_if(vec.begin(), vec.end(), pred), vec.end());
```

---

### **4. Partitioning & Sorting**

| Algorithm | Purpose | Complexity | Example |
|-----------|---------|------------|---------|
| `partition(first, last, pred)` | Split by condition | O(n) | Evens first |
| `stable_partition(...)` | Partition + order | O(n log n) | Stable split |
| `sort(first, last)` | Sort ascending | O(n log n) | Sort array |
| `sort(first, last, comp)` | Custom sort | O(n log n) | By length |
| `stable_sort(...)` | Sort + stable | O(n log n) | Stable order |
| `nth_element(first, nth, last)` | Partial sort | O(n) avg | Find median |

---

### **5. Numeric Algorithms** (`<numeric>`)

| Algorithm | Purpose | Complexity | Example |
|-----------|---------|------------|---------|
| `accumulate(first, last, init)` | Sum/reduce | O(n) | Total |
| `accumulate(first, last, init, op)` | Custom reduce | O(n) | Product |
| `inner_product(f1, l1, f2, init)` | Dot product | O(n) | a·b |
| `partial_sum(first, last, result)` | Prefix sums | O(n) | Running total |

---

### **6. Copy & Move Algorithms**

| Algorithm | Purpose | Complexity | Example |
|-----------|---------|------------|---------|
| `copy(first, last, result)` | Copy elements | O(n) | Duplicate |
| `copy_if(first, last, result, pred)` | Conditional copy | O(n) | Copy evens |
| `copy_n(first, n, result)` | Copy n elements | O(n) | First 10 |
| `move(first, last, result)` | Move elements | O(n) | Transfer |

---

## 🔥 Essential Patterns

### **Pattern 1: Transform (Map)**
```cpp
// Square all numbers
transform(nums.begin(), nums.end(), nums.begin(),
          [](int x) { return x * x; });

// To uppercase
transform(str.begin(), str.end(), str.begin(), ::toupper);

// Binary transform (add two vectors)
transform(a.begin(), a.end(), b.begin(), result.begin(),
          [](int x, int y) { return x + y; });
```

---

### **Pattern 2: Accumulate (Reduce)**
```cpp
// Sum
int sum = accumulate(nums.begin(), nums.end(), 0);

// Product
int prod = accumulate(nums.begin(), nums.end(), 1, multiplies<>());

// Custom: sum of squares
int sumSq = accumulate(nums.begin(), nums.end(), 0,
                       [](int acc, int x) { return acc + x*x; });

// String concatenation
string all = accumulate(words.begin(), words.end(), string(""));
```

---

### **Pattern 3: Filter (Copy_if)**
```cpp
// Extract evens
vector<int> evens;
copy_if(nums.begin(), nums.end(), back_inserter(evens),
        [](int x) { return x % 2 == 0; });

// Remove odds (in-place)
nums.erase(remove_if(nums.begin(), nums.end(),
                     [](int x) { return x % 2 != 0; }),
           nums.end());
```

---

### **Pattern 4: Find with Predicate**
```cpp
// Find first even
auto it = find_if(nums.begin(), nums.end(),
                  [](int x) { return x % 2 == 0; });
if (it != nums.end()) {
    cout << "Found: " << *it << " at index "
         << distance(nums.begin(), it) << "\n";
}

// Check if any/all/none
bool hasNegative = any_of(nums.begin(), nums.end(),
                          [](int x) { return x < 0; });
bool allPositive = all_of(nums.begin(), nums.end(),
                          [](int x) { return x > 0; });
```

---

### **Pattern 5: Partition & Sort**
```cpp
// Partition (evens before odds)
partition(nums.begin(), nums.end(),
          [](int x) { return x % 2 == 0; });

// Sort by custom comparator
sort(words.begin(), words.end(),
     [](const auto& a, const auto& b) {
         return a.length() < b.length();
     });

// Find kth largest (faster than full sort!)
nth_element(nums.begin(), nums.begin() + k - 1, nums.end(),
            greater<>());
int kthLargest = nums[k - 1];
```

---

### **Pattern 6: Generate Sequences**
```cpp
// Fill with constant
fill(vec.begin(), vec.end(), 42);

// Sequence 1,2,3,4,5...
iota(vec.begin(), vec.end(), 1);

// Generate with function
int counter = 0;
generate(vec.begin(), vec.end(), [&]() { return counter++; });

// Fibonacci
int a = 0, b = 1;
generate(fib.begin(), fib.end(), [&]() {
    int temp = a;
    a = b;
    b = temp + b;
    return temp;
});
```

---

## 🎓 Lambda Expression Syntax

### **Basic Forms**
```cpp
// No capture, no parameters
[]() { return 42; }

// Capture by value
[x]() { return x * 2; }

// Capture by reference
[&x]() { x *= 2; }

// Capture all by value
[=]() { return x + y; }

// Capture all by reference
[&]() { x++; y++; }

// Mixed capture
[x, &y]() { return x + y; }

// Mutable lambda (can modify captured values)
[x]() mutable { return ++x; }

// With parameters and return type
[](int x, int y) -> int { return x + y; }

// Generic lambda (C++14)
[](auto x, auto y) { return x + y; }
```

---

## 💡 Common Idioms

### **Erase-Remove**
```cpp
// Remove all zeros
vec.erase(remove(vec.begin(), vec.end(), 0), vec.end());

// Remove if condition
vec.erase(remove_if(vec.begin(), vec.end(),
                    [](int x) { return x < 0; }),
          vec.end());
```

### **Sort-Unique (Remove ALL Duplicates)**
```cpp
// Only consecutive duplicates removed
auto newEnd = unique(vec.begin(), vec.end());
vec.erase(newEnd, vec.end());

// Remove ALL duplicates
sort(vec.begin(), vec.end());
vec.erase(unique(vec.begin(), vec.end()), vec.end());
```

### **Back Inserter (Dynamic Growth)**
```cpp
// When output container size unknown
vector<int> result;
copy_if(nums.begin(), nums.end(), back_inserter(result),
        [](int x) { return x > 0; });

// Alternative: resize first
vector<int> result(nums.size());
auto end = copy_if(nums.begin(), nums.end(), result.begin(), pred);
result.erase(end, result.end());
```

---

## ⚡ Performance Tips

### **✅ DO:**
- Use algorithms when intent is clear
- Prefer `reserve()` before multiple `back_inserter` operations
- Use `const&` in lambda parameters for objects
- Chain algorithms for complex operations
- Use `nth_element` instead of full sort when possible

### **❌ DON'T:**
- Forget `erase` after `remove_if`
- Modify container while iterating
- Use `[]` on map to check existence (inserts!)
- Capture large objects by value in lambda
- Write complex lambdas (extract to function)

---

## 🎯 Today's TODOs

1. ✅ `convertToStrings()` - Transform int to string
2. ✅ `doubleEvens()` - Transform with conditional
3. ✅ `findMax()` - Accumulate to find maximum
4. ✅ `calculateAverage()` - Accumulate for average
5. ✅ `findLongString()` - Find_if with length check
6. ✅ `findFirstPrimeIndex()` - Find_if with prime check
7. ✅ `sortBySecond()` - Sort pairs by second element
8. ✅ `dutchFlagPartition()` - Three-way partition
9. ✅ `extractVowelWords()` - Copy_if vowel words
10. ✅ `removeDuplicates()` - Sort + unique
11. ✅ `generateSquares()` - Generate with counter
12. ✅ `sumOfSquaresOfPositives()` - One-liner composition
13. ✅ `wordFrequencyAnalysis()` - Complex analysis

---

## 🏆 LeetCode Practice

### **Algorithm-Focused Problems:**

**Easy:**
- [ ] Remove Element (27)
- [ ] Remove Duplicates from Sorted Array (26)
- [ ] Move Zeroes (283)
- [ ] Intersection of Two Arrays (349)

**Medium:**
- [ ] Sort Colors / Dutch National Flag (75)
- [ ] Kth Largest Element (215) - use nth_element!
- [ ] Top K Frequent Elements (347)
- [ ] Product of Array Except Self (238)

**Hard:**
- [ ] Median of Two Sorted Arrays (4)
- [ ] First Missing Positive (41)

---

## 🧪 Testing Commands

```bash
# Compile
g++ -std=c++17 -Wall -Wextra -O2 day03_iterators_algorithms.cpp -o day03

# Run
./day03

# Uncomment test cases in main() as you complete TODOs

# Debug
gdb ./day03
```

---

## 📊 Complexity Cheat Sheet

| Problem | Naive Loop | With Algorithm |
|---------|------------|----------------|
| Find element | O(n) | O(n) - same, but clearer |
| Transform all | O(n) | O(n) - same, but safer |
| Sort | O(n²) bubble | O(n log n) optimized |
| Kth largest | O(n log n) sort | O(n) with nth_element! |
| Partition | O(n) manual | O(n) optimized |
| Sum | O(n) | O(n) - more expressive |

---

## 🎯 End-of-Day Checklist

- [ ] Understand all 6 algorithm categories
- [ ] Can write lambdas with captures
- [ ] Know erase-remove idiom
- [ ] Completed at least 5 TODOs
- [ ] Solved 3+ LeetCode problems
- [ ] Understand when algorithms beat loops
- [ ] Know iterator categories
- [ ] Updated PROGRESS_TRACKER.md
- [ ] Git commit: "Day 3: STL algorithms mastery"

---

## 🚀 Tomorrow Preview

**Day 4: Stack, Queue, Deque, Priority Queue**
- LIFO and FIFO patterns
- Monotonic stack
- Sliding window maximum
- Priority queue for top K problems

---

**Master these algorithms - they're the building blocks of elegant C++ code! 💪**
