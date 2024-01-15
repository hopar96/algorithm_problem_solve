# https://leetcode.com/problems/network-delay-time/
import heapq
from collections import defaultdict


def networkDelayTime(times, n, k):
    """
    :type times: List[List[int]]
    :type n: int
    :type k: int
    :rtype: int
    """
    graph = defaultdict(list)
    for time in times:
        graph[time[0]].append((time[2], time[1]))

    cost = {}
    que = []
    heapq.heappush(que, (0, k))
    while que:
        cur_cost, cur_node = heapq.heappop(que)
        if cur_node not in cost:
            cost[cur_node] = cur_cost
            for next_cost, next_node in graph[cur_node]:
                heapq.heappush(que, (cur_cost + next_cost, next_node))

    if len(cost) != n:
        return -1
    else:
        return max(cost.values())




print(networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2))