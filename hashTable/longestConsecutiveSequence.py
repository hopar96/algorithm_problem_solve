
def longestConsecutive(nums) -> int:
    maxCnt = 0
    numDic = {}
    for num in nums:
        numDic[num] = True

    for num in numDic:
        if num - 1 not in numDic:
            cnt = 0
            next = num
            while next in numDic:
                cnt += 1
                next += 1
            maxCnt = max(cnt, maxCnt)

    return maxCnt



print(longestConsecutive([0,3,7,2,5,8,4,6,0,1]))