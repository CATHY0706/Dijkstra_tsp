# Dijkstra_tsp

## For Group2_Dijkstra algorithm.py

* ### Input: 
You only need to change the G and start_node variables to get the shortest path and cost.
In order to let python code run smoothly, you should follow the belowing guides.

### 1. At the G variable, you should enter the standard adjacency matrix.
please enter the adjacency matrix of the following form in the square brackets:

		[0,    16,      9,      35,     10000,  10000,  10000],
		[10000, 0,      10000,  12,     25,     10000,  10000],
		[10000, 10000,  0,      15,     10000,  22,     10000],
		[10000, 10000,  10000,  0,      14,     17,        19],
		[10000, 10000,  10000,  10000,  0,      10000,      8],
		[10000, 10000,  10000,  10000,  10000,  0,         14],
		[10000, 10000,  10000,  10000,  10000,  10000,      0]


(We have converted the 12-node and 20-node test matrices to standard forms, you can copy and paste them to run the python code.)

### 2. Python counts from zero.
For example, if you want to use the 3rd node as the starting node,you should enter number 2 for start_node.


* ### Output: 
You will get the shortest path and cost array.

### 1. Shortest path array:
* 0 represents the starting node
* -1 represents a node that is not reachable from the starting node

### 2. Cost array
No matter what the start node is, the third number represents the minimum cost from start node to the third node. The fifth number represents the minimum cost to the fifth node. Similarly, other numbers in the cost array have the same meaning.




## For Group2_debug code.py

Unit test is a common method for python to debug. The correctness of the code is ensured by comparing whether the artificial calculation result and the computer calculation result are the same.