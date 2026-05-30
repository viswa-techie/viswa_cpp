# Day 4 Quick Reference: Stacks, Queues, Deques

## 📚 Core Data Structures

### Stack (LIFO - Last In First Out)
```cpp
#include <stack>

stack<int> st;
st.push(5);        // Add to top - O(1)
st.pop();          // Remove from top - O(1)
int x = st.top();  // Access top - O(1)
bool empty = st.empty();
size_t sz = st.size();
```

**When to Use:**
- Function call tracking, recursion
- Expression evaluation (postfix, infix)
- Bracket matching, syntax parsing
- Undo/redo operations
- Backtracking algorithms

### Queue (FIFO - First In First Out)
```cpp
#include <queue>

queue<int> q;
q.push(5);          // Add to back - O(1)
q.pop();            // Remove from front - O(1)
int x = q.front();  // Access front - O(1)
int y = q.back();   // Access back - O(1)
bool empty = q.empty();
size_t sz = q.size();
```

**When to Use:**
- BFS traversal
- Task scheduling, job queues
- Buffering data streams
- Level-order processing

### Deque (Double-Ended Queue)
```cpp
#include <deque>

deque<int> dq;
dq.push_back(5);     // Add to back - O(1)
dq.push_front(3);    // Add to front - O(1)
dq.pop_back();       // Remove from back - O(1)
dq.pop_front();      // Remove from front - O(1)
int x = dq.front();  // Access front - O(1)
int y = dq.back();   // Access back - O(1)
int z = dq[i];       // Random access - O(1)
```

**When to Use:**
- Sliding window maximum/minimum
- Maintaining monotonic order
- Work-stealing queues
- Palindrome checking

### Priority Queue (Heap)
```cpp
#include <queue>

// Max heap (default)
priority_queue<int> maxHeap;
maxHeap.push(5);        // O(log n)
int max = maxHeap.top(); // O(1)
maxHeap.pop();          // O(log n)

// Min heap
priority_queue<int, vector<int>, greater<int>> minHeap;
minHeap.push(5);
int min = minHeap.top();

// Custom comparator
auto cmp = [](int a, int b) { return a > b; };
priority_queue<int, vector<int>, decltype(cmp)> pq(cmp);
```

**When to Use:**
- Top K elements
- Merge K sorted arrays/lists
- Median tracking (two heaps)
- Dijkstra's algorithm, A* search
- Event scheduling

---

## 🎯 Essential Patterns

### 1. Monotonic Stack Pattern
**Purpose:** Find next greater/smaller element in O(n)

```cpp
// Next Greater Element
vector<int> nextGreater(const vector<int>& nums) {
    int n = nums.size();
    vector<int> result(n, -1);
    stack<int> st;  // Store indices
    
    for (int i = 0; i < n; ++i) {
        // Pop smaller elements - they found their next greater
        while (!st.empty() && nums[st.top()] < nums[i]) {
            result[st.top()] = nums[i];
            st.pop();
        }
        st.push(i);
    }
    
    return result;
}
```

**Key Insight:** Maintain stack in monotonic order (increasing/decreasing)

**Variations:**
- Next Greater → Decreasing stack, pop when current > top
- Next Smaller → Increasing stack, pop when current < top
- Previous Greater → Same but traverse right to left

**Applications:**
- Daily Temperatures (LC 739)
- Stock Span Problem
- Largest Rectangle in Histogram (LC 84)

### 2. Sliding Window with Deque
**Purpose:** Find max/min in each sliding window in O(n)

```cpp
// Sliding Window Maximum
vector<int> maxSlidingWindow(const vector<int>& nums, int k) {
    deque<int> dq;  // Store indices in decreasing order of values
    vector<int> result;
    
    for (int i = 0; i < nums.size(); ++i) {
        // Remove elements outside window
        if (!dq.empty() && dq.front() <= i - k) {
            dq.pop_front();
        }
        
        // Remove smaller elements (they'll never be max)
        while (!dq.empty() && nums[dq.back()] < nums[i]) {
            dq.pop_back();
        }
        
        dq.push_back(i);
        
        if (i >= k - 1) {
            result.push_back(nums[dq.front()]);
        }
    }
    
    return result;
}
```

