
# 11659번 문제
# https://www.acmicpc.net/problem/11659

# 수 N개가 주어졌을 때, i번째 수부터 j번째 수까지 합을 구하는 프로그램을 작성하시오.
# 입력 : 첫째 줄에 수의 개수 N과 합을 구해야 하는 횟수 M이 주어진다. 둘째 줄에는 N개의 수가 주어진다.
#       수는 1,000보다 작거나 같은 자연수이다. 셋째 줄부터 M개의 줄에는 합을 구해야 하는 구간 i와 j가 주어진다.
# 출력 : 총 M개의 줄에 입력으로 주어진 i번째 수부터 j번째 수까지 합을 출력한다.
# 제한 : 1 ≤ N ≤ 100,000
#       1 ≤ M ≤ 100,000
#       1 ≤ i ≤ j ≤ N


nm = list(map(int, input().split()))
N = nm[0]
M = nm[1]


arr = []
arr = list(map(int, input().split()))

arr2 = [list(map(int, input().split())) for _ in range(M)]

arr3 = [0 for _ in range(N+1)]
index = 0
arr3[0] = 0
for a in arr:
    index += 1
    if index != 0:
        arr3[index] = arr3[index-1] + a


for x, y in arr2:
    print(arr3[y] - arr3[x-1])
