# 🚗 Project Ideas for Days 50-100

## 📋 Quick Reference

| Project | Difficulty | Duration | Skills Practiced |
|---------|-----------|----------|------------------|
| Lane Detection | Medium | 5-7 days | OpenCV, Image Processing |
| CLI Task Manager | Easy | 3-4 days | File I/O, Data Structures |
| Memory Profiler | Hard | 7-10 days | Smart Pointers, RAII |
| Mini Game Engine | Medium | 8-10 days | OOP, Design Patterns |
| CAN Bus Parser | Medium | 4-5 days | Automotive, Parsing |
| Thread Pool | Hard | 5-6 days | Concurrency, Sync |

---

## 🚗 Category 1: Automotive & ADAS Projects

### **Project 1: Lane Detection System**
**Duration:** 5-7 days | **Difficulty:** Medium

**What You'll Build:**
A real-time lane detection system that processes video frames and identifies lane markings.

**Skills Practiced:**
- OpenCV image processing
- Hough transform for line detection
- Region of interest masking
- Video stream processing

**Implementation Steps:**
```cpp
Day 1-2: Setup & Image Preprocessing
  - Load video with cv::VideoCapture
  - Convert to grayscale
  - Apply Gaussian blur
  - Canny edge detection

Day 3-4: Lane Detection Algorithm
  - Define region of interest (ROI)
  - Hough transform for line detection
  - Filter and average lines
  - Distinguish left/right lanes

Day 5-6: Optimization & Visualization
  - Real-time processing
  - Draw lanes on original frame
  - Calculate lane deviation
  - FPS optimization

Day 7: Testing & Documentation
  - Test on different videos
  - Edge case handling
  - Performance benchmarking
```

**Code Structure:**
```
lane-detection/
├── CMakeLists.txt
├── src/
│   ├── main.cpp
│   ├── lane_detector.cpp
│   ├── image_processor.cpp
│   └── video_handler.cpp
├── include/
│   ├── lane_detector.h
│   └── image_processor.h
└── test_videos/
```

**Reference Repos:**
- `open-adas/src/lane_detection/`
- `opencv/samples/cpp/tutorial_code/ImgTrans/`

**Key Algorithms:**
```cpp
// Canny Edge Detection
cv::Mat edges;
cv::Canny(gray_image, edges, 50, 150);

// Hough Line Transform
vector<cv::Vec4i> lines;
cv::HoughLinesP(edges, lines, 1, CV_PI/180, 50, 50, 10);

// Region of Interest Masking
cv::Mat mask = cv::Mat::zeros(image.size(), CV_8UC1);
cv::fillPoly(mask, roi_vertices, cv::Scalar(255));
cv::bitwise_and(edges, mask, masked_edges);
```

**Extensions:**
- Add curve fitting for curved roads
- Implement color-based lane detection
- Add nighttime detection capability
- Vehicle position calculation

---

### **Project 2: Object Detection & Tracking**
**Duration:** 7-10 days | **Difficulty:** Hard

**What You'll Build:**
Multi-object tracker using Kalman filter and YOLO/HOG detection.

**Features:**
- Real-time object detection
- Multi-object tracking with ID assignment
- Trajectory prediction
- Bounding box visualization

**Implementation Phases:**

**Phase 1: Detection (Days 1-3)**
```cpp
// Using HOG + SVM for pedestrian detection
cv::HOGDescriptor hog;
hog.setSVMDetector(cv::HOGDescriptor::getDefaultPeopleDetector());

vector<cv::Rect> detections;
hog.detectMultiScale(frame, detections);
```

**Phase 2: Tracking (Days 4-6)**
```cpp
// Kalman Filter for prediction
class ObjectTracker {
    cv::KalmanFilter kf;
    int track_id;
    
public:
    void predict();
    void update(cv::Rect measurement);
    cv::Rect getEstimate();
};
```

**Phase 3: Association (Days 7-8)**
- Hungarian algorithm for data association
- Handle occlusions and missed detections
- Track lifecycle management

**Skills Learned:**
- Computer vision algorithms
- State estimation (Kalman filter)
- Multi-object data association
- Template specialization

**Reference:**
- `opencv/samples/cpp/kalman.cpp`
- `open-adas/` tracking examples

---

### **Project 3: CAN Bus Message Parser**
**Duration:** 4-5 days | **Difficulty:** Medium

**What You'll Build:**
A parser for automotive CAN bus messages with DBC file support.

**Features:**
- Parse DBC (Database CAN) files
- Decode CAN messages
- Signal extraction and scaling
- Real-time message monitoring

