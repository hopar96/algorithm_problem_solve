# https://www.acmicpc.net/problem/17144
import copy


def solution(R, C, T, arr):
    dList = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    dList2 = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    dList3 = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    ac1 = None
    ac2 = None
    for r in range(R):
        if arr[r][1] == -1:
            ac1 = r
            ac2 = r+1
            break

    for i in range(T):
        print(arr)
        # 미세먼지 확산
        newArr = copy.deepcopy(arr)
        for r in range(1, R+1):
            for c in range(1, C+1):
                if arr[r][c] > 0:
                    print((r, c))
                    amt = arr[r][c] // 5
                    for dr, dc in dList:
                        if arr[r+dr][c+dc] > -1:
                            print('확산', (r+dr, c+dc))
                            newArr[r+dr][c+dc] += amt
                            newArr[r][c] -= amt
        arr = copy.deepcopy(newArr)

        for a in arr:
            print(a)

        # 공기 청정기 가동
        tmp = (ac1-1, 1)
        for index, (dr, dc) in enumerate(dList2):
            while True:
                if arr[tmp[0]+dr][tmp[1]+dc] == -2 or (index == 2 and tmp[0] == ac1):
                    print('break')
                    break
                elif arr[tmp[0]+dr][tmp[1]+dc] == -1:
                    arr[tmp[0]][tmp[1]] = 0
                    break
                elif arr[tmp[0]][tmp[1]] != -1:
                    print('상단', (tmp[0]+dr, tmp[1]+dc))
                    arr[tmp[0]][tmp[1]] = arr[tmp[0]+dr][tmp[1]+dc]
                tmp = (tmp[0] + dr, tmp[1] + dc)

        tmp = (ac2+1, 1)
        for index, (dr, dc) in enumerate(dList3):
            while True:
                if arr[tmp[0] + dr][tmp[1] + dc] == -2 or (index == 2 and tmp[0] == ac2):
                    break
                elif arr[tmp[0]+dr][tmp[1]+dc] == -1:
                    arr[tmp[0]][tmp[1]] = 0
                    break
                elif arr[tmp[0]][tmp[1]] != -1:
                    arr[tmp[0]][tmp[1]] = arr[tmp[0] + dr][tmp[1] + dc]
                tmp = (tmp[0] + dr, tmp[1] + dc)

        for a in arr:
            print(a)

    totAmt = 0
    for r in range(1, R + 1):
        for c in range(1, C + 1):
            if arr[r][c] > 0:
                totAmt += arr[r][c]

    print(totAmt)





RCT = list(map(int, input().split()))
R = RCT[0]
C = RCT[1]
T = RCT[2]
arr = []
arr.append([-2]*(C+2))
for _ in range(R):
    arr.append([-2] + list(map(int, input().split())) + [-2])
arr.append([-2] * (C + 2))

solution(R, C, T, arr)
