# MASTER INDEX — C++ Problem Solving Prompt Library
## Book-Alike Deep Learning Guide: All Levels (0–10)

---

## What Is This Library?

This is a **multi-document AI prompt library** designed to generate a complete, book-quality C++ learning resource — one problem/topic at a time. Each prompt file targets a specific skill range and contains:

1. **A master generation prompt** — paste into any AI (ChatGPT, Claude, Gemini, Copilot) with a problem name to get a full book chapter.
2. **A batch generation prompt** — generate an entire category at once.
3. **A complete problem bank** — every problem/topic for that level range.
4. **Supplementary problems** — additions from LeetCode, GeeksForGeeks, GitHub, Codeforces.
5. **A learning roadmap** — week-by-week study plan.
6. **Curated resources** — books, YouTube, GitHub repositories.

---

## Prompt Files

| File | Levels | Titles | Categories | Total Problems |
|------|--------|--------|------------|----------------|
| [PROMPT_01_Level0_Level1_Beginner.md](PROMPT_01_Level0_Level1_Beginner.md) | 0 + 1 | Absolute Beginner + Beginner | C00, C01, C10, C11, C12 | ~595 |
| [PROMPT_02_Level2_Level3_Elementary_Intermediate.md](PROMPT_02_Level2_Level3_Elementary_Intermediate.md) | 2 + 3 | Elementary + Intermediate | C20, C21, C22, C30, C31, C32 | ~705 |
| [PROMPT_03_Level4_Level5_UpperInt_Advanced.md](PROMPT_03_Level4_Level5_UpperInt_Advanced.md) | 4 + 5 | Upper Intermediate + Advanced | C40, C41, C50, C51 | ~525 |
| [PROMPT_04_Level6_Level7_UpperAdv_Expert.md](PROMPT_04_Level6_Level7_UpperAdv_Expert.md) | 6 + 7 | Upper Advanced + Expert | C60, C61, C70, C71 | ~490 |
| [PROMPT_05_Level8_Level9_UpperExpert_Pro.md](PROMPT_05_Level8_Level9_UpperExpert_Pro.md) | 8 + 9 | Upper Expert + Pro | C80, C81, C90 | ~400 |
| [PROMPT_06_Level10_ElitePro_Master.md](PROMPT_06_Level10_ElitePro_Master.md) | 10 | Elite Pro / Master | C100 | ~120 |

**Total: ~2,835+ problems and topics across all 11 levels**

---

## Level → Prompt Mapping

```
Level 0 (Absolute Beginner) ──► PROMPT_01
Level 1 (Beginner)          ──► PROMPT_01
Level 2 (Elementary)        ──► PROMPT_02
Level 3 (Intermediate)      ──► PROMPT_02
Level 4 (Upper Intermediate)──► PROMPT_03
Level 5 (Advanced)          ──► PROMPT_03
Level 6 (Upper Advanced)    ──► PROMPT_04
Level 7 (Expert)            ──► PROMPT_04
Level 8 (Upper Expert)      ──► PROMPT_05
Level 9 (Pro)               ──► PROMPT_05
Level 10 (Elite Pro/Master) ──► PROMPT_06
```

---

## Category Map

| ID | Category Name | Level | Prompt File |
|----|--------------|-------|-------------|
| C00 | C++ Syntax & Program Structure | 0 | PROMPT_01 |
| C01 | Data Types & Variables | 0 | PROMPT_01 |
| C10 | Control Flow & Loops | 1 | PROMPT_01 |
| C11 | Functions & Recursion | 1 | PROMPT_01 |
| C12 | Arrays & Strings (Core) | 1 | PROMPT_01 |
| C20 | Pointers & Memory Management | 2 | PROMPT_02 |
| C21 | OOP — Classes & Objects | 2 | PROMPT_02 |
| C22 | STL Containers & Iterators | 2 | PROMPT_02 |
| C30 | Linked Lists | 3 | PROMPT_02 |
| C31 | Stacks & Queues | 3 | PROMPT_02 |
| C32 | Hashing & Hash Tables | 3 | PROMPT_02 |
| C40 | Trees & Binary Search Trees | 4 | PROMPT_03 |
| C41 | Graphs — Fundamentals & Traversal | 4 | PROMPT_03 |
| C50 | Dynamic Programming | 5 | PROMPT_03 |
| C51 | Heaps, Priority Queues & Advanced Sorting | 5 | PROMPT_03 |
| C60 | Advanced Trees (Segment Tree, Fenwick, Trie, etc.) | 6 | PROMPT_04 |
| C61 | Advanced Graph Algorithms | 6 | PROMPT_04 |
| C70 | Templates & Generic Programming | 7 | PROMPT_04 |
| C71 | Concurrency & Multithreading | 7 | PROMPT_04 |
| C80 | Advanced Algorithms (String, Math, Number Theory) | 8 | PROMPT_05 |
| C81 | System Design & Low-Level C++ | 8 | PROMPT_05 |
| C90 | Competitive Programming Mastery | 9 | PROMPT_05 |
| C100 | Expert / Research-Level C++ & CS | 10 | PROMPT_06 |

---

## How to Generate a Single Problem Chapter

### Step 1: Find the problem
Browse the problem bank in the appropriate PROMPT file.

### Step 2: Copy the master prompt
Open the PROMPT file → copy the `===...===` block.

### Step 3: Fill in the problem name
Replace `{{PROBLEM_NAME}}` or `{{TOPIC_NAME}}` with the exact problem text.

