# 🚀 100-Day C++ Coding Challenge

**Start Date:** November 20, 2025  
**End Date:** February 27, 2026  
**Daily Commitment:** 2-3 hours

---

## 📂 Directory Structure

```
100-day-challenge/
├── README.md                           # You are here
├── QUICK_START.md                      # How to begin Day 1
├── 100_DAY_CPP_CHALLENGE.md           # Full 14-week roadmap
├── BEST_PRACTICES.md                   # Code patterns & snippets
├── PROJECT_IDEAS.md                    # 12 projects for days 50-100
├── PROGRESS_TRACKER.md                 # Daily tracking template
│
├── week-01/                            # Days 1-7: STL & Algorithms
│   ├── day01_vectors_algorithms.cpp    ✅ Created!
│   ├── day02_maps_sets.cpp            # Coming soon
│   └── ...
│
├── week-02/                            # Days 8-14
├── week-03/                            # Days 15-21
│   ...
├── week-14/                            # Days 92-100
│
└── projects/                           # Your capstone projects
    ├── lane-detection/
    ├── task-manager/
    └── ...
```

---

## 🎯 Challenge Goals

By Day 100, you will:
- ✅ Solve 200+ algorithmic problems
- ✅ Master modern C++ (C++11/14/17/20)
- ✅ Build 5+ portfolio projects
- ✅ Understand STL deeply
- ✅ Apply OOP & design patterns
- ✅ Integrate with OpenCV & automotive systems
- ✅ Write production-quality code

---

## 📚 What's Included

### 1️⃣ **Comprehensive Roadmap**
14-week structured plan with daily topics and exercises.

### 2️⃣ **Hands-On Exercises**
Working C++ code with detailed comments, explanations, and TODOs.

### 3️⃣ **Best Practices Guide**
Memory management, smart pointers, RAII, move semantics, templates.

### 4️⃣ **Project Ideas**
12 real-world projects: ADAS tools, CLI utilities, game engines, web servers.

### 5️⃣ **Progress Tracking**
Templates to measure daily/weekly growth and celebrate milestones.

---

## 🚀 Getting Started

### Option 1: Start Immediately
```bash
cd week-01
g++ -std=c++17 -Wall -Wextra -O2 day01_vectors_algorithms.cpp -o day01
./day01
```

### Option 2: Read the Roadmap First
```bash
# Open in your editor
code 100_DAY_CPP_CHALLENGE.md
code QUICK_START.md
```

### Option 3: Understand Best Practices
```bash
# Study code patterns
code BEST_PRACTICES.md
```

---

## 📖 Learning Path

### Phase 1: Foundations (Days 1-30)
**Focus:** STL, algorithms, problem-solving patterns

**Topics:**
- Vectors, strings, arrays
- Maps, sets, hash tables
- Iterators & algorithms
- Stack, queue, priority_queue
- Recursion & backtracking
- Dynamic programming
- Graph algorithms
- Trees & tries

**Outcome:** Comfortable solving medium LeetCode problems

---

### Phase 2: Advanced C++ (Days 31-50)
**Focus:** Modern C++ features, design patterns

**Topics:**
- Smart pointers (unique_ptr, shared_ptr, weak_ptr)
- Move semantics & perfect forwarding
- RAII & Rule of Five
- Templates & generic programming
- Lambda expressions
- SOLID principles
- Design patterns (Factory, Observer, Strategy, etc.)
- Multithreading basics

**Outcome:** Write production-quality, maintainable code

---

### Phase 3: Projects (Days 51-100)
**Focus:** Real-world applications, integration

**Projects:**
- **Automotive:** Lane detection, object tracking, CAN parser
- **Systems:** Thread pool, memory allocator, version control
- **Game Dev:** 2D physics engine, ECS architecture
- **Network:** HTTP server, key-value store
- **CLI Tools:** Task manager, code profiler

**Outcome:** Portfolio-ready projects on GitHub

---

## 📊 Success Metrics

### Daily (2-3 hours)
- [ ] Complete scheduled exercises
- [ ] Solve 2-3 problems
- [ ] Study 1 code example from workspace repos
- [ ] Update progress tracker

### Weekly
- [ ] 15+ problems solved
- [ ] All concepts understood
- [ ] Weekly summary completed
- [ ] No days skipped

### Monthly
- [ ] 60+ problems solved
- [ ] 1 project completed
- [ ] GitHub portfolio updated
- [ ] Measurable skill improvement

---

## 🛠️ Tools & Setup

