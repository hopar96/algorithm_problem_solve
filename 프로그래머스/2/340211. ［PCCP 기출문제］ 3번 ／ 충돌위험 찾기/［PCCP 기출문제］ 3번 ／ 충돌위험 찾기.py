import copy

dl, dr, dt, dd = (-1, 0), (1, 0), (0, -1), (0, 1)

def solution(points, routes):
    answer = 0
    time_route_list = []
    max_time = 0

    for route in routes:
        time_route_list.append(get_time_route(points, route))
        max_time = max(max_time, len(time_route_list[-1]))

    for i in range(max_time):
        check_dic = dict()
        for time_route in time_route_list:
            if len(time_route) > i:
                if time_route[i] in check_dic:
                    check_dic[time_route[i]] += 1
                else:
                    check_dic[time_route[i]] = 1

        for point in check_dic.keys():
            if check_dic[point] > 1:
                answer += 1

    return answer

def get_time_route(points, route):
    _route = copy.deepcopy(route)

    position = (points[_route[0] - 1][0], points[_route[0] - 1][1])
    del _route[0]
    timeRoute = [position]
    while _route:
        target = (points[_route[0] - 1][0], points[_route[0] - 1][1])
        # row 먼저 이동
        move = None
        if target[0] > position[0]:
            move = dr
        elif target[0] < position[0]:
            move = dl
        elif target[1] > position[1]:
            move = dd
        elif target[1] < position[1]:
            move = dt
        dx, dy = move
        position = (position[0] + dx, position[1] + dy)
        timeRoute.append(position)

        if position[0] == points[_route[0] - 1][0] and position[1] == points[_route[0] - 1][1]:
            del _route[0]

    return timeRoute
