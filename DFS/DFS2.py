# 22027번 문제
# https://www.acmicpc.net/problem/22027

# 통신망은 $N$개의 컴퓨터와 $M$개의 회선으로 구성된다. 컴퓨터는 $1$번부터 $N$번까지 번호가 붙어 있다. 하나의 회선은 서로 다른
# $2$개의 컴퓨터가 양방향으로 통신할 수 있도록 한다. 통신망의 어떤 두 컴퓨터도 하나 이상의 회선을 이용해서 통신이 가능하면 통신망은 연결되어 있다고 한다.
# 통신이 불가능한 컴퓨터의 쌍이 존재하는 경우 통신망은 끊어져 있다고 한다.
# 통신망의 한 회선 $c$의 위험도는 다음과 같이 정의된다.
# 통신망의 각 컴퓨터 $i$에 대해서, 컴퓨터 $i$를 제거했을 때 남은 통신망이 끊어져 있는 경우 컴퓨터 $i$를 위험한 컴퓨터라고 한다.
# 초기 통신망에서 $c$를 제거했을 때, 위험한 컴퓨터의 개수를 $c$의 위험도로 정의한다.
# 통신망을 입력으로 받아 각 회선의 위험도를 계산하는 프로그램을 작성하라.


def dfs(ownList, n):
    if ownList[n] is not None:
        return

        for lineLi in ownList[n]:
            dfs(ownList, n)


# 위험도 구하기
def getDangerDegree(idx):
    global lineList, N
    degree = 0
    for n in range(1, N + 1):  # n : 빠지는 컴퓨터

        ownList = [] * N  # 해당 index 컴퓨터가 가지고 있는 선 리스트
        for i in range(len(lineList)):
            if i == idx:  # 현재 회선 제외
                continue
            if lineList[i][0] == n or lineList[i][1] == n:  # 빠지는 컴퓨터가 있는 회선은 제외
                continue
            ownList[lineList[i][0]-1] = lineList[i][1]
            ownList[lineList[i][1]-1] = lineList[i][0]

        dfs(ownList)  # 가지고 있는 선 dfs

    return degree


# main
resultList = []
nm = list(map(int, input().split()))

N = nm[0]
m = nm[1]

lineList = [list(map(int, input().split())) for _ in range(m)]

for i in range(len(lineList)):
    resultList.append(getDangerDegree(i))

for x in resultList:
    print(x)

# def getDangerFlg(lineList,comCnt ,removeCom):
#     leftCnt = comCnt - 1
#     delLineList = []
#     for i in range(len(lineList)):
#         for j in range(2):
#             if removeCom == lineList[i][j]:
#                 delLineList.append(i)
#     delLineList.reverse()
#     for delLine in delLineList:
#         del lineList[delLine]
#
#     targetComList = [lineList[0][0]]
#     while 1:
#         tmpTargetList = []
#         delLineList = []
#         for i in range(len(lineList)):
#             for j in range(2):
#                 for x in targetComList:
#                     if x == lineList[i][j]:
#                         if j == 0:
#                             tmpTargetList.append(lineList[i][1])
#                             break;
#                         else:
#                             tmpTargetList.append(lineList[i][0])
#                         delLineList.append(i)
#         delLineList.reverse()
#         for delLine in delLineList:
#             del lineList[delLine]
#         leftCnt -= len(targetComList)
#         targetComList = copy.deepcopy(tmpTargetList)
#
#         if len(lineList) == 0:
#             break
#
#     if leftCnt <= 0:
#         return True
#     else:
#         return False
#
# nm = list(map(int, input().split()))
#
# n = nm[0]
# m = nm[1]
#
# lineList = [list(map(int, input().split())) for _ in range(m)]
# dangerDegreeList = []
#
# for i in range(len(lineList)):
#     dangerDegree = 0
#     for j in range(1, m+1):
#         dangerDegree += 1 if getDangerFlg(copy.deepcopy(lineList), m, j) else 0
#
#     dangerDegreeList.append(dangerDegree)
#
# for x in dangerDegreeList:
#     print(x)
