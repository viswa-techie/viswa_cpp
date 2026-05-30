/**
 * DAY 2: Maps, Sets & Hash Tables
 * 
 * Focus Areas:
 * - map vs unordered_map (BST vs Hash Table)
 * - set vs unordered_set
 * - Hash function basics
 * - Frequency counting patterns
 * - O(1) lookup optimization
 * 
 * Learning Objectives:
 * 1. Master hash table operations
 * 2. Understand when to use ordered vs unordered containers
 * 3. Practice frequency counting and grouping patterns
 * 4. Learn collision handling concepts
 */

#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <unordered_map>
#include <set>
#include <unordered_set>
#include <algorithm>
#include <sstream>
#include <chrono>

using namespace std;

// ==================================================================
// WARM-UP: Understanding map vs unordered_map
// ==================================================================

void demonstrateMapDifferences() {
    cout << "=== Map vs Unordered_Map Demo ===\n\n";
    
    // map: Ordered, Red-Black Tree, O(log n) operations
    map<string, int> orderedMap;
    orderedMap["zebra"] = 26;
    orderedMap["apple"] = 1;
    orderedMap["mango"] = 13;
    orderedMap["banana"] = 2;
    
    cout << "map (ordered by key):\n";
    for (const auto& [key, value] : orderedMap) {
        cout << "  " << key << " -> " << value << "\n";
    }
    //why ordered? because map stores keys in sorted order internally
    //whether sorted based on string or int for the orderedMap above
    // This ordering is maintained by the underlying Red-Black Tree structure
    
    // unordered_map: Unordered, Hash Table, O(1) average operations
    unordered_map<string, int> hashMap;
    hashMap["zebra"] = 26;
    hashMap["apple"] = 1;
    hashMap["mango"] = 13;
    hashMap["banana"] = 2;
    
    cout << "\nunordered_map (no specific order):\n";
    for (const auto& [key, value] : hashMap) {
        cout << "  " << key << " -> " << value << "\n";
    }
    
    // PERFORMANCE COMPARISON
    cout << "\n--- Performance Characteristics ---\n";
    cout << "map:            Insert O(log n), Search O(log n), Ordered iteration\n";
    cout << "unordered_map:  Insert O(1)*, Search O(1)*, Unordered iteration\n";
    cout << "                *Average case; worst case O(n) on collision\n";
    
    // WHEN TO USE WHICH?
    cout << "\n--- When to Use Which? ---\n";
    cout << "Use map when:\n";
    cout << "  - Need sorted keys\n";
    cout << "  - Need range queries (lower_bound, upper_bound)\n";
    cout << "  - Want predictable performance (no hash collisions)\n";
    cout << "\nUse unordered_map when:\n";
    cout << "  - Speed is critical (O(1) vs O(log n))\n";
    cout << "  - Don't need ordering\n";
    cout << "  - Have good hash function for your key type\n";
}


// ==================================================================
// EXERCISE 1: Valid Anagram
// Difficulty: Easy | Time: 15 minutes
// ==================================================================

/**
 * Problem: Check if two strings are anagrams
 * 
 * Anagram: Same characters, different arrangement
 * Example: "listen" and "silent" are anagrams
 * 
 * Approach 1: Sort both strings - O(n log n)
 * Approach 2: Frequency count - O(n)
 */

bool isAnagram_Sort(string s, string t) {
    // Simple but not optimal
    if (s.length() != t.length()) return false;
    
    //what does this sort do? It sorts the characters in the string in ascending order
    sort(s.begin(), s.end());
    sort(t.begin(), t.end());
    
    return s == t;
    
    // TIME: O(n log n) due to sorting
    // SPACE: O(1) if we don't count input modification
}

