# Named namespace basics

> **Level:** 0 — Absolute Beginner  
> **Category:** C00 — C++ Syntax & Program Structure  
> **Topic:** syntax

---

## Problem Statement
Create and use named namespaces to organize your code.

## What You Need to Know
- Named namespaces group related declarations under a unique name.
- They can span multiple files (the namespace is "reopened").
- Access members with `namespace_name::member`.

## Creating a Namespace
```cpp
#include <iostream>

namespace Graphics {
    struct Color {
        int r, g, b;
    };

    void setBackground(Color c) {
        std::cout << "BG: " << c.r << "," << c.g << "," << c.b << "\n";
    }
}

namespace Audio {
    void play(const std::string& file) {
        std::cout << "Playing: " << file << "\n";
    }

    void setVolume(int level) {
        std::cout << "Volume: " << level << "\n";
    }
}

int main() {
    Graphics::Color bg{255, 128, 0};
    Graphics::setBackground(bg);
    Audio::play("music.mp3");
    Audio::setVolume(80);
    return 0;
}
```

## Reopening a Namespace
```cpp
// file1.cpp
namespace Utils {
    int add(int a, int b) { return a + b; }
}

// file2.cpp — same namespace, adds more
namespace Utils {
    int multiply(int a, int b) { return a * b; }
}

// Both functions are in Utils namespace
```

## Namespace Aliases
```cpp
#include <iostream>

namespace VeryLongNamespaceName {
    void hello() { std::cout << "Hello!\n"; }
}

// Create a short alias
namespace VLN = VeryLongNamespaceName;

int main() {
    VLN::hello();   // Much shorter!
    return 0;
}
```

## Key Takeaways
1. `namespace Name { ... }` groups related code
2. Access with `Name::member`
3. Namespaces can be reopened across multiple files
4. Use `namespace Alias = LongName;` for shorter access
5. Organize code by module/feature into separate namespaces

## Common Mistakes
- Defining everything in the global namespace → name collisions
- Creating too many or too few namespaces → poor organization
- Forgetting that namespaces don't end with semicolons after `}`