**Structure:**
```cpp
class CANMessage {
    uint32_t id;
    vector<uint8_t> data;
    
public:
    template<typename T>
    T extractSignal(string signal_name);
};

class DBCParser {
    map<uint32_t, MessageDefinition> messages;
    
public:
    void loadDBC(string filename);
    CANMessage decode(vector<uint8_t> raw_data);
};
```

**Learning Focus:**
- Binary data manipulation
- Bit masking and shifting
- File parsing
- Template functions

**Test Data:**
Use `openpilot/opendbc/` DBC files

**Example:**
```cpp
// Extract speed from CAN message
// Signal: byte 2-3, little endian, scale 0.01, offset 0
uint16_t raw = (data[3] << 8) | data[2];
float speed_kph = raw * 0.01f;
```

---

## 💻 Category 2: CLI & Developer Tools

### **Project 4: Git-like Version Control**
**Duration:** 10-14 days | **Difficulty:** Hard

**What You'll Build:**
Simplified version control system with core Git features.

**Core Features:**
- Initialize repository
- Stage and commit files
- Branch management
- Diff visualization
- Hash-based object storage

**Day-by-Day Plan:**

**Days 1-3: Object Storage**
```cpp
class GitObject {
    string type; // blob, tree, commit
    string hash; // SHA-1
    vector<uint8_t> content;
    
public:
    void save();
    static GitObject load(string hash);
};

// Store objects in .mygit/objects/ab/cdef123...
```

**Days 4-6: Index & Staging**
```cpp
class Index {
    map<string, FileEntry> entries;
    
public:
    void addFile(string path);
    void removeFile(string path);
    void write();
};
```

**Days 7-9: Commit & History**
```cpp
class Commit {
    string tree_hash;
    vector<string> parent_hashes;
    string message;
    time_t timestamp;
    
public:
    string createCommit();
    static Commit load(string hash);
};
```

**Days 10-12: Branching**
- HEAD pointer management
- Branch creation/switching
- Merge conflict detection

**Days 13-14: CLI Interface**
```bash
$ mygit init
$ mygit add file.cpp
$ mygit commit -m "Initial commit"
$ mygit branch feature
$ mygit checkout feature
```

**Skills Learned:**
- File system operations
- SHA hashing (use OpenSSL or std::hash)
- Command-line parsing
- Data serialization

---

### **Project 5: Task Manager with SQLite**
**Duration:** 4-5 days | **Difficulty:** Easy-Medium

**What You'll Build:**
CLI task manager with database persistence.

**Features:**
```bash
$ taskman add "Complete Day 50 exercises" --priority high --due 2025-12-31
$ taskman list --filter priority:high
$ taskman complete 5
$ taskman stats
```

**Tech Stack:**
- SQLite3 for storage
- CLI11 or custom arg parser
- std::chrono for dates
- ncurses for TUI (optional)

**Database Schema:**
```sql
CREATE TABLE tasks (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    priority TEXT,
    status TEXT,
    created_at TIMESTAMP,
    due_date TIMESTAMP
);
```

**C++ Implementation:**
```cpp
class TaskManager {
    sqlite3* db;
    
public:
    void addTask(Task task);
    vector<Task> getTasks(Filter filter);
    void updateTask(int id, Task task);
    Statistics getStatistics();
};
```

**Learning Focus:**
- SQL integration
- RAII for database connections
- Command pattern for undo/redo
- Data validation

---

### **Project 6: Memory Leak Detector**
**Duration:** 6-8 days | **Difficulty:** Hard

**What You'll Build:**
A custom memory profiler to detect leaks and track allocations.

**Approach:**
Override global new/delete operators
```cpp
void* operator new(size_t size) {
    void* ptr = malloc(size);
    MemoryTracker::instance().recordAllocation(ptr, size);
    return ptr;
}

void operator delete(void* ptr) noexcept {
    MemoryTracker::instance().recordDeallocation(ptr);
    free(ptr);
}
```

**Features:**
- Track allocation/deallocation pairs
- Detect memory leaks at program exit
- Stack trace capture (use libunwind)
- Memory usage statistics
- Report generation

**Data Structure:**
```cpp
class MemoryTracker {
    struct AllocationInfo {
        size_t size;
        string file;
        int line;
        vector<void*> stack_trace;
    };
    
    map<void*, AllocationInfo> allocations;
    
public:
    void recordAllocation(void* ptr, size_t size);
    void recordDeallocation(void* ptr);
    void generateReport();
};
```

**Challenge:**
- Thread-safety (use mutex)
- Avoid infinite recursion (internal allocations)
- Minimal performance overhead

---

## 🎮 Category 3: Game Development

### **Project 7: 2D Physics Engine**
**Duration:** 8-10 days | **Difficulty:** Medium-Hard

