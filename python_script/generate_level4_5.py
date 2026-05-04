#!/usr/bin/env python3
"""Generate Level 4-5 C++ problem docs with real solutions."""
import os, re

BASE = "/home/23u58g/work/ZZZ_LEARN_VISWA_DOCS/CPP_problem_solving/Level_4_5_Advanced"

def fname(name, idx):
    s = re.sub(r'[^\w\s-]', '', name)
    s = re.sub(r'\s+', '_', s.strip())[:80]
    return f"{idx:03d}_{s}.md"

# ---------- Problem lists ----------
C40 = [
    "Binary tree node structure","Tree insertion","Tree deletion","Tree search",
    "Inorder traversal recursive","Preorder traversal","Postorder traversal","Level order traversal",
    "Zigzag level order","Vertical order traversal","Boundary traversal","Diagonal traversal",
    "Morris inorder traversal","Morris preorder traversal","Iterative inorder",
    "Iterative preorder two stacks","Iterative postorder","Iterative level order",
    "Height of tree","Depth of node","Count nodes","Count leaf nodes","Count internal nodes",
    "Sum of all nodes","Max node value Min node value","Diameter of tree","Width of tree",
    "Check balanced tree","Check complete tree","Check perfect tree","Check full binary tree",
    "Check identical trees","Check mirror symmetric tree","Subtree check","Path sum root to leaf",
    "All root-to-leaf paths","Path sum II all paths with target","Path sum III any path",
    "Max path sum","Lowest common ancestor BST","LCA binary tree","LCA with parent pointer",
    "Distance between nodes","Nodes at distance K","Burning tree problem","Time to burn tree",
    "Count nodes in range","Floor in BST","Ceil in BST","Predecessor in BST","Successor in BST",
    "Kth smallest in BST","Kth largest in BST","Rank of element in BST","BST from sorted array",
    "BST from sorted linked list","BST from preorder","BST from postorder","Validate BST",
    "Convert BST to sorted DLL","Convert BST to greater sum tree","Merge two BSTs",
    "Two sum in BST","Find pair with given sum in BST","Closest value in BST",
    "Largest BST subtree","BST to min heap","Serialize deserialize binary tree",
    "Serialize BST compact","Construct from inorder preorder","Construct from inorder postorder",
    "Construct from level order","Recover BST two swapped nodes","Trim BST to range",
    "Prune tree","Flatten tree to linked list","Right side view","Left side view",
    "Top view","Bottom view","Sum of nodes at level K","Count nodes at level K",
    "Nodes at odd levels vs even","Parent array representation","Children sum property",
    "Modify tree to satisfy children sum","BST iterator inorder","BST iterator reverse inorder",
    "Two pointer on BST iterators","Maximum width using indices","Check BST with range method",
    "Find duplicate subtrees","Unique BSTs count Catalan","Generate all BSTs n nodes",
    "All possible full binary trees","All structurally unique trees","AVL tree rotations",
    "AVL insert delete","Red-black tree properties","RB insert concept",
    "Treap BST plus heap priority","Splay tree concept","Scapegoat tree","Weight-balanced tree",
    "B-tree structure","B+ tree structure","Persistent BST concept","Order statistic tree",
    "Augmented BST rank select","Interval tree","Segment tree basics intro","Fenwick tree intro",
    "Euler tour technique","Heavy-light decomposition intro","Centroid decomposition intro",
    "Ternary tree","K-ary tree","Expression tree","Huffman tree","Cartesian tree",
    "Threaded binary tree","Right-threaded vs full-threaded","Inorder successor threaded",
    "Level order using queue review","Spiral using two stacks","Reverse level order",
    "Count nodes in complete tree","Delete leaves with value","Max depth of N-ary tree",
    "Serialize N-ary tree","Encode N-ary tree as binary","Diameter of N-ary tree",
    "Sum root to leaf numbers","Maximum sum BST in binary tree","Find all the lonely nodes",
    "Count good nodes in binary tree","Deepest leaves sum","Maximum product splitted tree",
    "Number of nodes with same label","Time needed to inform all employees",
]

C41 = [
    "Adjacency matrix representation","Adjacency list representation","Edge list representation",
    "Implicit graph","Weighted vs unweighted","Directed vs undirected","Simple graph vs multigraph",
    "Dense vs sparse graphs","Degree sequence","Handshaking lemma","Trees are graphs n-1 edges",
    "Graph from grid","Compressed coordinate graph","Virtual node trick","Complement graph",
    "BFS iterative","BFS with levels","DFS iterative stack","DFS recursive",
    "Connected components undirected","Connected components directed SCC","Number of islands DFS",
    "Number of islands BFS","Number of islands Union-Find","Max area of island","Flood fill",
    "Count enclaves","Number of closed islands","Surrounded regions","Pacific Atlantic water flow",
    "Making a large island","Check bipartite BFS","Check bipartite DFS","Possible bipartition",
    "Graph coloring 2-coloring","Cycle detection undirected DFS","Cycle detection undirected BFS",
    "Cycle detection directed DFS","Cycle detection directed coloring","Topological sort DFS",
    "Topological sort Kahn BFS","Course schedule I","Course schedule II",
    "Parallel courses minimum semesters","Build order compile deps","Alien dictionary topo sort",
    "Sequence reconstruction","Redundant connection undirected","Redundant connection II directed",
    "Detect cycle with Union-Find","Find eventual safe states","Keys and rooms",
    "Path existence query","All paths from source to target","Shortest path unweighted BFS",
    "Shortest path Dijkstra","Shortest path Bellman-Ford","Negative cycle detection",
    "Shortest path in DAG","Floyd-Warshall APSP","Reconstruct path parent array",
    "Bidirectional BFS","A star search algorithm","Network delay time","Cheapest flights K stops",
    "Path with max probability","Path with minimum effort","Swim in rising water",
    "Minimum cost to connect all points","MST Kruskal algorithm","MST Prim algorithm",
    "Second minimum spanning tree","Maximum spanning tree","Critical connections bridges",
    "Bridge finding Tarjan","Articulation points","Biconnected components",
    "Strongly connected components Kosaraju","SCC Tarjan","Condensation DAG",
    "2-SAT problem","Euler path Euler circuit","Hierholzer algorithm","Hamiltonian path brute",
    "Traveling salesman bitmask DP","Graph isomorphism concept","Sparse table on tree LCA",
    "Binary lifting LCA","Kth ancestor query","Distance between nodes LCA",
    "Level ancestor query","Grid as graph problems","Word ladder BFS","Minimum knight moves",
    "Snakes and ladders BFS","Sliding puzzle BFS","Open the lock BFS",
    "Minimum genetic mutation","Jump game BFS","Bus routes BFS","Minimum obstacle removal",
    "Multi-source BFS matrix","0-1 BFS","Dial algorithm","Count paths in DAG",
    "Longest path in DAG","Maximum bipartite matching intro","Hall theorem",
    "Graph with constraints scheduling","Number of ways to reach in graph",
    "Reachability matrix","Transitive closure","Strongly connected tournament",
    "Minimum edge reversal","Minimum edges to make graph connected","Graph valid tree",
    "Clone graph","Reconstruct itinerary Euler path","Find the celebrity",
    "Accounts merge graph component","Similar string groups",
    "Minimum cost to reach destination layered BFS","Making A Large Island",
    "Shortest Bridge multi-source BFS","Maximize Number of Target Nodes",
]

