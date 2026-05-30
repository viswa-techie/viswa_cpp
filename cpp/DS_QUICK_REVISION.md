# 🚀 Data Structures Quick Revision Guide - C++

**Start Date:** December 20, 2025  
**Goal:** Quick revision → Problem solving  
**Time:** 2-3 hrs daily

---

## 📋 Quick Revision Checklist (7 Days)

### **Day 1-2: Linear Data Structures** ✅
- [ ] Arrays & Vectors
- [ ] Linked Lists (Singly, Doubly, Circular)
- [ ] Stacks
- [ ] Queues (Simple, Circular, Priority)

### **Day 3-4: Trees & Hierarchical Structures** ✅
- [ ] Binary Trees (Traversals: Inorder, Preorder, Postorder)
- [ ] Binary Search Trees (BST)
- [ ] AVL Trees
- [ ] Heaps (Min/Max)
- [ ] Tries

### **Day 5: Advanced Trees & Graphs** ✅
- [ ] Red-Black Trees
- [ ] Segment Trees
- [ ] Graph Representations (Adjacency List/Matrix)
- [ ] Graph Traversals (BFS, DFS)

### **Day 6: Hash-Based & Advanced Structures** ✅
- [ ] Hash Tables/Maps
- [ ] Hash Sets
- [ ] Bloom Filters
- [ ] Skip Lists

### **Day 7: Review & Complexity Analysis** ✅
- [ ] Time Complexity (Big-O)
- [ ] Space Complexity
- [ ] STL Usage Best Practices

---

## 🎯 1. LINEAR DATA STRUCTURES

### 📦 Arrays & Vectors

**Key Concepts:**
- Dynamic arrays using `std::vector`
- Time: Access O(1), Insert/Delete O(n)
- Space: O(n)

**Essential Operations:**
```cpp
#include <vector>
#include <algorithm>

// Creation & Initialization
std::vector<int> v = {1, 2, 3, 4, 5};
std::vector<int> v2(10, 0);  // 10 elements, all 0

// Access
int first = v[0];
int last = v.back();

// Insertion
v.push_back(6);           // O(1) amortized
v.insert(v.begin() + 2, 99);  // O(n)

// Deletion
v.pop_back();             // O(1)
v.erase(v.begin() + 2);   // O(n)

// Searching
auto it = std::find(v.begin(), v.end(), 3);  // O(n)
bool found = (it != v.end());

// Sorting
std::sort(v.begin(), v.end());  // O(n log n)

// Size & Capacity
size_t size = v.size();
size_t cap = v.capacity();
```

**Practice Files:**
- `/cpp/C-Plus-Plus/data_structures/list_array.cpp`
- `/cpp/C-Plus-Plus/operations_on_datastructures/array_left_rotation.cpp`
- `/cpp/C-Plus-Plus/operations_on_datastructures/array_right_rotation.cpp`

---

### 🔗 Linked Lists

**Key Concepts:**
- Singly: Each node → next
- Doubly: Each node → next & prev
- Circular: Last node → first node
- Time: Access O(n), Insert/Delete O(1) at head

**Essential Implementation:**
```cpp
// Singly Linked List Node
struct Node {
    int data;
    Node* next;
    Node(int val) : data(val), next(nullptr) {}
};

// Insert at head - O(1)
void insertAtHead(Node*& head, int data) {
    Node* newNode = new Node(data);
    newNode->next = head;
    head = newNode;
}

// Insert at tail - O(n)
void insertAtTail(Node*& head, int data) {
    Node* newNode = new Node(data);
    if (!head) {
        head = newNode;
        return;
    }
    Node* temp = head;
    while (temp->next) temp = temp->next;
    temp->next = newNode;
}

// Delete node - O(n)
void deleteNode(Node*& head, int key) {
    if (!head) return;
    
    if (head->data == key) {
        Node* temp = head;
        head = head->next;
        delete temp;
        return;
    }
    
    Node* curr = head;
    while (curr->next && curr->next->data != key) {
        curr = curr->next;
    }
    
    if (curr->next) {
        Node* temp = curr->next;
        curr->next = curr->next->next;
        delete temp;
    }
}

// Reverse linked list - O(n)
void reverse(Node*& head) {
    Node* prev = nullptr;
    Node* curr = head;
    Node* next = nullptr;
    
    while (curr) {
        next = curr->next;
        curr->next = prev;
        prev = curr;
        curr = next;
    }
    head = prev;
}

// Detect cycle - Floyd's Algorithm O(n)
bool hasCycle(Node* head) {
    Node* slow = head;
    Node* fast = head;
    
    while (fast && fast->next) {
        slow = slow->next;
        fast = fast->next->next;
        if (slow == fast) return true;
    }
    return false;
}
```

