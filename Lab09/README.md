# LAB9_MoreHardProblems

## File Structure:
~~~
/LAB_09_HardProblems/
├── exercise1_
└── README.md
~~~

---

## Brief description of each solution

### Solution of exercise1_

This exercise implements the Influencer Coverage problem on a social network graph.

Users are modeled as nodes, and friendships are modeled as undirected edges.  
The goal is to select a minimum set of users such that every user is either selected or directly connected to at least one selected user.

The solution includes three main parts:

1. `is_valid_coverage(selected_users, graph)`

This function verifies whether a given set of selected users covers the whole graph.

A user is covered if:
- the user is selected
- or the user is directly connected to a selected user

2. `find_minimum_coverage(graph)`

This function finds the exact smallest coverage set.

It uses brute force by testing all possible subsets of users from the smallest size to the largest size.  
The first valid subset found is returned as the minimum solution.

This method is correct but only suitable for small graphs.

3. `find_fast_coverage(graph)`

This function uses a greedy approximation strategy.

At each step, it selects the user that covers the largest number of still-uncovered users.  
This method is faster than brute force and more suitable for larger graphs, but it does not always guarantee the optimal minimum solution.

---

## Complexity analysis summary

### Complexity of exercise1_

`is_valid_coverage(selected_users, graph)` : O(N + E)

This function marks all selected users and their neighbors as covered, then checks whether all users are covered.

`find_minimum_coverage(graph)` : O(2^N × (N + E))

This function tests all possible subsets of users.  
Since there are 2^N subsets, the runtime grows exponentially.

`find_fast_coverage(graph)` : O(N × (N + E))

In the simple implementation, each greedy step scans all users and checks the users they can cover.  
It is much faster than brute force, but it is still expensive for very large graphs without optimization.

---



The goal is to find a good enough solution in reasonable time, not necessarily the perfect minimum solution.

---

---
