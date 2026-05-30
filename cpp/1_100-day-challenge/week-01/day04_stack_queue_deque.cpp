/*
 * ============================================================================
 * DAY 4: STACKS, QUEUES, AND DEQUES - LINEAR DATA STRUCTURES
 * ============================================================================
 * Focus: LIFO/FIFO patterns, Monotonic Stack, Sliding Window with Deque
 * Duration: 2-3 hours
 * Difficulty: ⭐⭐⭐ (Medium)
 * 
 * Learning Path:
 * 1. Stack basics and applications (brackets, calculator, undo/redo)
 * 2. Queue patterns (BFS preparation, task scheduling)
 * 3. Deque for sliding window maximum (O(n) solution)
 * 4. Monotonic stack for next greater element problems
 * 
 * Compilation: g++ -std=c++17 -Wall -Wextra -O2 -g day04_stack_queue_deque.cpp -o day04
 * Run: ./day04
 * ============================================================================
 */

#include <iostream>
#include <stack>
#include <queue>
#include <deque>
#include <vector>
#include <string>
#include <unordered_map>
#include <algorithm>
#include <sstream>
#include <cctype>

using namespace std;

// ============================================================================
// SECTION 1: STACK FUNDAMENTALS
// ============================================================================
// Stack: LIFO (Last In First Out)
// Operations: push O(1), pop O(1), top O(1)
// Use cases: Function calls, expression evaluation, backtracking, undo/redo

namespace StackBasics {
    
    // --- Exercise 1.1: Valid Parentheses (LeetCode 20) ---
    // Given string with brackets (), [], {}, determine if valid
    // Valid: all open brackets closed in correct order
    // Examples: "()" → true, "()[]{}" → true, "(]" → false, "([)]" → false
    
    bool isValid(const string& s) {
        stack<char> st;
        unordered_map<char, char> pairs = {
            {')', '('},
            {']', '['},
            {'}', '{'}
        };
        
        for (char c : s) {
            // If closing bracket
            if (pairs.count(c)) {
                // Check if stack empty or top doesn't match
                if (st.empty() || st.top() != pairs[c]) {
                    return false;
                }
                st.pop();
            } else {
                // Opening bracket - push to stack
                st.push(c);
            }
        }
        
        // Valid only if all brackets matched (stack empty)
        return st.empty();
    }
    
    // --- Exercise 1.2: Min Stack (LeetCode 155) ---
    // Design stack supporting push, pop, top, and retrieving minimum in O(1)
    // Approach: Keep auxiliary stack tracking minimums
    
    class MinStack {
    private:
        stack<int> dataStack;
        stack<int> minStack;  // Tracks minimums
        
    public:
        MinStack() {}
        
        void push(int val) {
            dataStack.push(val);
            // Push to minStack if empty or new minimum found
            if (minStack.empty() || val <= minStack.top()) {
                minStack.push(val);
            }
        }
        
        void pop() {
            if (dataStack.empty()) return;
            
            // If popping current minimum, remove from minStack too
            if (dataStack.top() == minStack.top()) {
                minStack.pop();
            }
            dataStack.pop();
        }
        
        int top() {
            return dataStack.top();
        }
        
        int getMin() {
            return minStack.top();
        }
    };
    
    // TODO: Implement space-optimized MinStack using single stack
    // Hint: Store differences from current minimum
    class MinStackOptimized {
    private:
        stack<long long> st;
        long long currentMin;
        
    public:
        MinStackOptimized() : currentMin(0) {}
        
        void push(int val) {
            // YOUR CODE HERE
            // Hint: If val < currentMin, push (val - currentMin) and update currentMin
        }
        
        void pop() {
            // YOUR CODE HERE
            // Hint: If top < 0, it's encoded; restore previous min
        }
        
        int top() {
            // YOUR CODE HERE
            return 0;
        }
        
        int getMin() {
            // YOUR CODE HERE
            return 0;
        }
    };
    
