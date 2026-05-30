/**
 * DAY 3: Iterators & STL Algorithms
 * 
 * Focus Areas:
 * - Iterator types (input, output, forward, bidirectional, random access)
 * - STL algorithms: transform, accumulate, find_if, count_if, partition
 * - Lambda expressions and custom predicates
 * - Functional programming patterns in C++
 * - Algorithm composition
 * 
 * Learning Objectives:
 * 1. Master iterator concepts and usage
 * 2. Write expressive code using STL algorithms
 * 3. Practice lambda expressions
 * 4. Understand when algorithms are better than loops
 * 5. Learn algorithm complexity guarantees
 */

#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>
#include <string>
#include <functional>
#include <iterator>
#include <set>
#include <map>

using namespace std;

// ==================================================================
// WARM-UP: Iterator Types & Usage
// ==================================================================

void demonstrateIterators() {
    cout << "=== Iterator Types Demo ===\n\n";
    
    vector<int> vec = {1, 2, 3, 4, 5};
    
    // 1. Basic iteration
    cout << "Forward iteration: ";
    for (auto it = vec.begin(); it != vec.end(); ++it) {
        cout << *it << " ";
        cout << "(Address: " << &(*it) << ") ";
    }
    cout << "\n";

    // 2. Reverse iteration
    cout << "Reverse iteration: ";
    for (auto it = vec.rbegin(); it != vec.rend(); ++it) {
        cout << *it << " ";
        cout << "(Address: " << &(*it) << ") ";
    }
    cout << "\n";

    // 3. Random access (vector specific)
    cout << "Random access: vec[2] = " << vec[2] << "\n";
    auto it = vec.begin() + 2; // Jump to index 2
    cout << "Address of vec[2]: " << &vec[2] << "\n";
    cout << "Iterator arithmetic: *(begin + 2) = " << *it << "\n";
    
    // 4. Iterator distance
    cout << "Distance begin to end: " << distance(vec.begin(), vec.end()) << "\n";
    
    // 5. Advance iterator
    auto it2 = vec.begin();
    advance(it2, 3); // Move 3 positions forward
    cout << "After advance(it, 3): " << *it2 << "\n";
    
    cout << "\n--- Iterator Categories ---\n";
    cout << "Input Iterator:       Read-once, forward only (istream_iterator)\n";
    cout << "Output Iterator:      Write-once, forward only (ostream_iterator)\n";
    cout << "Forward Iterator:     Read/write, forward only (forward_list)\n";
    cout << "Bidirectional:        Read/write, forward/backward (list, set, map)\n";
    cout << "Random Access:        Full arithmetic support (vector, deque, array)\n";
}


// ==================================================================
// EXERCISE 1: Transform - Applying Functions to Elements
// Difficulty: Easy | Time: 20 minutes
// ==================================================================

/**
 * std::transform applies a function to each element
 * 
 * Two forms:
 * 1. Unary: transform(first, last, result, unary_op)
 * 2. Binary: transform(first1, last1, first2, result, binary_op)
 * 
 * Key: Result can be same or different container
 */

void demonstrateTransform() {
    cout << "\n=== Transform Examples ===\n\n";
    
    vector<int> nums = {1, 2, 3, 4, 5};
    vector<int> squares(nums.size());
    
    // Example 1: Square all numbers (using lambda)
    transform(nums.begin(), nums.end(), squares.begin(), [](int x) { return x * x; });
    
    cout << "Original: ";
    for (int x : nums) cout << x << " ";
    cout << "\nSquared:  ";
    for (int x : squares) cout << x << " ";
    cout << "\n\n";
    
    // Example 2: Convert to uppercase
    string text = "hello world";
    transform(text.begin(), text.end(), text.begin(), [](char c) { return toupper(c); });
    cout << "Uppercase: " << text << "\n\n";
    
    // Example 3: Binary transform - add two vectors
    vector<int> a = {1, 2, 3};
    vector<int> b = {4, 5, 6};
    vector<int> sum(3);
    
    transform(a.begin(), a.end(), b.begin(), sum.begin(), [](int x, int y) { return x + y; });
    
    cout << "Vector sum: ";
    for (int x : sum) cout << x << " ";
    cout << "\n";
}