**Practice Files:**
- `/cpp/C-Plus-Plus/data_structures/linked_list.cpp`
- `/cpp/C-Plus-Plus/data_structures/linkedlist_implentation_usingarray.cpp`
- `/cpp/C-Plus-Plus/operations_on_datastructures/circular_linked_list.cpp`
- `/cpp/C-Plus-Plus/operations_on_datastructures/reverse_a_linked_list_using_recusion.cpp`

---

### 📚 Stacks

**Key Concepts:**
- LIFO (Last In, First Out)
- Operations: push, pop, top, isEmpty
- All operations: O(1)

**Essential Operations:**
```cpp
#include <stack>

// Using STL
std::stack<int> st;

// Push - O(1)
st.push(10);
st.push(20);

// Pop - O(1)
st.pop();

// Top - O(1)
int topElement = st.top();

// Check empty
bool empty = st.empty();

// Size
size_t size = st.size();

// Custom implementation using array
class Stack {
    int* arr;
    int top;
    int capacity;
public:
    Stack(int size) : capacity(size), top(-1) {
        arr = new int[size];
    }
    
    void push(int x) {
        if (top >= capacity - 1) return; // overflow
        arr[++top] = x;
    }
    
    int pop() {
        if (top < 0) return -1; // underflow
        return arr[top--];
    }
    
    int peek() {
        if (top < 0) return -1;
        return arr[top];
    }
    
    bool isEmpty() { return top < 0; }
    
    ~Stack() { delete[] arr; }
};
```

**Common Problems:**
- Balanced parentheses
- Infix to postfix conversion
- Next greater element
- Stock span problem

**Practice Files:**
- `/cpp/C-Plus-Plus/data_structures/stack.hpp`
- `/cpp/C-Plus-Plus/data_structures/stack_using_array.cpp`
- `/cpp/C-Plus-Plus/data_structures/stack_using_linked_list.cpp`

---

### 🚶 Queues

**Key Concepts:**
- FIFO (First In, First Out)
- Operations: enqueue, dequeue, front
- Types: Simple, Circular, Priority, Deque

**Essential Operations:**
```cpp
#include <queue>
#include <deque>

// Simple Queue - STL
std::queue<int> q;
q.push(10);         // Enqueue - O(1)
q.push(20);
int front = q.front();  // O(1)
q.pop();            // Dequeue - O(1)

// Priority Queue (Max Heap by default)
std::priority_queue<int> pq;
pq.push(10);
pq.push(30);
pq.push(20);
int max = pq.top();  // 30
pq.pop();

// Min Heap
std::priority_queue<int, std::vector<int>, std::greater<int>> minPQ;

// Deque (Double-ended queue)
std::deque<int> dq;
dq.push_back(10);
dq.push_front(5);
dq.pop_back();
dq.pop_front();

// Circular Queue Implementation
class CircularQueue {
    int* arr;
    int front, rear, size, capacity;
public:
    CircularQueue(int k) : capacity(k), front(0), rear(-1), size(0) {
        arr = new int[k];
    }
    
    bool enqueue(int value) {
        if (size == capacity) return false;
        rear = (rear + 1) % capacity;
        arr[rear] = value;
        size++;
        return true;
    }
    
    bool dequeue() {
        if (size == 0) return false;
        front = (front + 1) % capacity;
        size--;
        return true;
    }
    
    int Front() {
        return size == 0 ? -1 : arr[front];
    }
    
    bool isEmpty() { return size == 0; }
    bool isFull() { return size == capacity; }
    
    ~CircularQueue() { delete[] arr; }
};
```

