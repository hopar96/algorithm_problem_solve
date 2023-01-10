# 16139번 문제
# https://www.acmicpc.net/problem/16139

# 승재는 인간-컴퓨터 상호작용에서 생체공학 설계를 공부하다가 키보드 자판이 실용적인지 궁금해졌다. 이를 알아보기 위해 승재는 다음과 같은 생각을 했다.
#
# '문자열에서 특정 알파벳이 몇 번 나타나는지 알아봐서 자주 나타나는 알파벳이 중지나 검지 위치에 오는 알파벳인지 확인하면 실용적인지 확인할 수 있을 것이다.'
# 승재를 도와 특정 문자열 $S, 특정 알파벳 $\alpha$와 문자열의 구간 $[l,r]$이 주어지면
# $S$의 $l$번째 문자부터 $r$번째 문자 사이에 $\alpha$가 몇 번 나타나는지 구하는 프로그램을 작성하여라. 승재는 문자열의 문자는 $0$번째부터 세며,
# $l$번째와 $r$번째 문자를 포함해서 생각한다. 주의할 점은 승재는 호기심이 많기에 (통계적으로 크게 무의미하지만) 같은 문자열을 두고 질문을 $q$번 할 것이다.


S = input()
q = int(input())

alrList = []
for i in range(0, q):
    alrList.append(list(map(str, input().split())))

alphaCntListMap = {}

for x in alrList:
    if alphaCntListMap.get(x[0]) is None:
        cnt = 0
        cntList = []
        for i in range(0, len(S)):
            if S[i] == x[0]:
                cnt += 1
            cntList.append(cnt)
        alphaCntListMap[x[0]] = cntList

for x in alrList:
    cntList = alphaCntListMap.get(x[0])
    if int(x[1]) - 1 > -1:
        print(cntList[int(x[2])] - cntList[int(x[1]) - 1])
    else:
        print(cntList[int(x[2])])
    # l = int(x[1]) - 1 if int(x[1]) - 1 > -1 else 0
    #
    # print(cntList[int(x[2])] - cntList[l])









