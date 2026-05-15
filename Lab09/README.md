# LAB9_MoreHardProblems

## File Structure:
~~~
/LAB_09_HardProblems/
├── ex1_influencer_coverage.py
├── ex2_conflict_free_labeling.py
└── README.md
~~~

---

## Brief description of each solution

### Solution of exercise1_influencer_coverage

This exercise implements the Influencer Coverage problem on a social network graph.

Users are modeled as nodes, and friendships are modeled as undirected edges.  
The goal is to select a minimum set of users such that every user is either selected or directly connected to at least one selected user.

The solution includes three main functions:

`is_valid_coverage(selected_users, graph)`

This function verifies whether a given set of selected users covers the whole graph.  
A user is covered if the user is selected or directly connected to a selected user.

`find_minimum_coverage(graph)`

This function finds the exact smallest coverage set.  
It uses brute force by testing all possible subsets of users from the smallest size to the largest size.  
The first valid subset found is returned as the minimum solution.

`find_fast_coverage(graph)`

This function uses a greedy approximation strategy.  
At each step, it selects the user that covers the largest number of still-uncovered users.  
This method is faster than brute force, but it does not always guarantee the optimal minimum solution.

---

### Solution of exercise2_conflict_free_labeling

This exercise implements the Conflict-Free Labeling problem, also known as the Graph Coloring problem.

Users are modeled as nodes, and friendships are modeled as undirected edges.  
The goal is to assign labels to users so that connected users have different labels.  
The total number of different labels should be minimized.

The solution includes three main functions:

`is_valid_labeling(labeling, graph)`

This function verifies whether a given labeling is valid.  
A labeling is valid if, for every edge `(u, v)`, the two connected users have different labels.

`assign_labels(k, graph)`

This function tries to color the graph using at most `k` labels.  
It uses backtracking. For each user, the algorithm tries labels from `0` to `k - 1`.  
If a label creates no conflict with already labeled friends, the algorithm continues with the next user.  
If it gets stuck, it backtracks and tries another label.

`find_min_labels(graph)`

This function finds the minimum number of labels needed.  
It tries `k = 1, 2, 3, ...` until `assign_labels(k, graph)` succeeds.  
The first successful `k` is returned as the minimum number of labels.

---

## Complexity analysis summary

### Complexity of exercise1_influencer_coverage

`is_valid_coverage(selected_users, graph)` : O(N + E)

This function marks all selected users and their neighbors as covered, then checks whether all users are covered.

`find_minimum_coverage(graph)` : O(2^N × (N + E))

This function tests all possible subsets of users.  
Since there are `2^N` subsets, the runtime grows exponentially.

`find_fast_coverage(graph)` : O(N × (N + E))

In the simple implementation, each greedy step scans all users and checks the users they can cover.  
It is much faster than brute force, but it is still expensive for very large graphs without optimization.

---

### Complexity of exercise2_conflict_free_labeling

`is_valid_labeling(labeling, graph)` : O(E)

This function checks every edge once.  
For each edge `(u, v)`, it verifies that `labeling[u]` is different from `labeling[v]`.

`can_use_label(user, label, labeling, graph)` : O(deg(user))

This helper function checks the neighbors of one user to see if the label creates a conflict.

`assign_labels(k, graph)` : O(k^N) in the worst case

Each of the `N` users may try up to `k` labels.  
In the worst case, backtracking may explore many possible assignments.

`find_min_labels(graph)` : exponential in the worst case

This function calls `assign_labels(k, graph)` repeatedly for increasing values of `k`.  
Since `assign_labels` can be exponential, the overall method is also exponential in the worst case.
