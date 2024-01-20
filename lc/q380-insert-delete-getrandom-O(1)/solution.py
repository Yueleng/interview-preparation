import random


class RandomizedSet:
    def __init__(self):
        self.data_map = {}
        self.data = []

    def insert(self, val: int) -> bool:
        if val in self.data_map:
            return False

        self.data_map[val] = len(self.data)

        self.data.append(val)

        return True

    def remove(self, val: int) -> bool:
        if val not in self.data_map:
            return False

        index = self.data_map[val]

        last = self.data[-1]
        self.data[index] = last
        self.data_map[last] = index
        self.data.pop()

        del self.data_map[val]
        return True

    def getRandom(self) -> int:
        # if running outside of leetcode, you need to `import random`.
        # random.choice will randomly select an element from the list of data.
        return random.choice(self.data)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
