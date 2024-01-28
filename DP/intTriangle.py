# https://school.programmers.co.kr/learn/courses/30/lessons/43105

def solution(triangle):
    dp = [{} for i in range(len(triangle))]

    dp[0][0] = triangle[0][0]
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            tmp1 = 0
            tmp2 = 0
            if (j - 1 >= 0):
                tmp1 = dp[i - 1][j-1] + triangle[i][j]
            if j < len(triangle[i-1]):
                tmp2 = dp[i - 1][j] + triangle[i][j]
            dp[i][j] = max(tmp1, tmp2)
    maxD = 0

    for d in dp[len(triangle)-1].values():
        maxD = max(maxD, d)
    return maxD