/**
 * DAY 1: Vector Mastery & Basic Algorithms
 * 
 * Focus Areas:
 * - std::vector operations
 * - Iterator usage
 * - STL algorithms: sort, reverse, binary_search
 * - Time complexity analysis
 * 
 * Learning Objectives:
 * 1. Master dynamic array operations
 * 2. Understand amortized O(1) push_back
 * 3. Practice range-based operations
 * 4. Learn when to reserve() capacity
 */

#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>
#include <chrono>
#include <unordered_map>
#include <set>
#include <unordered_set>
#include <climits>

using namespace std;

// ==================================================================
// EXERCISE 1: Two Sum Problem
// Difficulty: Easy | Time: 15 minutes
// ==================================================================

/**
 * Problem: Find two numbers in an array that add up to a target.
 * 
 * Logic:
 * - Use hash map for O(n) solution, but let's explore vector approach first
 * - This teaches: vector traversal, nested loops, optimization thinking
 * 
 * Example:
 * Input: nums = [2, 7, 11, 15], target = 9
 * Output: [0, 1] (because nums[0] + nums[1] = 9)
 */

vector<vector<int>> twoSum_BruteForce(const vector<int>& nums, int target) {
    // APPROACH 1: Brute Force - O(n²)
    // Try all pairs - good for learning, bad for performance
    
    //what if there are more than one solution? then what logic should be added?
// Solution: Return the first found pair, or store all pairs in a vector of vectors
//give me that solution also here modify the below 


    int n = nums.size();
    vector<vector<int>> allSolutions;
    // cout << "size of nums is " << n << endl;
    for (int i = 0; i < n - 1; i++) {
        for (int j = i + 1; j < n; j++) {
            if (nums[i] + nums[j] == target) {
                allSolutions.push_back({nums[i], nums[j]});
            }
        }
    }
        if(!allSolutions.empty())
        // cout << "Number of solutions found: " << allSolutions.size() << endl;
        return allSolutions; // Return first found solution
    return {}; // No solution found
    
    // COMMON MISTAKES:
    // 1. Starting j from 0 (would use same element twice)
    // 2. Not checking array bounds
    // 3. Forgetting to return empty vector when no solution
}

// YOUR TURN: Implement optimized O(n) solution using unordered_map
// Hint: Store {value -> index} mapping while iterating
vector<vector<int>> twoSum_Optimized(const vector<int>& nums, int target) {
    // TODO: Implement this using hash map
    // Think about: What to store? When to check?
    // Remember to handle duplicates and edge cases!
    //write the code here
    //what if there are more than one solution? then what logic should be added?
    vector<vector<int>> allSolutions;

    unordered_map<int, int> numMap; // value -> index
    for (int i = 0; i < nums.size(); i++) {
        int complement = target - nums[i];
        if (numMap.find(complement) != numMap.end()) {
            // cout << "Found complement " << complement << " for " << nums[i] << " at indices " << numMap[complement] << " and " << i << endl;

            allSolutions.push_back({complement, nums[i]});
            // cout << "Number of solutions found: " << allSolutions.size() << endl;
        }
        numMap[nums[i]] = i;
    }
    if(!allSolutions.empty())
        return allSolutions; // Return all found solutions
    
    return {};
}
//My own if duplicate exist
vector<vector<int>> twoSum_Optimized_duplicate(const vector<int>& nums, int target) {
    vector<vector<int>> allSolutions;
    unordered_map<int, int> numMap; // value -> index
    set<pair<int,int>> seenPairs;   // to avoid duplicates

    for (int i = 0; i < nums.size(); i++) {
        int complement = target - nums[i];
        if (numMap.find(complement) != numMap.end()) {
            int a = complement, b = nums[i];
            if (seenPairs.find({min(a,b), max(a,b)}) == seenPairs.end()) {
                allSolutions.push_back({a, b});
                seenPairs.insert({min(a,b), max(a,b)});
            }
        }
        numMap[nums[i]] = i;
    }
    return allSolutions;
}


// ==================================================================
// EXERCISE 2: Remove Duplicates from Sorted Array
// Difficulty: Easy | Time: 20 minutes
// ==================================================================

/**
 * Problem: Remove duplicates in-place, return new length
 * 
 * Logic (Two Pointer Technique):
 * - Keep one pointer for unique position
 * - Another pointer scans the array
 * - Only write when we find a new unique element
 * 
 * Key Insight: Array is SORTED, so duplicates are adjacent!
 */

