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

superMinCnt = K*K
for y in range(0, Y - K + 1):
    for x in range(0, X - K + 1):
        colorCount = 0
        for color in colorList:
            minCnt = 0
            lineCnt = 0
            for j in range(0, K):
                count = 0
                for i in range(0, K):
                    if board[y + j][x + i] != colorList[(colorCount+count + lineCnt) % 2]:
                        minCnt += 1
                    count += 1
                lineCnt += 1
            colorCount += 1

            superMinCnt = minCnt if minCnt < superMinCnt else superMinCnt

print(superMinCnt)