// YOUR TURN: Implement using transform
vector<string> convertToStrings(const vector<int>& nums) {
    // TODO: Convert vector<int> to vector<string> using transform
    // Hint: Use to_string() in lambda
    //solve below

    
    vector<string> result(nums.size());
    transform(nums.begin(), nums.end(), result.begin(), [](int x) { return to_string(x); });
    
    return result;
}

// Challenge: Double even numbers, keep odd numbers same
vector<int> doubleEvens(const vector<int>& nums) {
    // TODO: Use transform with conditional logic
    // Hint: Lambda can have if-else
    
    vector<int> result(nums.size());
    transform(nums.begin(), nums.end(), result.begin(),
              [](int x) {
                  if (x % 2 == 0) return x * 2;
                  else return x;
              });
    // Your code here
    
    return result;
}


// ==================================================================
// EXERCISE 2: Accumulate - Reducing to Single Value
// Difficulty: Easy | Time: 20 minutes
// ==================================================================

/**
 * std::accumulate (and std::reduce) combine elements
 * 
 * Forms:
 * - accumulate(first, last, init) - sum with init value
 * - accumulate(first, last, init, binary_op) - custom operation
 * 
 * Can be used for: sum, product, concatenation, max/min, etc.
 */

void demonstrateAccumulate() {
    cout << "\n=== Accumulate Examples ===\n\n";
    
    vector<int> nums = {1, 2, 3, 4, 5};
    
    // Example 1: Sum
    int sum = accumulate(nums.begin(), nums.end(), 0);
    cout << "Sum: " << sum << "\n";
    
    // Example 2: Product
    int product = accumulate(nums.begin(), nums.end(), 1,
                            [](int a, int b) { return a * b; });
    cout << "Product: " << product << "\n";
    
    // Example 3: String concatenation
    vector<string> words = {"Hello", " ", "World", "!"};
    string sentence = accumulate(words.begin(), words.end(), string(""));
    cout << "Concatenated: " << sentence << "\n";
    
    // Example 4: Count evens (clever use!)
    //explain below function argument of return count + (x % 2 == 0 ? 1 : 0);
    int evenCount = accumulate(nums.begin(), nums.end(), 0, [](int count, int x) {return count + (x % 2 == 0 ? 1 : 0);});
    cout << "Even numbers: " << evenCount << "\n";
}

// YOUR TURN: Find maximum using accumulate
int findMax(const vector<int>& nums) {
    // TODO: Use accumulate to find maximum element
    // Hint: Initial value should be first element or INT_MIN
    // Binary operation: max(a, b)
    
    if (nums.empty()) return 0;
    
    // Your code here
    return 0;
}

// Challenge: Calculate average (sum / count) using accumulate
double calculateAverage(const vector<int>& nums) {
    // TODO: Use accumulate for sum, then divide by size
    
    if (nums.empty()) return 0.0;
    
    // Your code here
    return 0.0;
}


// ==================================================================
// EXERCISE 3: Find Algorithms - Searching with Predicates
// Difficulty: Medium | Time: 25 minutes
// ==================================================================

/**
 * Search algorithms:
 * - find(first, last, value) - find specific value
 * - find_if(first, last, predicate) - find matching condition
 * - find_if_not(first, last, predicate) - find NOT matching
 * - count_if(first, last, predicate) - count matching
 * - any_of, all_of, none_of - check conditions
 * 
 * Return iterators (or bool for any_of/all_of/none_of)
 */

void demonstrateFindAlgorithms() {
    cout << "\n=== Find Algorithms ===\n\n";
    
    vector<int> nums = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    
    // Example 1: find
    auto it = find(nums.begin(), nums.end(), 5);
    if (it != nums.end()) {
        cout << "Found 5 at index: " << distance(nums.begin(), it) << "\n";
    }
    
    // Example 2: find_if (first even number)
    auto it2 = find_if(nums.begin(), nums.end(), [](int x) { return x % 2 == 0; });
    cout << "First even: " << *it2 << "\n";
    
    // Example 3: count_if (count odds)
    int oddCount = count_if(nums.begin(), nums.end(), [](int x) { return x % 2 != 0; });
    cout << "Odd count: " << oddCount << "\n";
    
    // Example 4: any_of, all_of, none_of
    //internally how the below three functions work
    // any_of returns true if any element satisfies the predicate
    // all_of returns true if all elements satisfy the predicate
    // none_of returns true if no elements satisfy the predicate
    bool hasEven = any_of(nums.begin(), nums.end(), [](int x) { return x % 2 == 0; });
    bool allPositive = all_of(nums.begin(), nums.end(), [](int x) { return x > 0; });
    bool noNegative = none_of(nums.begin(), nums.end(), [](int x) { return x < 0; });
    
    cout << "Has even: " << (hasEven ? "YES" : "NO") << "\n";
    cout << "All positive: " << (allPositive ? "YES" : "NO") << "\n";
    cout << "No negative: " << (noNegative ? "YES" : "NO") << "\n";
}

