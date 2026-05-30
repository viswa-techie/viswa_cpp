# 🚀 Quick Start Guide

## Welcome to Your 100-Day C++ Challenge!

You now have everything you need to begin your journey. Here's how to get started:

---

## 📁 What You Have

```
cpp/100-day-challenge/
├── 100_DAY_CPP_CHALLENGE.md    # Complete roadmap (weeks 1-14)
├── BEST_PRACTICES.md           # Code snippets & patterns
├── PROJECT_IDEAS.md            # 12 project ideas for days 50-100
├── PROGRESS_TRACKER.md         # Daily tracking template
├── QUICK_START.md              # This file
├── week-01/
│   └── day01_vectors_algorithms.cpp  # Today's exercises!
└── projects/                   # Your future projects go here
```

---

## ⚡ Start Day 1 Right Now!

### Step 1: Compile and Run Day 1 Exercise

```bash
cd /home/23u58g/work/viswa/cpp/100-day-challenge/week-01

# Compile with C++17 and optimizations
g++ -std=c++17 -Wall -Wextra -O2 -g day01_vectors_algorithms.cpp -o day01

# Run the program
./day01
```

**Expected Output:**
- Two Sum solution
- Remove duplicates demo
- Maximum subarray calculation
- Performance benchmark
- Product except self result

---

### Step 2: Study the Code

Open `day01_vectors_algorithms.cpp` in VS Code and:

1. **Read all comments** - They explain the logic
2. **Trace through examples** - Use debugger or print statements
3. **Understand time complexity** - Why is it O(n) or O(n²)?
4. **Complete the TODOs** - Implement the optimized versions

**TODOs in Day 1:**
- `twoSum_Optimized()` - Implement O(n) hash map solution
- `maxSubArray_WithIndices()` - Return subarray indices, not just sum

---

### Step 3: Practice on LeetCode

Solve these problems to reinforce learning:

