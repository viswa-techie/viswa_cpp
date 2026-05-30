# 📅 Day 2 Preview: Maps, Sets & Hash Tables

## 🎯 Learning Objectives
- Master unordered_map and map differences
- Understand hash functions and collision handling
- Use sets for unique element tracking
- Practice O(n) time complexity with hash tables

## 📚 Topics Covered

### 1. Map vs Unordered_Map
```cpp
// map: Ordered, O(log n) operations, uses BST
map<string, int> orderedMap;

// unordered_map: Unordered, O(1) average, uses hash table
unordered_map<string, int> hashMap;
```

### 2. Common Patterns
- Frequency counting
- Two-sum variations
- Grouping elements
- Anagram detection
- Caching/memoization

## 💻 Problems to Solve (Day 2)

### Easy (15 min each):
1. **Valid Anagram** - Check if two strings are anagrams
2. **Contains Duplicate** - Find if array has duplicates
3. **First Unique Character** - Find first non-repeating char

### Medium (30 min each):
1. **Group Anagrams** - Group strings that are anagrams
2. **Top K Frequent Elements** - Find k most frequent elements
3. **Longest Substring Without Repeating Characters** - Classic sliding window

## 🔧 Preparation

### Before Day 2:
1. Complete Day 1 exercises ✓
2. Read about hash tables in BEST_PRACTICES.md
3. Quick reference:
   ```cpp
   // Frequency map pattern
   unordered_map<char, int> freq;
   for (char c : str) freq[c]++;
   
   // Check existence
   if (freq.find(key) != freq.end()) { /* exists */ }
   
   // Iterate map
   for (const auto& [key, value] : freq) { /* ... */ }
   ```

## 📖 Study Materials

### From Your Workspace:
- `C-Plus-Plus/STL/Map/` - Basic examples
- `CPlusPlusThings/basic_content/` - Modern usage
- `TheAlgorithms/C-Plus-Plus/data_structures/` - Implementations

### Key Concepts:
- Hash function design
- Load factor and rehashing
- Collision resolution (chaining vs open addressing)
- When to use map vs unordered_map

## ⏰ Time Allocation (2-3 hours)

**30 min:** Read about maps/sets, hash tables theory
**90 min:** Solve 4-5 problems
**30 min:** Study hash table implementation, review solutions

## 🎯 Success Criteria

By end of Day 2, you should:
- [ ] Understand O(1) vs O(log n) lookup
- [ ] Know when to use each container
- [ ] Solve frequency counting problems easily
- [ ] Comfortable with iterator syntax
- [ ] Started thinking in hash table patterns

## 💡 Preview: Day 3

**Topic:** Iterators & STL Algorithms (transform, accumulate, find_if)
**Focus:** Functional programming style in C++

---

**Stay tuned! After completing Day 1, Day 2 exercises will be ready for you! 🚀**