### Step 4: Paste and generate
Paste into your AI of choice. You'll get a complete chapter with:
- Problem statement + examples
- Mental model + intuition
- Multiple solution approaches (brute force → optimal)
- Full C++17 code with comments
- Complexity analysis
- Edge cases + pitfalls
- Pattern recognition
- Practice variants
- Interview tips
- Quick reference card

---

## How to Generate an Entire Category

1. Open the PROMPT file for the desired level.
2. Copy the **Batch Generation Prompt** (`===...===` block).
3. Replace `{{CATEGORY_NAME}}` and paste the full problem list from that category's section.
4. The AI generates a mini-chapter per problem with consistent formatting.

**Pro tip:** For large categories (100+ problems), split into groups of 20–30 for better output quality.

---

## Recommended Workflow

### For Interview Preparation
```
1. Identify target level (e.g., aiming for senior SWE = Levels 3–6)
2. Open PROMPT_02 and PROMPT_03
3. Generate chapters for each problem you attempt
4. Fill in the self-study template (in PROMPT_01) after each problem
5. Track patterns: maintain a pattern recognition log
```

### For Competitive Programming
```
1. Start at PROMPT_03 (Level 4–5) if you know basics
2. Work through C50 (DP) systematically
3. Move to PROMPT_04 (C60, C61) for advanced DS/Graph
4. Graduate to PROMPT_05 (C90) for contest-level mastery
```

### For System/Embedded Engineering
```
1. Ensure C20+C21+C22 mastery (PROMPT_02)
2. Deep-dive C81 (System Design & Low-Level C++) via PROMPT_05
3. Study C71 (Concurrency) via PROMPT_04
4. Reach for C100 (kernel/RTOS) via PROMPT_06
```

### For General Knowledge Growth (1 problem/day)
```
Day 1: Open today's level prompt
Day 2: Generate chapter for one problem
Day 3: Implement it yourself (no looking at the chapter)
Day 4: Compare your impl to the chapter
Day 5: Solve 2 practice variants from the chapter
Day 6: Write your own "Quick Reference Card" from memory
Day 7: Rest / Review week's cards
```

---

## Templates

### Self-Study Log Template
```markdown
## Problem: [NAME]
**Date:** ___________  
**Level:** ___  
**Category:** ___  
**Source:** LeetCode # / GFG / Codeforces  

### Before Looking at Solution
My approach:
My code (sketch):
What I got stuck on:

### After Generating Chapter
Key insight I was missing:
Pattern this belongs to:
Similar problems to practice:

### Status
- [ ] Solved from scratch without hints
- [ ] Solved with pattern hint
- [ ] Solved with approach hint  
- [ ] Still need to review
```

### Pattern Recognition Log Template
```markdown
## Pattern: [NAME]
**Level introduced:** ___  
**Trigger:** When I see _______, I think _______  

**Core technique:** ___  
**Time complexity:** O(?)  
**Problems using this pattern:**
1. 
2. 
3. 
4. 
5. 
```

---

## Progress Tracker

Copy and maintain this in your notes:

```
Level 0 (C00): ___/120 | Level 0 (C01): ___/110
Level 1 (C10): ___/115 | Level 1 (C11): ___/120 | Level 1 (C12): ___/130
Level 2 (C20): ___/125 | Level 2 (C21): ___/120 | Level 2 (C22): ___/130
Level 3 (C30): ___/120 | Level 3 (C31): ___/115 | Level 3 (C32): ___/110
Level 4 (C40): ___/140 | Level 4 (C41): ___/125
Level 5 (C50): ___/150 | Level 5 (C51): ___/110
Level 6 (C60): ___/130 | Level 6 (C61): ___/120
Level 7 (C70): ___/120 | Level 7 (C71): ___/120
Level 8 (C80): ___/130 | Level 8 (C81): ___/120
Level 9 (C90): ___/150
Level 10 (C100): ___/120

TOTAL: ___/2835
```

---

## Quick Reference: AI Prompt Parameters

When generating chapters, you can customize the prompt:

| Parameter | Options | Effect |
|-----------|---------|--------|
| Code style | `competitive`, `production`, `both` | Output style |
| Depth | `brief`, `standard`, `deep-dive` | Chapter length |
| Language version | `C++11`, `C++14`, `C++17`, `C++20`, `C++23` | Standard used |
| Domain focus | `embedded`, `FAANG-interview`, `CP-contest`, `automotive` | Examples and emphasis |
| Math level | `intuition-only`, `proof-sketch`, `full-proof` | Rigor level |

Add these to any prompt: *"Focus on: {{PARAMETER}} = {{VALUE}}"*

---

## File Sizes & Contents Summary

```
PROMPT_01  ~600 problems  — Syntax, Types, Control Flow, Functions, Arrays
PROMPT_02  ~705 problems  — Memory, OOP, STL, Lists, Stacks, Hashing
PROMPT_03  ~525 problems  — Trees, Graphs, DP, Heaps, Sorting
PROMPT_04  ~490 problems  — Seg Trees, Advanced Graphs, Templates, Concurrency
PROMPT_05  ~400 problems  — String/Math Algorithms, Systems, CP Mastery
PROMPT_06  ~120 topics    — Language evolution, FP theory, Compilers, Distributed

Total: ~2,840 problems + topics
```

---

*Last updated: April 2026*  
*Based on: cpp_interview_prep.jsx — 11 levels, 23 categories*
