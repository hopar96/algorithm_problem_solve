import copy
from collections import defaultdict
from itertools import combinations


def solution(dice):
    answer = []
    n = len(dice)
    dice_case = list(combinations([i for i in range(len(dice))], len(dice) // 2))
    dice_set = [[dice_case[i], dice_case[-1 - i]] for i in range(len(dice_case) // 2)]

    dice_combine_win = {}

    # 주사위 조합
    for aSet, bSet in dice_set:
        case_a = defaultdict(int)
        case_b = defaultdict(int)
        for idx, i in enumerate(aSet):
            c_a = defaultdict(int)
            if idx == 0:
                for num in dice[i]:
                    case_a[num] += 1
            else:
                for before_case in case_a.keys():
                    for num in dice[i]:
                        c_a[before_case + num] += case_a[before_case]
                case_a = c_a

        for idx, i in enumerate(bSet):
            c_b = defaultdict(int)
            if idx == 0:
                for num in dice[i]:
                    case_b[num] += 1
            else:
                for before_case in case_b.keys():
                    for num in dice[i]:
                        c_b[before_case + num] += case_b[before_case]
                case_b = c_b

        win, draw, lose = 0, 0, 0
        for a in case_a.keys():
            for b in case_b.keys():
                if a > b:
                    win += case_a[a] * case_b[b]
                elif a == b:
                    draw += case_a[a] * case_b[b]
                else:
                    lose += case_a[a] * case_b[b]

        dice_combine_win[aSet] = win
        dice_combine_win[bSet] = lose

    max_win = (0, None)
    for win_key in dice_combine_win.keys():
        if max_win[0] < dice_combine_win[win_key]:
            max_win = (dice_combine_win[win_key], win_key)

    for dice_num in max_win[1]:
        answer.append(dice_num+1)

    return answer


print(solution([[1, 2, 3, 4, 5, 6], [3, 3, 3, 3, 4, 4], [1, 3, 3, 4, 4, 4], [1, 1, 4, 4, 5, 5]]))