**Easy (15-20 min each):**
1. [Two Sum](https://leetcode.com/problems/two-sum/)
2. [Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)
3. [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

**Medium (30-40 min each):**
1. [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)
2. [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/)

---

### Step 4: Track Your Progress

Update `PROGRESS_TRACKER.md` with:
- Time spent today
- Problems solved
- Key learnings
- Challenges faced

**Example Entry:**
```markdown
## Day 1 - November 20, 2025

### ⏱️ Time Spent
- Theory/Reading: 30 minutes
- Coding Practice: 90 minutes
- Code Review: 15 minutes
- **Total: 2.25 hours**

### ✅ Completed Tasks
- [x] Warm-up: Two Sum (LeetCode #1)
- [x] Main challenge 1: Remove Duplicates
- [x] Main challenge 2: Maximum Subarray
- [x] Deep dive topic: Vector performance benchmarking

### 💡 Key Learnings
1. reserve() significantly reduces reallocation overhead
2. Kadane's algorithm is elegant DP without explicit table
3. Pass by const reference avoids unnecessary copies
```

---

## 🎯 Daily Routine (2-3 Hours)

### ⏰ Recommended Schedule

**09:00-09:30 (30 min):** Theory & Reading
- Read today's exercise file
- Study relevant sections in BEST_PRACTICES.md
- Review one repo (C-Plus-Plus/, CPlusPlusThings/, etc.)

**09:30-11:00 (90 min):** Hands-On Coding
- Solve today's exercises
- Complete 2-3 LeetCode problems
- Implement TODOs

**11:00-11:30 (30 min):** Code Review & Reflection
- Compare your solution with expert solutions
- Study TheAlgorithms/C-Plus-Plus implementations
- Update progress tracker
- Plan tomorrow's focus

---

## 🛠️ Setup Your Environment

### Install Essential Tools

```bash
# Compiler (if not installed)
sudo apt update
sudo apt install build-essential g++ cmake

# Debugger
sudo apt install gdb

# Memory checker
sudo apt install valgrind

# Code formatter
sudo apt install clang-format

# Testing framework (Catch2)
cd ~/work/viswa/cpp
git clone https://github.com/catchorg/Catch2.git
```

### VS Code Extensions (Recommended)

Install these for better C++ development:
- **C/C++** (Microsoft) - IntelliSense, debugging
- **C++ TestMate** - Test runner
- **CMake Tools** - CMake integration
- **GitLens** - Git visualization
- **Code Spell Checker** - Catch typos in comments

---

## 📚 Using Your Workspace Repositories

### For Learning Patterns:

```bash
# Study STL examples
cd ~/work/viswa/cpp/C-Plus-Plus
# Explore: STL/, Data_Structures/, Algorithm/

# Modern C++ features
cd ~/work/viswa/cpp/CPlusPlusThings
# Check: basic_content/, modern_cpp/

# Best practices
cd ~/work/viswa/cpp/CppCoreGuidelines
# Read the guidelines

# Algorithm implementations
cd ~/work/viswa/cpp/C-Plus-Plus
# Study specific algorithms when needed
```

### For Real-World Projects (Later):

```bash
# OpenCV samples (Week 11-12)
cd ~/work/viswa/automotive/opencv/samples/cpp

# ADAS reference (Week 13-14)
cd ~/work/viswa/automotive/open-adas/src

# Apollo perception (Advanced)
cd ~/work/viswa/automotive/apollo/modules/perception
```

---

## 🎓 Learning Strategies

### 1. **Active Learning**
Don't just read code - type it out, modify it, break it!

### 2. **Spaced Repetition**
Review previous day's concepts for 10 minutes each morning

### 3. **Explain It**
Try explaining concepts to yourself (or a rubber duck!)

### 4. **Build, Don't Just Study**
Every concept learned should be applied in code

### 5. **Debug Everything**
Use gdb to step through complex algorithms:
```bash
gdb ./day01
(gdb) break main
(gdb) run
(gdb) step
(gdb) print variable_name
```

---

## 🚨 Common Pitfalls to Avoid

### ❌ Don't Do This:
1. **Copying without understanding** - Always know WHY code works
2. **Skipping hard problems** - They teach the most
3. **Not testing edge cases** - Empty arrays, single elements, negatives
4. **Ignoring compiler warnings** - They prevent bugs
5. **Perfectionism paralysis** - Better to write imperfect code than none

### ✅ Do This Instead:
1. **Understand first, optimize later**
2. **Test with sample inputs immediately**
3. **Write comments for your future self**
4. **Git commit daily** - "Day X: Completed vector exercises"
5. **Take breaks** - Pomodoro technique (25 min work, 5 min break)

---

## 📊 Measuring Success

### Daily Metrics:
- ✅ Completed scheduled exercises
- ✅ Solved at least 2 problems
- ✅ Updated progress tracker
- ✅ Committed code to Git

### Weekly Metrics:
- ✅ Solved 15+ problems
- ✅ Studied 5+ code examples from repos
- ✅ No day skipped (consistency!)
- ✅ Can explain this week's concepts

### Monthly Metrics:
- ✅ 60+ problems solved
- ✅ Built at least 1 project
- ✅ Portfolio updated on GitHub
- ✅ Noticeable improvement in speed & quality

---

## 💡 Motivation Tips

### When You Feel Stuck:
1. Take a 10-minute walk
2. Explain the problem to someone (or to a rubber duck)
3. Draw diagrams on paper
4. Sleep on it - solutions often come in the morning
5. Ask in communities: r/cpp, Stack Overflow, Discord

### Celebrate Small Wins:
- ✨ First accepted LeetCode solution
- ✨ Solved a problem faster than expected
- ✨ Debugged a tricky bug
- ✨ Completed a full day
- ✨ One week streak!

### Remember:
> "Debugging is twice as hard as writing the code in the first place. Therefore, if you write the code as cleverly as possible, you are, by definition, not smart enough to debug it." - Brian Kernighan

**Write simple, clear code!**

---

## 🔥 Day 1 Checklist

Before you finish today:
- [ ] Compiled and ran day01_vectors_algorithms.cpp
- [ ] Understood all 4 main exercises
- [ ] Completed at least 1 TODO function
- [ ] Solved 2 problems on LeetCode
- [ ] Updated PROGRESS_TRACKER.md
- [ ] Git commit with message "Day 1: Vector mastery complete"
- [ ] Planned which concepts to cover tomorrow

---

## 🗓️ Tomorrow (Day 2): Maps & Hash Tables

**Preview:**
- unordered_map vs map
- Hash function basics
- Collision handling
- Problems: Valid Anagram, Group Anagrams, Longest Substring

**Preparation:**
- Read BEST_PRACTICES.md section on containers
- Explore C-Plus-Plus/STL/Map/ examples

---

## 🆘 Need Help?

### Resources:
- **Documentation:** https://en.cppreference.com/
- **Visualizer:** https://pythontutor.com/cpp.html
- **Compiler Explorer:** https://godbolt.org/
- **Algorithms:** https://visualgo.net/

### Your Workspace:
- Check `CppCoreGuidelines/` for best practices
- Study `TheAlgorithms/C-Plus-Plus` for implementations
- Review `CPlusPlusThings/` for modern C++ features

---

## 🚀 Ready? Let's Begin!

```bash
cd /home/23u58g/work/viswa/cpp/100-day-challenge/week-01
g++ -std=c++17 -Wall -Wextra -O2 day01_vectors_algorithms.cpp -o day01
./day01
```

**Your 100-day journey starts NOW! 💪**

---

## 📝 Quick Commands Reference

```bash
# Compile with debugging symbols
g++ -std=c++17 -g -Wall file.cpp -o output

# Compile with optimizations
g++ -std=c++17 -O2 -Wall file.cpp -o output

# Check for memory leaks
valgrind --leak-check=full ./output

# Debug with gdb
gdb ./output

# Format code
clang-format -i file.cpp

# Run with AddressSanitizer
g++ -fsanitize=address -g file.cpp -o output && ./output
```

---

**Good luck! Remember: consistency over intensity. See you tomorrow for Day 2! 🎯**
