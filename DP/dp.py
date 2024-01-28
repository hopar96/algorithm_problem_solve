# https://school.programmers.co.kr/learn/courses/30/lessons/42895
from collections import deque



def solution(N, number):
    list = ['p', 'mi', 'mu', 'd', 'append']

    que = deque()
    que.append((0, 0))
    while que:
        curNumber, curIdx = que.popleft()
        if curIdx == 9:
            return -1
        if curNumber == number:
            return curIdx


        for i in list:
            if i == 'p':
                que.append((curNumber + N, curIdx + 1))
            if i == 'mi':
                que.append((curNumber - N, curIdx + 1))
            if i == 'mu':
                que.append((curNumber * N, curIdx + 1))
            if i == 'd':
                que.append((curNumber // N, curIdx + 1))
            if i == 'append':
                que.append((curNumber * 10 + N, curIdx + 1))



print(solution(5, 3025))