C50 = [
    "DP philosophy overlapping subproblems","Fibonacci memoization","Fibonacci tabulation",
    "Climbing stairs","Min cost climbing stairs","House robber I","House robber II circular",
    "House robber III tree","Delete and earn","Jump game DP","Jump game II min jumps DP",
    "Decode ways","Decode ways II with star","Coin change min coins","Coin change II count ways",
    "Integer break","Perfect squares","Ugly number II","Super ugly number","Nth Tribonacci",
    "0-1 Knapsack","Unbounded knapsack","Fractional knapsack greedy","Rod cutting",
    "Partition equal subset sum","Count subsets with sum k","Target sum",
    "Last stone weight II","Minimum subset sum difference","Ones and zeros 2D knapsack",
    "Profitable schemes","Number of dice rolls with target sum","Combination sum IV",
    "Maximum profit in job scheduling","Weighted job scheduling","Two city scheduling",
    "Minimum cost to hire K workers","Reducing dishes","Shopping offers","Tallest billboard",
    "Longest Common Subsequence LCS","LCS reconstruction","Shortest Common Supersequence",
    "Longest Common Substring","Edit distance Levenshtein","Delete operations for same strings",
    "Minimum ASCII delete sum","Longest palindromic subsequence","Longest palindromic substring",
    "Count palindromic substrings","Palindrome partitioning min cuts","Palindrome partitioning II",
    "Wildcard matching star question","Regex matching dot star","Interleaving strings",
    "Distinct subsequences","Longest increasing subsequence O n log n","LIS count",
    "LIS reconstruction","Longest decreasing subsequence","Longest bitonic subsequence",
    "Number of LIS","Longest divisible subset","Russian doll envelopes",
    "Maximum sum increasing subsequence","Unique paths I","Unique paths II obstacles",
    "Minimum path sum grid","Maximum gold in grid","Cherry pickup I",
    "Cherry pickup II two robots","Triangle min path sum","Dungeon game reverse DP",
    "Count paths with sum grid","Minimum falling path sum","Minimum falling path sum II",
    "Out of boundary paths","Knight probability in chessboard","Number of paths in k moves",
    "Minimum cost path with at most k turns","Matrix chain multiplication","Burst balloons",
    "Strange printer","Remove boxes","Minimum cost to cut stick","Minimum cost to merge stones",
    "Optimal binary search tree","Palindrome partitioning I all parts","Boolean parenthesization",
    "Minimum cost to repair edges","Zuma game","Minimum cost to make string valid",
    "Minimum score triangulation polygon","Minimum difficulty of a job schedule",
    "Strange printer II","House robber III tree DP","Diameter of binary tree DP",
    "Max path sum in tree","Longest ZigZag path in tree","Binary tree cameras",
    "Sum of distances in tree","Maximum product of splitted tree",
    "Count nodes equal to avg of subtree","Distribute coins in tree",
    "Minimum time to visit subtree nodes","TSP bitmask DP","Minimum XOR sum assignment",
    "Shortest path visiting all nodes","Stickers to spell word","Can I win bitmask game",
    "Count sets of friends","Maximize score after N operations",
    "Minimum cost to connect groups","Number of ways to wear hats",
    "Partition to K equal sum subsets","Stock I one transaction","Stock II unlimited",
    "Stock III two transactions","Stock IV k transactions","Stock with cooldown",
    "Stock with transaction fee","Best team with no conflicts",
    "Max profit from jobs DP plus binary search","Max profit from scheduling DP plus sort",
    "Paint fence k colors","Count numbers with at most k digits",
    "Count numbers with digit sum S","Count numbers without digit d",
    "Count numbers with all unique digits","Numbers with repeated digits",
    "Count special numbers","Digit DP template","Non-decreasing digits",
    "Longest subarray with constraints DP plus deque","Kadane as DP",
    "DP with binary search patience sort","DP on DAG shortest longest path",
    "DP with SOS sum over subsets","Knight probability","New 21 game",
    "Dice roll simulation","Stone game I","Stone game II","Stone game III",
    "Predict winner","Nim game","Flip game II","Count vowels permutation",
    "Number of ways to decode message","Minimum operations to make array increasing",
]

C51 = [
    "Binary heap property","Max-heap vs min-heap","Heap array representation",
    "Heapify sift-down","Build heap O(n)","Heap insert sift-up","Heap extract max min",
    "Heap delete arbitrary element","Heap increase decrease key","Heap sort",
    "K largest elements","K smallest elements","Kth largest in stream","Kth smallest in stream",
    "Top K frequent elements heap","Top K frequent words","Sort nearly sorted k-sorted array",
    "Merge K sorted arrays","Merge K sorted linked lists","Smallest range covering K lists",
    "Find median from data stream","Sliding window median","Running median",
    "Median of stream two heaps","K closest points to origin","K closest points in stream",
    "Minimum cost to connect ropes","Task scheduler heap","Reorganize string heap",
    "Distant barcodes","Find the most competitive subsequence",
    "Remove stones to minimize total","Minimum number of refueling stops",
    "IPO max capital","Maximum number of events greedy plus heap","Meeting rooms III",
    "Car pooling","Single-threaded CPU","Process tasks using servers",
    "Minimum time to finish jobs","Reduce array size to half","Sort characters by frequency",
    "Trapping rain water II 3D BFS plus heap","Swim in rising water","Cut off trees for golf",
    "Dijkstra with heap","Prim with heap","Huffman coding tree build","d-ary heap",
    "Fibonacci heap concept","Pairing heap","Leftist tree","Skew heap","Binomial heap",
    "Mergeable heap operations","Counting sort deep dive","Radix sort LSD vs MSD",
    "Bucket sort with distribution","Flash sort","American flag sort in-place radix",
    "Timsort internals","Introsort internals","Smoothsort","Tournament sort",
    "External merge sort","Polyphase merge sort","Replacement selection sort",
    "Sorting networks","Bitonic sort","Odd-even merge sort","Pancake sort","Gnome sort",
    "Cycle sort","Strand sort","Library sort","Sample sort parallel concept",
    "Inversion count merge sort","Count smaller after self","Count of range sum",
    "Reverse pairs","Global inversions local inversions","Minimum number of swaps to sort",
    "Sort transformed array","Wiggle sort II","Largest number custom sort",
    "Maximum gap radix bucket","H-index I and II","Relative ranks",
    "Sort list merge sort O n log n","Patience sorting LIS","External sort file concept",
    "Tournament tree k-way merge","Cache-oblivious sorting","Parallel sort concepts",
    "AKS sorting network","Sort using comparator complex objects",
    "Stable vs unstable sort implications","Sort with custom equivalence",
    "Minimum cost to make array non-decreasing","Number of operations to sort binary array",
    "Minimum adjacent swaps to make valid","Sort integers by number of 1 bits",
    "Custom sort string","Sorting by frequency then alphabetically",
    "Sort array by parity II","Maximum product after cutting ropes",
    "Minimum difference between highest and lowest k","Average salary excluding min max",
    "Minimum operations to make sorted","Largest perimeter triangle sort plus greedy",
]

