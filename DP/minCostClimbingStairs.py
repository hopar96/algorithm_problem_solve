# https://leetcode.com/problems/min-cost-climbing-stairs/description/

def minCostClimbingStairs(cost):
    stairLen = len(cost)
    cost = cost + [0]
    lowCostList = [False]*(stairLen+1)
    lowCostList[0] = cost[0]
    lowCostList[1] = cost[1]

    def dfs(stairNum):
        if stairNum < 2:
            return lowCostList[stairNum]

        firstDfs = lowCostList[stairNum-1]
        if firstDfs is False:
            firstDfs = dfs(stairNum-1)

        secondDfs = lowCostList[stairNum - 2]
        if secondDfs is False:
            secondDfs = dfs(stairNum - 2)
        lowCostList[stairNum] = min(firstDfs, secondDfs) + cost[stairNum]
        return lowCostList[stairNum]

    dfs(stairLen)
    print(lowCostList)
    return lowCostList[stairLen]

print(minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))
