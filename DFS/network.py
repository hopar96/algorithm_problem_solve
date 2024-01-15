# https://school.programmers.co.kr/learn/courses/30/lessons/43162

def solution(n, computers):
    def dfs(idx):
        for j in range(n):
            if computers[idx][j] == 1:
                if j not in vList:
                    vList[j] = True
                    dfs(j)

    answer = 0
    i = 0
    vList = {}
    while len(vList) != n:
        if i not in vList:
            vList[i] = True
            dfs(i)
            answer += 1
        i += 1

    return answer


print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))