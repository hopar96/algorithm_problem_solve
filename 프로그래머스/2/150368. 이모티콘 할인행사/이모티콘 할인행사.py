import copy
answer = [0,0]

def solution(users, emoticons):
    global answer
    
    discount_result = {}
    
    
#     for idx, emo in enumerate(emoticons):
#         for dp in [10,20,30,40]:
#             for user in users:
#                 if user[0] <= dp:
                        
                
#                 emo * dp / 100
                
#             dis_emo = []

    
    dfs(-1, 0, [0 for _ in range(len(users)) ], users, emoticons)
    return answer

def dfs(cidx, discount, user_price, users, emoticons):
    global answer
    if cidx >= len(emoticons):
        buy_cnt = 0
        for idx, user in enumerate(users):
            if user_price[idx] >= user[1]:
                user_price[idx] = 0
                buy_cnt += 1
                
        if answer[0] < buy_cnt:
            answer[0] = buy_cnt
            answer[1] = sum(user_price)
        elif answer[0] == buy_cnt and answer[1] < sum(user_price):
            answer[0] = buy_cnt
            answer[1] = sum(user_price)
        return
    
    _user_price = copy.deepcopy(user_price)
    
    if cidx != -1:
        for idx, user in enumerate(users):
            if user[0] <= discount:
                _user_price[idx] += emoticons[cidx] * (100-discount) / 100
                
    # print("cidx : ",cidx, ", discount:", discount, ", userprice: ", user_price)            
    
    for dp in [10,20,30,40]:
        dfs(cidx+1, dp, _user_price, users, emoticons)
    
    