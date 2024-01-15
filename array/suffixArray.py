# https://www.acmicpc.net/problem/9248



def getSuffixAndLcp(s):

    suffixList = []
    for i in range(len(s)):
        suffixList.append((s[i:], 0, 0))

    idx = 1
    preLcp = 2
    for j in range(len(suffixList)):
        # suffix = suffixList[j]
        lcp = 0
        for i in range(preLcp-1, len(suffixList[j][0])):
            pattern = suffixList[j][0][:i]
            if pattern in suffixList[j][0][1:]:
                lcp = len(pattern)
            else:
                break
        suffixList[j] = (suffixList[j][0], idx, lcp)
        idx += 1
        preLcp = max(lcp, 2)
    suffixList.sort()

    suffixStr = ''
    lcpStr = 'x'
    firstFlg = True
    for i in range(len(suffixList)):
        suffixStr += ' ' + str(suffixList[i][1])
        if not firstFlg:
            lcpStr += ' ' + str(suffixList[i][2])
        else:
            firstFlg = False

    print(suffixStr.lstrip())
    print(lcpStr.strip())

S = input()
getSuffixAndLcp(S)
