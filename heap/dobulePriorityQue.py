# https://school.programmers.co.kr/learn/courses/30/lessons/42628
import heapq


def solution(operations):
    answer = []

    list = []

    for i in operations:
        if i.startswith("I "):
            list.append(int(i.split("I ")[1]))
        elif list:
            if i.startswith("D 1"):
                list = heapq.nlargest(len(list), list)[1:]
            elif i.startswith("D -1"):
                list = heapq.nsmallest(len(list), list)[1:]

    if list:
        answer.append(heapq.nlargest(len(list), list)[0])
        answer.append(heapq.nsmallest(len(list), list)[0])
    else:
        answer = [0, 0]

    return answer

print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))
# print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))

# print( int("I 15".split("I ")[1]) )