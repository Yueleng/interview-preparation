## yield O(1)


def dfs(nested):
    for elem in nested:
        if elem.isInteger():
            yield elem.getInteger()
        else:
            for n in dfs(elem.getList()):
                yield n


class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.it = iter(dfs(nestedList))

    def next(self) -> int:
        return self.n

    def hasNext(self) -> bool:
        try:
            self.n = next(self.it)
            return True
        except StopIteration:
            return False
