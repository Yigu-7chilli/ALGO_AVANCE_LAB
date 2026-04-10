# LAB6_01_Revision

## File Structure:
~~~
/LAB _ 06/
├── exercise1_
└── README.md
~~~

---


##  Brief description of each solution

### Solution of exercise1_

This scheme implements a social network graph using both adjacency matrices and adjacency lists.

Users are modeled as nodes, and friend relationships are modeled as undirected edges. The system supports core graph operations, such as adding/deleting friend relationships, checking connections, and retrieving neighbors.

Furthermore, it includes graph attribute computation, such as integrity, density, and degree distribution, as well as conversion between adjacency matrix and adjacency list representations.



## Complexity analysis summary

### Complexity of exercise1_

add_friendship(u, v) : O(1)
remove_friendship(u, v) : O(n)
are_friends(u, v) : O(1)
get_friends(u) : O(k)
get_degree(u) : O(1)
get_num_users(): O(1)
get_num_edges() : O(1)

is_complete_graph() : O(n²)
graph_density() : O(1)
degree_distribution() : O(n)
matrix_to_list() : O(n²)
list_to_matrix() : O(n + m)


---
