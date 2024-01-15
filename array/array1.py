# https://www.acmicpc.net/problem/3033

def find_string(parent, pattern):
    parent_len = len(parent)
    pattern_len = len(pattern)
    parent_hash = 0
    pattern_hash = 0
    power = 1
    for i in range(parent_len - pattern_len + 1):
        if i == 0:
            for j in range(pattern_len):
                parent_hash += ord(parent[pattern_len - 1 - j]) * power
                pattern_hash += ord(pattern[pattern_len - 1 - j]) * power
                if j < pattern_len - 1:
                    power *= 2
        else:
            parent_hash = 2 * (parent_hash - ord(parent[i - 1]) * power) + ord(parent[pattern_len - 1 + i])

        if parent_hash == pattern_hash:
            found = True
            for j in range(pattern_len):
                if parent[i + j] != pattern[j]:
                    found = False
                    break
            if found:
                # print(f'{i + 1}번째에서 발견했습니다')
                return found

def longestString(l, N):
    result = 0

    for j in range(0, l, 1):
        checkLen = result + 1
        for i in range(checkLen, l, 1):
            if i + j > l:
                break
            s = N[j : j+i]
            leftStr = N[:j]
            rightStr = N[j+1:]
            fullStr = leftStr + ' ' + rightStr
            breakFlg = True
            # print(s)
            # if s in fullStr:
            if find_string(fullStr, s):
                result = max(result, i)
                breakFlg = False

            # if len(leftStr) >= len(s):
            #     if s in leftStr:
            #         result = max(result, i)
            #         breakFlg = False
            # if len(rightStr) >= len(s):
            #     if s in rightStr:
            #         result = max(result, i)
            #         breakFlg = False
            if breakFlg:
                break
    return result

l = int(input())
N= input()

print(longestString(l, N))

#


# def longestString(l, N):
#     result = 0
#
#     for i in range(l, 1, -1):
#         dic = {}
#         for j in range(0, l-i, 1):
#             s = N[j: j + i]
#             if s in dic:
#                 return max(result, i)
#             else:
#                 dic[s] = True
#
#     return result
