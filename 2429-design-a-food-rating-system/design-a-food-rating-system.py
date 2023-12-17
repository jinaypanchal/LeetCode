from collections import defaultdict
from heapq import heappush, heappop
from sortedcontainers import SortedSet


class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.d=defaultdict(dict)
        self.fc={}
        self.pq=defaultdict(list)
        for f,c,r in zip(foods,cuisines,ratings):
            self.d[c][f]=r
            self.fc[f]=c
            heappush(self.pq[c],(-r,f))


    def changeRating(self, food: str, newRating: int) -> None:
        cuis=self.fc[food]
        self.d[cuis][food]=newRating
        heappush(self.pq[cuis],(-newRating,food))
        

    def highestRated(self, cuisine: str) -> str:
        while self.pq[cuisine]:
            ele=self.pq[cuisine][0]
            if self.d[cuisine][ele[1]]!=-ele[0]:
                heappop(self.pq[cuisine])
            else: return ele[1]        


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)