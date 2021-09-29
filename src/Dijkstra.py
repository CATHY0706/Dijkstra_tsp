#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Tianyi Zhang and Botao Gao
Created on Tue Dec 1st 14:03:37 2020
Based on the code found in tutorial at this website: 'https://blog.csdn.net/u014798883/article/details/106200697'

"""


def dijkstra(adjacency_matrix, start, path, cost, max):
    """
    Solve the shortest path problem with Dijkstra's algorithm.
    :param adjacency_matrix: A two-dimensional array (an adjacency matrix), which  used to represent indicate whether pairs
        of vertices are adjacent or not in the graph.
    :param start: starting node, input by user, int type
    :param path:transit point, the previous node of the node vi.
    :param cost: the shortest known path length from V0 to Vi
    :param max: int type, an infinite number, usually represented by 10000
    mid_node: transit point, take the shortest path from V0 to Vi as the transit point.
    next_node: centering on the transit point, try to optimize the path. To check whether the path which next_node
        direct to V0 or the path which passes mid_node to V0 is better.
    check_node: Index, searching for the shortest path point in the cost array. The shortest point will be assigned
        to mid_node as a transit point.
    :return path: the shortest path
    """
    # get the size of the adjacency matrix
    length = len(adjacency_matrix)

    # Initialize the p array to 0, to mark whether the point has been added to the shortest path
    p = [0] * length

    # Initialize path，cost，p
    for i in range(length):
        if i == start:
            # set the start node as 1
            p[start] = 1
        else:
            # cost[i]: Get the cost of reaching other points directly from the starting point
            cost[i] = adjacency_matrix[start][i]
            # if cannot reach the starting point directly, set as -1
            path[i] = (start if (cost[i] < max) else -1)

    # print p, cost, path
    # Traverse all points (excluding the starting point)
    for i in range(1, length):
        # Maximum initial value
        min_cost = max
        mid_node = -1

        # Search for a point closest to the starting point v0 as a transit point mid_node
        for check_node in range(length):
            if p[check_node] == 0 and cost[check_node] < min_cost:
                # If it is found that the cost of passing a transit point is less than the minimum cost
                # then update the min_cost and check_node
                min_cost = cost[check_node]
                mid_node = check_node

        # If the path with a cost less than the minimum cost cannot be found, jump out of the loop
        if mid_node == -1:
            break
        # If the path with a cost less than the minimum cost has been found, add the check_node to the shortest path
        p[mid_node] = 1

        # for loop: Update the cost and path of other nodes
        for next_node in range(length):
            # Check all points next_node which are not traversed
            # Check the influence of mid_node (which has been added to the path in the previous step) on next_node
            # If the total cost is less than the existing minimum cost, update the path and cost array
            if p[next_node] == 0 and (adjacency_matrix[mid_node][next_node] + cost[mid_node] < cost[next_node]):
                # update cost
                cost[next_node] = adjacency_matrix[mid_node][next_node] + cost[mid_node]
                # update path
                path[next_node] = mid_node

    # return the shortest path
    return path


if __name__ == '__main__':
    maximum = 10000

    G = [
        
        # this is the area for you to enter your adjacency matrix
        [0,     294,    1076,   1021,   10000,  10000,  10000,  10000],
        [294,   0,      794,    906,    896,    10000,  10000,  10000],
        [1076,  794,    0,      1106,   740,    743,    10000,  10000],
        [1021,  906,    1106,   0,      536,    10000,  1362,   10000],
        [10000, 896,    740,    536,    0,      1141,   985,     1566],
        [10000, 10000,  743,    10000,  1141,   0,      1582,     894],
        [10000, 10000,  10000,  1362,   985,    1582,   0,       1342],
        [10000, 10000,  10000,  10000,  1566,   894,    1342,       0]
        # this is the area for you to enter your adjacency matrix

        ]

    # enter your starting node here
    start_node = 0

    path = [0] * len(G)
    cost = [0] * len(G)
    print('The shortest path:', dijkstra(G, start_node, path, cost, maximum))
    print('The cost to each node:', cost)