**What You'll Build:**
Rigid body physics simulation with collision detection.

**Core Components:**

**Day 1-2: Math Library**
```cpp
struct Vec2 {
    float x, y;
    Vec2 operator+(const Vec2& other) const;
    float dot(const Vec2& other) const;
    float magnitude() const;
};

struct Transform {
    Vec2 position;
    float rotation;
};
```

**Day 3-4: Rigid Bodies**
```cpp
class RigidBody {
    Vec2 position;
    Vec2 velocity;
    Vec2 acceleration;
    float mass;
    float rotation;
    float angular_velocity;
    
public:
    void applyForce(Vec2 force);
    void update(float dt);
};
```

**Day 5-6: Collision Detection**
```cpp
// AABB (Axis-Aligned Bounding Box)
bool checkCollision(const AABB& a, const AABB& b);

// Circle collision
bool checkCollision(const Circle& a, const Circle& b);

// SAT (Separating Axis Theorem) for polygons
bool checkCollision(const Polygon& a, const Polygon& b);
```

**Day 7-8: Collision Response**
- Impulse-based resolution
- Friction and restitution
- Contact manifold generation

**Day 9-10: Integration & Demo**
- Integrate with SDL2 for visualization
- Create interactive demo
- Optimize broad phase (spatial hashing)

**Learning:**
- Vector math
- Numerical integration (Verlet, RK4)
- Template metaprogramming
- Design patterns (Component pattern)

---

### **Project 8: Entity Component System (ECS)**
**Duration:** 6-8 days | **Difficulty:** Hard

**What You'll Build:**
Data-oriented game architecture like Unity's ECS.

**Architecture:**
```cpp
// Component: Plain data
struct Position { float x, y; };
struct Velocity { float dx, dy; };
struct Sprite { string texture; };

// Entity: Just an ID
using Entity = uint32_t;

// System: Logic operating on components
class MovementSystem : public System {
public:
    void update(EntityManager& em, float dt) {
        for (auto entity : entities_with<Position, Velocity>()) {
            auto& pos = em.getComponent<Position>(entity);
            auto& vel = em.getComponent<Velocity>(entity);
            pos.x += vel.dx * dt;
            pos.y += vel.dy * dt;
        }
    }
};
```

**Key Concepts:**
- Component storage (SoA vs AoS)
- Archetype-based organization
- Cache-friendly iteration
- Type-safe component access

**Implementation Challenges:**
- Template metaprogramming for queries
- Memory pool allocators
- Component bitmasks
- System dependencies

**Reference:** Study `richard/ecs/` examples

---

## 🔧 Category 4: Systems Programming

### **Project 9: Thread Pool Implementation**
**Duration:** 5-6 days | **Difficulty:** Hard

**What You'll Build:**
Production-quality thread pool with work stealing.

**Features:**
- Fixed-size worker threads
- Task queue with priorities
- Work stealing for load balancing
- Future/Promise pattern
- Graceful shutdown

**Interface:**
```cpp
class ThreadPool {
public:
    ThreadPool(size_t num_threads);
    ~ThreadPool();
    
    template<typename F, typename... Args>
    auto submit(F&& f, Args&&... args) 
        -> std::future<decltype(f(args...))>;
    
    void shutdown();
};

// Usage
ThreadPool pool(4);
auto future = pool.submit([]{ return 42; });
int result = future.get();
```

**Implementation Details:**

**Day 1-2: Basic Thread Pool**
```cpp
class ThreadPool {
    vector<thread> workers;
    queue<function<void()>> tasks;
    mutex queue_mutex;
    condition_variable cv;
    bool stop;
    
    void workerThread();
};
```

**Day 3-4: Future/Promise Integration**
```cpp
template<typename F, typename... Args>
auto submit(F&& f, Args&&... args) {
    using ReturnType = decltype(f(args...));
    auto task = make_shared<packaged_task<ReturnType()>>(
        bind(forward<F>(f), forward<Args>(args)...)
    );
    
    future<ReturnType> result = task->get_future();
    
    {
        unique_lock<mutex> lock(queue_mutex);
        tasks.emplace([task]{ (*task)(); });
    }
    
    cv.notify_one();
    return result;
}
```

**Day 5: Work Stealing**
- Per-thread work queues
- Lock-free deques
- Steal from other threads when idle

**Day 6: Testing & Benchmarking**
- Stress tests with many tasks
- Compare with std::async
- Measure throughput

**Skills:**
- Advanced concurrency
- Perfect forwarding
- Template metaprogramming
- Lock-free programming

---

### **Project 10: Custom Memory Allocator**
**Duration:** 7-9 days | **Difficulty:** Hard

**What You'll Build:**
High-performance memory allocators for different use cases.