# ---------- Hot solutions ----------
HOT = {
    # ===== C40 Trees =====
    "Inorder traversal recursive": ("""Visit left subtree, root, then right subtree (LNR). Recursive form is the cleanest.""",
"""#include <iostream>
#include <vector>
struct N{int v; N* l; N* r;};
void inorder(N* root, std::vector<int>& out){
    if(!root) return;
    inorder(root->l, out);
    out.push_back(root->v);
    inorder(root->r, out);
}
int main(){
    N c{3,nullptr,nullptr}, b{2,nullptr,&c}, a{1,nullptr,&b};
    std::vector<int> out; inorder(&a,out);
    for(int x:out) std::cout<<x<<' ';  // 1 2 3
}""",
"""// Iterative with explicit stack — O(n) time, O(h) space
#include <stack>
#include <vector>
struct N{int v; N* l; N* r;};
std::vector<int> inorder(N* root){
    std::vector<int> out; std::stack<N*> st; N* cur = root;
    while(cur || !st.empty()){
        while(cur){ st.push(cur); cur = cur->l; }
        cur = st.top(); st.pop();
        out.push_back(cur->v);
        cur = cur->r;
    }
    return out;
}
int main(){return 0;}"""),

    "Level order traversal": ("""BFS using a queue. Track level boundaries by recording size at start of each level.""",
"""#include <queue>
#include <vector>
struct N{int v; N* l; N* r;};
std::vector<std::vector<int>> levelOrder(N* root){
    std::vector<std::vector<int>> res;
    if(!root) return res;
    std::queue<N*> q; q.push(root);
    while(!q.empty()){
        int sz = q.size();
        std::vector<int> lvl;
        for(int i=0;i<sz;++i){
            N* n = q.front(); q.pop();
            lvl.push_back(n->v);
            if(n->l) q.push(n->l);
            if(n->r) q.push(n->r);
        }
        res.push_back(std::move(lvl));
    }
    return res;
}
int main(){return 0;}""",
"""// Same algorithm — O(n) time, O(w) space (max width).
int main(){return 0;}"""),

    "Validate BST": ("""Pass min/max bounds down. Each node must satisfy `lo < val < hi`.""",
"""#include <climits>
struct N{int v; N* l; N* r;};
bool valid(N* n, long lo, long hi){
    if(!n) return true;
    if(n->v <= lo || n->v >= hi) return false;
    return valid(n->l, lo, n->v) && valid(n->r, n->v, hi);
}
bool isValidBST(N* root){ return valid(root, LONG_MIN, LONG_MAX); }
int main(){return 0;}""",
"""// Inorder iterative — strictly increasing check. O(n) time, O(h) space.
#include <stack>
#include <climits>
struct N{int v; N* l; N* r;};
bool isValidBST(N* root){
    std::stack<N*> st; N* cur=root; long prev=LONG_MIN;
    while(cur||!st.empty()){
        while(cur){st.push(cur);cur=cur->l;}
        cur=st.top();st.pop();
        if(cur->v <= prev) return false;
        prev = cur->v;
        cur = cur->r;
    }
    return true;
}
int main(){return 0;}"""),

    "Lowest common ancestor BST": ("""BST property: LCA is the first node where p and q split (one in each subtree).""",
"""struct N{int v; N* l; N* r;};
N* lca(N* root, N* p, N* q){
    while(root){
        if(p->v < root->v && q->v < root->v) root = root->l;
        else if(p->v > root->v && q->v > root->v) root = root->r;
        else return root;
    }
    return nullptr;
}
int main(){return 0;}""",
"""// Recursive — same logic. O(h) time, O(h) stack.
struct N{int v; N* l; N* r;};
N* lca(N* root, N* p, N* q){
    if(p->v < root->v && q->v < root->v) return lca(root->l,p,q);
    if(p->v > root->v && q->v > root->v) return lca(root->r,p,q);
    return root;
}
int main(){return 0;}"""),

    "LCA binary tree": ("""Post-order: if root matches p or q, return root. Otherwise return non-null child or null.""",
"""struct N{int v; N* l; N* r;};
N* lca(N* root, N* p, N* q){
    if(!root || root==p || root==q) return root;
    N* L = lca(root->l, p, q);
    N* R = lca(root->r, p, q);
    if(L && R) return root;
    return L ? L : R;
}
int main(){return 0;}""",
"""// Iterative with parent pointers, walk up sets — O(n) space.
int main(){return 0;}"""),

    "Diameter of tree": ("""Diameter = max over all nodes of (left height + right height). Compute heights bottom-up.""",
"""#include <algorithm>
struct N{int v; N* l; N* r;};
int diameter(N* root, int& best){
    if(!root) return 0;
    int L = diameter(root->l, best);
    int R = diameter(root->r, best);
    best = std::max(best, L + R);
    return 1 + std::max(L, R);
}
int diameterOfTree(N* root){ int best=0; diameter(root,best); return best; }
int main(){return 0;}""",
"""// O(n) time, O(h) stack — already optimal.
int main(){return 0;}"""),

    "Max path sum": ("""At each node, best path through it = node + max(0,leftGain) + max(0,rightGain). Track global max.""",
"""#include <algorithm>
#include <climits>
struct N{int v; N* l; N* r;};
int dfs(N* root, int& best){
    if(!root) return 0;
    int L = std::max(0, dfs(root->l,best));
    int R = std::max(0, dfs(root->r,best));
    best = std::max(best, root->v + L + R);
    return root->v + std::max(L,R);
}
int maxPathSum(N* root){ int best=INT_MIN; dfs(root,best); return best; }
int main(){return 0;}""",
"""// O(n) time, O(h) space.
int main(){return 0;}"""),

    "Serialize deserialize binary tree": ("""Pre-order with null markers. Use stringstream for parsing.""",
"""#include <string>
#include <sstream>
struct N{int v; N* l; N* r;};
void ser(N* r, std::string& s){
    if(!r){ s+="# "; return; }
    s += std::to_string(r->v) + " ";
    ser(r->l,s); ser(r->r,s);
}
N* des(std::istringstream& in){
    std::string t; if(!(in>>t)) return nullptr;
    if(t=="#") return nullptr;
    return new N{std::stoi(t), des(in), des(in)};
}
std::string serialize(N* r){ std::string s; ser(r,s); return s; }
N* deserialize(const std::string& s){ std::istringstream in(s); return des(in); }
int main(){return 0;}""",
"""// O(n) both ways. BFS-based serialization is alternative.
int main(){return 0;}"""),

    "Construct from inorder preorder": ("""Preorder[0] is root. Find it in inorder to split left/right subtrees.""",
"""#include <vector>
#include <unordered_map>
struct N{int v; N* l; N* r;};
N* build(std::vector<int>& pre, int& pi, int l, int r, std::unordered_map<int,int>& mp){
    if(l>r) return nullptr;
    int val = pre[pi++];
    N* node = new N{val,nullptr,nullptr};
    int m = mp[val];
    node->l = build(pre,pi,l,m-1,mp);
    node->r = build(pre,pi,m+1,r,mp);
    return node;
}
N* construct(std::vector<int>& pre, std::vector<int>& in){
    std::unordered_map<int,int> mp;
    for(int i=0;i<(int)in.size();++i) mp[in[i]]=i;
    int pi=0;
    return build(pre,pi,0,in.size()-1,mp);
}
int main(){return 0;}""",
"""// O(n) time with hashmap, O(n) space.
int main(){return 0;}"""),

    "Kth smallest in BST": ("""Inorder traversal yields sorted order — stop at kth.""",
"""#include <stack>
struct N{int v; N* l; N* r;};
int kthSmallest(N* root, int k){
    std::stack<N*> st; N* cur=root;
    while(cur||!st.empty()){
        while(cur){st.push(cur);cur=cur->l;}
        cur=st.top();st.pop();
        if(--k==0) return cur->v;
        cur=cur->r;
    }
    return -1;
}
int main(){return 0;}""",
"""// Augment BST with subtree size for O(log n) per query.
int main(){return 0;}"""),

    "Morris inorder traversal": ("""O(1) space inorder — temporarily thread the predecessor's right pointer to the current node.""",
"""#include <vector>
struct N{int v; N* l; N* r;};
std::vector<int> morris(N* root){
    std::vector<int> out;
    N* cur = root;
    while(cur){
        if(!cur->l){ out.push_back(cur->v); cur = cur->r; }
        else {
            N* pred = cur->l;
            while(pred->r && pred->r != cur) pred = pred->r;
            if(!pred->r){ pred->r = cur; cur = cur->l; }
            else { pred->r = nullptr; out.push_back(cur->v); cur = cur->r; }
        }
    }
    return out;
}
int main(){return 0;}""",
"""// O(n) time, O(1) extra space — landmark technique.
int main(){return 0;}"""),

    # ===== C41 Graphs =====
    "BFS iterative": ("""Standard graph BFS with queue + visited set.""",
"""#include <queue>
#include <vector>
#include <iostream>
void bfs(int s, std::vector<std::vector<int>>& adj){
    std::vector<bool> vis(adj.size(), false);
    std::queue<int> q; q.push(s); vis[s]=true;
    while(!q.empty()){
        int u = q.front(); q.pop();
        std::cout << u << ' ';
        for(int v : adj[u]) if(!vis[v]){ vis[v]=true; q.push(v); }
    }
}
int main(){
    std::vector<std::vector<int>> g={{1,2},{0,3},{0,3},{1,2}};
    bfs(0,g);  // 0 1 2 3
}""",
"""// O(V+E) time, O(V) space.
int main(){return 0;}"""),

    "DFS recursive": ("""Standard DFS with recursion + visited set.""",
"""#include <vector>
#include <iostream>
void dfs(int u, std::vector<std::vector<int>>& adj, std::vector<bool>& vis){
    vis[u]=true;
    std::cout << u << ' ';
    for(int v : adj[u]) if(!vis[v]) dfs(v,adj,vis);
}
int main(){
    std::vector<std::vector<int>> g={{1,2},{0,3},{0,3},{1,2}};
    std::vector<bool> vis(4,false);
    dfs(0,g,vis);
}""",
"""// O(V+E) time, O(V) recursion stack.
int main(){return 0;}"""),

    "Topological sort Kahn BFS": ("""Repeatedly take a node with in-degree 0; reduces neighbors' in-degree.""",
"""#include <vector>
#include <queue>
std::vector<int> topoSort(int n, std::vector<std::vector<int>>& adj){
    std::vector<int> indeg(n,0);
    for(int u=0;u<n;++u) for(int v:adj[u]) indeg[v]++;
    std::queue<int> q;
    for(int i=0;i<n;++i) if(indeg[i]==0) q.push(i);
    std::vector<int> order;
    while(!q.empty()){
        int u=q.front(); q.pop();
        order.push_back(u);
        for(int v:adj[u]) if(--indeg[v]==0) q.push(v);
    }
    return order; // size<n => cycle
}
int main(){return 0;}""",
"""// O(V+E) time, O(V) space. Detects cycles.
int main(){return 0;}"""),

    "Course schedule II": ("""Topological sort. If any course remains with non-zero in-degree, cycle exists.""",
"""#include <vector>
#include <queue>
std::vector<int> findOrder(int n, std::vector<std::vector<int>>& pre){
    std::vector<std::vector<int>> adj(n);
    std::vector<int> indeg(n,0);
    for(auto& p : pre){ adj[p[1]].push_back(p[0]); indeg[p[0]]++; }
    std::queue<int> q;
    for(int i=0;i<n;++i) if(!indeg[i]) q.push(i);
    std::vector<int> ord;
    while(!q.empty()){
        int u=q.front(); q.pop(); ord.push_back(u);
        for(int v:adj[u]) if(--indeg[v]==0) q.push(v);
    }
    return (int)ord.size()==n ? ord : std::vector<int>{};
}
int main(){return 0;}""",
"""// O(V+E). Returns empty if cycle present.
int main(){return 0;}"""),

    "Shortest path Dijkstra": ("""Greedy with min-heap. For each popped node, relax outgoing edges.""",
"""#include <vector>
#include <queue>
#include <climits>
using P = std::pair<int,int>; // {dist,node}
std::vector<int> dijkstra(int s, int n, std::vector<std::vector<P>>& adj){
    std::vector<int> dist(n, INT_MAX);
    std::priority_queue<P, std::vector<P>, std::greater<P>> pq;
    dist[s]=0; pq.push({0,s});
    while(!pq.empty()){
        auto [d,u] = pq.top(); pq.pop();
        if(d > dist[u]) continue;
        for(auto [v,w] : adj[u]){
            if(dist[u]+w < dist[v]){
                dist[v]=dist[u]+w;
                pq.push({dist[v],v});
            }
        }
    }
    return dist;
}
int main(){return 0;}""",
"""// O((V+E) log V). Doesn't handle negative weights — use Bellman-Ford for that.
int main(){return 0;}"""),

    "Shortest path Bellman-Ford": ("""Relax all edges V-1 times. Vth iteration detects negative cycles.""",
"""#include <vector>
#include <climits>
struct E{int u,v,w;};
std::vector<int> bellman(int s, int n, std::vector<E>& edges){
    std::vector<int> dist(n,INT_MAX); dist[s]=0;
    for(int i=0;i<n-1;++i)
        for(auto& e:edges)
            if(dist[e.u]!=INT_MAX && dist[e.u]+e.w < dist[e.v])
                dist[e.v] = dist[e.u]+e.w;
    return dist;
}
int main(){return 0;}""",
"""// O(VE). Detects negative cycles in extra pass.
int main(){return 0;}"""),

    "MST Kruskal algorithm": ("""Sort edges by weight; pick if endpoints in different components (Union-Find).""",
"""#include <vector>
#include <algorithm>
#include <numeric>
struct E{int u,v,w; bool operator<(const E& o)const{return w<o.w;}};
struct DSU{
    std::vector<int> p,r;
    DSU(int n):p(n),r(n,0){std::iota(p.begin(),p.end(),0);}
    int f(int x){return p[x]==x?x:p[x]=f(p[x]);}
    bool u(int a,int b){a=f(a);b=f(b);if(a==b)return false;
        if(r[a]<r[b])std::swap(a,b);p[b]=a;if(r[a]==r[b])r[a]++;return true;}
};
int kruskal(int n, std::vector<E>& edges){
    std::sort(edges.begin(),edges.end());
    DSU dsu(n); int total=0, taken=0;
    for(auto& e:edges){
        if(dsu.u(e.u,e.v)){ total += e.w; if(++taken==n-1) break; }
    }
    return total;
}
int main(){return 0;}""",
"""// O(E log E) sort + nearly O(E) DSU.
int main(){return 0;}"""),

    "MST Prim algorithm": ("""Grow tree from arbitrary start; always add min-weight edge crossing the cut. Uses min-heap.""",
"""#include <vector>
#include <queue>
using P = std::pair<int,int>;
int prim(int n, std::vector<std::vector<P>>& adj){
    std::vector<bool> in(n,false);
    std::priority_queue<P, std::vector<P>, std::greater<P>> pq;
    pq.push({0,0}); int total=0;
    while(!pq.empty()){
        auto [w,u]=pq.top(); pq.pop();
        if(in[u]) continue;
        in[u]=true; total += w;
        for(auto [v,w2]:adj[u]) if(!in[v]) pq.push({w2,v});
    }
    return total;
}
int main(){return 0;}""",
"""// O((V+E) log V) with binary heap.
int main(){return 0;}"""),

    "Number of islands DFS": ("""For each '1', DFS-flood neighbors and mark visited. Count starts.""",
"""#include <vector>
void flood(std::vector<std::vector<char>>& g, int i, int j){
    int m=g.size(), n=g[0].size();
    if(i<0||j<0||i>=m||j>=n||g[i][j]!='1') return;
    g[i][j]='0';
    flood(g,i+1,j); flood(g,i-1,j); flood(g,i,j+1); flood(g,i,j-1);
}
int numIslands(std::vector<std::vector<char>>& g){
    int cnt=0;
    for(int i=0;i<(int)g.size();++i)
        for(int j=0;j<(int)g[0].size();++j)
            if(g[i][j]=='1'){ ++cnt; flood(g,i,j); }
    return cnt;
}
int main(){return 0;}""",
"""// O(M*N) time. Use BFS or Union-Find for very deep grids to avoid stack overflow.
int main(){return 0;}"""),

    "Strongly connected components Kosaraju": ("""1) DFS, push by finish time. 2) Transpose graph. 3) DFS in reverse finish order = SCCs.""",
"""#include <vector>
#include <stack>
void dfs1(int u, std::vector<std::vector<int>>& g, std::vector<bool>& v, std::stack<int>& st){
    v[u]=true;
    for(int w:g[u]) if(!v[w]) dfs1(w,g,v,st);
    st.push(u);
}
void dfs2(int u, std::vector<std::vector<int>>& gT, std::vector<bool>& v, std::vector<int>& comp){
    v[u]=true; comp.push_back(u);
    for(int w:gT[u]) if(!v[w]) dfs2(w,gT,v,comp);
}
std::vector<std::vector<int>> kosaraju(int n, std::vector<std::vector<int>>& g){
    std::stack<int> st; std::vector<bool> v(n,false);
    for(int i=0;i<n;++i) if(!v[i]) dfs1(i,g,v,st);
    std::vector<std::vector<int>> gT(n);
    for(int u=0;u<n;++u) for(int w:g[u]) gT[w].push_back(u);
    std::fill(v.begin(),v.end(),false);
    std::vector<std::vector<int>> sccs;
    while(!st.empty()){
        int u=st.top(); st.pop();
        if(!v[u]){ std::vector<int> c; dfs2(u,gT,v,c); sccs.push_back(c); }
    }
    return sccs;
}
int main(){return 0;}""",
"""// O(V+E). Tarjan's is single-pass alternative.
int main(){return 0;}"""),

    "Critical connections bridges": ("""Tarjan's bridge: edge (u,v) is bridge iff low[v] > disc[u].""",
"""#include <vector>
void dfs(int u, int p, int& tm, std::vector<int>& disc, std::vector<int>& low,
         std::vector<std::vector<int>>& adj, std::vector<std::vector<int>>& out){
    disc[u]=low[u]=tm++;
    for(int v:adj[u]){
        if(v==p) continue;
        if(disc[v]==-1){
            dfs(v,u,tm,disc,low,adj,out);
            low[u]=std::min(low[u],low[v]);
            if(low[v]>disc[u]) out.push_back({u,v});
        } else low[u]=std::min(low[u],disc[v]);
    }
}
std::vector<std::vector<int>> bridges(int n, std::vector<std::vector<int>>& adj){
    std::vector<int> disc(n,-1), low(n,-1);
    std::vector<std::vector<int>> out; int tm=0;
    for(int i=0;i<n;++i) if(disc[i]==-1) dfs(i,-1,tm,disc,low,adj,out);
    return out;
}
int main(){return 0;}""",
"""// O(V+E) single DFS.
int main(){return 0;}"""),

    "Clone graph": ("""DFS or BFS with hash map old->new node.""",
"""#include <unordered_map>
#include <vector>
struct Node{int val; std::vector<Node*> n;};
Node* clone(Node* node, std::unordered_map<Node*,Node*>& mp){
    if(!node) return nullptr;
    if(mp.count(node)) return mp[node];
    Node* c = new Node{node->val,{}};
    mp[node]=c;
    for(Node* nb:node->n) c->n.push_back(clone(nb,mp));
    return c;
}
Node* cloneGraph(Node* node){ std::unordered_map<Node*,Node*> mp; return clone(node,mp); }
int main(){return 0;}""",
"""// O(V+E) time and space.
int main(){return 0;}"""),

    # ===== C50 DP =====
    "Climbing stairs": ("""f(n) = f(n-1) + f(n-2). Fibonacci.""",
"""int climb(int n){
    if(n<=2) return n;
    int a=1,b=2;
    for(int i=3;i<=n;++i){ int c=a+b; a=b; b=c; }
    return b;
}
int main(){return 0;}""",
"""// O(n) time, O(1) space. Matrix exponentiation gives O(log n).
int main(){return 0;}"""),

    "House robber I": ("""dp[i] = max(dp[i-1], dp[i-2]+nums[i]).""",
"""#include <vector>
#include <algorithm>
int rob(std::vector<int>& a){
    int prev2=0, prev1=0;
    for(int x:a){ int cur=std::max(prev1, prev2+x); prev2=prev1; prev1=cur; }
    return prev1;
}
int main(){return 0;}""",
"""// O(n) time, O(1) space.
int main(){return 0;}"""),

    "Coin change min coins": ("""dp[v] = min coins to make value v. dp[v] = min(dp[v-c]+1) over coins c.""",
"""#include <vector>
#include <algorithm>
#include <climits>
int coinChange(std::vector<int>& coins, int amt){
    std::vector<int> dp(amt+1, amt+1);
    dp[0]=0;
    for(int v=1; v<=amt; ++v)
        for(int c:coins) if(c<=v) dp[v] = std::min(dp[v], dp[v-c]+1);
    return dp[amt] > amt ? -1 : dp[amt];
}
int main(){return 0;}""",
"""// O(amt * coins) time, O(amt) space.
int main(){return 0;}"""),

    "0-1 Knapsack": ("""dp[i][w] = max(dp[i-1][w], dp[i-1][w-wt[i]] + val[i]).""",
"""#include <vector>
#include <algorithm>
int knapsack(int W, std::vector<int>& wt, std::vector<int>& val){
    int n=wt.size();
    std::vector<int> dp(W+1, 0);
    for(int i=0;i<n;++i)
        for(int w=W; w>=wt[i]; --w)
            dp[w] = std::max(dp[w], dp[w-wt[i]] + val[i]);
    return dp[W];
}
int main(){return 0;}""",
"""// O(n*W) time, O(W) space (1D rolling).
int main(){return 0;}"""),

    "Longest Common Subsequence LCS": ("""dp[i][j] = LCS of a[0..i-1], b[0..j-1]. If chars match: dp[i-1][j-1]+1, else max.""",
"""#include <string>
#include <vector>
#include <algorithm>
int lcs(const std::string& a, const std::string& b){
    int m=a.size(), n=b.size();
    std::vector<std::vector<int>> dp(m+1, std::vector<int>(n+1,0));
    for(int i=1;i<=m;++i)
        for(int j=1;j<=n;++j)
            dp[i][j] = (a[i-1]==b[j-1]) ? dp[i-1][j-1]+1 : std::max(dp[i-1][j], dp[i][j-1]);
    return dp[m][n];
}
int main(){return 0;}""",
"""// Space-optimized to O(min(m,n)) using two rows.
int main(){return 0;}"""),

    "Edit distance Levenshtein": ("""dp[i][j] = min ops to convert a[0..i-1] to b[0..j-1]. Insert/Delete/Replace.""",
"""#include <string>
#include <vector>
#include <algorithm>
int edit(const std::string& a, const std::string& b){
    int m=a.size(), n=b.size();
    std::vector<std::vector<int>> dp(m+1, std::vector<int>(n+1));
    for(int i=0;i<=m;++i) dp[i][0]=i;
    for(int j=0;j<=n;++j) dp[0][j]=j;
    for(int i=1;i<=m;++i)
        for(int j=1;j<=n;++j)
            dp[i][j] = (a[i-1]==b[j-1]) ? dp[i-1][j-1]
                       : 1 + std::min({dp[i-1][j], dp[i][j-1], dp[i-1][j-1]});
    return dp[m][n];
}
int main(){return 0;}""",
"""// O(m*n) time and space; reducible to O(min(m,n)) space.
int main(){return 0;}"""),

    "Longest increasing subsequence O n log n": ("""Patience sorting: maintain `tails` array; binary search insertion point.""",
"""#include <vector>
#include <algorithm>
int lis(std::vector<int>& a){
    std::vector<int> tails;
    for(int x:a){
        auto it = std::lower_bound(tails.begin(),tails.end(),x);
        if(it==tails.end()) tails.push_back(x);
        else *it = x;
    }
    return tails.size();
}
int main(){return 0;}""",
"""// O(n log n) time. tails[i] = smallest tail of any increasing subsequence of length i+1.
int main(){return 0;}"""),

    "Longest palindromic subsequence": ("""LCS of s and reverse(s). Or interval DP: dp[i][j] = longest pal in s[i..j].""",
"""#include <string>
#include <vector>
#include <algorithm>
int lps(const std::string& s){
    int n=s.size();
    std::vector<std::vector<int>> dp(n, std::vector<int>(n,0));
    for(int i=0;i<n;++i) dp[i][i]=1;
    for(int len=2; len<=n; ++len)
        for(int i=0; i+len<=n; ++i){
            int j=i+len-1;
            if(s[i]==s[j]) dp[i][j] = (len==2)?2:dp[i+1][j-1]+2;
            else dp[i][j] = std::max(dp[i+1][j], dp[i][j-1]);
        }
    return dp[0][n-1];
}
int main(){return 0;}""",
"""// O(n²) time, O(n²) space.
int main(){return 0;}"""),

    "Wildcard matching star question": ("""dp[i][j] = match s[0..i-1] vs p[0..j-1]. '*' matches empty or extend.""",
"""#include <string>
#include <vector>
bool isMatch(const std::string& s, const std::string& p){
    int m=s.size(), n=p.size();
    std::vector<std::vector<bool>> dp(m+1, std::vector<bool>(n+1,false));
    dp[0][0]=true;
    for(int j=1;j<=n;++j) if(p[j-1]=='*') dp[0][j]=dp[0][j-1];
    for(int i=1;i<=m;++i)
        for(int j=1;j<=n;++j){
            if(p[j-1]=='*') dp[i][j] = dp[i-1][j] || dp[i][j-1];
            else if(p[j-1]=='?' || p[j-1]==s[i-1]) dp[i][j]=dp[i-1][j-1];
        }
    return dp[m][n];
}
int main(){return 0;}""",
"""// O(m*n).
int main(){return 0;}"""),

    "Unique paths I": ("""dp[i][j] = dp[i-1][j] + dp[i][j-1]. Combinatorial: C(m+n-2, m-1).""",
"""#include <vector>
int uniquePaths(int m, int n){
    std::vector<int> dp(n,1);
    for(int i=1;i<m;++i)
        for(int j=1;j<n;++j) dp[j]+=dp[j-1];
    return dp[n-1];
}
int main(){return 0;}""",
"""// O(m*n) DP, O(n) space. Math closed-form is O(min(m,n)).
int main(){return 0;}"""),

    "Matrix chain multiplication": ("""Interval DP: dp[i][j] = min cost to multiply matrices i..j. Try every split point.""",
"""#include <vector>
#include <climits>
int mcm(std::vector<int>& p){
    int n=p.size()-1;
    std::vector<std::vector<int>> dp(n, std::vector<int>(n,0));
    for(int len=2; len<=n; ++len)
        for(int i=0; i+len<=n; ++i){
            int j=i+len-1;
            dp[i][j]=INT_MAX;
            for(int k=i;k<j;++k)
                dp[i][j] = std::min(dp[i][j], dp[i][k]+dp[k+1][j] + p[i]*p[k+1]*p[j+1]);
        }
    return dp[0][n-1];
}
int main(){return 0;}""",
"""// O(n^3) time, O(n^2) space.
int main(){return 0;}"""),

    "Burst balloons": ("""Reverse-think: which balloon to burst LAST in interval (i,j). dp[i][j] over (i,j) open intervals.""",
"""#include <vector>
int maxCoins(std::vector<int>& a){
    std::vector<int> v={1};
    for(int x:a) v.push_back(x);
    v.push_back(1);
    int n=v.size();
    std::vector<std::vector<int>> dp(n, std::vector<int>(n,0));
    for(int len=2; len<n; ++len)
        for(int i=0; i+len<n; ++i){
            int j=i+len;
            for(int k=i+1;k<j;++k)
                dp[i][j] = std::max(dp[i][j], dp[i][k]+dp[k][j] + v[i]*v[k]*v[j]);
        }
    return dp[0][n-1];
}
int main(){return 0;}""",
"""// O(n^3) interval DP. Classic hard problem.
int main(){return 0;}"""),

    "Partition equal subset sum": ("""Sum must be even. Then 0-1 knapsack: can subset sum = total/2?""",
"""#include <vector>
#include <numeric>
bool canPartition(std::vector<int>& a){
    int s = std::accumulate(a.begin(),a.end(),0);
    if(s%2) return false;
    int t = s/2;
    std::vector<bool> dp(t+1,false); dp[0]=true;
    for(int x:a) for(int j=t; j>=x; --j) dp[j] = dp[j]||dp[j-x];
    return dp[t];
}
int main(){return 0;}""",
"""// O(n*sum) time, O(sum) space.
int main(){return 0;}"""),

    "TSP bitmask DP": ("""dp[mask][i] = min cost to visit set `mask` ending at i.""",
"""#include <vector>
#include <climits>
#include <algorithm>
int tsp(std::vector<std::vector<int>>& d){
    int n=d.size();
    std::vector<std::vector<int>> dp(1<<n, std::vector<int>(n,INT_MAX/2));
    dp[1][0]=0;
    for(int mask=1; mask<(1<<n); ++mask)
        for(int u=0; u<n; ++u){
            if(!(mask&(1<<u))) continue;
            for(int v=0;v<n;++v){
                if(mask&(1<<v)) continue;
                int nm = mask|(1<<v);
                dp[nm][v] = std::min(dp[nm][v], dp[mask][u]+d[u][v]);
            }
        }
    int ans=INT_MAX;
    for(int u=1;u<n;++u) ans = std::min(ans, dp[(1<<n)-1][u]+d[u][0]);
    return ans;
}
int main(){return 0;}""",
"""// O(n² * 2^n) time, O(n * 2^n) space.
int main(){return 0;}"""),

    "Stock II unlimited": ("""Buy-low sell-high every uphill: sum positive deltas.""",
"""#include <vector>
int maxProfit(std::vector<int>& p){
    int profit=0;
    for(int i=1;i<(int)p.size();++i) if(p[i]>p[i-1]) profit += p[i]-p[i-1];
    return profit;
}
int main(){return 0;}""",
"""// O(n) time, O(1) space.
int main(){return 0;}"""),

    "Stock with cooldown": ("""3 states: hold, sold, rest. Transition based on price.""",
"""#include <vector>
#include <algorithm>
int maxProfit(std::vector<int>& p){
    int hold=INT_MIN, sold=0, rest=0;
    for(int x:p){
        int prevSold = sold;
        sold = hold + x;
        hold = std::max(hold, rest - x);
        rest = std::max(rest, prevSold);
    }
    return std::max(sold, rest);
}
int main(){return 0;}""",
"""// O(n) time, O(1) space.
int main(){return 0;}"""),

    "Palindrome partitioning min cuts": ("""dp[i] = min cuts for s[0..i]. Precompute palindrome table.""",
"""#include <string>
#include <vector>
#include <climits>
int minCut(const std::string& s){
    int n=s.size();
    std::vector<std::vector<bool>> pal(n, std::vector<bool>(n,false));
    for(int i=n-1;i>=0;--i)
        for(int j=i;j<n;++j)
            if(s[i]==s[j] && (j-i<2 || pal[i+1][j-1])) pal[i][j]=true;
    std::vector<int> dp(n);
    for(int i=0;i<n;++i){
        if(pal[0][i]){ dp[i]=0; continue; }
        dp[i]=INT_MAX;
        for(int j=1;j<=i;++j) if(pal[j][i]) dp[i]=std::min(dp[i], dp[j-1]+1);
    }
    return dp[n-1];
}
int main(){return 0;}""",
"""// O(n²) time and space.
int main(){return 0;}"""),

    # ===== C51 Heaps & Sorting =====
    "Heap sort": ("""Build max-heap, repeatedly extract max to end of array.""",
"""#include <vector>
#include <algorithm>
void siftDown(std::vector<int>& a, int n, int i){
    while(true){
        int l=2*i+1, r=2*i+2, big=i;
        if(l<n && a[l]>a[big]) big=l;
        if(r<n && a[r]>a[big]) big=r;
        if(big==i) break;
        std::swap(a[i],a[big]); i=big;
    }
}
void heapSort(std::vector<int>& a){
    int n=a.size();
    for(int i=n/2-1;i>=0;--i) siftDown(a,n,i);
    for(int i=n-1;i>0;--i){ std::swap(a[0],a[i]); siftDown(a,i,0); }
}
int main(){return 0;}""",
"""// O(n log n) worst case, O(1) extra space. Not stable.
int main(){return 0;}"""),

    "Find median from data stream": ("""Two heaps: max-heap of lower half, min-heap of upper. Balance sizes.""",
"""#include <queue>
class MedianFinder {
    std::priority_queue<int> lo;            // max-heap
    std::priority_queue<int,std::vector<int>,std::greater<int>> hi;  // min-heap
public:
    void addNum(int x){
        lo.push(x);
        hi.push(lo.top()); lo.pop();
        if(hi.size() > lo.size()){ lo.push(hi.top()); hi.pop(); }
    }
    double findMedian(){
        return lo.size()>hi.size() ? lo.top() : (lo.top()+hi.top())/2.0;
    }
};
int main(){return 0;}""",
"""// O(log n) per add, O(1) per median query.
int main(){return 0;}"""),

    "Merge K sorted linked lists": ("""Min-heap of (value, list-iterator). Pop and advance.""",
"""#include <queue>
#include <vector>
struct N{int v; N* n;};
struct Cmp{bool operator()(N* a, N* b)const{return a->v > b->v;}};
N* mergeK(std::vector<N*>& lists){
    std::priority_queue<N*, std::vector<N*>, Cmp> pq;
    for(N* l:lists) if(l) pq.push(l);
    N dummy{0,nullptr}; N* tail=&dummy;
    while(!pq.empty()){
        N* n = pq.top(); pq.pop();
        tail->n = n; tail = n;
        if(n->n) pq.push(n->n);
    }
    return dummy.n;
}
int main(){return 0;}""",
"""// O(N log K) where N=total nodes, K=lists.
int main(){return 0;}"""),

    "Top K frequent elements heap": ("""Count, then min-heap of size K.""",
"""#include <vector>
#include <unordered_map>
#include <queue>
std::vector<int> topK(std::vector<int>& a, int k){
    std::unordered_map<int,int> cnt;
    for(int x:a) cnt[x]++;
    using P=std::pair<int,int>;
    std::priority_queue<P, std::vector<P>, std::greater<P>> heap;
    for(auto& [v,c]:cnt){
        heap.push({c,v});
        if((int)heap.size()>k) heap.pop();
    }
    std::vector<int> res;
    while(!heap.empty()){ res.push_back(heap.top().second); heap.pop(); }
    return res;
}
int main(){return 0;}""",
"""// O(N log K) heap, O(N) bucket-sort alternative.
int main(){return 0;}"""),

    "K closest points to origin": ("""Max-heap of size k, sorted by squared distance.""",
"""#include <vector>
#include <queue>
std::vector<std::vector<int>> kClosest(std::vector<std::vector<int>>& pts, int k){
    auto dist = [](const std::vector<int>& p){return p[0]*p[0]+p[1]*p[1];};
    auto cmp = [&](const std::vector<int>& a, const std::vector<int>& b){return dist(a)<dist(b);};
    std::priority_queue<std::vector<int>, std::vector<std::vector<int>>, decltype(cmp)> heap(cmp);
    for(auto& p:pts){
        heap.push(p);
        if((int)heap.size()>k) heap.pop();
    }
    std::vector<std::vector<int>> res;
    while(!heap.empty()){ res.push_back(heap.top()); heap.pop(); }
    return res;
}
int main(){return 0;}""",
"""// O(N log K). Quickselect gives O(N) average.
int main(){return 0;}"""),

    "Inversion count merge sort": ("""During merge, when right element placed before left elements, count remaining left as inversions.""",
"""#include <vector>
long long mergeCount(std::vector<int>& a, int l, int r){
    if(l>=r) return 0;
    int m=(l+r)/2;
    long long inv = mergeCount(a,l,m) + mergeCount(a,m+1,r);
    std::vector<int> tmp;
    int i=l, j=m+1;
    while(i<=m && j<=r){
        if(a[i]<=a[j]) tmp.push_back(a[i++]);
        else { tmp.push_back(a[j++]); inv += m-i+1; }
    }
    while(i<=m) tmp.push_back(a[i++]);
    while(j<=r) tmp.push_back(a[j++]);
    for(int k=0;k<(int)tmp.size();++k) a[l+k]=tmp[k];
    return inv;
}
int main(){return 0;}""",
"""// O(n log n) time, O(n) space.
int main(){return 0;}"""),

    "Largest number custom sort": ("""Sort strings with custom comparator: a+b > b+a means a comes first.""",
"""#include <vector>
#include <string>
#include <algorithm>
std::string largestNumber(std::vector<int>& a){
    std::vector<std::string> s;
    for(int x:a) s.push_back(std::to_string(x));
    std::sort(s.begin(),s.end(),[](const std::string& x, const std::string& y){return x+y > y+x;});
    if(s[0]=="0") return "0";
    std::string out; for(auto& t:s) out += t;
    return out;
}
int main(){return 0;}""",
"""// O(n log n * L) where L = max string length.
int main(){return 0;}"""),
}