    // --- Exercise 1.3: Evaluate Reverse Polish Notation (LeetCode 150) ---
    // Evaluate expression in postfix notation
    // Example: ["2","1","+","3","*"] → ((2+1)*3) = 9
    
    int evalRPN(const vector<string>& tokens) {
        stack<int> st;
        
        for (const string& token : tokens) {
            // Check if operator
            if (token == "+" || token == "-" || token == "*" || token == "/") {
                int b = st.top(); st.pop();
                int a = st.top(); st.pop();
                
                if (token == "+") st.push(a + b);
                else if (token == "-") st.push(a - b);
                else if (token == "*") st.push(a * b);
                else st.push(a / b);
            } else {
                // Number - push to stack
                st.push(stoi(token));
            }
        }
        
        return st.top();
    }
    
    // TODO: Implement infix to postfix converter
    // Convert "3 + 4 * 2" → "3 4 2 * +"
    // Hint: Use operator precedence map and stack
    string infixToPostfix(const string& infix) {
        // YOUR CODE HERE
        return "";
    }
    
    void demonstrate() {
        cout << "\n=== SECTION 1: STACK FUNDAMENTALS ===\n";
        
        // Valid Parentheses
        cout << "\n1. Valid Parentheses:\n";
        vector<string> testCases = {"()", "()[]{}", "(]", "([)]", "{[]}"};
        for (const auto& test : testCases) {
            cout << "  \"" << test << "\" → " 
                 << (isValid(test) ? "Valid" : "Invalid") << "\n";
        }
        
        // Min Stack
        cout << "\n2. Min Stack:\n";
        MinStack minStack;
        minStack.push(-2);
        minStack.push(0);
        minStack.push(-3);
        cout << "  Pushed: -2, 0, -3\n";
        cout << "  getMin() → " << minStack.getMin() << " (should be -3)\n";
        minStack.pop();
        cout << "  After pop()\n";
        cout << "  top() → " << minStack.top() << " (should be 0)\n";
        cout << "  getMin() → " << minStack.getMin() << " (should be -2)\n";
        
        // RPN Evaluation
        cout << "\n3. Evaluate RPN:\n";
        vector<vector<string>> rpnTests = {
            {"2", "1", "+", "3", "*"},
            {"4", "13", "5", "/", "+"}
        };
        for (const auto& tokens : rpnTests) {
            cout << "  [ ";
            for (const auto& t : tokens) cout << t << " ";
            cout << "] → " << evalRPN(tokens) << "\n";
        }
    }
}

// ============================================================================
// SECTION 2: MONOTONIC STACK - ADVANCED PATTERN
// ============================================================================
// Monotonic Stack: Stack maintaining elements in monotonic order
// Use cases: Next greater/smaller element, histogram problems, stock span

namespace MonotonicStack {
    
    // --- Exercise 2.1: Next Greater Element I (LeetCode 496) ---
    // For each element in nums1, find next greater element in nums2
    // nums1 is subset of nums2
    // Example: nums1=[4,1,2], nums2=[1,3,4,2] → [-1,3,-1]
    
    vector<int> nextGreaterElement(const vector<int>& nums1, const vector<int>& nums2) {
        unordered_map<int, int> nextGreater;
        stack<int> st;
        
        // Build next greater map for nums2
        for (int num : nums2) {
            // Pop smaller elements - they found their next greater
            while (!st.empty() && st.top() < num) {
                nextGreater[st.top()] = num;
                st.pop();
            }
            st.push(num);
        }
        
        // Remaining elements have no next greater
        while (!st.empty()) {
            nextGreater[st.top()] = -1;
            st.pop();
        }
        
        // Build result for nums1
        vector<int> result;
        for (int num : nums1) {
            result.push_back(nextGreater[num]);
        }
        
        return result;
    }
    
    // --- Exercise 2.2: Daily Temperatures (LeetCode 739) ---
    // Given daily temperatures, return array where answer[i] is number of days
    // until warmer temperature. If no future day, answer[i] = 0
    // Example: [73,74,75,71,69,72,76,73] → [1,1,4,2,1,1,0,0]
    
