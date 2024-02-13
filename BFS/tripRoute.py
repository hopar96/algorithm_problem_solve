# https://school.programmers.co.kr/learn/courses/30/lessons/43164
from _operator import itemgetter


def solution(tickets):

    def dfs(dest, list):
        print(list)
        if len(list) == N+1:
            return list
        for i in range(N):
            tmp = None
            if vList[i] == 0 and dest == tickets[i][0]:
                vList[i] = 1
                tmp = dfs(tickets[i][1], list + [tickets[i][1]])
                vList[i] = 0

            if tmp is not None:
                return tmp

        return None

    N = len(tickets)
    vList = [0]*N

    tickets = sorted(tickets, key=itemgetter(0), reverse=False)
    tickets = sorted(tickets, key=itemgetter(1), reverse=False)

    return dfs("ICN", ["ICN"])


print(solution([["ICN", "JFK"], ["HND", "IAD"],  ["IAD", "HND"], ["HND", "IAD"], ["JFK", "HND"]]))