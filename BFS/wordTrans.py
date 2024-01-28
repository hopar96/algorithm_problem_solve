# https://school.programmers.co.kr/learn/courses/30/lessons/43163
from collections import deque

def valiCheck(word, target):
    difCnt = 0
    for i in range(len(word)):
        if word[i] != target[i]:
            difCnt += 1
        if difCnt > 1:
            return False
    return True

def solution(begin, target, words):
    if target not in words:
        return 0
    answer = len(words)
    vList = [0] * len(words)
    que = deque()
    que.append((begin, 1))

    while que:
        curWord, curCnt = que.popleft()
        if valiCheck(curWord, target):
            answer = min(answer, curCnt)

        for i in range(len(words)):
            if vList[i] == 0 and valiCheck(curWord, words[i]):
                vList[i] = 1
                que.append((words[i], curCnt + 1))

    return answer

# print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))