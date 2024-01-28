# https://school.programmers.co.kr/learn/courses/30/lessons/42627
import heapq


def solution(jobs):
    jobCnt = len(jobs)

    totTime = 0
    waitList = []
    schedule = 0  # job index, 끝나는 시각
    for time in range(1000 * 500):
        if not jobs and not waitList:
            break
        delList = []
        for idx, job in enumerate(jobs):
            if job[0] == time:  # 시작시간이 됐다면
                heapq.heappush(waitList, (job[1], job[0]))
                delList.append(job)

        for deljob in delList:
            jobs.remove(deljob)

        if schedule <= time:  # 작업이 없으면
            if waitList:
                takeTime, sttTime = heapq.heappop(waitList)
                schedule = time + takeTime
                totTime += time + takeTime - sttTime

    return totTime // jobCnt


# print(solution([[0, 3], [1, 9], [2, 6]]	))
# print(solution([[0, 3], [10, 1]))
# print(solution([[7, 8], [3, 5], [9, 6]]))
# print(solution([[1, 4], [7, 9], [1000, 3]]))
print(solution([[0, 1], [2, 2], [2, 3]]))