int removeDuplicates(vector<int>& nums) {
    if (nums.empty()) return 0;
    
    int writePos = 1; // Position to write next unique element
    
    // Scan from second element
    for (int readPos = 1; readPos < nums.size(); readPos++) {
        // If current element differs from previous unique element
        if (nums[readPos] != nums[writePos - 1]) {
            nums[writePos] = nums[readPos];
            writePos++;
        }
    }
    
    return writePos; // New length
    
    // PERFORMANCE TIP:
    // - This is O(n) time, O(1) space
    // - We modify array in-place (memory efficient)
    // - STL alternative: std::unique() + erase()
}
// Variation: Remove duplicates from UNSORTED array
int removeDuplicates_unsorted(vector<int>& nums) {
    if (nums.empty()) return 0;

    unordered_set<int> seen;
    int writePos = 0;

    for (int readPos = 0; readPos < nums.size(); readPos++) {
        if (seen.find(nums[readPos]) == seen.end()) {
            seen.insert(nums[readPos]);
            nums[writePos] = nums[readPos];
            writePos++;
        }
    }

    return writePos;
}


// ALTERNATIVE: Using STL (more idiomatic C++)
int removeDuplicates_STL(vector<int>& nums) {
    // std::unique moves duplicates to end, returns iterator to new end
    auto newEnd = unique(nums.begin(), nums.end());
    nums.erase(newEnd, nums.end()); // Remove the duplicates
    return nums.size();
    
    // LESSON: STL often has optimized implementations
    // But understanding manual approach helps in interviews!
}


// ==================================================================
// EXERCISE 3: Maximum Subarray Sum (Kadane's Algorithm)
// Difficulty: Medium | Time: 30 minutes
// ==================================================================

/**
 * Problem: Find contiguous subarray with largest sum
 * 
 * Example: [-2,1,-3,4,-1,2,1,-5,4]
 * Output: 6 (subarray [4,-1,2,1])
 * 
 * Kadane's Algorithm - Classic DP problem!
 * Logic:
 * - At each position, decide: extend current subarray OR start new one?
 * - Keep track of global maximum seen so far
 */

int maxSubArray(const vector<int>& nums) {
    if (nums.empty()) return 0;
    
    int currentSum = nums[0];  // Best sum ending at current position
    int maxSum = nums[0];      // Global maximum
    
    for (int i = 1; i < nums.size(); i++) {
        // Key decision: extend previous subarray or start fresh?
        //modify below line into 2 step to understand better
        int extend = currentSum + nums[i];
        currentSum = max(nums[i], extend);
        // currentSum = max(nums[i], currentSum + nums[i]);        
        // Update global maximum
        maxSum = max(maxSum, currentSum);
        
        // WHY THIS WORKS:
        // If currentSum becomes negative, better to start new subarray
        // We're doing DP without explicit table!
    }
    
    return maxSum;
}

// VARIATION: Return the actual subarray (not just sum)
vector<int> maxSubArray_WithIndices(const vector<int>& nums) {
    // TODO: Modify above to track start and end indices
    // Hint: Update indices when currentSum resets or maxSum updates
    //write the todo code here complete it
    int currentSum = 0;
    int maxSum = INT_MIN; // Initialize to smallest integer
    int start = 0, end = 0, tempStart = 0;
    cout << "size of nums is " << nums.size() << endl;
    cout << "INT_MIN is " << INT_MIN << endl;

    //explain core logic in comments
    // If currentSum is negative or zero, start new subarray at current index
    // Otherwise, extend the existing subarray by adding current element

    for (int i = 0; i < nums.size(); i++) {
        // If currentSum is negative or zero, start new subarray at current index
        //corner case is covered here when all elements are negative?
        //so that maxSum is at least the maximum element
        //if all elemenets are positive then also it works fine without any change
        //if contains both positive and negative elements also it works fine
        //expected output for the all negative elements is the maximum element among them
        //ex : vector is vector<int> nums = {-2, -1, -3, -4, -1, -2, -1, -5, -4}; expected output here is -1 but I'm getting -2
        //what is currentsum & maxsum refers here?
        // currentSum refers to the maximum sum of the subarray ending at the current index
        // maxSum refers to the maximum sum found so far among all subarrays
        if (currentSum <= 0) {
            currentSum = nums[i];
            tempStart = i;
        } 
        //else if currentSum is positive, extend the subarray
        else {
            currentSum += nums[i];
        }

        if (currentSum > maxSum) {
            maxSum = currentSum;
            start = tempStart;
            end = i;
        }
    }
    cout << "Maximum Subarray Sum: " << maxSum << "\n";
    cout << "Subarray: ";
    for (int i = start; i <= end; i++) {
        cout << nums[i] << " " << i << ", ";
    }
    cout << "\n";

    return vector<int>(nums.begin() + start, nums.begin() + end + 1);
}