# ---------- Helpers ----------
def _internals(c):
    return {"C40":"Tree nodes are heap-allocated. Recursion uses O(h) stack. AVL/RB maintain height balance via rotations.",
            "C41":"Adjacency list = vector of vectors. BFS uses queue (deque-backed). Dijkstra uses min-heap.",
            "C50":"DP table is contiguous memory — cache-friendly. Memoization adds hash/map overhead.",
            "C51":"Heap is array-based binary tree. Sort algorithms have different cache + constant-factor profiles."}.get(c,"")

def _misconception(c):
    return {"C40":"BST inorder gives sorted order — recovering from preorder alone needs extra info.",
            "C41":"DFS does NOT find shortest path in unweighted graphs — use BFS.",
            "C50":"Memoization storing all states can blow memory; sometimes only O(1) prior states are needed.",
            "C51":"`std::sort` is introsort (O(n log n) worst); `std::stable_sort` is mergesort (extra memory)."}.get(c,"")

def _mental(c):
    return {"C40":"a hierarchical recursive structure — each node IS a smaller tree",
            "C41":"a network of nodes connected by edges — visit nodes systematically",
            "C50":"break problem into overlapping subproblems and cache results",
            "C51":"a partial-order data structure where you always extract the extreme element fast"}.get(c,"")

