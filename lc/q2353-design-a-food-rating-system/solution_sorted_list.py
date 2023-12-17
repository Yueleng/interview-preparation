from collections import defaultdict
from typing import List
from sortedcontainers import SortedList


class FoodRatings:
    def __init__(
        self, foods: List[str], cuisine: List[str], ratings: List[int]
    ) -> None:
        # store the relationship between food and cuisine
        # fast access food's cuisine and current rating
        self.mp = {}
        self.data = defaultdict(SortedList)
        for food, cuisine, rating in zip(foods, cuisine, ratings):
            self.mp[food] = (cuisine, rating)
            self.data[cuisine].add((-rating, food))

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine, rating = self.mp[food]
        self.mp[food] = (cuisine, newRating)
        self.data[cuisine].remove((-rating, food))
        self.data[cuisine].add((-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        return self.data[cuisine][0][1]