bool isAnagram_HashMap(const string& s, const string& t) {
    if (s.length() != t.length()) return false;
    
    // Count character frequencies
    unordered_map<char, int> freq;
    
    // Increment for first string
    //what this for loop for explains? It counts the frequency of each character in the first string
    for (char c : s) {
        freq[c]++;
        cout<<"Incrementing frequency of character '"<<c<<"' to "<<freq[c]<<"\n";
    }
    
    // Decrement for second string
    for (char c : t) {
        freq[c]--;
        cout<<"Decrementing frequency of character '"<<c<<"' to "<<freq[c]<<"\n";
        //what below optimization does? It checks if the frequency of the character goes below zero
        if (freq[c] < 0) return false; // Early exit optimization
    }
    
    // Check if all frequencies are zero
    for (const auto& [ch, count] : freq) {
        if (count != 0) return false;
    }
    
    return true;
    
    // TIME: O(n) - single pass through both strings
    // SPACE: O(k) where k is alphabet size (max 26 for lowercase)
    
    // OPTIMIZATION TIP: For English lowercase only, use array[26] instead of map
}

// BONUS: Array optimization for lowercase English letters
bool isAnagram_Array(const string& s, const string& t) {
    if (s.length() != t.length()) return false;
    
    int freq[26] = {0}; // Fixed size array for a-z
    
    //what do this for loop do ? It counts the frequency of each character in both strings using an array
    for (int i = 0; i < s.length(); i++) {
        //how the below line works? It maps 'a' to index 0, 'b' to index 1, ..., 'z' to index 25
        //but how? because 'a' - 'a' = 0, 'b' - 'a' = 1, ..., 'z' - 'a' = 25
        //with my example string s & t given above, for s="anagram" and t="nagaram"
        //for i=0, s[0]='a' -> freq[0]++, t[0]='n' -> freq[13]--
        //for i=1, s[1]='n' -> freq[13]++, t[1]='a' -> freq[0]--
        //and so on...
        freq[s[i] - 'a']++; // Map 'a' to 0, 'b' to 1, etc.
        freq[t[i] - 'a']--; // Decrement for second string
    }
    
    for (int count : freq) {
        if (count != 0) return false;
    }
    
    return true;
    
    // TIME: O(n)
    // SPACE: O(1) - constant 26 elements
    // FASTEST: No hash computation, cache-friendly
}


// ==================================================================
// EXERCISE 2: Group Anagrams
// Difficulty: Medium | Time: 30 minutes
// ==================================================================

/**
 * Problem: Group strings that are anagrams together
 * 
 * Example:
 * Input: ["eat", "tea", "tan", "ate", "nat", "bat"]
 * Output: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
 * 
 * Key Insight: Anagrams have the same sorted form!
 * Use sorted string as hash key to group anagrams
 */

vector<vector<string>> groupAnagrams(vector<string>& strs) {
    // Map from sorted string -> list of original strings
    unordered_map<string, vector<string>> groups;
    
    for (const string& s : strs) {
        // Create sorted version as key
        string key = s;
        sort(key.begin(), key.end());
        
        // Add original string to appropriate group
        groups[key].push_back(s);
        cout<<"Adding string '"<<s<<"' to group with key '"<<key<<"'\n";
    }
    
    // Extract all groups into result
    vector<vector<string>> result;
    for (const auto& [key, group] : groups) {
        result.push_back(group);
        cout<<"Group with key '"<<key<<"' has "<<group.size()<<" strings\n";
    }
    
    return result;
    
    // TIME: O(n * k log k) where n = number of strings, k = max string length
    // SPACE: O(n * k) for storing all strings
    
    // PATTERN: Using derived property as hash key
    // This is a VERY common interview pattern!
}

// ALTERNATIVE: Character count as key (more efficient for long strings)
vector<vector<string>> groupAnagrams_CharCount(vector<string>& strs) {
    unordered_map<string, vector<string>> groups;
    
    for (const string& s : strs) {
        // Create character count string as key
        int count[26] = {0};
        for (char c : s) {
            count[c - 'a']++;
        }
        
        // Build key like "1a2b1c" for "abc"
        string key = "";
        for (int i = 0; i < 26; i++) {
            if (count[i] > 0) {
                key += to_string(count[i]) + char('a' + i);
            }
        }
        
        groups[key].push_back(s);
    }
    
    vector<vector<string>> result;
    for (const auto& [key, group] : groups) {
        result.push_back(group);
    }
    
    return result;
    
    // TIME: O(n * k) - Better than sorting approach!
    // SPACE: O(n * k)
}


