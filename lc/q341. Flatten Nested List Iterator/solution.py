# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """


class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        _list = []

        def flatten(_nestedList: [NestedInteger]):
            output = []
            for e in _nestedList:
                if e.isInteger():
                    output.append(e)
                else:
                    output.extend(flatten(e.getList()))
            return output

        self._list = flatten(nestedList)
        self.index = 0

    def next(self) -> int:
        # _next = self._list[0]
        # self._list = self._list[1:]
        # return _next
        self.index += 1
        return self._list[self.index - 1]

    def hasNext(self) -> bool:
        #  return len(self._list)
        return self.index < len(self._list)


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
