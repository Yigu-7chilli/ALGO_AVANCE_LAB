# LAB8_01_Revision

## File Structure:
~~~
/LAB _ 08/
├── exercise1_BinarySearchTrees
├── exercise2_BinaryHeap 
└── README.md
~~~

---



---

## Brief description of each solution


### Solution of exercise1_BinarySearchTrees

This exercise implements a Binary Search Tree to manage user profiles in a social network.

Each node stores:
- `user_id`
- `name`
- `friends`
- `left`
- `right`

The main operations are:
- `insert(user_id, name, friends_list)`
- `find(user_id)`
- `inorder_traversal()`
- `delete(user_id)`

Additional operations are:
- `suggest_friends(user_id, max_suggestions)`
- `get_height()`
- `is_balanced()`
- `get_leaf_count()`

The tree keeps users ordered by `user_id`, so search, insertion, and deletion are efficient in the average case.



### Solution of exercise2_BinaryHeap

This exercise implements a Max-Heap to maintain trending posts by likes.

Each heap entry stores:
- `likes`
- `post_id`
- `timestamp`

The main operations are:
- `push(post_id, likes, timestamp)`
- `pop_max()`
- `peek_max()`
- `get_top_k(k)`
- `update_likes(post_id, new_likes, timestamp)`
- `size()`

Additional operations are:
- `is_valid_heap()`
- `get_height()`
- `get_level_order()`

The heap keeps the most liked posts at the top, which makes trending post retrieval efficient.

A simulation is also included:
- start with 100 posts
- perform 10,000 like updates
- display the top 5 posts every 1,000 updates
- measure the average time per operation

---



## Complexity analysis summary

### Complexity of exercise1_BinarySearchTrees

- `insert`: average **O(log n)**, worst case **O(n)**
- `find`: average **O(log n)**, worst case **O(n)**
- `delete`: average **O(log n)**, worst case **O(n)**
- `inorder_traversal`: **O(n)**
- `get_height`: **O(n)**
- `get_leaf_count`: **O(n)**
- `is_balanced`: **O(n²)** in the simple recursive version
- `suggest_friends`: depends on the number of friends and friends of friends


### Complexity of exercise2_BinaryHeap

- `push`: **O(log n)**
- `pop_max`: **O(log n)**
- `peek_max`: **O(1)**
- `get_top_k(k)`: **O(k log n)**
- `update_likes`: **O(log n)**
- `size`: **O(1)**
- `is_valid_heap`: **O(n)**
- `get_height`: **O(log n)**
- `get_level_order`: **O(n)**





---
