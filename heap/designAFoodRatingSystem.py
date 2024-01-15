# https://leetcode.com/problems/design-a-food-rating-system/
import heapq
from collections import defaultdict


class FoodRatings(object):
    def __init__(self, foods, cuisines, ratings):
        self.map = {}
        self.dic = defaultdict(list)
        for i in range(len(foods)):
            heapq.heappush(self.dic[cuisines[i]], (-1 * ratings[i], foods[i], True))
            self.map[foods[i]] = cuisines[i]

    def changeRating(self, food, newRating):
        cuisine = self.map[food]
        cur_list = self.dic[cuisine]
        for i in range(len(cur_list)):
            if cur_list[i][1] == food and cur_list[i][2]:
                cur_list[i] = (cur_list[i][0], cur_list[i][1], False)
                self.dic[cuisine] = cur_list
                heapq.heappush(cur_list, (-1 * newRating, food, True))
                return


    def highestRated(self, cuisine):
        idx = 0
        while True:
            if self.dic[cuisine][0][2]:
                return self.dic[cuisine][0][1]
            idx += 1
            heapq.heappop(self.dic[cuisine])


foodRatings = FoodRatings(["김치", "된장", "초밥", "무사카", "라면", "불고기"], ["한국어", "일본어", "일본어", "그리스어", "일본어", "한국어"], [9, 12, 8, 15, 14, 7]);
print(foodRatings.highestRated('일본어'))
print(foodRatings.changeRating('라면', 1))
print(foodRatings.highestRated('일본어'))
# print(foodRatings.highestRated("한국어"));

#      def __init__(self, foods, cuisines, ratings):
#         self.map = {}
#         self.dic = defaultdict(list)
#         for i in range(len(foods)):
#             heapq.heappush(self.dic[cuisines[i]], (-1 * ratings[i], foods[i]))
#             self.map[foods[i]] = cuisines[i]
#
#     def changeRating(self, food, newRating):
#         cuisine = self.map[food]
#         cur_list = self.dic[cuisine]
#         for i in range(len(cur_list)):
#             if cur_list[i][1] == food:
#                 cur_list[i] = (-1 * newRating, food)
#                 heapq.heapify(cur_list)
#                 self.dic[cuisine] = cur_list
#                 return
#
#
#     def highestRated(self, cuisine):
#         return self.dic[cuisine][0][1]