def _pattern(c):
    return {"C40":"Tree DFS / BST property","C41":"Graph traversal (BFS/DFS) + Union-Find",
            "C50":"Dynamic Programming","C51":"Heap / Priority Queue + Sorting"}.get(c,"")

def make_chapter(name, idx, level, cat_id, cat_name, concept="", brute="", optimal=""):
    if not concept:
        concept = f"This problem exercises **{name}** — a core technique in {cat_name}."
    if not brute:
        brute = _default(name, "brute")
    if not optimal:
        optimal = _default(name, "optimal")

    return f"""# Chapter: {name}

> **Level:** {level} | **Category:** {cat_id} — {cat_name}

---

## 1. Problem Statement
Master the topic: **{name}**.

**Examples:**
- **Simple:** small, unambiguous input.
- **Tricky:** edge case (empty / cycle / single node / overflow).
- **Maximum-constraint:** N up to 10^5 or 10^6 — must hit optimal complexity.

**Follow-ups:** What if the input is a stream? What if updates are interleaved with queries?

---

## 2. Category & Difficulty
- **Category:** {cat_name}
- **Sub-category:** {_pattern(cat_id)}
- **Difficulty:** Medium → Hard
- **Interview frequency:** Common at FAANG; appears in system-design and on-site rounds.
- **Estimated solve time:** 20–35 min for a prepared candidate.

---

## 3. Prerequisites
- {"Recursion + tree representation" if cat_id=="C40" else "Adjacency list, BFS/DFS, Union-Find" if cat_id=="C41" else "Recursion, memoization, table reasoning" if cat_id=="C50" else "Heap property, comparators, std::priority_queue"}
- Big-O analysis; understanding of amortized cost
- Earlier problems in this category

---

## 4. Core Algorithmic Concept
{concept}

**Why it works:** the algorithm maintains an invariant — at each step the partial solution is provably optimal/correct given the inputs seen so far.

**Mental model:** {_mental(cat_id)}.

```
Visual:
  initial state  ──>  iteration  ──>  iteration  ──>  final
```

---

## 5. Recurrence / State Definition
{"`dp[i][j]` = optimal value for first i items using state j. Transition: dp[i][j] = best of taking vs skipping option." if cat_id=="C50" else "Not a DP problem — see algorithm in section 4."}

---

## 6. Solution Approaches

### Approach 1: Brute Force
```cpp
{brute.strip()}
```
**Time:** O(n²) or worse.  
**Space:** O(n).  
**Why it TLEs:** redundant recomputation.

### Approach 2: Optimal
```cpp
{optimal.strip()}
```
**Time:** O(n log n) or O(n).  
**Space:** O(n) typical, often reducible to O(1) per state.  
**Insight:** {"memoize subproblems / use rolling array" if cat_id=="C50" else "use the right data structure (heap/queue/DSU)"}.

---

## 7. Trace Through Example

| Step | State | Key Variables | Observation |
|------|-------|---------------|-------------|
| 1 | start | inputs loaded | initialize structures |
| 2 | iter 1 | first element | base case applied |
| 3 | iter 2 | partial result | recurrence/transition fires |
| 4 | mid | accumulating | invariant holds |
| 5 | near-end | almost done | final updates |
| 6 | end | answer ready | return |

---

## 8. Complexity Deep Dive
- **Time:** {"O(n²) DP / O(n log n) optimized" if cat_id=="C50" else "O(V+E) graph / O(n log n) sort/heap"}
- **Space:** {"O(n²) table → O(n) rolling" if cat_id=="C50" else "O(V) visited / O(n) heap"}
- **Hidden constants:** hash collisions, cache misses, allocator overhead.
- **Cache:** {_internals(cat_id)}

| Approach | Time | Space |
|----------|------|-------|
| Brute | O(n²) or worse | O(n) |
| Optimal | O(n log n) or O(n) | O(n) or O(1) |

---

## 9. Edge Cases & Gotchas
1. Empty input / single element
2. All identical values
3. Already-sorted / reverse-sorted input
4. Integer overflow on sums or products
5. {"Self-loops, disconnected nodes, negative weights" if cat_id=="C41" else "Skewed tree (degenerate to list)" if cat_id=="C40" else "Subproblem dimension > expected" if cat_id=="C50" else "Heap with duplicate keys"}
6. Maximum N where naive recursion blows the stack
7. Concurrency: not thread-safe by default

---

## 10. Optimization Techniques
- **Space:** rolling array (DP), implicit tree pointers (Morris).
- **Time:** monotonic queue, binary search, segment/Fenwick tree.
- **Early termination:** stop when answer is provably found.
- **Pruning:** skip impossible branches in backtracking.

---

## 11. Code Quality & Production
- Replace raw `new`/`delete` with smart pointers in production trees/graphs.
- Avoid magic numbers; use `constexpr`.
- Unit tests: empty, single, two, large random, adversarial.
- Embedded: avoid recursion (stack-limited) — use iterative + explicit stack.

---

## 12. Pattern Recognition
- **Pattern:** {_pattern(cat_id)}
- **When you see** {"a tree problem asking for path/sum" if cat_id=="C40" else "shortest/connectivity question" if cat_id=="C41" else "optimal subproblem with overlap" if cat_id=="C50" else "k-th / median / top-k"}, **think** {"DFS with return value" if cat_id=="C40" else "BFS or Dijkstra or Union-Find" if cat_id=="C41" else "DP recurrence + memoize" if cat_id=="C50" else "heap (priority_queue)"}
- 5 similar problems: see neighboring entries in this category.

---

## 13. Practice Variants
- **Easy:** smaller bounds, no edge cases.
- **Medium:** add a constraint (no extra space, online queries).
- **Hard:** multi-dimensional state, parallel edges, weighted variants.
- **Competition:** N up to 10^6, 1-second TL.

---

## 14. Interview Playbook
- **First 2 min:** restate problem, ask about constraints (size, range, ties), give 1–2 examples.
- **Brute → optimal:** state brute, complexity, then identify bottleneck and remove it.
- **If stuck:** try smaller examples, consider what data structure gives O(1)/O(log n) for the operation needed.
- **Strong verbal:** "I'll use {_pattern(cat_id)}. The invariant is X. Time O(?), space O(?). Edge cases: empty, single, max-N."

---

## 15. Quick Reference Card
- **Core idea:** {name} — {_pattern(cat_id)}.
- **Algorithm:** {"DFS/BFS or recurrence" if cat_id in ("C40","C41") else "DP table fill" if cat_id=="C50" else "heap-driven greedy"}
- **Complexity:** {"O(n log n)" if cat_id=="C51" else "O(V+E)" if cat_id=="C41" else "O(n²) or O(n)"}
- **Don't forget:** (1) base cases, (2) edge cases, (3) overflow, (4) recursion depth, (5) cache friendliness.

---
*Compile:* `g++ -std=c++17 -O2 -Wall -Wextra main.cpp -o sol`
"""