// ==================================================================
// EXERCISE 4: Vector Operations Benchmark
// Learning: Performance characteristics of vector operations
// ==================================================================

void demonstrateVectorPerformance() {
    cout << "\n=== Vector Performance Analysis ===\n";
    
    // 1. push_back with and without reserve
    auto start = chrono::high_resolution_clock::now();
    
    vector<int> v1;
    for (int i = 0; i < 100000; i++) {
        v1.push_back(i);
    }
    auto end = chrono::high_resolution_clock::now();
    auto duration1 = chrono::duration_cast<chrono::microseconds>(end - start);
    
    // With reserve
    start = chrono::high_resolution_clock::now();
    vector<int> v2;
    v2.reserve(100000); // Pre-allocate memory
    for (int i = 0; i < 100000; i++) {
        v2.push_back(i);
    }
    end = chrono::high_resolution_clock::now();
    auto duration2 = chrono::duration_cast<chrono::microseconds>(end - start);
    
    cout << "Without reserve: " << duration1.count() << " µs\n";
    cout << "With reserve: " << duration2.count() << " µs\n";
    cout << "Speedup: " << (float)duration1.count() / duration2.count() << "x\n";
    
    // LESSON: reserve() avoids multiple reallocations!
    // Use it when you know approximate size
}


// ==================================================================
// BONUS EXERCISE: Product of Array Except Self
// Difficulty: Medium | Time: 30 minutes
// ==================================================================

/**
 * Problem: Return array where output[i] = product of all elements except nums[i]
 * Constraint: Don't use division, solve in O(n)
 * 
 * Example: [1,2,3,4] → [24,12,8,6]
 * 
 * Clever Logic:
 * - output[i] = (product of all left elements) × (product of all right elements)
 * - Use two passes: left-to-right and right-to-left
 */

vector<int> productExceptSelf(const vector<int>& nums) {
    int n = nums.size();
    vector<int> output(n, 1);
    //        vector<int> nums = {1, 2, 3, 4};
    //expected left products = {1, 1, 2, 6}
    //expected right products = {24, 12, 4, 1}
    //final output = {24, 12, 8, 6}
    //how the logic works? explain in comments
    // Left pass calculates product of all elements to the left of each index
    // Right pass multiplies by product of all elements to the right of each index
    //then how output tells except that no. at that index?
    //whether logic works for zeroes & negative numbers also?
    //yes it works for zeroes and negative numbers also
    //if there is one zero in the array then all elements except that index will be zero
    //if there are two zeroes in the array then all elements will be zero
    //if there are negative numbers then also it works fine as multiplication is commutative

    
    // Left pass: output[i] contains product of all elements to the left
    int leftProduct = 1;
    for (int i = 0; i < n; i++) {
        output[i] = leftProduct;
        leftProduct *= nums[i];
        cout << "Left pass - i: " << i << ", leftProduct: " << leftProduct << ", output[" << i << "]: " << output[i] << endl;
    }
    
    // Right pass: multiply by product of all elements to the right
    int rightProduct = 1;
    for (int i = n - 1; i >= 0; i--) {
        output[i] *= rightProduct;
        rightProduct *= nums[i];
        cout << "Right pass - i: " << i << ", rightProduct: " << rightProduct << ", output[" << i << "]: " << output[i] << endl;
    }
    cout << "Final output array: ";
    for (int val : output) {
        cout << val << " ";
    }
    cout << endl;
    
    return output;
    
    // SPACE OPTIMIZATION: O(1) extra space (output array doesn't count)
    // TIME: O(n) - two passes
    // TRICK: We're essentially building prefix and suffix products!
}


// ==================================================================
// MAIN: Test All Exercises
// ==================================================================

