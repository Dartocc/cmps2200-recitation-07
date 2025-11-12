# CMPS 2200 Recitation 10## Answers

**Name:**_________________________
**Name:**_________________________


Place all written answers from `recitation-07.md` here for easier grading.



- **2)**
-   The work of reachable is O(n + m) where n= the number of nodes, and m= number of edges because each edge is visited at most once O(n) and each edge is examined at most twice O(m).

- **4)**
  1, because if the graph is connected, one call to reachable from any node is enough. And if the graph is disconnected, one call will find the component containing the starting node, and you can check if all nodes were reached.
- **5)**
-   The work of connected is O(n + m) it calls reachable once (O(n + m)), and then checks if the size of the reachable set equals the number of nodes (O(n))

- **7)**
-   yes, the work increases from O(n + m) to O(n^2), If we switch to an adjacency matrix representation, then checking all neighbors of a node takes O(n), because must scan the whole row for each node. Visiting all n nodes → total work O(n^2)