### Required
- **Compiler:** g++ or clang++ (C++17 or later)
- **Build System:** CMake (optional but recommended)
- **Version Control:** Git

### Recommended
- **Debugger:** gdb or lldb
- **Memory Checker:** Valgrind
- **Formatter:** clang-format
- **Testing:** Catch2
- **Editor:** VS Code with C++ extensions

### Installation
```bash
# Ubuntu/Debian
sudo apt install build-essential cmake gdb valgrind clang-format

# macOS
brew install gcc cmake gdb llvm

# Verify
g++ --version
cmake --version
```

---

## 📂 Using Your Workspace

You have excellent repositories to learn from:

### For Learning Patterns:
- **C-Plus-Plus/** - STL examples, data structures
- **CPlusPlusThings/** - Modern C++ features
- **CppCoreGuidelines/** - Best practices
- **TheAlgorithms/C-Plus-Plus** - Algorithm implementations
- **design-patterns-cpp/** - Design pattern examples

### For Real-World Reference:
- **opencv/** - Computer vision (weeks 11-12)
- **open-adas/** - ADAS algorithms (weeks 13-14)
- **apollo/** - Autonomous driving framework
- **autoware/** - ROS2-based autonomous vehicle platform
- **openpilot/** - Advanced driver assistance

**Strategy:** Study these repos when working on related topics!

---

## 💡 Tips for Success

### 1. **Consistency Over Intensity**
Better to code 2 hours daily than 14 hours once a week.

### 2. **Understand, Don't Memorize**
Ask "why?" for every line of code.

### 3. **Test Everything**
Edge cases reveal understanding gaps.

### 4. **Refactor Later**
Make it work first, then make it clean, then make it fast.

### 5. **Learn from Others**
Study expert code in your workspace repos.

### 6. **Track Progress**
Update PROGRESS_TRACKER.md daily - it's motivating!

### 7. **Take Breaks**
Pomodoro technique: 25 min work, 5 min break.

### 8. **Celebrate Wins**
Solved a hard problem? Commit it with a proud message!

---

## 🎯 Milestone Rewards

- **Day 10:** You understand STL! 🎉
- **Day 25:** 50+ problems solved! 🏆
- **Day 50:** Mid-challenge, you're halfway there! 🎖️
- **Day 75:** Advanced C++ mastery! 🚀
- **Day 100:** Challenge complete, portfolio ready! 🎊

---

## 📞 Getting Help

### When Stuck:
1. Read the problem 3 times
2. Draw on paper
3. Check BEST_PRACTICES.md
4. Study similar examples in workspace repos
5. Debug with gdb
6. Search on cppreference.com
7. Ask on r/cpp or Stack Overflow

### Resources:
- **Documentation:** https://en.cppreference.com/
- **Visualizer:** https://pythontutor.com/cpp.html
- **Compiler Explorer:** https://godbolt.org/
- **Algorithms:** https://visualgo.net/

---

## 🌟 What Makes This Different?

### Not Just LeetCode:
While problem-solving is important, you'll also:
- Build real projects
- Learn production patterns
- Study actual codebases (Apollo, OpenCV, etc.)
- Integrate with industry tools

### Mentor-Style Learning:
- **Logic explanations:** Understand WHY, not just HOW
- **Alternative approaches:** Learn multiple solutions
- **Common mistakes:** Avoid pitfalls
- **Performance tips:** Write efficient code

### Career-Ready:
By Day 100, you'll have:
- Portfolio projects on GitHub
- Deep understanding of modern C++
- Experience with real-world codebases
- Interview readiness

---

## 🔥 Ready to Begin?

### Day 1 Starts Now!

```bash
cd /home/23u58g/work/viswa/cpp/100-day-challenge
cat QUICK_START.md

# Then dive in:
cd week-01
./day01
```

---

## 📅 Quick Links

- [Start Here - Day 1 Guide](./QUICK_START.md)
- [Full 100-Day Plan](./100_DAY_CPP_CHALLENGE.md)
- [Code Best Practices](./BEST_PRACTICES.md)
- [Project Ideas](./PROJECT_IDEAS.md)
- [Progress Tracker](./PROGRESS_TRACKER.md)

---

## 💬 Final Words

> "The only way to learn a new programming language is by writing programs in it." - Dennis Ritchie

You have everything you need. The roadmap is clear, the exercises are ready, and your workspace is full of excellent learning resources.

**Now it's time to code.**

Start small. Stay consistent. Trust the process.

See you at Day 100! 🚀💪

---

**Happy Coding!**
*Your C++ Mentor* 🎓