**Key Insight:** Deque maintains candidates in monotonic order

**Why Deque?**
- Need to remove from both ends
- O(1) operations on both ends
- Can't use stack (need front removal) or queue (need back removal)

### 3. Min/Max Stack Pattern
**Purpose:** Get minimum/maximum in O(1) alongside push/pop

```cpp
class MinStack {
    stack<int> dataStack;
    stack<int> minStack;
    
public:
    void push(int val) {
        dataStack.push(val);
        if (minStack.empty() || val <= minStack.top()) {
            minStack.push(val);
        }
    }
    
    void pop() {
        if (dataStack.top() == minStack.top()) {
            minStack.pop();
        }
        dataStack.pop();
    }
    
    int top() { return dataStack.top(); }
    int getMin() { return minStack.top(); }
};
```

**Key Insight:** Auxiliary stack tracks extremes

### 4. Two Heaps Pattern (Median Tracking)
**Purpose:** Find median in O(1) with O(log n) insertions

```cpp
class MedianFinder {
    priority_queue<int> maxHeap;  // Left half
    priority_queue<int, vector<int>, greater<int>> minHeap;  // Right half
    
public:
    void addNum(int num) {
        maxHeap.push(num);
        minHeap.push(maxHeap.top());
        maxHeap.pop();
        
        if (minHeap.size() > maxHeap.size()) {
            maxHeap.push(minHeap.top());
            minHeap.pop();
        }
    }
    
    double findMedian() {
        return maxHeap.size() > minHeap.size() 
            ? maxHeap.top() 
            : (maxHeap.top() + minHeap.top()) / 2.0;
    }
};
```

**Key Insight:** Balance two heaps to keep sizes equal or diff = 1

**Invariants:**
- Max heap size ≥ min heap size
- All elements in max heap ≤ all in min heap
- Median = max heap top (odd) or average (even)

### 5. K-Way Merge Pattern
**Purpose:** Merge K sorted arrays/lists efficiently

```cpp
// Merge K Sorted Lists
ListNode* mergeKLists(vector<ListNode*>& lists) {
    auto cmp = [](ListNode* a, ListNode* b) {
        return a->val > b->val;  // Min heap
    };
    priority_queue<ListNode*, vector<ListNode*>, decltype(cmp)> pq(cmp);
    
    // Add first node of each list
    for (ListNode* list : lists) {
        if (list) pq.push(list);
    }
    
    ListNode dummy(0);
    ListNode* tail = &dummy;
    
    while (!pq.empty()) {
        ListNode* node = pq.top();
        pq.pop();
        
        tail->next = node;
        tail = tail->next;
        
        if (node->next) {
            pq.push(node->next);
        }
    }
    
    return dummy.next;
}
```

**Complexity:** O(N log K) where N = total elements, K = number of lists

---

## ⚡ Time Complexity Cheat Sheet

| Operation | Stack | Queue | Deque | Priority Queue |
|-----------|-------|-------|-------|----------------|
| Push/Insert | O(1) | O(1) | O(1) | O(log n) |
| Pop/Delete | O(1) | O(1) | O(1) | O(log n) |
| Peek/Top | O(1) | O(1) | O(1) | O(1) |
| Search | O(n) | O(n) | O(n) | O(n) |
| Random Access | ❌ | ❌ | O(1) | ❌ |

### Problem Type → Data Structure Mapping

| Problem Type | Best Data Structure | Complexity |
|--------------|---------------------|------------|
| Next Greater/Smaller Element | Monotonic Stack | O(n) |
| Sliding Window Max/Min | Deque | O(n) |
| Top K Elements | Min/Max Heap | O(n log k) |
| Kth Largest in Stream | Min Heap (size k) | O(log k) per insert |
| Median in Stream | Two Heaps | O(log n) insert, O(1) find |
| Valid Parentheses | Stack | O(n) |
| BFS Traversal | Queue | O(V + E) |
| Merge K Sorted | Priority Queue | O(N log K) |
| Task Scheduling | Queue/Priority Queue | O(n log n) |

---

## 🔥 Common Mistakes to Avoid