// YOUR TURN: Find first string longer than n characters
string findLongString(const vector<string>& words, int minLength) {
    // TODO: Use find_if to find first string with length > minLength
    // Return empty string if not found
    
    // Your code here
    //why [minLength]? in lambda function
    auto it = find_if(words.begin(), words.end(), [minLength](const string& s) { return s.length() > minLength; });
    if (it != words.end()) {
        return *it;
    }
    
    return "";
}

// Challenge: Find index of first prime number
int findFirstPrimeIndex(const vector<int>& nums) {
    // TODO: Implement isPrime as lambda, use find_if
    // Return -1 if no prime found
    
    auto isPrime = [](int n) {
        // TODO: Implement prime check
        if (n < 2) return false;
        // Your code here
        return true;
    };
    
    // Use find_if with isPrime
    // Your code here
    
    return -1;
}


// ==================================================================
// EXERCISE 4: Partition & Sort with Custom Comparators
// Difficulty: Medium | Time: 30 minutes
// ==================================================================

/**
 * Reordering algorithms:
 * - partition(first, last, predicate) - split by condition
 * - stable_partition - maintains relative order
 * - sort(first, last, comparator) - custom sorting
 * - nth_element - partial sort (O(n) average!)
 */

void demonstratePartitionSort() {
    cout << "\n=== Partition & Sort ===\n\n";
    
    vector<int> nums = {1, 5, 2, 8, 3, 9, 4, 7, 6};
    
    // Example 1: Partition (evens before odds)
    //how this order is formed After partition (evens first): 6 4 2 8 3 9 5 7 1  explain?
    auto boundary = partition(nums.begin(), nums.end(),[](int x) { return x % 2 == 0; });
    
    cout << "After partition (evens first): ";
    for (int x : nums) cout << x << " ";
    cout << "\nBoundary index: " << distance(nums.begin(), boundary) << "\n\n";
    
    // Example 2: Sort with custom comparator
    vector<string> words = {"apple", "pie", "a", "zoo", "at"};
    sort(words.begin(), words.end(), [](const string& a, const string& b) { return a.length() < b.length(); // Sort by length
         });
    
    cout << "Sorted by length: ";
    for (const auto& w : words) cout << w << " ";
    cout << "\n\n";
    
    // Example 3: nth_element (find 5th smallest)
    vector<int> nums2 = {3, 1, 4, 1, 5, 9, 2, 6, 5};
    nth_element(nums2.begin(), nums2.begin() + 4, nums2.end());
    cout << "5th smallest element: " << nums2[4] << "\n";
    cout << "After nth_element: ";
    for (int x : nums2) cout << x << " ";
    cout << "\n(Elements before are smaller, after are larger)\n";
}

// YOUR TURN: Sort vector of pairs by second element
void sortBySecond(vector<pair<string, int>>& pairs) {
    // TODO: Use sort with lambda to compare by .second
    sort(pairs.begin(), pairs.end(), [](const pair<string, int>& a, const pair<string, int>& b) {
        return a.second < b.second;
    });
    
    // Your code here
}

// Challenge: Partition into three groups (negative, zero, positive)
// This is "Dutch National Flag" problem!
void dutchFlagPartition(vector<int>& nums) {
    // TODO: Partition into [negative, zero, positive]
    // Hint: Use two partition calls, or manual three-way partition
    // Try using partition twice!
    auto mid = partition(nums.begin(), nums.end(), [](int x) { return x < 0; });
    partition(mid, nums.end(), [](int x) { return x == 0; });

    
    // Your code here
}


// ==================================================================
// EXERCISE 5: Copy, Remove, Unique - Filtering Algorithms
// Difficulty: Medium | Time: 25 minutes
// ==================================================================

