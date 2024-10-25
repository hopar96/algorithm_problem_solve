def solution(diffs, times, limit):
    _min = 100000
    _max = 1

    while _max <= _min:
        level = (_max + _min) // 2
        mid = get_tot_time(diffs, times, level)

        if mid > limit:
            _max = level + 1
        else:
            _min = level - 1

    return _max


def get_tot_time(diffs, times, level):
    time = 0
    for i in range(len(diffs)):
        prev_time = 0 if i == 0 else times[i - 1]
        time += solve_time(diffs[i], prev_time, times[i], level)

    return time


def solve_time(diff, time_prev, time_cur, level):
    back_times = 0 if diff <= level else diff - level
    return time_cur + (time_prev + time_cur) * back_times

