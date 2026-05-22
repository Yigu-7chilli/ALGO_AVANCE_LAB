# LAB10_01_Revision

## File Structure:
~~~
/LAB _ 10/
├── ex1_Event_Invitation.py
├── ex2_Viral_Message_Timing.py
└── README.md
~~~

---


##  Brief description of each solution


### Solution of exercise1

Exercise 1 solves the Event Invitation problem using the idea of Maximum Independent Set.

Users are represented as nodes, and conflicts are represented as edges.  
The goal is to invite the largest possible group of users such that no two invited users have a conflict.

The solution includes three functions:

- `is_valid_invitation(invited, graph)` checks if a given invited list is valid.
- `find_max_invitations_exact(graph)` uses backtracking with pruning to find the exact maximum invited set.
- `find_max_invitations_greedy(graph)` uses a greedy heuristic by repeatedly choosing the node with the smallest degree.

The exact method gives the optimal answer for small graphs, while the greedy method is faster but does not always guarantee the optimal solution.

### Solution of exercise2

Exercise 2 solves the Viral Message Timing problem using the idea of 0/1 Knapsack.

Each user has a cost and a reach value.  
The goal is to select users to maximize the total reach without exceeding the budget.

The solution includes three functions:

- `is_within_budget(selection, costs, budget)` checks if the selected users stay within the budget.
- `maximize_reach_exact(budget, costs, reaches)` uses dynamic programming to find the exact optimal solution.
- `maximize_reach_greedy(budget, costs, reaches)` selects users by the highest `reach / cost` ratio first.

The dynamic programming method gives the optimal answer when the budget is not too large.  
The greedy method is faster and easier to scale, but it may fail to find the optimal solution.

## Complexity analysis summary

### Complexity of exercise1

`is_valid_invitation(invited, graph)`:  
Checks every pair of invited users.

Time complexity: `O(k²)`  
where `k` is the number of invited users.

`find_max_invitations_exact(graph)`:  
Uses backtracking and tries selecting or not selecting each user.

Worst-case time complexity: `O(2^N)`  
where `N` is the number of users.

With pruning, some branches can be stopped early, but the worst case is still exponential.

`find_max_invitations_greedy(graph)`:  
Repeatedly finds the node with the smallest degree and removes it with its neighbors.

Simple implementation time complexity: `O(N²)`  
It is faster than the exact method, but it is not guaranteed to be optimal.

### Complexity of exercise2

`is_within_budget(selection, costs, budget)`:  
Sums the costs of the selected users.

Time complexity: `O(N)`  
or more precisely `O(k)`, where `k` is the number of selected users.

`maximize_reach_exact(budget, costs, reaches)`:  
Uses dynamic programming with a table of size `N × budget`.

Time complexity: `O(N × budget)`  
Space complexity: `O(N × budget)`

This is not exponential because the algorithm stores and reuses previous results.

`maximize_reach_greedy(budget, costs, reaches)`:  
Sorts users by `reach / cost` ratio and selects users while the budget allows.

Time complexity: `O(N log N)` if sorting is used.

The greedy method is fast and scalable, but it does not always find the optimal solution.



Exercise 2 is based on 0/1 Knapsack.  
Its exact version is pseudo-polynomial, so it works well when the budget is small or medium, but it becomes too expensive when both `N` and `budget` are very large.

In practice, exact algorithms are useful for small test cases.  
For large social network data, greedy algorithms, heuristics, and approximation methods are more realistic.