    vector<int> dailyTemperatures(const vector<int>& temperatures) {
        int n = temperatures.size();
        vector<int> answer(n, 0);
        stack<int> st;  // Store indices
        
        for (int i = 0; i < n; ++i) {
            // Current temp is warmer than stack top's temp
            while (!st.empty() && temperatures[i] > temperatures[st.top()]) {
                int prevIdx = st.top();
                st.pop();
                answer[prevIdx] = i - prevIdx;  // Days to wait
            }
            st.push(i);
        }
        
        // Remaining indices have no warmer day (already 0)
        return answer;
    }
    
    // TODO: Implement Next Greater Element II (circular array)
    // Array is circular: next element of last is first
    // Example: [1,2,1] → [2,-1,2]
    vector<int> nextGreaterElements(const vector<int>& nums) {
        // YOUR CODE HERE
        // Hint: Traverse array twice (simulate circular with % operator)
        return {};
    }
    
    // --- Exercise 2.3: Largest Rectangle in Histogram (LeetCode 84) ---
    // Find largest rectangle area in histogram
    // Example: [2,1,5,6,2,3] → 10 (rectangle 5,6)
    
    int largestRectangleArea(const vector<int>& heights) {
        stack<int> st;  // Store indices of increasing heights
        int maxArea = 0;
        int n = heights.size();
        
        for (int i = 0; i <= n; ++i) {
            int h = (i == n) ? 0 : heights[i];
            
            // Current height less than stack top - calculate area
            while (!st.empty() && h < heights[st.top()]) {
                int height = heights[st.top()];
                st.pop();
                int width = st.empty() ? i : i - st.top() - 1;
                maxArea = max(maxArea, height * width);
            }
            
            st.push(i);
        }
        
        return maxArea;
    }
    
    // TODO: Implement Maximal Rectangle (LeetCode 85)
    // Given 2D binary matrix, find largest rectangle containing only 1s
    // Hint: Use largestRectangleArea for each row treating as histogram base
    int maximalRectangle(const vector<vector<char>>& matrix) {
        // YOUR CODE HERE
        return 0;
    }
    
    void demonstrate() {
        cout << "\n=== SECTION 2: MONOTONIC STACK ===\n";
        
        // Next Greater Element
        cout << "\n1. Next Greater Element:\n";
        vector<int> nums1 = {4, 1, 2};
        vector<int> nums2 = {1, 3, 4, 2};
        auto result = nextGreaterElement(nums1, nums2);
        cout << "  nums1: [4,1,2], nums2: [1,3,4,2]\n";
        cout << "  Result: [";
        for (size_t i = 0; i < result.size(); ++i) {
            cout << result[i] << (i < result.size()-1 ? "," : "");
        }
        cout << "]\n";
        
        // Daily Temperatures
        cout << "\n2. Daily Temperatures:\n";
        vector<int> temps = {73, 74, 75, 71, 69, 72, 76, 73};
        auto days = dailyTemperatures(temps);
        cout << "  Temps: [73,74,75,71,69,72,76,73]\n";
        cout << "  Days:  [";
        for (size_t i = 0; i < days.size(); ++i) {
            cout << days[i] << (i < days.size()-1 ? "," : "");
        }
        cout << "]\n";
        
        // Largest Rectangle
        cout << "\n3. Largest Rectangle in Histogram:\n";
        vector<int> heights = {2, 1, 5, 6, 2, 3};
        cout << "  Heights: [2,1,5,6,2,3]\n";
        cout << "  Max Area: " << largestRectangleArea(heights) << "\n";
    }
}

// ============================================================================
// SECTION 3: QUEUE FUNDAMENTALS
// ============================================================================
// Queue: FIFO (First In First Out)
// Operations: push O(1), pop O(1), front O(1)
// Use cases: BFS, task scheduling, buffering, caching

