# https://leetcode.com/problems/diagonal-traverse-ii/description/?envType=daily-question&envId=2023-11-22
from operator import itemgetter


def findDiagonalOrder(nums):

    slist = []
    for i in range(len(nums)):
        for j in range(len(nums[i])):
            slist.append((i+j, i, nums[i][j]))

    slist = sorted(slist, key=itemgetter(1), reverse=True)
    slist = sorted(slist,  key=itemgetter(0))

    return list(map(lambda i: i[2], slist))



print(findDiagonalOrder([[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]))

# def findDiagonalOrder(nums):
#     result = []
#     for i in range(len(nums)):
#         nxt = i
#         targetIdx = 0
#         while nxt >= 0:
#             print(nxt)
#             if len(nums[nxt]) >= (targetIdx+1):
#                 result.append(nums[nxt][targetIdx])
#             nxt -= 1
#             targetIdx += 1
#     return result