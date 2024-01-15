# https://leetcode.com/problems/two-sum/

def twoSum(nums, target):

    dic = {}
    for i in range(len(nums)):
        v = nums[i]
        needNum = target - v
        if needNum in dic:
            return [i, dic[needNum]]

        dic[v] = i
    return []



print(twoSum([3,2,4], 6))
