# https://leetcode.com/problems/subsets-ii/description/

def subsetsWithDup( nums):
    ans = []
    nums.sort()

    def backTracking(idx, cur):
        if len(cur) == k:
            ans.append(cur[:])
            return

        for i in range(idx, len(nums)):
            if i > idx and nums[i-1] == nums[i]:
                continue
            cur.append(nums[i])
            backTracking(i+1, cur)
            cur.pop()

    for k in range(len(nums) + 1):
        backTracking(0, [])

    return ans




print(subsetsWithDup(nums = [1,2,2]))
