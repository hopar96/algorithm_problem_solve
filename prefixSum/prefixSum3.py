# 25682번 문제
# https://www.acmicpc.net/problem/25682

# 지민이는 자신의 저택에서 MN개의 단위 정사각형으로 나누어져 있는 M×N 크기의 보드를 찾았다.
# 어떤 정사각형은 검은색으로 칠해져 있고, 나머지는 흰색으로 칠해져 있다. 지민이는 이 보드를 잘라서 K×K 크기의 체스판으로 만들려고 한다.
# 체스판은 검은색과 흰색이 번갈아서 칠해져 있어야 한다. 구체적으로, 각 칸이 검은색과 흰색 중 하나로 색칠되어 있고,
# 변을 공유하는 두 개의 사각형은 다른 색으로 칠해져 있어야 한다. 따라서 이 정의를 따르면 체스판을 색칠하는 경우는 두 가지뿐이다.
# 하나는 맨 왼쪽 위 칸이 흰색인 경우, 하나는 검은색인 경우이다.
# 보드가 체스판처럼 칠해져 있다는 보장이 없어서, 지민이는 K×K 크기의 체스판으로 잘라낸 후에 몇 개의 정사각형을 다시 칠해야겠다고 생각했다.
# 당연히 K×K 크기는 아무데서나 골라도 된다. 지민이가 다시 칠해야 하는 정사각형의 최소 개수를 구하는 프로그램을 작성하시오.

mnk = list(map(int, input().split()))
Y = mnk[0]
X = mnk[1]
K = mnk[2]
colorList = ['B', 'W']
board = [str(input()) for _ in range(Y)]

chgMap = {}


for colorCnt in range(0, len(colorList)):
    chgList = [[0 for _ in range(0, X)] for _ in range(Y)]
    lineCnt = 0
    for y in range(0, Y):
        columnCnt = 0
        for x in range(0, X):
            if board[y][x] != colorList[(colorCnt + lineCnt + columnCnt) % 2]:
                chgList[y][x] += 1
            columnCnt += 1
        lineCnt += 1
    chgMap[colorList[colorCnt]] = chgList


prefixMap = {}

for color in colorList:
    chgList = chgMap[color]
    sumList = [[0 for _ in range(X + 1)] for _ in range(Y + 1)]
    for y in range(1, Y+1):
        for x in range(1, X+1):
            sumList[y][x] = chgList[y-1][x-1] + sumList[y-1][x] + sumList[y][x-1] - sumList[y-1][x-1]
    prefixMap[color] = sumList

superMin = K*K
for color in colorList:
    sumList = prefixMap[color]
    for y in range(0, Y - K + 1):
        for x in range(0, X - K + 1):
            # xy -> x+k-1, y+k-1
            minCnt = sumList[y+K][x+K] - sumList[y][x+K] - sumList[y+K][x] + sumList[y][x]
            superMin = superMin if superMin < minCnt else minCnt

print(superMin)