**Practice Files:**
- `/cpp/C-Plus-Plus/data_structures/queue.hpp`
- `/cpp/C-Plus-Plus/data_structures/queue_using_array.cpp`
- `/cpp/C-Plus-Plus/data_structures/queue_using_linked_list.cpp`
- `/cpp/C-Plus-Plus/data_structures/circular_queue_using_linked_list.cpp`

---

## 🌳 2. TREES & HIERARCHICAL STRUCTURES

### 🌲 Binary Trees

**Key Concepts:**
- Each node has max 2 children
- Height: O(log n) balanced, O(n) skewed
- Traversals: Inorder, Preorder, Postorder, Level-order

**Essential Implementation:**
```cpp
struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

// Inorder Traversal (Left → Root → Right) - O(n)
void inorder(TreeNode* root, std::vector<int>& result) {
    if (!root) return;
    inorder(root->left, result);
    result.push_back(root->val);
    inorder(root->right, result);
}

// Preorder Traversal (Root → Left → Right) - O(n)
void preorder(TreeNode* root, std::vector<int>& result) {
    if (!root) return;
    result.push_back(root->val);
    preorder(root->left, result);
    preorder(root->right, result);
}

// Postorder Traversal (Left → Right → Root) - O(n)
void postorder(TreeNode* root, std::vector<int>& result) {
    if (!root) return;
    postorder(root->left, result);
    postorder(root->right, result);
    result.push_back(root->val);
}

// Level Order Traversal (BFS) - O(n)
std::vector<std::vector<int>> levelOrder(TreeNode* root) {
    std::vector<std::vector<int>> result;
    if (!root) return result;
    
    std::queue<TreeNode*> q;
    q.push(root);
    
    while (!q.empty()) {
        int size = q.size();
        std::vector<int> level;
        
        for (int i = 0; i < size; i++) {
            TreeNode* node = q.front();
            q.pop();
            level.push_back(node->val);
            
            if (node->left) q.push(node->left);
            if (node->right) q.push(node->right);
        }
        result.push_back(level);
    }
    return result;
}

// Height of tree - O(n)
int height(TreeNode* root) {
    if (!root) return 0;
    return 1 + std::max(height(root->left), height(root->right));
}

// Check if balanced - O(n)
bool isBalanced(TreeNode* root) {
    if (!root) return true;
    int leftHeight = height(root->left);
    int rightHeight = height(root->right);
    
    return abs(leftHeight - rightHeight) <= 1 &&
           isBalanced(root->left) &&
           isBalanced(root->right);
}
```

---

### 🔍 Binary Search Trees (BST)

**Key Concepts:**
- Left subtree < root < Right subtree
- Search, Insert, Delete: O(log n) avg, O(n) worst
- Inorder gives sorted sequence

**Essential Operations:**
```cpp
// Search in BST - O(log n) avg
TreeNode* search(TreeNode* root, int key) {
    if (!root || root->val == key) return root;
    if (key < root->val) return search(root->left, key);
    return search(root->right, key);
}

// Insert in BST - O(log n) avg
TreeNode* insert(TreeNode* root, int key) {
    if (!root) return new TreeNode(key);
    
    if (key < root->val)
        root->left = insert(root->left, key);
    else if (key > root->val)
        root->right = insert(root->right, key);
    
    return root;
}

// Find minimum value node
TreeNode* minValueNode(TreeNode* node) {
    TreeNode* current = node;
    while (current && current->left)
        current = current->left;
    return current;
}

// Delete from BST - O(log n) avg
TreeNode* deleteNode(TreeNode* root, int key) {
    if (!root) return root;
    
    if (key < root->val)
        root->left = deleteNode(root->left, key);
    else if (key > root->val)
        root->right = deleteNode(root->right, key);
    else {
        // Node with only one child or no child
        if (!root->left) {
            TreeNode* temp = root->right;
            delete root;
            return temp;
        }
        else if (!root->right) {
            TreeNode* temp = root->left;
            delete root;
            return temp;
        }
        
        // Node with two children
        TreeNode* temp = minValueNode(root->right);
        root->val = temp->val;
        root->right = deleteNode(root->right, temp->val);
    }
    return root;
}

// Validate BST - O(n)
bool isValidBST(TreeNode* root, long min = LONG_MIN, long max = LONG_MAX) {
    if (!root) return true;
    if (root->val <= min || root->val >= max) return false;
    return isValidBST(root->left, min, root->val) &&
           isValidBST(root->right, root->val, max);
}
```

