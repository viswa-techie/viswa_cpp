# Nested namespace (C++17)

> **Level:** 0 — Absolute Beginner  
> **Category:** C00 — C++ Syntax & Program Structure  
> **Topic:** syntax

---

## Problem Statement
Use nested namespaces and the C++17 shorthand for deep namespace hierarchies.

## What You Need to Know
- Namespaces can be nested: `namespace A { namespace B { ... } }`.
- C++17 adds shorthand: `namespace A::B { ... }`.
- Common in large projects to organize code hierarchically.

## Pre-C++17: Nested Namespaces
```cpp
#include <iostream>

namespace Company {
    namespace Project {
        namespace Module {
            void hello() {
                std::cout << "Hello from Company::Project::Module\n";
            }
        }
    }
}

int main() {
    Company::Project::Module::hello();
    return 0;
}
```

## C++17: Compact Syntax
```cpp
#include <iostream>

namespace Company::Project::Module {
    void hello() {
        std::cout << "Hello from Company::Project::Module\n";
    }
}

int main() {
    Company::Project::Module::hello();
    return 0;
}
```

## Real-World Example
```cpp
#include <iostream>
#include <string>

namespace myapp::graphics::rendering {
    struct Viewport {
        int width, height;
    };

    void render(const Viewport& vp) {
        std::cout << "Rendering " << vp.width << "x" << vp.height << "\n";
    }
}

namespace myapp::audio {
    void playSound(const std::string& name) {
        std::cout << "Playing: " << name << "\n";
    }
}

int main() {
    myapp::graphics::rendering::Viewport vp{1920, 1080};
    myapp::graphics::rendering::render(vp);
    myapp::audio::playSound("click.wav");

    // Alias for convenience
    namespace gfx = myapp::graphics::rendering;
    gfx::render(vp);

    return 0;
}
```

## Key Takeaways
1. Nested namespaces organize large projects hierarchically
2. C++17 shorthand: `namespace A::B::C { }` instead of three nested blocks
3. Use namespace aliases for deep hierarchies: `namespace ns = A::B::C;`
4. Access with full path: `A::B::C::function()`
5. Must compile with `-std=c++17` or later for the shorthand

## Common Mistakes
- Using `::` syntax in pre-C++17 code → compile error
- Deeply nested namespaces making code verbose → use aliases
- Forgetting `-std=c++17` flag → "expected '{'" errors