// ==================================================================
// EXERCISE 3: First Unique Character
// Difficulty: Easy | Time: 15 minutes
// ==================================================================

/**
 * Problem: Find first non-repeating character in string
 * 
 * Example: "leetcode" -> 0 (first 'l' appears once)
 *          "loveleetcode" -> 2 (first 'v' appears once)
 *          "aabb" -> -1 (no unique character)
 * 
 * Pattern: Frequency counting
 */

int firstUniqChar(const string& s) {
    // Step 1: Count frequencies
    unordered_map<char, int> freq;
    for (char c : s) {
        //what does this for loop do? It counts the frequency of each character in the string
        freq[c]++;
    }
    
    // Step 2: Find first character with frequency 1
    for (int i = 0; i < s.length(); i++) {
        if (freq[s[i]] == 1) {
            return i;
        }
    }
    
    return -1; // No unique character
    
    // TIME: O(n) - two passes
    // SPACE: O(k) where k is alphabet size
    
    // TRICK: Can't do it in one pass optimally!
    // We need to see all characters first to know frequencies
}

// YOUR TURN: Implement variation that returns the CHARACTER, not index
char firstUniqChar_ReturnChar(const string& s) {
    // TODO: Modify above to return the character instead of index
    // Return '\0' if no unique character found
    
    return '\0'; // Placeholder
}


// ==================================================================
// EXERCISE 4: Contains Duplicate
// Difficulty: Easy | Time: 10 minutes
// ==================================================================

/**
 * Problem: Check if array has any duplicates
 * 
 * Multiple approaches to explore!
 */

// Approach 1: Using set (optimal)
bool containsDuplicate_Set(const vector<int>& nums) {
    unordered_set<int> seen;
    //how this for loop works? It iterates through each number in the input array
    for (int num : nums) {
        if (seen.find(num) != seen.end()) {
            return true; // Found duplicate
        }
        seen.insert(num);
    }
    
    return false;
    
    // TIME: O(n)
    // SPACE: O(n)
}

// Approach 2: Using set size comparison (clever!)
bool containsDuplicate_SetSize(const vector<int>& nums) {
    unordered_set<int> uniqueNums(nums.begin(), nums.end());
    
    // If set size < vector size, there were duplicates
    return uniqueNums.size() < nums.size();
    
    // TIME: O(n)
    // SPACE: O(n)
    // TRADEOFF: More concise but processes entire array
}

// Approach 3: Sorting (if modification allowed)
bool containsDuplicate_Sort(vector<int> nums) {
    sort(nums.begin(), nums.end());
    
    for (int i = 1; i < nums.size(); i++) {
        if (nums[i] == nums[i-1]) {
            return true;
        }
    }
    
    return false;
    
    // TIME: O(n log n) - sorting dominates
    // SPACE: O(1) - in-place sort
    // WHEN TO USE: When space is very limited
}


// ==================================================================
// EXERCISE 5: Longest Substring Without Repeating Characters
// Difficulty: Medium | Time: 35 minutes
// ==================================================================

/**
 * Problem: Find length of longest substring with all unique characters
 * 
 * Example: "abcabcbb" -> 3 ("abc")
 *          "bbbbb" -> 1 ("b")
 *          "pwwkew" -> 3 ("wke")
 * 
 * Technique: Sliding Window + Hash Set
 * 
 * This is a CLASSIC interview problem!
 */

