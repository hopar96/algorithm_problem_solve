# https://leetcode.com/problems/maximum-depth-of-binary-tree/
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root) -> int:
        if root is None:
            return 0
        que = deque()
        que.append([root, 1])
        cnt = 1
        while len(que) > 0:
            popLi = que.popleft()
            print(popLi)
            tree = popLi[0]
            depth = popLi[1] + 1

            if tree.left is not None:
                que.append([tree.left, depth])
                cnt = depth
            if tree.right is not None:
                que.append([tree.right, depth])
                cnt = depth

        return cnt



Solution.maxDepth(TreeNode())