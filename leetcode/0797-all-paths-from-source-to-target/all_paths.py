# Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1 and return them in any order.
# The graph is given as follows: graph[i] is a list of all nodes you can visit from node i (i.e., there is a directed edge from node i to node graph[i][j]).

# Input: graph = [[1,2],[3],[3],[]]
# Output: [[0,1,3],[0,2,3]]
# Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.

from typing import List


class Solution:

    def filterOut(self, node: List[List[int]], visited:List[int]):
        return [i for i in node if i not in visited]

    def visit(self, graph, idx=0, visited=[]):
        if not graph or not graph[0]:
            return [] # bad graph: [[],[whatever..]]. First node goes nowhere.

        visited = visited.copy()
        visited.append(idx)
        if idx == len(graph)-1:
            return [visited]

        options = self.filterOut(graph[idx], visited)
        if not options:
            return []

        results = []
        for o in options:
            vr = self.visit(graph, o, visited)
            for path in vr:
                if path:
                    results.append(path)
        return results

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        return self.visit(graph)