int lengthOfLongestSubstring(const string& s) {
    unordered_set<char> window; // Characters in current window
    int maxLen = 0;
    int left = 0; // Left boundary of window
    
//where the window is assigned? It is defined by the left and right pointers
//explain why for, while loop is there? The for loop expands the right pointer of the window
//The while loop contracts the left pointer until there are no duplicates
//This way, we maintain a window of unique characters
    for (int right = 0; right < s.length(); right++) {
        // Shrink window until no duplicate
        //give me for each for loop iteration explanation
        //right =0, s[0]='a', window is empty, so while loop skipped, window={'a'}, maxLen=1
        //right =1, s[1]='b', window={'a'}, while loop skipped, window={'a','b'}, maxLen=2
        //right =2, s[2]='c', window={'a','b'}, while loop skipped, window={'a','b','c'}, maxLen=3
        //right =3, s[3]='a', window={'a','b','c'}, while loop triggered, left moves from 0 to 1, window={'b','c'}, then window={'b','c','a'}, maxLen=3
        while (window.find(s[right]) != window.end()) {
            window.erase(s[left]);
            left++;
        }
        
        // Add current character to window
        window.insert(s[right]);
        
        // Update max length
        maxLen = max(maxLen, right - left + 1);
    }
    
    return maxLen;
    
    // TIME: O(n) - each character visited at most twice
    // SPACE: O(k) where k is charset size
    
    // KEY INSIGHT: Sliding window expands right, contracts left
    // When we find duplicate, we move left until it's removed
}

// OPTIMIZED: Track character positions for faster left pointer movement
int lengthOfLongestSubstring_Optimized(const string& s) {
    unordered_map<char, int> charIndex; // char -> last seen index
    int maxLen = 0;
    int left = 0;
    
    for (int right = 0; right < s.length(); right++) {
        char c = s[right];
        
        // If character seen before and is in current window
        if (charIndex.find(c) != charIndex.end() && charIndex[c] >= left) {
            left = charIndex[c] + 1; // Jump left pointer
        }
        
        charIndex[c] = right;
        maxLen = max(maxLen, right - left + 1);
    }
    
    return maxLen;
    
    // TIME: O(n) - single pass
    // SPACE: O(k)
    // OPTIMIZATION: No while loop, direct jump
}


// ==================================================================
// EXERCISE 6: Top K Frequent Elements
// Difficulty: Medium | Time: 25 minutes
// ==================================================================

/**
 * Problem: Find k most frequent elements in array
 * 
 * Example: nums = [1,1,1,2,2,3], k = 2
 * Output: [1,2]
 * 
 * Multiple approaches with different time complexities!
 */

// Approach 1: Sort by frequency
vector<int> topKFrequent_Sort(vector<int>& nums, int k) {
    // Step 1: Count frequencies
    unordered_map<int, int> freq;
    //how for loop works? It counts the frequency of each number in the input array
    //I dont understand how the for loop works here, explain in comments
    // For each number in nums, increment its count in freq map

    for (int num : nums) {
        freq[num]++;
        cout <<"Number "<<num<<" has frequency "<<freq[num]<<"\n";
    }
    
    // Step 2: Create vector of (num, frequency) pairs
    vector<pair<int, int>> freqPairs;
    for (const auto& [num, count] : freq) {
        freqPairs.push_back({num, count});
        cout <<"Pair added: ("<<num<<", "<<count<<")\n";
    }
    
    // Step 3: Sort by frequency (descending)
    sort(freqPairs.begin(), freqPairs.end(), 
         [](const auto& a, const auto& b) {
            //  return a.second > b.second; // Compare by frequency
             cout <<"Comparing pairs: ("<<a.first<<", "<<a.second<<") and ("<<b.first<<", "<<b.second<<")\n";
             return a.second > b.second; // Compare by frequency
         });
    
    // Step 4: Extract top k
    vector<int> result;
    for (int i = 0; i < k; i++) {
        result.push_back(freqPairs[i].first);
        cout <<"Top "<<(i+1)<<" frequent element: "<<freqPairs[i].first<<" with frequency "<<freqPairs[i].second<<"\n";
    }
    
    return result;
    
    // TIME: O(n log n) - sorting dominates
    // SPACE: O(n)
    
    // LEARNING: Custom comparator in lambda!
}

// YOUR TURN: Implement using priority_queue (heap) for O(n log k)
#include <queue>

vector<int> topKFrequent_Heap(vector<int>& nums, int k) {
    // TODO: Use min heap of size k
    // Hint: priority_queue<pair<int, int>, vector<pair<int,int>>, greater<pair<int,int>>>
    // Keep only top k frequent elements in heap
    
    return {}; // Placeholder
}


