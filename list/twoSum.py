# https://leetcode.com/problems/two-sum/

import copy

def twoSum(nums, target):
    sortedList = copy.deepcopy(nums)
    sortedList.sort()
    left = 0
    right = len(nums) - 1

    while left < right:
        sum = sortedList[left] + sortedList[right]
        if sum == target:
            rtnList = []
            for i in range(len(nums)):
                if sortedList[left] == nums[i]:
                    rtnList.append(i)
                elif sortedList[right] == nums[i]:
                    rtnList.append(i)
            return rtnList
        elif sum > target:
            right -= 1
        elif sum < target:
            left += 1
    return False


print(twoSum([3,2,4], 6))
