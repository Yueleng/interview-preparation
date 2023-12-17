from ast import List
from functools import cmp_to_key


def compare(item1, item2):
    if item1[2] < item2[2]:
        return 1
    elif item1[2] > item2[2]:
        return -1
    elif item1[0] < item2[0]:
        return -1
    elif item1[0] > item2[0]:
        return 1
    else:
        return 0


class FoodRatings:
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food_cuisine_ratings = [
            [foods[i], cuisines[i], ratings[i]] for i in range(len(foods))
        ]
        # self.food_cuisine_ratings.sort(key=compare)
        self.food_cuisine_ratings = sorted(
            self.food_cuisine_ratings, key=cmp_to_key(compare)
        )

    def changeRating(self, food: str, newRating: int) -> None:
        for i in range(len(self.food_cuisine_ratings)):
            if food == self.food_cuisine_ratings[i][0]:
                self.food_cuisine_ratings[i][2] = newRating
        self.food_cuisine_ratings = sorted(
            self.food_cuisine_ratings, key=cmp_to_key(compare)
        )

    def highestRated(self, cuisine: str) -> str:
        for i in range(len(self.food_cuisine_ratings)):
            if self.food_cuisine_ratings[i][1] == cuisine:
                return self.food_cuisine_ratings[i][0]
