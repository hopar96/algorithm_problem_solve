def solution(friends, gifts):
    answer = 0
    gift_rate = {}
    gifted_list = {}
    will_gift = {}
    for friend in friends:
        gift_rate[friend] = 0
        gifted_list[friend] = []
        will_gift[friend] = []
    
    for gift in gifts:
        glist = gift.split(" ")
        gift_rate[glist[0]] = gift_rate[glist[0]]+ 1
        gift_rate[glist[1]] = gift_rate[glist[1]] - 1
        
        gifted_list[glist[1]].append(glist[0])
        
    for friend in friends:
        for op in friends:
            if friend == op:    continue
            if friend in will_gift[op] or op in will_gift[friend]:     continue
            
            friend_cnt = 0
            op_cnt = 0
            for t in gifted_list[friend]:
                if op == t:
                    op_cnt += 1
            for t in gifted_list[op]:
                if friend == t:
                    friend_cnt += 1
                    
            if friend_cnt > op_cnt:
                will_gift[friend].append(op)
            elif friend_cnt < op_cnt:
                will_gift[op].append(friend)
            else:
                if gift_rate[friend] > gift_rate[op]:
                    will_gift[friend].append(op)
                elif gift_rate[friend] < gift_rate[op]:
                    will_gift[op].append(friend)
        
    for key in will_gift:
        answer = max(answer, len(will_gift[key]))
    
    return answer