### 1. Forgetting to Check Empty
```cpp
// ❌ WRONG
int x = st.top();  // Crash if empty!

// ✅ CORRECT
if (!st.empty()) {
    int x = st.top();
}
```

### 2. Monotonic Stack: Using Values Instead of Indices
```cpp
// ❌ WRONG - Can't track position
stack<int> st;
st.push(nums[i]);

// ✅ CORRECT - Store indices
stack<int> st;
st.push(i);  // Access value with nums[st.top()]
```

### 3. Sliding Window: Not Removing Out-of-Window Elements
```cpp
// ❌ WRONG - Old elements stay in deque
while (!dq.empty() && nums[dq.back()] < nums[i]) {
    dq.pop_back();
}

// ✅ CORRECT - Remove first
if (!dq.empty() && dq.front() <= i - k) {
    dq.pop_front();
}
```

### 4. Priority Queue: Wrong Comparator
```cpp
// ❌ WRONG - Still max heap!
priority_queue<int, vector<int>, less<int>> pq;

// ✅ CORRECT - Min heap
priority_queue<int, vector<int>, greater<int>> pq;
```

### 5. Circular Queue: Incorrect Size Tracking
```cpp
// ❌ WRONG - Can't distinguish empty from full
tail = (tail + 1) % capacity;

// ✅ CORRECT - Track size separately
tail = (tail + 1) % capacity;
size++;
```

---

## 🎯 Problem-Solving Decision Tree

```
Need to find next greater/smaller?
├─ YES → Monotonic Stack
└─ NO ↓

Need max/min in sliding window?
├─ YES → Deque (monotonic)
└─ NO ↓

Need top K elements?
├─ YES → Min/Max Heap (size K)
└─ NO ↓

Need median from stream?
├─ YES → Two Heaps (max + min)
└─ NO ↓

Need to merge K sorted?
├─ YES → Priority Queue (K-way merge)
└─ NO ↓

Need to match brackets/validate syntax?
├─ YES → Stack
└─ NO ↓

Need BFS traversal?
├─ YES → Queue
└─ NO ↓

Need undo/redo functionality?
├─ YES → Stack
└─ NO ↓

Need task scheduling with priorities?
└─ YES → Priority Queue
```

---

## 📖 LeetCode Problem Roadmap

### Easy (Foundations)
- [20] Valid Parentheses ⭐
- [225] Implement Stack using Queues
- [232] Implement Queue using Stacks
- [703] Kth Largest Element in Stream

### Medium (Core Patterns)
- [155] Min Stack ⭐
- [739] Daily Temperatures ⭐
- [496] Next Greater Element I ⭐
- [503] Next Greater Element II
- [239] Sliding Window Maximum ⭐⭐
- [622] Design Circular Queue
- [215] Kth Largest Element
- [347] Top K Frequent Elements
- [1696] Jump Game VI
- [295] Find Median from Data Stream ⭐⭐

### Hard (Mastery)
- [84] Largest Rectangle in Histogram ⭐⭐
- [85] Maximal Rectangle
- [862] Shortest Subarray with Sum at Least K ⭐⭐
- [480] Sliding Window Median
- [23] Merge K Sorted Lists ⭐
- [1425] Constrained Subsequence Sum

**Legend:**
- ⭐ Must practice
- ⭐⭐ Advanced pattern (interview favorite)

---

## 💡 Pro Tips

1. **Monotonic Stack:** If problem asks "next greater/smaller", think monotonic stack first
2. **Deque over Queue:** When you need both front AND back operations efficiently
3. **Two Heaps Trick:** Perfect for median, order statistics
4. **Index vs Value:** Store indices in stack/deque when you need position info
5. **Circular Buffer:** Use `(index + 1) % capacity` for wraparound
6. **Space Optimization:** MinStack can be done with single stack (store differences)

---

## 🔗 Related Topics for Next Days
- **Day 5:** Recursion and Backtracking (uses call stack)
- **Day 6:** Binary Trees (BFS uses queue)
- **Day 7:** Graphs (BFS/DFS with stack/queue)
- **Week 2:** Dynamic Programming (monotonic stack optimizations)

---

**Remember:** These data structures are tools. Master the patterns, then recognize which tool fits each problem! 🚀