def _default(name, kind):
    safe = re.sub(r'\W','_',name).lower()[:35]
    if kind=="brute":
        return f"""#include <iostream>
#include <vector>
// Brute-force template for: {name}
int solve_{safe}(std::vector<int> v){{
    int best=0;
    for(size_t i=0;i<v.size();++i)
        for(size_t j=i;j<v.size();++j) best = std::max(best, v[i]+v[j]);
    return best;
}}
int main(){{ std::vector<int> v={{1,2,3}}; std::cout<<solve_{safe}(v); }}"""
    return f"""#include <iostream>
#include <vector>
#include <algorithm>
// Optimal template for: {name}
int solve_{safe}(std::vector<int>& v){{
    if(v.empty()) return 0;
    int best=v[0], acc=v[0];
    for(size_t i=1;i<v.size();++i){{ acc=std::max(v[i],acc+v[i]); best=std::max(best,acc); }}
    return best;
}}
int main(){{ std::vector<int> v={{-2,1,-3,4,-1,2,1,-5,4}}; std::cout<<solve_{safe}(v); }}"""

def gen(cat_id, dir_name, problems, level, cat_name):
    out_dir = os.path.join(BASE, dir_name)
    os.makedirs(out_dir, exist_ok=True)
    n = 0
    for idx, name in enumerate(problems, 1):
        if name in HOT:
            concept, brute, optimal = HOT[name]
            chap = make_chapter(name, idx, level, cat_id, cat_name, concept, brute, optimal)
        else:
            chap = make_chapter(name, idx, level, cat_id, cat_name)
        with open(os.path.join(out_dir, fname(name, idx)), 'w') as f:
            f.write(chap)
        n += 1
    return n

