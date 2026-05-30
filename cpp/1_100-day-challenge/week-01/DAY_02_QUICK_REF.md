# 📋 Day 2 Quick Reference Card

## 🎯 Today's Focus: Maps, Sets & Hash Tables

---

## 📚 Container Cheat Sheet

### **When to Use What?**

| Need | Use | Time | Space | Notes |
|------|-----|------|-------|-------|
| Fast lookup | `unordered_set` | O(1)* | O(n) | Check existence |
| Fast key-value | `unordered_map` | O(1)* | O(n) | Quick lookups |
| Sorted unique | `set` | O(log n) | O(n) | Auto-sorted |
| Sorted key-value | `map` | O(log n) | O(n) | Range queries |
| Unique count | `unordered_map` | O(1)* | O(n) | Frequency map |

*Average case; O(n) worst case on hash collisions

---

## 🔑 Key Patterns to Master

### **1. Frequency Counting**
```cpp
unordered_map<char, int> freq;
for (char c : str) {
    freq[c]++;
}
```

**Use for:** Character/element counting, finding duplicates

---

### **2. Complement/Pair Finding**
```cpp
unordered_set<int> seen;
for (int num : nums) {
    if (seen.count(target - num)) {
        // Found pair!
    }
    seen.insert(num);
}
```

**Use for:** Two sum, pair problems, subset sum

---

### **3. Grouping by Property**
```cpp
unordered_map<string, vector<string>> groups;
for (const string& s : strs) {
    string key = computeProperty(s); // sorted, hash, etc.
    groups[key].push_back(s);
}
```

**Use for:** Anagrams, grouping similar items

---

### **4. Sliding Window**
```cpp
unordered_set<char> window;
int left = 0, maxLen = 0;
for (int right = 0; right < s.length(); right++) {
    while (window.count(s[right])) {
        window.erase(s[left++]);
    }
    window.insert(s[right]);
    maxLen = max(maxLen, right - left + 1);
}
```

**Use for:** Longest substring problems, variable window

---

### **5. Prefix Sum + Hash**
```cpp
unordered_map<int, int> prefixCount;
prefixCount[0] = 1;
int sum = 0, count = 0;
for (int num : nums) {
    sum += num;
    count += prefixCount[sum - k];
    prefixCount[sum]++;
}
```

**Use for:** Subarray sum problems, range queries

---

## ⚡ Quick Operations

### **Map/Set Operations**
```cpp
// Check existence (SAFE - doesn't insert)
if (map.find(key) != map.end()) { }
if (map.count(key) > 0) { }

// Insert/Update
map[key] = value;        // Creates if not exists
map.insert({key, value}); // Doesn't overwrite

// Access (throws if not found)
auto val = map.at(key);  // Safe access

// Iterate
for (const auto& [key, value] : map) { }

// Delete
map.erase(key);
```

---

## 🎓 Today's Exercises (TODOs)

1. **firstUniqChar_ReturnChar** - Return character instead of index
2. **topKFrequent_Heap** - Use min heap for O(n log k)

---

## 🏆 LeetCode Practice (Do Today!)

### **Easy (15-20 min each):**
- [ ] Valid Anagram (242)
- [ ] Contains Duplicate (217)
- [ ] First Unique Character (387)

### **Medium (30-40 min each):**
- [ ] Group Anagrams (49)
- [ ] Longest Substring Without Repeating Characters (3)
- [ ] Top K Frequent Elements (347)

### **Bonus Medium:**
- [ ] Subarray Sum Equals K (560)

---

## 💡 Common Mistakes to Avoid

❌ **Using [] for checking existence**
```cpp
if (map[key]) { } // BAD: Creates entry if not exists!
```

✅ **Use find() or count()**
```cpp
if (map.find(key) != map.end()) { } // GOOD
if (map.count(key)) { }              // GOOD
```

---

❌ **Forgetting const& in range loops**
```cpp
for (auto item : largeMap) { } // BAD: Copies each pair!
```

✅ **Use const reference**
```cpp
for (const auto& [k, v] : largeMap) { } // GOOD
```

---

❌ **Not initializing prefix sum base case**
```cpp
unordered_map<int, int> prefixCount;
// Missing: prefixCount[0] = 1;
```

✅ **Always initialize base case**
```cpp
prefixCount[0] = 1; // Empty prefix has sum 0
```

---

## 🧪 Test Your Code

```bash
# Compile with warnings
g++ -std=c++17 -Wall -Wextra -O2 day02_maps_sets.cpp -o day02

# Run
./day02

# Debug with gdb (if needed)
gdb ./day02
```

---

## 📊 Complexity Reference

| Operation | unordered_map | map | unordered_set | set |
|-----------|---------------|-----|---------------|-----|
| Insert | O(1)* | O(log n) | O(1)* | O(log n) |
| Find | O(1)* | O(log n) | O(1)* | O(log n) |
| Delete | O(1)* | O(log n) | O(1)* | O(log n) |
| Iterate | O(n) | O(n) | O(n) | O(n) |
| Ordered? | ❌ | ✅ | ❌ | ✅ |

---

## 🎯 End-of-Day Checklist

Before finishing Day 2:
- [ ] Compiled and ran day02_maps_sets.cpp
- [ ] Understood all 6 main exercises
- [ ] Completed at least 1 TODO function
- [ ] Solved 3+ LeetCode problems
- [ ] Can explain map vs unordered_map
- [ ] Know all 5 key patterns above
- [ ] Updated PROGRESS_TRACKER.md
- [ ] Git commit: "Day 2: Maps and hash tables complete"

---

## 🚀 Tomorrow Preview

**Day 3: Iterators & STL Algorithms**
- transform, accumulate, find_if
- Custom predicates and lambdas
- Algorithm complexity
- Functional programming in C++

---

**Keep coding! You're building strong foundations! 💪**
