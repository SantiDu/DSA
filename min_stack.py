from math import inf

class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []   
        self.stack_mins = [inf]

    def push(self, val: int) -> None:
        if val <= self.stack_mins[-1]:
            self.stack_mins.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.stack_mins[-1]:
            self.stack_mins.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        if (min_ := self.stack_mins[-1]) == inf:
            return None
        else:
            return min_