**Practice Files:**
- `/cpp/C-Plus-Plus/data_structures/binary_search_tree.cpp`
- `/cpp/C-Plus-Plus/data_structures/binary_search_tree2.cpp`
- `/cpp/C-Plus-Plus/operations_on_datastructures/inorder_successor_of_bst.cpp`

---

### ⚖️ AVL Trees & Heaps

**AVL Tree (Self-balancing BST):**
- Balance factor = height(left) - height(right)
- Balance factor ∈ {-1, 0, 1}
- Rotations: LL, RR, LR, RL

**Heap (Binary Heap):**
- Complete binary tree
- Max Heap: parent ≥ children
- Min Heap: parent ≤ children
- Insert: O(log n), Delete: O(log n), Get min/max: O(1)

```cpp
#include <queue>

// Min Heap using STL
std::priority_queue<int, std::vector<int>, std::greater<int>> minHeap;

// Max Heap
std::priority_queue<int> maxHeap;

// Custom comparator
auto cmp = [](int a, int b) { return a > b; };
std::priority_queue<int, std::vector<int>, decltype(cmp)> pq(cmp);
```

**Practice Files:**
- `/cpp/C-Plus-Plus/data_structures/avltree.cpp`
- `/cpp/C-Plus-Plus/data_structures/binaryheap.cpp`

---

### 📖 Tries

**Key Concepts:**
- Prefix tree for strings
- Each node represents a character
- Insert, Search: O(m) where m = string length

```cpp
class TrieNode {
public:
    std::unordered_map<char, TrieNode*> children;
    bool isEndOfWord;
    
    TrieNode() : isEndOfWord(false) {}
};

class Trie {
    TrieNode* root;
public:
    Trie() { root = new TrieNode(); }
    
    void insert(std::string word) {
        TrieNode* node = root;
        for (char ch : word) {
            if (!node->children[ch])
                node->children[ch] = new TrieNode();
            node = node->children[ch];
        }
        node->isEndOfWord = true;
    }
    
    bool search(std::string word) {
        TrieNode* node = root;
        for (char ch : word) {
            if (!node->children[ch])
                return false;
            node = node->children[ch];
        }
        return node->isEndOfWord;
    }
    
    bool startsWith(std::string prefix) {
        TrieNode* node = root;
        for (char ch : prefix) {
            if (!node->children[ch])
                return false;
            node = node->children[ch];
        }
        return true;
    }
};
```

**Practice Files:**
- `/cpp/C-Plus-Plus/data_structures/trie_modern.cpp`
- `/cpp/C-Plus-Plus/data_structures/trie_tree.cpp`

---

## 📊 3. GRAPHS

**Key Concepts:**
- Vertex/Node + Edge
- Directed/Undirected, Weighted/Unweighted
- Representations: Adjacency List, Adjacency Matrix

```cpp
#include <vector>
#include <queue>
#include <stack>

// Adjacency List representation
class Graph {
    int V; // vertices
    std::vector<std::vector<int>> adj;
public:
    Graph(int V) : V(V), adj(V) {}
    
    void addEdge(int u, int v) {
        adj[u].push_back(v);
        adj[v].push_back(u); // For undirected
    }
    
    // BFS - O(V + E)
    void BFS(int start) {
        std::vector<bool> visited(V, false);
        std::queue<int> q;
        
        visited[start] = true;
        q.push(start);
        
        while (!q.empty()) {
            int v = q.front();
            q.pop();
            std::cout << v << " ";
            
            for (int u : adj[v]) {
                if (!visited[u]) {
                    visited[u] = true;
                    q.push(u);
                }
            }
        }
    }
    
    // DFS - O(V + E)
    void DFSUtil(int v, std::vector<bool>& visited) {
        visited[v] = true;
        std::cout << v << " ";
        
        for (int u : adj[v]) {
            if (!visited[u])
                DFSUtil(u, visited);
        }
    }
    
    void DFS(int start) {
        std::vector<bool> visited(V, false);
        DFSUtil(start, visited);
    }
    
    // Detect cycle in undirected graph
    bool isCyclicUtil(int v, std::vector<bool>& visited, int parent) {
        visited[v] = true;
        
        for (int u : adj[v]) {
            if (!visited[u]) {
                if (isCyclicUtil(u, visited, v))
                    return true;
            }
            else if (u != parent)
                return true;
        }
        return false;
    }
    
    bool isCyclic() {
        std::vector<bool> visited(V, false);
        for (int i = 0; i < V; i++) {
            if (!visited[i])
                if (isCyclicUtil(i, visited, -1))
                    return true;
        }
        return false;
    }
};
```