/**
 * Filtering and copying:
 * - copy_if(first, last, result, predicate) - copy matching
 * - remove_if(first, last, predicate) - "remove" matching (returns iterator)
 * - unique(first, last) - remove consecutive duplicates
 * 
 * NOTE: remove_if doesn't actually delete! Use erase after!
 */

void demonstrateFilteringAlgorithms() {
    cout << "\n=== Filtering Algorithms ===\n\n";
    
    vector<int> nums = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    
    // Example 1: copy_if (copy evens to new vector)
    vector<int> evens;
    copy_if(nums.begin(), nums.end(), back_inserter(evens), [](int x) { return x % 2 == 0; });
    
    cout << "Evens: ";
    for (int x : evens) cout << x << " ";
    cout << "\n";
    
    // Example 2: remove_if (remove odds)
    vector<int> nums2 = {1, 2, 3, 4, 5, 6};
    auto newEnd = remove_if(nums2.begin(), nums2.end(), [](int x) { return x % 2 != 0; });
    nums2.erase(newEnd, nums2.end()); // Actually delete!
    
    cout << "After remove_if odds: ";
    for (int x : nums2) cout << x << " ";
    cout << "\n";
    
    // Example 3: unique (remove consecutive duplicates)
    vector<int> nums3 = {1, 1, 2, 2, 2, 3, 3, 1, 1};
    auto newEnd2 = unique(nums3.begin(), nums3.end());
    nums3.erase(newEnd2, nums3.end());
    
    cout << "After unique: ";
    for (int x : nums3) cout << x << " ";
    cout << "\n(Note: Only removes CONSECUTIVE duplicates)\n";
}

// YOUR TURN: Extract all words starting with vowel
vector<string> extractVowelWords(const vector<string>& words) {
    // TODO: Use copy_if to extract words starting with vowel
    // Hint: Check if first char is in "aeiouAEIOU"
    
    vector<string> result;
    // Your code here
    
    return result;
}

// Challenge: Remove duplicates from UNSORTED vector (all duplicates, not just consecutive)
vector<int> removeDuplicates(vector<int> nums) {
    // TODO: First sort, then use unique
    // Or use set for tracking seen elements
    
    // Your code here
    
    return nums;
}


// ==================================================================
// EXERCISE 6: Generate & Fill - Creating Data
// Difficulty: Easy | Time: 15 minutes
// ==================================================================

/**
 * Generation algorithms:
 * - fill(first, last, value) - fill with constant
 * - fill_n(first, count, value) - fill n elements
 * - generate(first, last, generator) - fill with function result
 * - iota(first, last, start_value) - fill with sequence
 */

void demonstrateGenerateAlgorithms() {
    cout << "\n=== Generate Algorithms ===\n\n";
    
    // Example 1: fill
    vector<int> v1(5);
    fill(v1.begin(), v1.end(), 42);
    cout << "fill(42): ";
    for (int x : v1) cout << x << " ";
    cout << "\n";
    
    // Example 2: iota (sequence)
    vector<int> v2(10);
    iota(v2.begin(), v2.end(), 1); // 1, 2, 3, ...
    cout << "iota(1): ";
    for (int x : v2) cout << x << " ";
    cout << "\n";
    
    // Example 3: generate (random numbers)
    vector<int> v3(5);
    generate(v3.begin(), v3.end(), []() { return rand() % 100; });
    cout << "generate(random): ";
    for (int x : v3) cout << x << " ";
    cout << "\n";
    
    // Example 4: generate (fibonacci-like)
    vector<int> v4(10);
    int a = 0, b = 1;
    generate(v4.begin(), v4.end(), [&]() {
        int temp = a;
        a = b;
        b = temp + b;
        return temp;
    });
    cout << "Fibonacci: ";
    for (int x : v4) cout << x << " ";
    cout << "\n";
}

// YOUR TURN: Generate squares sequence [1, 4, 9, 16, 25, ...]
vector<int> generateSquares(int n) {
    // TODO: Use generate with lambda that produces squares
    // Hint: Use capture by reference to track counter
    
    vector<int> result(n);
    // Your code here
    
    return result;
}


// ==================================================================
// BONUS: Algorithm Composition - Chaining Operations
// Difficulty: Hard | Time: 30 minutes
// ==================================================================

/**
 * Combining multiple algorithms for complex operations
 * This is functional programming in C++!
 */