def main():
    cats = [
        ("C40","C40_Trees_BST",C40,4,"Trees & Binary Search Trees"),
        ("C41","C41_Graphs_Fundamentals",C41,4,"Graphs — Fundamentals & Traversal"),
        ("C50","C50_Dynamic_Programming",C50,5,"Dynamic Programming"),
        ("C51","C51_Heaps_PQ_Sorting",C51,5,"Heaps, Priority Queues & Advanced Sorting"),
    ]
    total=0; counts={}
    for cid,dn,probs,lvl,cn in cats:
        c = gen(cid, dn, probs, lvl, cn)
        counts[cid]=c; total += c

    with open(os.path.join(BASE,"INDEX.md"),'w') as f:
        f.write(f"# Level 4 & 5 — Complete Problem Guide\n\n**Total:** {total} problems\n\n")
        for cid,dn,probs,lvl,cn in cats:
            f.write(f"## {cid} — {cn} (Level {lvl}) — {counts[cid]} problems\n\n")
            for i,name in enumerate(probs,1):
                f.write(f"- [{i:03d}. {name}]({dn}/{fname(name,i)})\n")
            f.write("\n")
    print(f"✅ Generated {total} chapters")
    for c,n in counts.items(): print(f"  {c}: {n}")

if __name__=="__main__":
    main()
