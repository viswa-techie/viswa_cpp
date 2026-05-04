# Reading multiple inputs

> **Level:** 0 — Absolute Beginner  
> **Category:** C00 — C++ Syntax & Program Structure  
> **Topic:** syntax

---

## Problem Statement
Read multiple values from the user in one or more `cin` operations.

## Solution 1: Chained extraction
```cpp
#include <iostream>

int main() {
    int a, b, c;
    std::cout << "Enter three numbers: ";
    std::cin >> a >> b >> c;  // User can type: 10 20 30
    std::cout << "Sum: " << (a + b + c) << "\n";
    return 0;
}
```

## Solution 2: Reading in a loop
```cpp
#include <iostream>
#include <vector>

int main() {
    int n;
    std::cout << "How many numbers? ";
    std::cin >> n;

    std::vector<int> nums(n);
    for (int i = 0; i < n; ++i) {
        std::cin >> nums[i];
    }

    int sum = 0;
    for (int x : nums) sum += x;
    std::cout << "Sum: " << sum << "\n";
    return 0;
}
```

## Solution 3: Reading until EOF
```cpp
#include <iostream>

int main() {
    int x, sum = 0, count = 0;
    while (std::cin >> x) {  // Reads until EOF (Ctrl+D on Linux, Ctrl+Z on Windows)
        sum += x;
        ++count;
    }
    std::cout << "Average: " << (count > 0 ? (double)sum / count : 0) << "\n";
    return 0;
}
```

## Key Takeaways
1. `cin >>` skips whitespace between values
2. Chained `>>` reads multiple values separated by spaces or newlines
3. `while (cin >> x)` is the standard pattern for reading until EOF
4. Check `cin.fail()` after reading to detect invalid input
