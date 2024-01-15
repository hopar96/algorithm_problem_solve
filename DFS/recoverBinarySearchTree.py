# https://leetcode.com/problems/recover-binary-search-tree/description/
from collections import deque


# def swap(self, root, swpList):
#
#     wrongList = []
#     que = deque()
#     que.append(root)
#     while que and len(wrongList) != 2:
#         cur = que.popleft()
#         if cur.left and cur.left.val >= cur.val:
#             if cur.right and cur.left.val < cur.right.val:
#                 wrongList.append(cur)
#             else:
#                 wrongList.append(cur.left)
#             que.append(cur.left)
#         if cur.right and cur.right.val >= cur.val:
#             if cur.left and cur.left.val < cur.right.val:
#                 wrongList.append(cur)
#             else:
#                 wrongList.append(cur.left)
#             que.append(cur.right)
#
#     wrongList[0].val, wrongList[1].val = wrongList[1].val, wrongList[0].val