void demonstrateComposition() {
    cout << "\n=== Algorithm Composition ===\n\n";
    
    vector<int> nums = {1, -2, 3, -4, 5, -6, 7, -8, 9, -10};
    
    // Task: Sum of squares of positive numbers
    // Step by step composition
    
    // Step 1: Filter positives
    //back_inserter allows us to insert elements at the end of the vector
    vector<int> positives;
    copy_if(nums.begin(), nums.end(), back_inserter(positives),
            [](int x) { return x > 0; });

    //print positives
    cout << "Positives: ";
    for (int x : positives) cout << x << " ";
    cout << "\n";
    
    // Step 2: Square them
    vector<int> squares(positives.size());
    transform(positives.begin(), positives.end(), squares.begin(),
              [](int x) { return x * x; });
    //print squares
    cout << "Squares: ";
    for (int x : squares) cout << x << " ";
    cout << "\n";
    
    // Step 3: Sum
    int sum = accumulate(squares.begin(), squares.end(), 0);
    //print sum
    cout << "Sum of squares: " << sum << "\n";
    
    cout << "Original: ";
    for (int x : nums) cout << x << " ";
    cout << "\nPositives: ";
    for (int x : positives) cout << x << " ";
    cout << "\nSquares: ";
    for (int x : squares) cout << x << " ";
    cout << "\nSum of squares: " << sum << "\n";
}

// YOUR TURN: Implement one-liner (no intermediate vectors)
int sumOfSquaresOfPositives(const vector<int>& nums) {
    // TODO: Combine filtering, squaring, and summing in one expression
    // Hint: Use accumulate with complex lambda that checks and squares
    
    // Your code here
    
    return 0;
}

// CHALLENGE: Word frequency analysis
void wordFrequencyAnalysis(const vector<string>& words) {
    // TODO: Using STL algorithms, find:
    // 1. Most common word
    // 2. Longest word
    // 3. Count of unique words
    // 4. Words that appear more than once
    
    cout << "\n=== Word Frequency Analysis ===\n";
    
    // Your code here
    
    cout << "Most common: ???\n";
    cout << "Longest: ???\n";
    cout << "Unique count: ???\n";
    cout << "Duplicates: ???\n";
}


// ==================================================================
// MAIN: Test All Exercises
// ==================================================================

int main() {
    cout << "🚀 DAY 3: Iterators & STL Algorithms\n";
    cout << "=====================================\n\n";
    
    // Demonstrate basics
    // demonstrateIterators();
    // demonstrateTransform();
    // demonstrateAccumulate();
    // demonstrateFindAlgorithms();
    // demonstratePartitionSort();
    // demonstrateFilteringAlgorithms();
    // demonstrateGenerateAlgorithms();
    // demonstrateComposition();
    
    cout << "\n\n--- Testing Your Implementations ---\n";
    
    // Test TODOs (uncomment as you complete them)
    
    {
        cout << "\n1. Convert to strings:\n";
        vector<int> nums = {1, 2, 3, 4, 5};
        auto strs = convertToStrings(nums);
        for (const auto& s : strs) cout << s << " ";
        cout << "\n";
    }
    
    {
        cout << "\n2. Find max:\n";
        vector<int> nums = {3, 1, 4, 1, 5, 9, 2, 6};
        int maxVal = *max_element(nums.begin(), nums.end());
        cout << "Max: " << maxVal << "\n";
    }
    
    {
        cout << "\n3. Find long string:\n";
        vector<string> words = {"hi", "hello", "hey", "greetings"};
        cout << "First word > 5 chars: " << findLongString(words, 5) << "\n";
    }
    
    {
        cout << "\n4. Sort by second:\n";
        vector<pair<string, int>> pairs = {{"a", 3}, {"b", 1}, {"c", 2}};
        sortBySecond(pairs);
        for (const auto& [k, v] : pairs) {
            cout << k << ":" << v << " ";
        }
        cout << "\n";
    }
    
    {
        cout << "\n5. Extract vowel words:\n";
        vector<string> words = {"apple", "banana", "cat", "egg", "dog"};
        auto vowelWords = extractVowelWords(words);
        for (const auto& w : vowelWords) cout << w << " ";
        cout << "\n";
    }
    
    {
        cout << "\n6. Generate squares:\n";
        auto squares = generateSquares(10);
        for (int x : squares) cout << x << " ";
        cout << "\n";
    }
    {
        cout << "\n7. Sum of squares of positives:\n";
        vector<int> nums = {-3, 1, 2, -4, 5};
        int sum = sumOfSquaresOfPositives(nums);
        cout << "Sum: " << sum << "\n";
    }
    
    {
        cout << "\n8. Word frequency analysis:\n";
        vector<string> words = {"apple", "banana", "apple", "orange", "banana", "kiwi"};
        wordFrequencyAnalysis(words);
    }
    
    cout << "\n✅ Day 3 Complete! You now think in algorithms, not loops!\n";
    cout << "📝 Tomorrow: Stack, Queue, Deque - Linear Data Structures\n";
    
    return 0;
}