**Types to Implement:**

**1. Pool Allocator (Fixed-size)**
```cpp
template<typename T, size_t BlockSize>
class PoolAllocator {
    union Block {
        T value;
        Block* next;
    };
    
    Block* free_list;
    
public:
    T* allocate();
    void deallocate(T* ptr);
};
```

**2. Stack Allocator (Linear)**
```cpp
class StackAllocator {
    char* buffer;
    size_t offset;
    size_t capacity;
    
public:
    void* allocate(size_t size, size_t alignment);
    void reset(); // Free all at once
};
```

**3. Buddy Allocator**
- Power-of-two block sizes
- Fast coalescing
- Minimal fragmentation

**Benchmarking:**
Compare against malloc/new:
- Allocation speed
- Deallocation speed
- Fragmentation
- Cache performance

**Integration:**
```cpp
// Use with STL containers
vector<int, PoolAllocator<int, 1024>> vec;
```

---

## 🌐 Category 5: Network & Distributed

### **Project 11: HTTP Server**
**Duration:** 8-10 days | **Difficulty:** Medium-Hard

**What You'll Build:**
Minimal HTTP/1.1 server with routing.

**Features:**
- Socket programming (POSIX or Boost.Asio)
- HTTP parsing
- Route handlers
- Static file serving
- Multithreaded request handling

**Example API:**
```cpp
HttpServer server(8080);

server.get("/api/users", [](const Request& req, Response& res) {
    res.json({{"users", getUserList()}});
});

server.post("/api/users", [](const Request& req, Response& res) {
    auto user = req.jsonBody<User>();
    createUser(user);
    res.status(201).send("Created");
});

server.listen();
```

**Day-by-Day:**
1-2: Socket basics, accept connections
3-4: HTTP parser (method, headers, body)
5-6: Routing system with regex matching
7-8: Response builder, content types
9-10: Thread pool integration, stress testing

---

### **Project 12: Distributed Key-Value Store**
**Duration:** 14+ days | **Difficulty:** Very Hard

**What You'll Build:**
Simplified Redis-like in-memory database.

**Features:**
- TCP server for client connections
- Data structures: strings, lists, sets, hashes
- Persistence (AOF, snapshots)
- Replication
- Pub/Sub messaging

**Commands:**
```bash
SET key value
GET key
LPUSH list value
HSET hash field value
PUBLISH channel message
```

**Architecture:**
```cpp
class KVStore {
    map<string, Value> storage;
    mutex storage_mutex;
    
public:
    void set(string key, Value value);
    optional<Value> get(string key);
};

class ReplicationManager {
    void sendToReplicas(Command cmd);
    void syncWithMaster();
};
```

**Advanced Topics:**
- RESP protocol implementation
- Event loop (epoll/kqueue)
- Consistent hashing for sharding
- Raft consensus for high availability

---

## 📊 Project Selection Guide

### **Choose Based on Your Interest:**

**Computer Vision Enthusiast?**
→ Lane Detection, Object Tracking

**Systems Programmer?**
→ Thread Pool, Memory Allocator, Version Control

**Game Developer?**
→ Physics Engine, ECS, Mini Game

**Backend Developer?**
→ HTTP Server, Task Manager, KV Store

**Automotive Engineer?**
→ CAN Parser, ADAS Tools, Open-ADAS integration

---

## 🎯 Success Metrics

For each project, aim to:
- ✅ Write clean, documented code
- ✅ Include unit tests (use Catch2)
- ✅ Benchmark performance
- ✅ Create demo/example usage
- ✅ Write README with build instructions
- ✅ Push to GitHub portfolio

---

## 🔗 Integration with Your Repos

**Apollo Integration:**
- Study `apollo/modules/perception/` for vision
- Use `apollo/cyber/` for messaging patterns
- Learn from `apollo/modules/planning/` for algorithms

**Autoware Integration:**
- Check `autoware/docker/` for containerization
- Study `autoware/ansible/` for deployment
- Learn ROS2 patterns if interested

**OpenCV Integration:**
- Use `opencv/samples/` as reference
- Study `opencv/modules/` implementation
- Contribute improvements back

**Open-ADAS:**
- Fork and enhance existing features
- Add new detection algorithms
- Improve real-time performance

---

## 💡 Pro Tips

1. **Start Small:** Pick easy projects first to build confidence
2. **Iterate:** V1 doesn't need all features
3. **Document:** Write design docs before coding
4. **Test:** TDD helps prevent bugs
5. **Profile:** Use gprof, valgrind, perf
6. **Refactor:** Clean code after it works
7. **Share:** Blog about your learnings

---

**Ready to build? Start with the project that excites you most! 🚀**