namespace QueueBasics {
    
    // --- Exercise 3.1: Implement Queue using Stacks (LeetCode 232) ---
    // Implement FIFO queue using only two stacks
    
    class MyQueue {
    private:
        stack<int> inStack;   // For push operations
        stack<int> outStack;  // For pop operations
        
        // Transfer elements from inStack to outStack
        void transfer() {
            while (!inStack.empty()) {
                outStack.push(inStack.top());
                inStack.pop();
            }
        }
        
    public:
        MyQueue() {}
        
        void push(int x) {
            inStack.push(x);
        }
        
        int pop() {
            if (outStack.empty()) {
                transfer();
            }
            int front = outStack.top();
            outStack.pop();
            return front;
        }
        
        int peek() {
            if (outStack.empty()) {
                transfer();
            }
            return outStack.top();
        }
        
        bool empty() {
            return inStack.empty() && outStack.empty();
        }
    };
    
    // TODO: Implement Stack using Queues (LeetCode 225)
    // Implement LIFO stack using only queues
    class MyStack {
    private:
        queue<int> q;
        
    public:
        MyStack() {}
        
        void push(int x) {
            // YOUR CODE HERE
            // Hint: Push x, then rotate all previous elements to back
        }
        
        int pop() {
            // YOUR CODE HERE
            return 0;
        }
        
        int top() {
            // YOUR CODE HERE
            return 0;
        }
        
        bool empty() {
            // YOUR CODE HERE
            return false;
        }
    };
    
    // --- Exercise 3.2: Design Circular Queue (LeetCode 622) ---
    // Fixed-size queue with circular buffer
    
    class MyCircularQueue {
    private:
        vector<int> data;
        int head;
        int tail;
        int size;
        int capacity;
        
    public:
        MyCircularQueue(int k) : data(k), head(0), tail(0), size(0), capacity(k) {}
        
        bool enQueue(int value) {
            if (isFull()) return false;
            data[tail] = value;
            tail = (tail + 1) % capacity;
            size++;
            return true;
        }
        
        bool deQueue() {
            if (isEmpty()) return false;
            head = (head + 1) % capacity;
            size--;
            return true;
        }
        
        int Front() {
            return isEmpty() ? -1 : data[head];
        }
        
        int Rear() {
            return isEmpty() ? -1 : data[(tail - 1 + capacity) % capacity];
        }
        
        bool isEmpty() {
            return size == 0;
        }
        
        bool isFull() {
            return size == capacity;
        }
    };
    
    // --- Exercise 3.3: Task Scheduler (LeetCode 621) ---
    // Given tasks with cooldown period n, find minimum intervals needed
    // Example: tasks=['A','A','A','B','B','B'], n=2 → 8
    // Optimal: A → B → idle → A → B → idle → A → B
    
    int leastInterval(const vector<char>& tasks, int n) {
        // Count task frequencies
        vector<int> freq(26, 0);
        for (char task : tasks) {
            freq[task - 'A']++;
        }
        
        // Find max frequency
        int maxFreq = *max_element(freq.begin(), freq.end());
        
        // Count how many tasks have max frequency
        int maxCount = count(freq.begin(), freq.end(), maxFreq);
        
        // Formula: (maxFreq - 1) * (n + 1) + maxCount
        // Or total tasks if no idle needed
        int intervals = (maxFreq - 1) * (n + 1) + maxCount;
        return max(intervals, static_cast<int>(tasks.size()));
    }
    
    // TODO: Implement simulation-based task scheduler using priority queue
    // This approach is more intuitive but same time complexity
    int leastIntervalSimulation(const vector<char>& tasks, int n) {
        // YOUR CODE HERE
        // Hint: Use max heap for frequencies, cooldown queue for waiting tasks
        return 0;
    }
    