// ==================================================================
// BONUS EXERCISE: Subarray Sum Equals K
// Difficulty: Medium | Time: 30 minutes
// ==================================================================

/**
 * Problem: Count subarrays with sum equal to k
 * 
 * Example: nums = [1,1,1], k = 2
 * Output: 2 (subarrays [1,1] at two different positions)
 * 
 * KEY TRICK: Prefix sum + hash map
 * If prefixSum[j] - prefixSum[i] = k, then sum(i+1...j) = k
 */

int subarraySum(vector<int>& nums, int k) {
    unordered_map<int, int> prefixSumCount; // prefix sum -> frequency
    prefixSumCount[0] = 1; // Base case: empty prefix has sum 0
    
    int currentSum = 0;
    int count = 0;
    
    for (int num : nums) {
        currentSum += num;
        
        // Check if (currentSum - k) exists
        // If yes, we found subarray(s) ending here with sum k
        int complement = currentSum - k;
        if (prefixSumCount.find(complement) != prefixSumCount.end()) {
            count += prefixSumCount[complement];
            cout <<"Found "<<prefixSumCount[complement]<<" subarray(s) ending here with sum "<<k<<"\n";
        }
        
        // Add current sum to map
        prefixSumCount[currentSum]++;
        cout <<"Current prefix sum: "<<currentSum<<", count now: "<<prefixSumCount[currentSum]<<"\n";
    
    }
    
    return count;
    
    // TIME: O(n)
    // SPACE: O(n)
    
    // BRILLIANT INSIGHT: Don't compute all subarrays!
    // Use mathematical property: sum(i..j) = prefixSum[j] - prefixSum[i-1]
    // This pattern appears in MANY problems!
}


// ==================================================================
// HASH FUNCTION DEEP DIVE
// ==================================================================

void demonstrateHashFunctions() {
    cout << "\n=== Hash Function Examples ===\n\n";
    
    // Built-in hash functions
    hash<string> stringHash;
    hash<int> intHash;
    
    cout << "Hash values (may vary by platform):\n";
    cout << "  hash(\"hello\") = " << stringHash("hello") << "\n";
    cout << "  hash(\"world\") = " << stringHash("world") << "\n";
    cout << "  hash(42) = " << intHash(42) << "\n";
    
    // Collision demonstration
    cout << "\n--- Collision Handling ---\n";
    cout << "unordered_map uses chaining (linked lists in each bucket)\n";
    cout << "Load factor triggers rehashing (usually at 1.0)\n";
    
    // Custom hash for pair (useful for 2D coordinates)
    struct PairHash {
        size_t operator()(const pair<int, int>& p) const {
            // Combine hashes using XOR and bit shifting
            cout <<"Hashing pair ("<<p.first<<", "<<p.second<<")\n";
            return hash<int>()(p.first) ^ (hash<int>()(p.second) << 1);
        }
    };
    
    unordered_map<pair<int, int>, string, PairHash> coordinates;
    coordinates[{0, 0}] = "origin";
    coordinates[{1, 2}] = "point A";
    cout << "Custom hash allows using pairs as keys!\n" << "  coordinates[{1,2}] = " << coordinates[{1, 2}] << "\n";    
    cout << "\nCustom hash allows using pairs as keys!\n";
    cout << "  coordinates[{0,0}] = " << coordinates[{0, 0}] << "\n";
}


// ==================================================================
// MAIN: Test All Exercises
// ==================================================================

