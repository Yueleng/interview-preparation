class MyQueue:
    def __init__(self):
        self.in_stk = []
        self.out_stk = []

    def push(self, x: int) -> None:
        self.in_stk.append(x)

    def pop(self) -> int:
        self.peek()
        return self.out_stk.pop()

    def peek(self) -> int:
        # this if condition is important,
        # it ensures that last dumpped out_stk is cleared out before a new dump
        if not self.out_stk:
            while self.in_stk:
                self.out_stk.append(self.in_stk.pop())
        return self.out_stk[-1]

    def empty(self) -> bool:
        return not self.in_stk and not self.out_stk


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
