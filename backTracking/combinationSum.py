# https://leetcode.com/problems/combination-sum-ii/description/

def combinationSum2(candidates: list, target: int) -> list[list[int]]:
    ans = []
    candidates.sort()

    def backTracking(start, cur):


        if sum(cur) == target:
            ans.append(cur[:])
            return
        elif sum(cur) > target:
            return

        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i-1]:
                continue
            cur.append(candidates[i])
            backTracking(i + 1, cur)
            cur.pop()

    backTracking(start=0, cur=[])

    return ans


print(combinationSum2(candidates=[10, 1, 2, 7, 6, 1, 5], target=8))
#
# print([1, 2] == [2, 1])