int main() {
    cout << "🚀 DAY 2: Maps, Sets & Hash Tables\n";
    cout << "===================================\n\n";
    
    // Demo: Map differences
    // demonstrateMapDifferences();
    
    cout << "\n\n";
    /*
    // Test Exercise 1: Valid Anagram
    {
        //is there a way where I can see each function call time taken? if so help me implement that
        cout << "--- Exercise 1: Valid Anagram ---\n";
        //anagram means? same characters different arrangement
        cout << "\"anagram\" and \"nagaram\": ";
        int start_1 = chrono::high_resolution_clock::now().time_since_epoch().count();
        cout << (isAnagram_Sort("anagram", "nagaram") ? "YES" : "NO") << "\n";
        int end_1 = chrono::high_resolution_clock::now().time_since_epoch().count();
        cout << "Time taken (sort method): " << (end_1 - start_1) << " ns\n";
        cout << (isAnagram_HashMap("anagram", "nagaram") ? "YES" : "NO") << "\n";
        cout << "\"listen\" and \"silent\": ";
        cout << (isAnagram_HashMap("listen", "silent") ? "YES" : "NO") << "\n";
        cout << "\"hello\" and \"world\": ";
        cout << (isAnagram_HashMap("hello", "world") ? "YES" : "NO") << "\n";
        
        // Performance comparison
        cout << "Array method (fastest): ";
        int start = chrono::high_resolution_clock::now().time_since_epoch().count();
        //do same in microseconds
        int start_micro = chrono::duration_cast<chrono::microseconds>(chrono::high_resolution_clock::now().time_since_epoch()).count();
        cout << (isAnagram_Array("anagram", "nagaram") ? "YES" : "NO") << "\n";
        int end = chrono::high_resolution_clock::now().time_since_epoch().count();
        int end_micro = chrono::duration_cast<chrono::microseconds>(chrono::high_resolution_clock::now().time_since_epoch()).count();
        cout << "Time taken (array method): " << (end - start) << " ns\n";
        cout << "Time taken (array method): " << (end_micro - start_micro) << " µs\n";
        //1sec to 1000milliseonds to 1000000 microseconds to 1000000000 nanoseconds
    }
    
    // Test Exercise 2: Group Anagrams
    {
        cout << "\n--- Exercise 2: Group Anagrams ---\n";
        vector<string> strs = {"eat", "tea", "tan", "ate", "nat", "bat"};
        int start = chrono::high_resolution_clock::now().time_since_epoch().count();
        auto groups = groupAnagrams(strs);
        int end = chrono::high_resolution_clock::now().time_since_epoch().count();
        cout << "Time taken (groupAnagrams): " << (end - start) << " ns\n";
        
        cout << "Groups found: " << groups.size() << "\n";
        for (const auto& group : groups) {
            cout << "  [";
            for (int i = 0; i < group.size(); i++) {
                cout << group[i];
                if (i < group.size() - 1) cout << ", ";
                // cout<<"(string: '"<<group[i]<<"') ";
            }
            cout << "]\n";
        }
    }
    
    // Test Exercise 3: First Unique Character
    {
        cout << "\n--- Exercise 3: First Unique Character ---\n";
        string s1 = "leetcode";
        string s2 = "loveleetcode";
        string s3 = "aabb";
        
        cout << "\"" << s1 << "\" -> index " << firstUniqChar(s1) << "\n";
        cout << "\"" << s2 << "\" -> index " << firstUniqChar(s2) << "\n";
        cout << "\"" << s3 << "\" -> index " << firstUniqChar(s3) << "\n";
    }
    
    // Test Exercise 4: Contains Duplicate
    {
        cout << "\n--- Exercise 4: Contains Duplicate ---\n";
        vector<int> nums1 = {1, 2, 3, 1};
        vector<int> nums2 = {1, 2, 3, 4};
        
        cout << "[1,2,3,1] has duplicate: " 
             << (containsDuplicate_Set(nums1) ? "YES" : "NO") << "\n";
        cout << "[1,2,3,4] has duplicate: " 
             << (containsDuplicate_Set(nums2) ? "YES" : "NO") << "\n";
    }
    
    // Test Exercise 5: Longest Substring
    {
        cout << "\n--- Exercise 5: Longest Substring ---\n";
        string s1 = "abcabcbb";
        string s2 = "bbbbb";
        string s3 = "pwwkew";
        
        cout << "\"" << s1 << "\" -> " << lengthOfLongestSubstring(s1) << "\n";
        cout << "\"" << s2 << "\" -> " << lengthOfLongestSubstring(s2) << "\n";
        cout << "\"" << s3 << "\" -> " << lengthOfLongestSubstring_Optimized(s3) << "\n";
    }
    
    // Test Exercise 6: Top K Frequent
    {
        cout << "\n--- Exercise 6: Top K Frequent Elements ---\n";
        vector<int> nums = {1,1,1,2,2,3};
        int k = 2;
        
        int start = chrono::high_resolution_clock::now().time_since_epoch().count();
        auto result = topKFrequent_Sort(nums, k);
        int end = chrono::high_resolution_clock::now().time_since_epoch().count();
        cout << "Time taken (topKFrequent_Sort): " << (end - start) << " ns\n";

        cout << "Top " << k << " frequent in [1,1,1,2,2,3]: [";
        for (int i = 0; i < result.size(); i++) {
            cout << result[i];
            if (i < result.size() - 1) cout << ", ";
        }
        cout << "]\n";
    }
    */
    // Test Bonus: Subarray Sum
    {
        cout << "\n--- Bonus: Subarray Sum Equals K ---\n";
        vector<int> nums = {1, 1, 1};
        int k = 2;
        
        cout << "Array [1,1,1], k=2: " << subarraySum(nums, k) << " subarrays\n";
    }
    
    // Hash function demo
    demonstrateHashFunctions();
    
    cout << "\n✅ Day 2 Complete! Master these patterns - they're interview gold!\n";
    cout << "📝 Tomorrow: Iterators & STL Algorithms (transform, accumulate, find_if)\n";
    
    return 0;
}

