def solution(N, arr):

    def dfs(curDay, endWorkDay, jobList, money):
        if curDay == N+1:
            return money

        maxMoney = 0
        if curDay > endWorkDay and (curDay + arr[curDay][0]-1) <= N:  # 일할 수 있는 경우
            # 현재 날짜의 일을 하는 경우
            maxMoney = max(maxMoney, dfs(curDay + arr[curDay][0], (curDay + arr[curDay][0]-1), jobList + [curDay], money + arr[curDay][1]))

        # 현재 날짜의 일을 안하는 경우
        maxMoney = max(maxMoney, dfs(curDay + 1, endWorkDay, jobList, money))

        return maxMoney

    N -= 1
    print(dfs(0, -1, [], 0))



N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

solution(N, arr)