/* ==================================================================
   🎓 KEY TAKEAWAYS FROM DAY 3:
   ==================================================================
   
   1. ITERATOR CATEGORIES:
      - Know which algorithms work with which iterators
      - Random access (vector) enables more algorithms than bidirectional (list)
      - Always check iterator validity after modifications
   
   2. WHY USE ALGORITHMS OVER LOOPS:
      - More expressive: Intent is clear from algorithm name
      - Less error-prone: No manual index management
      - Optimized: STL implementations are highly tuned
      - Composable: Easier to chain operations
      - Generic: Works with any container
   
   3. LAMBDA EXPRESSIONS:
   //explain me what is capture here?
   
      - [capture](params) { body }
      - Capture by value [=] or reference [&]
      - Capture specific variables [x, &y]
      - Mutable lambdas: [=]() mutable { }
   
   4. ALGORITHM PATTERNS:
      - Transform: Apply function to each element
      - Accumulate: Reduce to single value
      - Find: Search with predicate
      - Partition: Split by condition
      - Copy/Remove: Filter elements
      - Generate: Create sequences
   
   5. PERFORMANCE NOTES:
      - Most algorithms are O(n) single pass
      - sort is O(n log n)
      - partition is O(n) linear!
      - nth_element is O(n) average (faster than full sort!)
      - Algorithms with _if suffix take predicates
   
   6. COMMON GOTCHAS:
      - remove_if doesn't delete! Use erase-remove idiom
      - unique only removes CONSECUTIVE duplicates (sort first!)
      - back_inserter for dynamic containers
      - Check iterator != end() before dereferencing
   
   ==================================================================
   🔍 ALGORITHM COMPLEXITY REFERENCE:
   ==================================================================
   
   O(1):     fill, fill_n, swap
   O(n):     transform, accumulate, find, count, copy, partition, unique
   O(n²):    (none in STL! avoid nested loops)
   O(n log n): sort, stable_sort, partial_sort
   O(n) avg: nth_element (O(n²) worst)
   
   ==================================================================
   📚 FURTHER PRACTICE:
   ==================================================================
   
   LeetCode Problems (Algorithm-Focused):
   - Easy: Remove Element, Move Zeroes, Intersection of Arrays
   - Medium: Product of Array Except Self, Sort Colors (Dutch Flag)
   - Medium: Kth Largest Element (use nth_element!)
   - Medium: Top K Frequent Elements
   - Hard: Median of Two Sorted Arrays
   
   Study Resources:
   - cppreference.com/algorithms
   - CPlusPlusThings/basic_content/algorithm
   - CppCoreGuidelines on algorithm usage
   
   ==================================================================
   💪 CHALLENGE EXERCISES (Optional):
   ==================================================================
   
   1. Implement map/filter/reduce using only STL algorithms
   2. Chain algorithms to solve: "Sum of squares of even numbers > 10"
   3. Implement quicksort using partition
   4. Use nth_element to find median in O(n)
   5. Custom comparator for complex sorting (sort by multiple fields)
   6. Implement set operations (union, intersection) with algorithms
   
   ==================================================================
   🎯 STYLE GUIDE:
   ==================================================================
   
   ✅ PREFER:
   - STL algorithms over manual loops (when clear)
   - Lambda captures: [&] for reference, [=] for value
   - const& in lambda parameters for objects
   - auto for iterator types
   - Range-based for when not using algorithms
   
   ❌ AVOID:
   - Manual index loops when algorithm exists
   - Forgetting erase after remove_if
   - Modifying container while iterating
   - Complex lambdas (extract to named function)
   
   ================================================================== */