/* ==================================================================
   🎓 KEY TAKEAWAYS FROM DAY 2:
   ==================================================================
   
   1. CONTAINER SELECTION:
      - unordered_map: O(1) average, use for speed
      - map: O(log n), use when need ordering or range queries
      - set/unordered_set: Same rules, but for unique elements only
   
   2. COMMON PATTERNS:
      - Frequency Counting: Count occurrences of elements
      - Grouping: Use derived property as hash key (sorted string, etc.)
      - Complement Finding: Check if (target - current) exists
      - Sliding Window: Expand right, contract left with set/map
      - Prefix Sum + Hash: Solve subarray sum problems in O(n)
   
   3. OPTIMIZATION TECHNIQUES:
      - Array[26] instead of map for lowercase English (O(1) space)
      - Track indices, not just presence (enables jumping)
      - Use set size comparison for duplicate detection
      - Prefix sum transforms range problems to point lookups
   
   4. TIME COMPLEXITIES:
      - Hash table operations: O(1) average, O(n) worst case
      - Tree operations: O(log n) guaranteed
      - Sorting: O(n log n)
      - Frequency counting: O(n)
   
   5. INTERVIEW GOLD PATTERNS:
      ⭐ Anagram detection (sort or char count)
      ⭐ Grouping by property (hash key = derived property)
      ⭐ Sliding window (two pointers + set/map)
      ⭐ Prefix sum + hash (subarray problems)
      ⭐ Frequency + heap (top K elements)
   
   ==================================================================
   🔍 DEBUGGING TIPS:
   ==================================================================
   
   - Print map contents: for (auto& [k, v] : map) cout << k << ":" << v
   - Check if key exists: map.find(key) != map.end()
   - Use map.count(key) for existence (returns 0 or 1)
   - Watch out for: auto-insertion with [] operator
   - Safe access: map.at(key) throws exception if not found
   
   ==================================================================
   📚 FURTHER PRACTICE:
   ==================================================================
   
   LeetCode Problems:
   - Easy: Two Sum, Valid Anagram, Contains Duplicate
   - Medium: Group Anagrams, Top K Frequent, Longest Substring
   - Medium: Subarray Sum Equals K, 4Sum II
   - Hard: Substring with Concatenation of All Words
   
   Study Resources:
   - C-Plus-Plus/STL/Map examples
   - CPlusPlusThings/basic_content/containers
   - CppCoreGuidelines on container selection
   
   ==================================================================
   💪 CHALLENGE EXERCISES (Optional):
   ==================================================================
   
   1. Implement your own hash table with chaining
   2. Find all anagrams in a string (sliding window)
   3. Longest consecutive sequence using hash set
   4. Design a LRU Cache using unordered_map + doubly linked list
   5. Word pattern matching (bijection with two maps)
   
   ================================================================== */
