# https://leetcode.com/problems/longest-palindromic-substring/description/
import math


def longestPalindrome(s):
    sLen = len(s)
    maxStr = ''

    for i in range(sLen):
        # 홀수
        for j in range(2, sLen, 2):
            halfJ = int(j / 2)
            if 0 <= i - halfJ and i + halfJ < sLen:
                if i + halfJ == sLen - 1:
                    lStr = s[i - halfJ:i]
                    rStr = s[i + 1:]
                else:
                    lStr = s[i - halfJ:i]
                    rStr = s[i + 1:i + halfJ + 1]
                if lStr == rStr[::-1]:
                    if len(maxStr) < j+1:
                        maxStr = lStr + s[i] + rStr
                else:
                    break
            else:
                break

        for o in range(0, int(math.floor((sLen - i)/ 2) )):
            if len(maxStr) < 2 * o + 2:
                if s[i:i + o + 1] == s[i + o + 1:i + 2 * o + 2][::-1]:
                    maxStr = s[i:i + 2 * o + 2]

    return maxStr


print(longestPalindrome('aaaa'))

# print('babad'[0:6])
