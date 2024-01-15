# https://leetcode.com/problems/letter-case-permutation/description/

def letterCasePermutation(s):
    ans = []

    def backTracking(cur):
        if len(cur) == len(s):
            ans.append(cur)
            return

        if s[len(cur)].isalpha():
            if s[len(cur)].isupper():
                backTracking(cur + s[len(cur)].lower())
            else:
                backTracking(cur + s[len(cur)].upper())
        backTracking(cur + s[len(cur)])

    backTracking('')
    return ans






print(letterCasePermutation('a1b2'))
# print('11'.isupper())

