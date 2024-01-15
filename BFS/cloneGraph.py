# https://leetcode.com/problems/clone-graph/
# TODO
from collections import deque
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def cloneGraph(self, node):
    """
    :type node: Node
    :rtype: Node
    """

    aleadyCreate = {}

    def dfs(targetNode):
        if targetNode in aleadyCreate:
            return aleadyCreate[targetNode]

        cp = Node(targetNode.val, [])
        aleadyCreate[targetNode] = cp
        newNeighbors = []
        for n in targetNode.neighbors:
            newNeighbors.append(dfs(n))
        cp.neighbors = newNeighbors

        return cp

    return dfs(node)