int main() {
    cout << "🚀 DAY 1: Vector Mastery & Algorithms\n";
    cout << "======================================\n\n";
    /*
    // Test Exercise 1: Two Sum
    {
        //add logic to find how much time it took time to execute the function
        auto start = chrono::high_resolution_clock::now();
        vector<int> nums = {2, 7, 11, 15, 9, 0, 1, 3, 6};
        int target = 9;
        auto result = twoSum_BruteForce(nums, target);
        auto end = chrono::high_resolution_clock::now();
        auto duration = chrono::duration_cast<chrono::microseconds>(end - start);
        cout << "Execution time for twoSum_BruteForce: " << duration.count() << " µs\n";

        cout << sizeof(result) << endl;
        cout << "size of result is " << result.size() << endl;
        cout << "Two Sum (target " << target << "): [";
        if (!result.empty()) {
            for(int i=0; i<result.size(); i++){
                cout << "[" << result[i][0] << ", " << result[i][1] << "]" << (i < result.size() - 1 ? ", " : "");
            }

        }
        cout << "]\n";
    }
    //two sum optimized
    {
        //check time taken to execute the function here
        auto start = chrono::high_resolution_clock::now();
        vector<int> nums = {2, 7, 11, 15, 9, 0, 1, 3, 6};
        int target = 9;
        auto result = twoSum_Optimized(nums, target);
        auto end = chrono::high_resolution_clock::now();
        auto duration = chrono::duration_cast<chrono::microseconds>(end - start);
        cout << "Execution time: for twoSum_Optimized: " << duration.count() << " µs\n";

        cout << "Two Sum Optimized (target " << target << "): [";
        if (!result.empty()) {
            for(int i=0; i<result.size(); i++){
                cout << "[" << result[i][0] << ", " << result[i][1] << "]" << (i < result.size() - 1 ? ", " : "");
            }
        }
        cout << "]\n";
    }
    //three duplicate pair if exist
    {
        auto start = chrono::high_resolution_clock::now();
        vector<int> nums = {1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6};
        int target = 7;
        auto result = twoSum_Optimized_duplicate(nums, target);
        auto end = chrono::high_resolution_clock::now();
        auto duration = chrono::duration_cast<chrono::microseconds>(end - start);
        cout << "Execution time: for twoSum_Optimized_duplicate: " << duration.count() << " µs\n";
        cout << "Two Sum Optimized (target " << target << "): [";
        if (!result.empty()) {
            for(int i=0; i<result.size(); i++){
                cout << "[" << result[i][0] << ", " << result[i][1] << "]" << (i < result.size() - 1 ? ", " : "");
            }
        }
        cout << "]\n";
    }
*/

/*
    // Test Exercise 2: Remove Duplicates
    {
        auto start = chrono::high_resolution_clock::now();
        vector<int> nums = {1, 1, 2, 2, 2, 3, 4, 4, 5};
        cout << "Before: "; 
        for (int x : nums) cout << x << " ";
        
        int newLen = removeDuplicates(nums);
        auto end = chrono::high_resolution_clock::now();
        auto duration = chrono::duration_cast<chrono::microseconds>(end - start);
        cout << "\nExecution time for removeDuplicates: " << duration.count() << " µs\n"; 
        //time taken to execute the function in microseconds = 1/1000000 seconds = 1/1000 milliseconds
        cout << "\nAfter removing duplicates: ";
        for (int i = 0; i < newLen; i++) cout << nums[i] << " ";
        cout << " (length: " << newLen << ")\n";
    }
    //remove duplicate element from an unsorted array
    {
        auto start = chrono::high_resolution_clock::now();
        vector<int> nums = {4, 2, 1, 2, 3, 4, 5, 1, 6};
        cout << "Before (unsorted): "; 
        for (int x : nums) cout << x << " ";
        
        // Sort first
        sort(nums.begin(), nums.end());
        int newLen = removeDuplicates_unsorted(nums);
        auto end = chrono::high_resolution_clock::now();
        auto duration = chrono::duration_cast<chrono::microseconds>(end - start);
        cout << "\nExecution time for removeDuplicates_unsorted: " << duration.count() << " µs\n";
        cout << "\nAfter removing duplicates from unsorted array: ";
        for (int i = 0; i < newLen; i++) cout << nums[i] << " ";
        cout << " (length: " << newLen << ")\n";
    }

//write for removeDuplicates_STL
    // Test Exercise 2: Remove Duplicates using STL
    {
        auto start = chrono::high_resolution_clock::now();
        vector<int> nums = {1, 1, 2, 2, 2, 3, 4, 4, 5};
        cout << "Before (STL): "; 
        for (int x : nums) cout << x << " ";
        
        int newLen = removeDuplicates_STL(nums);
        auto end = chrono::high_resolution_clock::now();
        auto duration = chrono::duration_cast<chrono::microseconds>(end - start);
        cout << "\nExecution time for removeDuplicates_STL: " << duration.count() << " µs\n";
        cout << "\nAfter removing duplicates using STL: ";
        for (int i = 0; i < newLen; i++) cout << nums[i] << " ";
        cout << " (length: " << newLen << ")\n";
    }
*/
    // Test Exercise 3: Maximum Subarray
    /*
    {
        vector<int> nums = {-2, 1, -3, 4, -1, 2, 1, -5, 4};
        int maxSum = maxSubArray(nums);
        cout << "\nMaximum Subarray Sum: " << maxSum << "\n";
    }
    // Test Exercise 3: Maximum Subarray with indices
    {
        // vector<int> nums = {-2, 1, -3, 4, -1, 2, 1, -5, 4};
        vector<int> nums = {-2, 1, -3, 4, -1, 2, 1, -5, 4};
        auto subarray = maxSubArray_WithIndices(nums);
        int maxSum = accumulate(subarray.begin(), subarray.end(), 0);
        cout << "Subarray: ";
        for (int x : subarray) cout << x << " ";
        cout << "\n";

        cout << "\nMaximum Subarray for maxSubArray_WithIndices Sum: " << maxSum << "\n";
    }
    */
    // Test Performance
    // demonstrateVectorPerformance();
    
    // Test Bonus: Product Except Self
    {
        vector<int> nums = {1, 2, 3, 4, 0, 5};
        auto result = productExceptSelf(nums);
        cout << "\nProduct Except Self [1,2,3,4]: [";
        for (int i = 0; i < result.size(); i++) {
            cout << result[i];
            if (i < result.size() - 1) cout << ", ";
        }
        cout << "]\n";
    }
    
    cout << "\n✅ Day 1 Complete! Review the code and understand each algorithm.\n";
    cout << "📝 Tomorrow: Maps, Sets, and Hash Tables\n";
    
    return 0;
}

