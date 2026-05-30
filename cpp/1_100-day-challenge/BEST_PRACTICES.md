# 🎓 C++ Best Practices & Code Snippets

## Table of Contents
1. [Memory Management](#memory-management)
2. [Smart Pointers](#smart-pointers)
3. [RAII Pattern](#raii-pattern)
4. [Move Semantics](#move-semantics)
5. [Templates](#templates)
6. [OOP Design](#oop-design)
7. [STL Best Practices](#stl-best-practices)
8. [Performance Tips](#performance-tips)
9. [Debugging Techniques](#debugging-techniques)

---

## 🧠 Memory Management

### **Rule #1: Avoid Manual Memory Management**

❌ **BAD - Manual new/delete:**
```cpp
void processData() {
    int* data = new int[1000];
    // If exception thrown here, memory leaks!
    process(data);
    delete[] data; // Easy to forget
}
```

✅ **GOOD - Use containers or smart pointers:**
```cpp
void processData() {
    vector<int> data(1000);
    process(data); // Automatic cleanup, exception-safe
}

void processData_Alternative() {
    auto data = make_unique<int[]>(1000);
    process(data.get());
    // Automatic cleanup guaranteed
}
```

**Why?**
- Containers manage memory automatically
- Exception-safe (no leaks even if exception thrown)
- Compiler can optimize (NRVO, RVO)

---

### **Rule #2: Match new/delete Correctly**

❌ **WRONG - Mixing new[]/delete:**
```cpp
int* arr = new int[10];
delete arr; // UNDEFINED BEHAVIOR! Should be delete[]
```

✅ **CORRECT:**
```cpp
int* single = new int;
delete single; // Matches new

int* array = new int[10];
delete[] array; // Matches new[]

// BETTER: Don't use raw new at all!
auto single = make_unique<int>(42);
auto array = make_unique<int[]>(10);
```

---

### **Rule #3: Avoid Memory Leaks with RAII**

**RAII = Resource Acquisition Is Initialization**

❌ **BAD - Manual cleanup:**
```cpp
void readFile() {
    FILE* file = fopen("data.txt", "r");
    if (!file) return; // Forgot to close!
    
    // ... processing ...
    if (error) return; // Leaked file handle!
    
    fclose(file); // Only reached on success path
}
```

✅ **GOOD - RAII wrapper:**
```cpp
class FileHandle {
    FILE* file;
public:
    FileHandle(const char* filename, const char* mode) 
        : file(fopen(filename, mode)) {
        if (!file) throw runtime_error("Cannot open file");
    }
    
    ~FileHandle() { 
        if (file) fclose(file); 
    }
    
    // Delete copy operations (file handles shouldn't be copied)
    FileHandle(const FileHandle&) = delete;
    FileHandle& operator=(const FileHandle&) = delete;
    
    // Allow move operations
    FileHandle(FileHandle&& other) noexcept : file(other.file) {
        other.file = nullptr;
    }
    
    FILE* get() { return file; }
};

void readFile() {
    FileHandle file("data.txt", "r"); // Automatic cleanup!
    // ... processing ...
    // File automatically closed when scope exits (even on exception)
}

// EVEN BETTER: Use standard library
void readFile_Modern() {
    ifstream file("data.txt");
    if (!file) throw runtime_error("Cannot open file");
    // ... processing ...
    // Automatic cleanup
}
```

**Key Insight:** 
- Constructor acquires resource
- Destructor releases resource
- Guaranteed cleanup via stack unwinding

---

## 🔒 Smart Pointers

### **unique_ptr - Single Ownership**

Use when: One owner, no sharing needed

```cpp
// Creation
auto ptr = make_unique<Widget>(arg1, arg2); // Preferred
unique_ptr<Widget> ptr2(new Widget());      // Avoid this

// Ownership transfer (move semantics)
unique_ptr<Widget> owner1 = make_unique<Widget>();
unique_ptr<Widget> owner2 = move(owner1); // owner1 is now nullptr

// Cannot copy (compilation error)
// unique_ptr<Widget> copy = owner2; // ERROR!

// Custom deleter
auto deleter = [](Widget* w) { 
    cout << "Custom cleanup\n"; 
    delete w; 
};
unique_ptr<Widget, decltype(deleter)> ptr(new Widget(), deleter);

// Array support
auto arr = make_unique<int[]>(100); // Calls delete[] automatically
```

**Common Pattern: Factory Functions**
```cpp
unique_ptr<Shape> createShape(string type) {
    if (type == "circle") return make_unique<Circle>();
    if (type == "square") return make_unique<Square>();
    return nullptr;
}

auto shape = createShape("circle"); // Transfer ownership
```

---

### **shared_ptr - Shared Ownership**

Use when: Multiple owners, reference counting needed

```cpp
// Creation
auto ptr1 = make_shared<Widget>(); // Efficient (single allocation)
shared_ptr<Widget> ptr2(new Widget()); // Less efficient (two allocations)

// Sharing ownership
shared_ptr<Widget> ptr3 = ptr1; // Both own the Widget
cout << ptr1.use_count(); // Prints: 2

// Reference counting
{
    auto ptr4 = ptr1; // use_count = 3
} // ptr4 destroyed, use_count = 2

// Object deleted when last shared_ptr destroyed
ptr1.reset(); // use_count = 1
ptr3.reset(); // use_count = 0, Widget deleted

// Custom deleter
auto deleter = [](Widget* w) { delete w; };
shared_ptr<Widget> ptr(new Widget(), deleter);

// Aliasing constructor (share ownership, different pointer)
shared_ptr<int> parent = make_shared<vector<int>>(10);
shared_ptr<int> element(&(*parent)[0], parent); // Keep vector alive
```

**⚠️ DANGER: Circular References**
```cpp
struct Node {
    shared_ptr<Node> next; // Problem: creates cycle
};

auto n1 = make_shared<Node>();
auto n2 = make_shared<Node>();
n1->next = n2;
n2->next = n1; // Cycle! Memory never freed!
```

---

### **weak_ptr - Break Cycles**

Use when: Observer pattern, cache, break circular references

```cpp
struct Node {
    shared_ptr<Node> next;
    weak_ptr<Node> prev; // Doesn't increase ref count!
};

// Creating weak_ptr from shared_ptr
shared_ptr<Widget> shared = make_shared<Widget>();
weak_ptr<Widget> weak = shared; // Observer, doesn't own

// Accessing through weak_ptr (must check validity)
if (auto locked = weak.lock()) { // Returns shared_ptr if valid
    locked->doSomething();
} else {
    // Object was deleted
}

// Check if expired
if (weak.expired()) {
    cout << "Object deleted\n";
}
```

**Real-World Example: Cache**
```cpp
class WidgetCache {
    map<string, weak_ptr<Widget>> cache;
    
public:
    shared_ptr<Widget> get(const string& key) {
        auto it = cache.find(key);
        if (it != cache.end()) {
            if (auto locked = it->second.lock()) {
                return locked; // Cache hit
            }
            cache.erase(it); // Entry expired
        }
        
        // Cache miss: create new
        auto widget = make_shared<Widget>(key);
        cache[key] = widget;
        return widget;
    }
};
```

---

### **Smart Pointer Decision Tree**

```
Need shared ownership?
├─ NO → Use unique_ptr
│      └─ Need to transfer ownership? → Return by value (move)
│
└─ YES → Use shared_ptr
       ├─ Need to observe without owning? → Also use weak_ptr
       └─ Beware of circular references!
```

---

## 🚀 Move Semantics

### **Understanding Lvalues vs Rvalues**

```cpp
int x = 5;          // x is lvalue (has address, persistent)
int y = x + 2;      // x+2 is rvalue (temporary, no address)

string s1 = "hi";   // s1 is lvalue
string s2 = s1;     // Copy: s1 is lvalue
string s3 = "hi";   // Move: "hi" is rvalue (temporary)
```

### **Move Constructor & Move Assignment**

```cpp
class Buffer {
    char* data;
    size_t size;
    
public:
    // Regular constructor
    Buffer(size_t sz) : size(sz), data(new char[sz]) {
        cout << "Allocating " << sz << " bytes\n";
    }
    
    // Copy constructor (expensive)
    Buffer(const Buffer& other) : size(other.size), data(new char[other.size]) {
        cout << "Copying " << size << " bytes\n";
        copy(other.data, other.data + size, data);
    }
    
    // Move constructor (cheap - steal resources)
    Buffer(Buffer&& other) noexcept 
        : size(other.size), data(other.data) {
        cout << "Moving " << size << " bytes\n";
        other.data = nullptr; // Leave source in valid state
        other.size = 0;
    }
    
    // Copy assignment
    Buffer& operator=(const Buffer& other) {
        if (this != &other) {
            delete[] data;
            size = other.size;
            data = new char[size];
            copy(other.data, other.data + size, data);
        }
        return *this;
    }
    
    // Move assignment
    Buffer& operator=(Buffer&& other) noexcept {
        if (this != &other) {
            delete[] data; // Clean up current resources
            
            data = other.data; // Steal resources
            size = other.size;
            
            other.data = nullptr; // Leave source valid
            other.size = 0;
        }
        return *this;
    }
    
    ~Buffer() {
        delete[] data;
        cout << "Destroying buffer\n";
    }
};

// Usage
Buffer b1(1000);                    // Constructor
Buffer b2 = b1;                     // Copy constructor
Buffer b3 = move(b1);               // Move constructor (b1 now empty)
Buffer b4 = createBuffer();         // Move (return value optimization)
```

**Output:**
```
Allocating 1000 bytes
Copying 1000 bytes
Moving 1000 bytes
```

---

### **std::move vs std::forward**

```cpp
// std::move: Unconditional cast to rvalue
template<typename T>
void process(T&& arg) {
    // Wrong: moves even if arg was lvalue
    someFunction(move(arg)); 
}

// std::forward: Conditional cast (perfect forwarding)
template<typename T>
void process(T&& arg) {
    // Preserves lvalue/rvalue nature
    someFunction(forward<T>(arg)); 
}
```

**Perfect Forwarding Example:**
```cpp
template<typename T, typename... Args>
unique_ptr<T> make_unique_verbose(Args&&... args) {
    cout << "Creating object...\n";
    return unique_ptr<T>(new T(forward<Args>(args)...));
}

// Usage
auto ptr = make_unique_verbose<string>(10, 'x'); // Forwards all args
```

---

### **Move-Only Types**

```cpp
class FileHandle {
    int fd;
    
public:
    FileHandle(const char* path) : fd(open(path, O_RDONLY)) {}
    
    // Delete copy (file handles shouldn't be copied)
    FileHandle(const FileHandle&) = delete;
    FileHandle& operator=(const FileHandle&) = delete;
    
    // Allow move
    FileHandle(FileHandle&& other) noexcept : fd(other.fd) {
        other.fd = -1;
    }
    
    FileHandle& operator=(FileHandle&& other) noexcept {
        if (this != &other) {
            if (fd >= 0) close(fd);
            fd = other.fd;
            other.fd = -1;
        }
        return *this;
    }
    
    ~FileHandle() {
        if (fd >= 0) close(fd);
    }
};

// Usage
FileHandle f1("data.txt");
// FileHandle f2 = f1;      // ERROR: cannot copy
FileHandle f2 = move(f1);   // OK: transfer ownership
```

---

## 📐 Templates

### **Function Templates**

```cpp
// Basic function template
template<typename T>
T max(T a, T b) {
    return (a > b) ? a : b;
}

// Multiple type parameters
template<typename T, typename U>
auto add(T a, U b) -> decltype(a + b) {
    return a + b;
}

// C++14: auto return type deduction
template<typename T, typename U>
auto add_modern(T a, U b) {
    return a + b;
}

// Template specialization
template<>
const char* max<const char*>(const char* a, const char* b) {
    return (strcmp(a, b) > 0) ? a : b;
}
```

---

### **Class Templates**

```cpp
template<typename T, size_t N>
class Array {
    T data[N];
    
public:
    constexpr size_t size() const { return N; }
    
    T& operator[](size_t i) { return data[i]; }
    const T& operator[](size_t i) const { return data[i]; }
    
    // Member function templates
    template<typename Func>
    void forEach(Func f) {
        for (size_t i = 0; i < N; i++) {
            f(data[i]);
        }
    }
};

// Usage
Array<int, 5> arr;
arr.forEach([](int& x) { x *= 2; });
```

---

### **Variadic Templates**

```cpp
// Recursive case
template<typename T, typename... Args>
void print(T first, Args... rest) {
    cout << first << " ";
    if constexpr (sizeof...(rest) > 0) {
        print(rest...); // Unpack and recurse
    }
}

// C++17: Fold expressions
template<typename... Args>
auto sum(Args... args) {
    return (args + ...); // Fold over +
}

// Usage
print(1, 2.5, "hello", 'x'); // Prints: 1 2.5 hello x
int total = sum(1, 2, 3, 4, 5); // Returns: 15
```

---

### **SFINAE & Concepts**

**SFINAE (Substitution Failure Is Not An Error)**

```cpp
// Enable if type is integral
template<typename T>
typename enable_if<is_integral<T>::value, T>::type
increment(T value) {
    return value + 1;
}

// Enable if type is floating point
template<typename T>
typename enable_if<is_floating_point<T>::value, T>::type
increment(T value) {
    return value + 1.0;
}
```

**C++20 Concepts (Modern Approach)**

```cpp
// Define concept
template<typename T>
concept Numeric = is_arithmetic_v<T>;

// Use concept
template<Numeric T>
T increment(T value) {
    return value + 1;
}

// More complex concept
template<typename T>
concept Container = requires(T c) {
    { c.size() } -> convertible_to<size_t>;
    { c.begin() } -> same_as<typename T::iterator>;
    { c.end() } -> same_as<typename T::iterator>;
};
```

---

## 🏗️ OOP Design Principles

### **SOLID Principles**

#### **S - Single Responsibility**

❌ **BAD:**
```cpp
class User {
    string name;
    string email;
    
    void save() { /* database logic */ }
    void sendEmail() { /* email logic */ }
    string generateReport() { /* reporting logic */ }
};
// Problem: Too many responsibilities!
```

✅ **GOOD:**
```cpp
class User {
    string name;
    string email;
public:
    // Only user data management
    string getName() const { return name; }
    string getEmail() const { return email; }
};

class UserRepository {
public:
    void save(const User& user) { /* database */ }
};

class EmailService {
public:
    void send(const User& user, const string& msg) { /* email */ }
};

class ReportGenerator {
public:
    string generate(const User& user) { /* reporting */ }
};
```

---

#### **O - Open/Closed**

❌ **BAD:**
```cpp
class Shape {
public:
    enum Type { CIRCLE, RECTANGLE };
    Type type;
    
    double area() {
        if (type == CIRCLE) { /* circle area */ }
        else if (type == RECTANGLE) { /* rectangle area */ }
        // Need to modify this function for new shapes!
    }
};
```

✅ **GOOD:**
```cpp
class Shape {
public:
    virtual ~Shape() = default;
    virtual double area() const = 0; // Pure virtual
};

class Circle : public Shape {
    double radius;
public:
    Circle(double r) : radius(r) {}
    double area() const override { return 3.14159 * radius * radius; }
};

class Rectangle : public Shape {
    double width, height;
public:
    Rectangle(double w, double h) : width(w), height(h) {}
    double area() const override { return width * height; }
};

// Can add new shapes without modifying existing code!
class Triangle : public Shape {
    double base, height;
public:
    Triangle(double b, double h) : base(b), height(h) {}
    double area() const override { return 0.5 * base * height; }
};
```

---

### **Rule of Zero/Three/Five**

**Rule of Zero:** If you don't need custom resource management, don't declare any special members.

```cpp
class Widget {
    string name;
    vector<int> data;
public:
    // No destructor, copy/move needed - compiler generates them correctly
};
```

**Rule of Three:** If you declare one of (destructor, copy constructor, copy assignment), declare all three.

```cpp
class Buffer {
    char* data;
public:
    ~Buffer() { delete[] data; }
    Buffer(const Buffer& other); // Must declare
    Buffer& operator=(const Buffer& other); // Must declare
};
```

**Rule of Five:** In modern C++, also declare move constructor and move assignment.

```cpp
class Buffer {
    char* data;
public:
    ~Buffer() { delete[] data; }
    
    Buffer(const Buffer& other);
    Buffer& operator=(const Buffer& other);
    
    Buffer(Buffer&& other) noexcept;
    Buffer& operator=(Buffer&& other) noexcept;
};
```

---

## ⚡ Performance Tips

### **1. Pass by const reference**

❌ **Slow:**
```cpp
void process(vector<int> data) { // Copies entire vector!
    // ...
}
```

✅ **Fast:**
```cpp
void process(const vector<int>& data) { // No copy
    // ...
}
```

---

### **2. Reserve capacity**

```cpp
vector<int> v;
v.reserve(1000); // Allocate once
for (int i = 0; i < 1000; i++) {
    v.push_back(i); // No reallocations
}
```

---

### **3. Use emplace instead of push**

```cpp
vector<pair<int, string>> vec;

// Old way: creates temporary, then copies
vec.push_back(make_pair(1, "hello"));

// New way: constructs in-place
vec.emplace_back(1, "hello");
```

---

### **4. Avoid unnecessary copies**

```cpp
// Iterate with const reference
for (const auto& item : large_vector) {
    // No copies
}

// Not: for (auto item : large_vector) // Copies each element!
```

---

### **5. Use string_view**

```cpp
void process(string_view sv) { // No copy, just pointer + length
    cout << sv;
}

string s = "hello";
process(s);           // OK
process("world");     // OK
process(s.substr(0, 3)); // OK
```

---

## 🐛 Debugging Techniques

### **Assertions**

```cpp
#include <cassert>

void setAge(int age) {
    assert(age >= 0 && age < 150); // Debug builds only
    this->age = age;
}

// Production-safe assertions
void setAge_Safe(int age) {
    if (!(age >= 0 && age < 150)) {
        throw invalid_argument("Invalid age");
    }
    this->age = age;
}
```

### **Sanitizers**

```bash
# Address Sanitizer (detects memory errors)
g++ -fsanitize=address -g program.cpp

# Undefined Behavior Sanitizer
g++ -fsanitize=undefined -g program.cpp

# Thread Sanitizer (data races)
g++ -fsanitize=thread -g program.cpp
```

### **Valgrind**

```bash
# Memory leak detection
valgrind --leak-check=full ./program

# Cache profiling
valgrind --tool=cachegrind ./program
```

---

**Continue practicing these patterns daily! They form the foundation of professional C++ code. 🚀**
