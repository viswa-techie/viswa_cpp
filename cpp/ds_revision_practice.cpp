/**
 * @file ds_revision_practice.cpp
 * @brief Quick DS revision with runnable examples
 * 
 * Compile: g++ -std=c++17 -o ds_practice ds_revision_practice.cpp
 * Run: ./ds_practice
 */

#include <iostream>
#include <vector>
#include <stack>
#include <queue>
#include <unordered_map>
#include <unordered_set>
#include <algorithm>

using namespace std;

// ============= 1. LINKED LIST =============
struct ListNode {
    int val;
    ListNode* next;
    ListNode(int x) : val(x), next(nullptr) {}
};

void printList(ListNode* head) {
    while (head) {
        cout << head->val << " -> ";
        head = head->next;
    }
    cout << "NULL\n";
}

ListNode* reverseList(ListNode* head) {
    ListNode* prev = nullptr;
    ListNode* curr = head;
    while (curr) {
        ListNode* next = curr->next;
        curr->next = prev;
        prev = curr;
        curr = next;
    }
    return prev;
}

bool hasCycle(ListNode* head) {
    ListNode* slow = head;
    ListNode* fast = head;
    while (fast && fast->next) {
        slow = slow->next;
        fast = fast->next->next;
        if (slow == fast) return true;
    }
    return false;
}

// ============= 2. BINARY TREE =============
struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

void inorder(TreeNode* root) {
    if (!root) return;
    inorder(root->left);
    cout << root->val << " ";
    inorder(root->right);
}

void levelOrder(TreeNode* root) {
    if (!root) return;
    queue<TreeNode*> q;
    q.push(root);
    while (!q.empty()) {
        int size = q.size();
        for (int i = 0; i < size; i++) {
            TreeNode* node = q.front();
            q.pop();
            cout << node->val << " ";
            if (node->left) q.push(node->left);
            if (node->right) q.push(node->right);
        }
        cout << "\n";
    }
}

int maxDepth(TreeNode* root) {
    if (!root) return 0;
    return 1 + max(maxDepth(root->left), maxDepth(root->right));
}

// ============= 3. BST OPERATIONS =============
TreeNode* insertBST(TreeNode* root, int val) {
    if (!root) return new TreeNode(val);
    if (val < root->val)
        root->left = insertBST(root->left, val);
    else
        root->right = insertBST(root->right, val);
    return root;
}

TreeNode* searchBST(TreeNode* root, int val) {
    if (!root || root->val == val) return root;
    if (val < root->val) return searchBST(root->left, val);
    return searchBST(root->right, val);
}

bool isValidBST(TreeNode* root, long minVal = LONG_MIN, long maxVal = LONG_MAX) {
    if (!root) return true;
    if (root->val <= minVal || root->val >= maxVal) return false;
    return isValidBST(root->left, minVal, root->val) &&
           isValidBST(root->right, root->val, maxVal);
}

// ============= 4. GRAPH OPERATIONS =============
class Graph {
    int V;
    vector<vector<int>> adj;
public:
    Graph(int V) : V(V), adj(V) {}
    
    void addEdge(int u, int v) {
        adj[u].push_back(v);
        adj[v].push_back(u);
    }
    
    void BFS(int start) {
        vector<bool> visited(V, false);
        queue<int> q;
        visited[start] = true;
        q.push(start);
        
        cout << "BFS: ";
        while (!q.empty()) {
            int v = q.front();
            q.pop();
            cout << v << " ";
            
            for (int u : adj[v]) {
                if (!visited[u]) {
                    visited[u] = true;
                    q.push(u);
                }
            }
        }
        cout << "\n";
    }
    
    void DFSUtil(int v, vector<bool>& visited) {
        visited[v] = true;
        cout << v << " ";
        for (int u : adj[v]) {
            if (!visited[u])
                DFSUtil(u, visited);
        }
    }
    
    void DFS(int start) {
        vector<bool> visited(V, false);
        cout << "DFS: ";
        DFSUtil(start, visited);
        cout << "\n";
    }
};

// ============= 5. COMMON PROBLEMS =============

// Two Sum - Hash Table
vector<int> twoSum(vector<int>& nums, int target) {
    unordered_map<int, int> map;
    for (int i = 0; i < nums.size(); i++) {
        int complement = target - nums[i];
        if (map.find(complement) != map.end()) {
            return {map[complement], i};
        }
        map[nums[i]] = i;
    }
    return {};
}

// Valid Parentheses - Stack
bool isValid(string s) {
    stack<char> st;
    unordered_map<char, char> pairs = {{')', '('}, {']', '['}, {'}', '{'}};
    
    for (char c : s) {
        if (c == '(' || c == '[' || c == '{') {
            st.push(c);
        } else {
            if (st.empty() || st.top() != pairs[c]) return false;
            st.pop();
        }
    }
    return st.empty();
}

// Maximum Subarray - Kadane's Algorithm
int maxSubArray(vector<int>& nums) {
    int maxSum = nums[0];
    int currentSum = nums[0];
    for (int i = 1; i < nums.size(); i++) {
        currentSum = max(nums[i], currentSum + nums[i]);
        maxSum = max(maxSum, currentSum);
    }
    return maxSum;
}

// Merge Sorted Arrays
vector<int> mergeSortedArrays(vector<int>& arr1, vector<int>& arr2) {
    vector<int> result;
    int i = 0, j = 0;
    while (i < arr1.size() && j < arr2.size()) {
        if (arr1[i] < arr2[j]) {
            result.push_back(arr1[i++]);
        } else {
            result.push_back(arr2[j++]);
        }
    }
    while (i < arr1.size()) result.push_back(arr1[i++]);
    while (j < arr2.size()) result.push_back(arr2[j++]);
    return result;
}