/* ==================================================================
   🎓 KEY TAKEAWAYS FROM DAY 1:
   ==================================================================
   
   1. VECTOR OPERATIONS:
      - push_back is O(1) amortized (occasionally O(n) when resizing)
      - Use reserve() when size is known → significant speedup
      - emplace_back constructs in-place (better for objects)
   
   2. ALGORITHM PATTERNS:
      - Two Pointers: Read/Write pointers for in-place modifications
      - Kadane's Algorithm: Local vs global optimum tracking
      - Prefix/Suffix Products: Process array in multiple passes
   
   3. TIME COMPLEXITY:
      - Nested loops = O(n²) → Look for hash map optimization
      - Single pass with hash = O(n) → Space-time tradeoff
      - Two separate passes = Still O(n), not O(2n)
   
   4. MEMORY MANAGEMENT:
      - Passing by const reference avoids copies
      - In-place algorithms save space (O(1) extra)
      - Reserve capacity to avoid reallocations
   
   5. STL WISDOM:
      - std::unique, std::sort are highly optimized
      - But manual implementation helps understanding
      - Know both approaches for interviews and production
   
   ==================================================================
   🔍 DEBUGGING TIPS:
   ==================================================================
   
   - Print vector size before accessing: avoid seg faults
   - Use .at() instead of [] for bounds checking (debug builds)
   - Compile with: g++ -std=c++17 -Wall -Wextra -O2
   - Run with valgrind to detect memory issues
   
   ==================================================================
   📚 FURTHER READING:
   ==================================================================
   
   1. Study CPlusPlusThings/basic_content/const for const correctness
   2. Check C-Plus-Plus/ STL examples
   3. Review TheAlgorithms/C-Plus-Plus/array problems
   4. Read CppCoreGuidelines on vector usage
   
   ==================================================================
   💪 CHALLENGE EXERCISES (Optional):
   ==================================================================
   
   1. Implement 3Sum problem (find three numbers that sum to target)
   2. Rotate array by k positions (in-place)
   3. Find all permutations of a vector
   4. Implement your own dynamic array class (like vector)
   
Excellent work on Day 1! I can see you've gone beyond the basics and even added your own variations. Let me review and test your understanding with some questions.

🎓 Day 1 Review - Knowledge Check
1. Two Sum Understanding (Your Modified Solution)
Q1: In your twoSum_Optimized() solution, you're storing multiple solutions. 
What would happen if the input is [3, 3, 6] with target 9? Would you get duplicate pairs, and if so, why?
//answer: Yes, you would get duplicate pairs because the code does not check for duplicates before adding a pair to allSolutions. 
// Each time it finds a complement that matches, it adds the pair to the results, 
// leading to duplicates if the same numbers appear multiple times in the input.


Q2: Why did you create twoSum_Optimized_duplicate() with a set<pair<int,int>>? 
What problem does it solve that the first version doesn't?
//answer: I created twoSum_Optimized_duplicate() with a set<pair<int,int>> to avoid duplicate pairs in the output.
// The set ensures that each unique pair is only added once, regardless of how many times the same numbers appear in the input array.   

Q3: What's the space complexity of your optimized solution? Is it still O(n)?
//answer: Yes, the space complexity of the optimized solution is still O(n) because we are using an unordered_map to store the elements of the input array,
// which in the worst case can store all n elements if there are no duplicates.

2. Remove Duplicates - Two Approaches
Q4: You added removeDuplicates_unsorted(). What's the time and space complexity compared to the sorted version? When would you choose one over the other?
//answer: The time complexity of removeDuplicates_unsorted() is O(n) because we traverse the array once and perform O(1) operations for each element.
// The space complexity is also O(n) due to the unordered_set used to track seen elements.
// In contrast, the sorted version has a time complexity of O(n) and a space complexity of O(1) since it modifies the array in place without extra storage.
// I would choose the sorted version when the input array is already sorted or can be sorted easily,
// and the unsorted version when the input array is not sorted and we want to maintain the original order of elements.

Q5: In the sorted version, why do we compare nums[readPos] with nums[writePos - 1] instead of nums[writePos]?
//answer: We compare nums[readPos] with nums[writePos - 1] because writePos points to the position where the next unique element should be written.
// Since writePos is incremented only when a new unique element is found, nums[writePos - 1] always holds the last unique element added to the array.
// Comparing with nums[writePos] would be incorrect because that position may not have been updated yet and could still contain a duplicate value.

3. Performance & Best Practices
Q6: You saw the reserve() benchmark showing 1.8x speedup. When exactly does vector reallocation happen? Can you explain the amortized O(1) concept for push_back()? 
//answer: Vector reallocation happens when the current capacity of the vector is exceeded by a push_back() operation.
When this occurs, the vector allocates a new block of memory (usually double the current capacity), copies the existing elements to the new block, and then adds the new element.
// This reallocation is an O(n) operation because it involves copying all existing elements.
// However, the amortized O(1) concept means that while individual push_back() calls may take O(n) time during reallocation,
// the average time per push_back() over a sequence of operations remains O(1).

Q7: Why is passing vectors by const reference (like const vector<int>&) better than passing by value? What happens internally?
//answer: Passing vectors by const reference is better than passing by value because it avoids making a copy of the entire vector.
When you pass by value, a new copy of the vector is created, which involves copying all its elements, leading to O(n) time and space complexity.
// By passing by const reference, we simply pass a reference to the original vector without copying it,
// which is much more efficient, especially for large vectors. The const qualifier ensures that the function cannot modify the original vector.

4. Algorithm Patterns
Q8: Kadane's Algorithm uses the key decision: max(nums[i], currentSum + nums[i]). Why does this work? What does it mean when we "start fresh"?
//answer: This works because at each element nums[i], we have two choices:
1. Include nums[i] in the existing subarray (currentSum + nums[i])
2. Start a new subarray beginning with nums[i] (just nums[i])
// We choose the option that gives us the maximum sum at that position.
When we "start fresh," it means that the previous subarray sum (currentSum) was negative or zero,
// and including it would only decrease the sum of the new subarray starting at nums[i].
// Therefore, starting a new subarray with nums[i] alone is more beneficial.

Q9: In the "Product Except Self" problem, why can't we use division? What makes the two-pass solution elegant?
//answer: We can't use division in the "Product Except Self" problem because the problem constraints explicitly forbid it.
Using division would also fail in cases where the input array contains zeros, as division by zero is undefined.
// The two-pass solution is elegant because it efficiently computes the product of all elements to the left and right of each index without using division.
// By maintaining running products in two separate passes, we can achieve the desired result in O(n) time and O(1) extra space (excluding the output array).
   ================================================================== */
