#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 2st 22:52:36 2020

@author: Botao Gao and Tianyi Zhang

"""

import unittest
from Algorithm import dijkstra, main


class MainTest(unittest.TestCase):

    def test_dijkstra_7nodes(self):
        graph_7 = [
        [0, 294, 1076, 1021, 10000, 10000, 10000, 10000],
        [294, 0, 792, 906, 896, 10000, 10000, 10000],
        [1076, 792, 0, 1106, 740, 743, 10000, 10000],
        [1021, 906, 1106, 0, 536, 10000, 1362, 10000],
        [10000, 896, 740, 536, 0, 1141, 985, 1566],
        [10000, 10000, 743, 10000, 1141, 0, 1582, 849],
        [10000, 10000, 10000, 1362, 985, 1582, 0, 1342],
        [10000, 10000, 10000, 10000, 1566, 849, 1342, 0]
    ]
        graph_7_path = [0, 0, 0, 0, 1, 2, 4, 5]
        graph_7_cost = [0, 294, 1076, 1021, 1190, 1819, 2175, 2668]
        path = [0] * len(graph_7)
        cost = [0] * len(graph_7)
        max = 10000
        path, cost = dijkstra(graph_7, 0, path, cost, max)
        self.assertEqual(path, graph_7_path)
        self.assertEqual(cost, graph_7_cost)

    def test_dijkstra_20nodes(self):
        graph_20 = [[0	,10000	,369	,10000	,10000	,10000	,10000	,219	,10000	,10000	,489	,10000	,331	,10000	,443	,10000	,460	,437	,10000	,250],
        [10000	,0	,10000	,10000	,10000	,10000	,468	,10000	,10000	,10000	,10000	,10000	,305	,10000	,10000	,10000	,10000	,245	,10000	,10000],
        [369	,10000	,0	,280	,10000	,261	,10000	,184	,180	,431	,367	,468	,469	,10000	,294	,382	,464	,10000	,10000	,10000],
        [10000	,10000	,280	,0	,10000	,284	,10000	,406	,197	,10000	,490	,216	,10000	,10000	,285	,310	,10000	,10000	,309	,10000],
        [10000	,10000	,10000	,10000	,0	,10000	,286	,10000	,10000	,10000	,10000	,10000	,10000	,10000	,400	,275	,10000	,10000	,10000	,10000],
        [10000	,10000	,261	,284	,10000	,0	,10000	,472	,104	,286	,288	,447	,10000	,340	,493	,10000	,449	,10000	,10000	,10000],
        [10000	,468	,10000	,10000	,286	,10000	,0	,10000	,10000	,10000	,10000	,10000	,374	,10000	,268	,211	,10000	,279	,10000	,10000],
        [219	,10000	,184	,406	,10000	,472	,10000	,0	,364	,10000	,453	,10000	,297	,10000	,259	,375	,10000	,369	,10000	,306],
        [10000	,10000	,180	,197	,10000	,104	,10000	,364	,0	,316	,293	,341	,10000	,480	,402	,472	,454	,10000	,434	,467],
        [10000	,10000	,431	,10000	,10000	,286	,10000	,10000	,316	,0	,164	,10000	,10000	,198	,10000	,10000	,325	,10000	,10000	,400],
        [489	,10000	,367	,490	,10000	,288	,10000	,453	,293	,164	,0	,10000	,10000	,335	,10000,	10000	,161	,10000	,10000	,236],
        [10000	,10000	,468	,216	,10000	,447	,10000	,10000	,341	,10000	,10000	,0	,10000	,10000	,490	,467	,10000	,10000	,106	,10000],
        [331	,305	,469	,10000	,10000	,10000	,374	,297	,10000	,10000	,10000	,10000	,0	,10000	,317	,386	,10000	,106	,10000	,10000],
        [10000	,10000	,10000	,10000	,10000	,340	,10000	,10000	,480	,198	,335	,10000	,10000	,0	,10000	,10000	,496	,10000	,10000	,10000],
        [443	,10000	,294	,285	,400	,493	,268	,259	,402	,10000	,10000	,490	,317	,10000	,0	,116	,10000	,285	,10000	,10000],
        [10000	,10000	,382	,310	,275	,10000	,211	,375	,472	,10000	,10000	,467	,386	,10000	,116	,0	,10000	,348	,447	,10000],
        [460	,10000	,464	,10000	,10000	,449	,10000	,10000	,454	,325	,161	,10000	,10000	,496	,10000	,10000	,0	,10000	,10000	,210],
        [437	,245	,10000	,10000	,10000	,10000	,279	,369	,10000	,10000	,10000	,10000	,106	,10000	,285	,348	,10000	,0	,10000	,10000],
        [10000	,10000	,10000	,309	,10000	,10000	,10000	,10000	,434	,10000	,10000	,106	,10000	,10000	,10000	,447	,10000	,10000	,0	,10000],
        [250	,10000	,10000	,10000	,10000	,10000	,10000	,306	,467	,400	,236	,10000	,10000	,10000	,10000	,10000	,210	,10000	,10000	,0]]
        graph_20_path = [0, 12, 0, 7, 15, 2, 12, 0, 2, 19, 19, 2, 0, 10, 0, 14, 0, 0, 3, 0]
        graph_20_cost = [0, 636, 369, 625, 834, 630, 705, 219, 549, 650, 486, 837, 331, 821, 443, 559, 460, 437, 934, 250]
        path = [0] * len(graph_20)
        cost = [0] * len(graph_20)
        max = 10000
        path, cost = dijkstra(graph_20, 0, path, cost, max)
        self.assertEqual(path, graph_20_path)
        self.assertEqual(cost, graph_20_cost)


if __name__ == '__main__':
	unittest.main()