    void demonstrate() {
        cout << "\n=== SECTION 3: QUEUE FUNDAMENTALS ===\n";
        
        // Queue using Stacks
        cout << "\n1. Queue using Stacks:\n";
        MyQueue q;
        q.push(1);
        q.push(2);
        q.push(3);
        cout << "  Pushed: 1, 2, 3\n";
        cout << "  peek() → " << q.peek() << "\n";
        cout << "  pop() → " << q.pop() << "\n";
        cout << "  peek() → " << q.peek() << "\n";
        
        // Circular Queue
        cout << "\n2. Circular Queue (size 3):\n";
        MyCircularQueue cq(3);
        cout << "  enQueue(1): " << (cq.enQueue(1) ? "Success" : "Failed") << "\n";
        cout << "  enQueue(2): " << (cq.enQueue(2) ? "Success" : "Failed") << "\n";
        cout << "  enQueue(3): " << (cq.enQueue(3) ? "Success" : "Failed") << "\n";
        cout << "  enQueue(4): " << (cq.enQueue(4) ? "Success" : "Failed") << " (full)\n";
        cout << "  Front: " << cq.Front() << ", Rear: " << cq.Rear() << "\n";
        cout << "  deQueue(): " << (cq.deQueue() ? "Success" : "Failed") << "\n";
        cout << "  enQueue(4): " << (cq.enQueue(4) ? "Success" : "Failed") << "\n";
        cout << "  Front: " << cq.Front() << ", Rear: " << cq.Rear() << "\n";
        
        // Task Scheduler
        cout << "\n3. Task Scheduler:\n";
        vector<char> tasks = {'A', 'A', 'A', 'B', 'B', 'B'};
        int n = 2;
        cout << "  Tasks: [A,A,A,B,B,B], cooldown: 2\n";
        cout << "  Min intervals: " << leastInterval(tasks, n) << "\n";
    }
}

// ============================================================================
// SECTION 4: DEQUE AND SLIDING WINDOW MAXIMUM
// ============================================================================
// Deque: Double-ended queue, O(1) insert/delete at both ends
// Use cases: Sliding window problems, palindrome checking, work stealing

namespace DequePatterns {
    
    // --- Exercise 4.1: Sliding Window Maximum (LeetCode 239) ---
    // Given array and window size k, return max of each window
    // Example: nums=[1,3,-1,-3,5,3,6,7], k=3 → [3,3,5,5,6,7]
    
    vector<int> maxSlidingWindow(const vector<int>& nums, int k) {
        deque<int> dq;  // Store indices in decreasing order of values
        vector<int> result;
        
        for (int i = 0; i < nums.size(); ++i) {
            // Remove elements outside current window
            if (!dq.empty() && dq.front() <= i - k) {
                dq.pop_front();
            }
            
            // Remove smaller elements from back (they'll never be max)
            while (!dq.empty() && nums[dq.back()] < nums[i]) {
                dq.pop_back();
            }
            
            dq.push_back(i);
            
            // Add to result once we have full window
            if (i >= k - 1) {
                result.push_back(nums[dq.front()]);
            }
        }
        
        return result;
    }
    
    // TODO: Implement Sliding Window Minimum
    // Same as maximum but track minimums
    vector<int> minSlidingWindow(const vector<int>& nums, int k) {
        // YOUR CODE HERE
        return {};
    }
    
    // --- Exercise 4.2: Jump Game VI (LeetCode 1696) ---
    // Start at index 0, jump at most k steps, maximize score
    // Score = sum of values at visited indices
    // Use deque to track max scores in sliding window
    
    int maxResult(const vector<int>& nums, int k) {
        int n = nums.size();
        vector<int> dp(n);
        dp[0] = nums[0];
        
        deque<int> dq;  // Store indices with decreasing dp values
        dq.push_back(0);
        
        for (int i = 1; i < n; ++i) {
            // Remove indices outside window [i-k, i-1]
            while (!dq.empty() && dq.front() < i - k) {
                dq.pop_front();
            }
            
            // Best score to reach i
            dp[i] = nums[i] + dp[dq.front()];
            
            // Maintain decreasing order
            while (!dq.empty() && dp[dq.back()] <= dp[i]) {
                dq.pop_back();
            }
            
            dq.push_back(i);
        }
        
        return dp[n - 1];
    }
    