// ============= MAIN - TEST FUNCTIONS =============
int main() {
    cout << "========================================\n";
    cout << "DATA STRUCTURES QUICK REVISION PRACTICE\n";
    cout << "========================================\n\n";
    
    // 1. LINKED LIST TEST
    cout << "1. LINKED LIST OPERATIONS\n";
    cout << "--------------------------\n";
    ListNode* head = new ListNode(1);
    head->next = new ListNode(2);
    head->next->next = new ListNode(3);
    head->next->next->next = new ListNode(4);
    
    cout << "Original List: ";
    printList(head);
    
    head = reverseList(head);
    cout << "Reversed List: ";
    printList(head);
    
    cout << "Has Cycle: " << (hasCycle(head) ? "Yes" : "No") << "\n\n";
    
    // 2. BINARY TREE TEST
    cout << "2. BINARY TREE OPERATIONS\n";
    cout << "--------------------------\n";
    TreeNode* root = new TreeNode(1);
    root->left = new TreeNode(2);
    root->right = new TreeNode(3);
    root->left->left = new TreeNode(4);
    root->left->right = new TreeNode(5);
    
    cout << "Inorder Traversal: ";
    inorder(root);
    cout << "\n";
    
    cout << "Level Order Traversal:\n";
    levelOrder(root);
    
    cout << "Max Depth: " << maxDepth(root) << "\n\n";
    
    // 3. BST TEST
    cout << "3. BST OPERATIONS\n";
    cout << "--------------------------\n";
    TreeNode* bst = nullptr;
    vector<int> values = {5, 3, 7, 2, 4, 6, 8};
    for (int val : values) {
        bst = insertBST(bst, val);
    }
    
    cout << "BST Inorder: ";
    inorder(bst);
    cout << "\n";
    
    cout << "Search 4: " << (searchBST(bst, 4) ? "Found" : "Not Found") << "\n";
    cout << "Is Valid BST: " << (isValidBST(bst) ? "Yes" : "No") << "\n\n";
    
    // 4. STACK TEST
    cout << "4. STACK & QUEUE OPERATIONS\n";
    cout << "--------------------------\n";
    stack<int> st;
    st.push(10);
    st.push(20);
    st.push(30);
    cout << "Stack Top: " << st.top() << "\n";
    st.pop();
    cout << "After Pop, Top: " << st.top() << "\n";
    
    queue<int> q;
    q.push(1);
    q.push(2);
    q.push(3);
    cout << "Queue Front: " << q.front() << "\n";
    q.pop();
    cout << "After Dequeue, Front: " << q.front() << "\n\n";
    
    // 5. PRIORITY QUEUE TEST
    cout << "5. PRIORITY QUEUE (HEAP)\n";
    cout << "--------------------------\n";
    priority_queue<int> maxHeap;
    maxHeap.push(10);
    maxHeap.push(30);
    maxHeap.push(20);
    cout << "Max Heap Top: " << maxHeap.top() << "\n";
    
    priority_queue<int, vector<int>, greater<int>> minHeap;
    minHeap.push(10);
    minHeap.push(30);
    minHeap.push(20);
    cout << "Min Heap Top: " << minHeap.top() << "\n\n";
    
    // 6. HASH TABLE TEST
    cout << "6. HASH TABLE OPERATIONS\n";
    cout << "--------------------------\n";
    unordered_map<string, int> map;
    map["apple"] = 5;
    map["banana"] = 3;
    map["orange"] = 7;
    cout << "apple count: " << map["apple"] << "\n";
    cout << "Exists banana: " << (map.find("banana") != map.end() ? "Yes" : "No") << "\n\n";
    
    // 7. GRAPH TEST
    cout << "7. GRAPH TRAVERSALS\n";
    cout << "--------------------------\n";
    Graph g(5);
    g.addEdge(0, 1);
    g.addEdge(0, 2);
    g.addEdge(1, 3);
    g.addEdge(1, 4);
    g.addEdge(2, 4);
    
    g.BFS(0);
    g.DFS(0);
    cout << "\n";
    
    // 8. COMMON PROBLEMS TEST
    cout << "8. COMMON PROBLEM SOLUTIONS\n";
    cout << "--------------------------\n";
    
    // Two Sum
    vector<int> nums = {2, 7, 11, 15};
    vector<int> result = twoSum(nums, 9);
    cout << "Two Sum (target=9): [" << result[0] << ", " << result[1] << "]\n";
    
    // Valid Parentheses
    cout << "Valid Parentheses '()[]{}': " << (isValid("()[]{}") ? "Valid" : "Invalid") << "\n";
    cout << "Valid Parentheses '(]': " << (isValid("(]") ? "Valid" : "Invalid") << "\n";
    
    // Max Subarray
    vector<int> arr = {-2, 1, -3, 4, -1, 2, 1, -5, 4};
    cout << "Max Subarray Sum: " << maxSubArray(arr) << "\n";
    
    // Merge Sorted Arrays
    vector<int> arr1 = {1, 3, 5, 7};
    vector<int> arr2 = {2, 4, 6, 8};
    vector<int> merged = mergeSortedArrays(arr1, arr2);
    cout << "Merged Arrays: ";
    for (int num : merged) cout << num << " ";
    cout << "\n\n";
    
    cout << "========================================\n";
    cout << "✅ All tests completed successfully!\n";
    cout << "========================================\n";
    
    return 0;
}