---

## 🗺️ 4. HASH TABLES

**Key Concepts:**
- Hash function maps keys to indices
- Avg case: Insert, Delete, Search - O(1)
- Collision handling: Chaining, Open Addressing

```cpp
#include <unordered_map>
#include <unordered_set>
#include <map>
#include <set>

// Unordered Map (Hash Table) - O(1) avg
std::unordered_map<std::string, int> hashMap;
hashMap["apple"] = 5;
hashMap["banana"] = 3;
int count = hashMap["apple"];

// Check existence
if (hashMap.find("apple") != hashMap.end()) {
    // exists
}

// Unordered Set - O(1) avg
std::unordered_set<int> hashSet;
hashSet.insert(10);
hashSet.insert(20);
bool exists = hashSet.count(10);

// Ordered Map (Red-Black Tree) - O(log n)
std::map<std::string, int> orderedMap;

// Ordered Set - O(log n)
std::set<int> orderedSet;
```

---

## 📈 5. COMPLEXITY CHEAT SHEET

| Data Structure | Access | Search | Insert | Delete | Space |
|---------------|--------|--------|--------|--------|-------|
| Array | O(1) | O(n) | O(n) | O(n) | O(n) |
| Linked List | O(n) | O(n) | O(1)* | O(1)* | O(n) |
| Stack | O(n) | O(n) | O(1) | O(1) | O(n) |
| Queue | O(n) | O(n) | O(1) | O(1) | O(n) |
| Hash Table | - | O(1) | O(1) | O(1) | O(n) |
| BST | O(log n) | O(log n) | O(log n) | O(log n) | O(n) |
| AVL Tree | O(log n) | O(log n) | O(log n) | O(log n) | O(n) |
| Binary Heap | O(log n) | O(n) | O(log n) | O(log n) | O(n) |

*at head/tail

---

## 🎯 NEXT STEPS - PROBLEM SOLVING ROADMAP

### Week 1: Easy Problems (20-30 problems)
- Arrays: Two Sum, Best Time to Buy Stock
- Strings: Valid Palindrome, Reverse String
- Linked List: Reverse, Detect Cycle
- Stacks/Queues: Valid Parentheses, Implement Queue using Stacks

### Week 2: Medium Problems (15-20 problems)
- Trees: Level Order, Validate BST, Lowest Common Ancestor
- Graphs: Number of Islands, Clone Graph
- Dynamic Programming: Climbing Stairs, House Robber

### Week 3+: Mix of Medium & Hard
- Focus on patterns: Sliding Window, Two Pointers, Fast & Slow Pointers
- Practice on LeetCode, Codeforces, HackerRank

---

## 📚 Your Resources

**Best Repositories to Practice:**
1. `/cpp/C-Plus-Plus/` - Complete implementations
2. `/cpp/C-Plus-Plus/data_structures/` - All DS implementations
3. `/cpp/C-Plus-Plus/operations_on_datastructures/` - Operations & algorithms

**Learning Resources:**
- `/cpp/CPlusPlusThings/` - Modern C++ concepts
- `/cpp/CppCoreGuidelines/` - Best practices
- `/cpp/Modern-CPP-Programming/` - Modern C++ features

---

## ✅ Daily Practice Template

```
Date: ___________

✅ Concepts Revised: _________________
✅ Code Files Studied: _________________
✅ Problems Solved: _________________
✅ Time Spent: _____ hrs

Notes & Key Learnings:
_____________________________________
_____________________________________
```

---

**Remember:**
- Start with fundamentals, build gradually
- Solve problems immediately after revising concepts
- Focus on understanding, not memorizing
- Track your progress daily

🚀 **You got this! Start today, revise quickly, and jump into problem-solving!**