    // TODO: Implement Constrained Subsequence Sum (LeetCode 1425)
    // Similar to Jump Game VI but can skip indices
    int constrainedSubsetSum(const vector<int>& nums, int k) {
        // YOUR CODE HERE
        return 0;
    }
    
    // --- Exercise 4.3: Shortest Subarray with Sum at Least K (LeetCode 862) ---
    // Find shortest contiguous subarray with sum >= k
    // Uses prefix sum + deque maintaining increasing order
    
    int shortestSubarray(const vector<int>& nums, int k) {
        int n = nums.size();
        vector<long long> prefix(n + 1, 0);
        
        // Build prefix sum
        for (int i = 0; i < n; ++i) {
            prefix[i + 1] = prefix[i] + nums[i];
        }
        
        deque<int> dq;  // Store indices with increasing prefix sums
        int minLen = n + 1;
        
        for (int i = 0; i <= n; ++i) {
            // Check if we found valid subarray
            while (!dq.empty() && prefix[i] - prefix[dq.front()] >= k) {
                minLen = min(minLen, i - dq.front());
                dq.pop_front();
            }
            
            // Maintain increasing order (remove larger prefix sums)
            while (!dq.empty() && prefix[i] <= prefix[dq.back()]) {
                dq.pop_back();
            }
            
            dq.push_back(i);
        }
        
        return minLen <= n ? minLen : -1;
    }
    
    void demonstrate() {
        cout << "\n=== SECTION 4: DEQUE AND SLIDING WINDOW ===\n";
        
        // Sliding Window Maximum
        cout << "\n1. Sliding Window Maximum:\n";
        vector<int> nums = {1, 3, -1, -3, 5, 3, 6, 7};
        int k = 3;
        auto maxWindow = maxSlidingWindow(nums, k);
        cout << "  nums: [1,3,-1,-3,5,3,6,7], k=3\n";
        cout << "  Max in each window: [";
        for (size_t i = 0; i < maxWindow.size(); ++i) {
            cout << maxWindow[i] << (i < maxWindow.size()-1 ? "," : "");
        }
        cout << "]\n";
        
        // Jump Game VI
        cout << "\n2. Jump Game VI:\n";
        vector<int> jumpNums = {1, -1, -2, 4, -7, 3};
        int jumpK = 2;
        cout << "  nums: [1,-1,-2,4,-7,3], k=2\n";
        cout << "  Max score: " << maxResult(jumpNums, jumpK) << "\n";
        cout << "  Path: 1 → -1 → 4 → 3 = 7\n";
        
        // Shortest Subarray
        cout << "\n3. Shortest Subarray with Sum >= K:\n";
        vector<int> shortNums = {2, -1, 2};
        int targetK = 3;
        cout << "  nums: [2,-1,2], k=3\n";
        cout << "  Shortest length: " << shortestSubarray(shortNums, targetK) << "\n";
    }
}

// ============================================================================
// SECTION 5: PRIORITY QUEUE (HEAP)
// ============================================================================
// Priority Queue: Max heap by default, O(log n) insert/delete, O(1) access max
// Use cases: Top K problems, merge sorted arrays, median tracking

namespace PriorityQueuePatterns {
    
    // --- Exercise 5.1: Kth Largest Element in Stream (LeetCode 703) ---
    // Design class to find kth largest element in stream
    
    class KthLargest {
    private:
        priority_queue<int, vector<int>, greater<int>> minHeap;  // Min heap
        int k;
        
    public:
        KthLargest(int k, const vector<int>& nums) : k(k) {
            for (int num : nums) {
                add(num);
            }
        }
        
        int add(int val) {
            minHeap.push(val);
            if (minHeap.size() > k) {
                minHeap.pop();  // Remove smallest
            }
            return minHeap.top();  // kth largest
        }
    };
    
    // --- Exercise 5.2: Find Median from Data Stream (LeetCode 295) ---
    // Design to support adding numbers and finding median in O(log n)
    
    class MedianFinder {
    private:
        priority_queue<int> maxHeap;  // Left half (max heap)
        priority_queue<int, vector<int>, greater<int>> minHeap;  // Right half (min heap)
        
    public:
        MedianFinder() {}
        
        void addNum(int num) {
            // Add to max heap first
            maxHeap.push(num);
            
            // Balance: move largest from max heap to min heap
            minHeap.push(maxHeap.top());
            maxHeap.pop();
            
            // If min heap larger, balance back
            if (minHeap.size() > maxHeap.size()) {
                maxHeap.push(minHeap.top());
                minHeap.pop();
            }
        }
        
        double findMedian() {
            if (maxHeap.size() > minHeap.size()) {
                return maxHeap.top();
            }
            return (maxHeap.top() + minHeap.top()) / 2.0;
        }
    };
    
    // TODO: Implement Sliding Window Median (LeetCode 480)
    // Find median of each sliding window of size k
    vector<double> medianSlidingWindow(const vector<int>& nums, int k) {
        // YOUR CODE HERE
        // Hint: Use MedianFinder concept but need to remove elements
        return {};
    }
    
    // --- Exercise 5.3: Merge K Sorted Lists (LeetCode 23) ---
    // Merge k sorted linked lists into one sorted list
    
    struct ListNode {
        int val;
        ListNode* next;
        ListNode(int x) : val(x), next(nullptr) {}
    };
    
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        auto cmp = [](ListNode* a, ListNode* b) {
            return a->val > b->val;  // Min heap
        };
        priority_queue<ListNode*, vector<ListNode*>, decltype(cmp)> pq(cmp);
        
        // Add first node of each list
        for (ListNode* list : lists) {
            if (list) {
                pq.push(list);
            }
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
    
    // TODO: Implement merge K sorted arrays
    vector<int> mergeKArrays(const vector<vector<int>>& arrays) {
        // YOUR CODE HERE
        // Hint: Store (value, arrayIdx, elementIdx) in priority queue
        return {};
    }
    
    void demonstrate() {
        cout << "\n=== SECTION 5: PRIORITY QUEUE (HEAP) ===\n";
        
        // Kth Largest
        cout << "\n1. Kth Largest in Stream:\n";
        vector<int> initial = {4, 5, 8, 2};
        KthLargest kthLargest(3, initial);
        cout << "  Initial: [4,5,8,2], k=3\n";
        cout << "  add(3) → " << kthLargest.add(3) << " (3rd largest)\n";
        cout << "  add(5) → " << kthLargest.add(5) << "\n";
        cout << "  add(10) → " << kthLargest.add(10) << "\n";
        
        // Median Finder
        cout << "\n2. Find Median from Stream:\n";
        MedianFinder mf;
        mf.addNum(1);
        mf.addNum(2);
        cout << "  Added: 1, 2\n";
        cout << "  Median: " << mf.findMedian() << "\n";
        mf.addNum(3);
        cout << "  Added: 3\n";
        cout << "  Median: " << mf.findMedian() << "\n";
        
        // Merge K Lists (using arrays for demo)
        cout << "\n3. Merge K Sorted Lists:\n";
        cout << "  Concept: Use min heap to always pick smallest element\n";
        cout << "  Lists: [1→4→5], [1→3→4], [2→6]\n";
        cout << "  Merged: [1,1,2,3,4,4,5,6]\n";
    }
}

// ============================================================================
// MAIN - RUN ALL DEMONSTRATIONS
// ============================================================================

int main() {
    cout << R"(
╔════════════════════════════════════════════════════════════════╗
║                  DAY 4: STACKS, QUEUES, DEQUES                 ║
║                  Linear Data Structures Mastery                ║
╚════════════════════════════════════════════════════════════════╝
)";

    try {
        StackBasics::demonstrate();
        MonotonicStack::demonstrate();
        QueueBasics::demonstrate();
        DequePatterns::demonstrate();
        PriorityQueuePatterns::demonstrate();
        
        cout << R"(

╔════════════════════════════════════════════════════════════════╗
║                      🎯 YOUR TODO LIST                         ║
╚════════════════════════════════════════════════════════════════╝

Section 1: Stack Fundamentals
  [ ] MinStackOptimized - Space O(1) min tracking
  [ ] infixToPostfix - Expression converter

Section 2: Monotonic Stack
  [ ] nextGreaterElements - Circular array version
  [ ] maximalRectangle - 2D histogram problem

Section 3: Queue Fundamentals
  [ ] MyStack - Implement stack using queues
  [ ] leastIntervalSimulation - Task scheduler with heap

Section 4: Deque Patterns
  [ ] minSlidingWindow - Track minimums
  [ ] constrainedSubsetSum - DP with deque optimization

Section 5: Priority Queue
  [ ] medianSlidingWindow - Sliding window median
  [ ] mergeKArrays - Merge sorted arrays

╔════════════════════════════════════════════════════════════════╗
║                   📚 PRACTICE PROBLEMS                         ║
╚════════════════════════════════════════════════════════════════╝

Essential (Do These First):
  ★ LeetCode 20 - Valid Parentheses
  ★ LeetCode 155 - Min Stack
  ★ LeetCode 232 - Implement Queue using Stacks
  ★ LeetCode 239 - Sliding Window Maximum ⭐
  ★ LeetCode 295 - Find Median from Data Stream ⭐

Monotonic Stack:
  ★ LeetCode 496 - Next Greater Element I
  ★ LeetCode 739 - Daily Temperatures
  ★ LeetCode 503 - Next Greater Element II
  ★ LeetCode 84 - Largest Rectangle in Histogram ⭐⭐

Advanced Deque:
  ★ LeetCode 1696 - Jump Game VI
  ★ LeetCode 1425 - Constrained Subsequence Sum
  ★ LeetCode 862 - Shortest Subarray with Sum at Least K ⭐⭐

Priority Queue:
  ★ LeetCode 703 - Kth Largest Element in Stream
  ★ LeetCode 23 - Merge K Sorted Lists ⭐
  ★ LeetCode 480 - Sliding Window Median ⭐⭐

╔════════════════════════════════════════════════════════════════╗
║                    🎓 KEY TAKEAWAYS                            ║
╚════════════════════════════════════════════════════════════════╝

1. Stack Patterns:
   • Use for bracket matching, expression evaluation
   • Monotonic stack → O(n) for next greater/smaller problems
   • Auxiliary stack trick for O(1) getMin()

2. Queue Patterns:
   • FIFO perfect for BFS, task scheduling
   • Circular queue for fixed-size buffers
   • Two stacks can simulate queue (amortized O(1))

3. Deque Patterns:
   • Sliding window maximum/minimum in O(n)
   • Maintain monotonic order (increasing/decreasing)
   • Critical for DP optimizations

4. Priority Queue:
   • Top K problems → Min/Max heap
   • Two heaps (max + min) for median tracking
   • Merge K sorted → Use heap as merger

5. Complexity Analysis:
   • Stack/Queue: O(1) push/pop, O(n) space
   • Monotonic stack: O(n) time for n elements
   • Deque sliding window: O(n) vs O(nk) naive
   • Priority queue: O(log n) insert, O(n log k) for top K

╔════════════════════════════════════════════════════════════════╗
║               ✅ Day 4 Complete! Tomorrow: Recursion           ║
║           "Think in patterns, not individual problems"         ║
╚════════════════════════════════════════════════════════════════╝
)";

    } catch (const exception& e) {
        cerr << "Error: " << e.what() << "\n";
        return 1;
    }

    return 0;
}
