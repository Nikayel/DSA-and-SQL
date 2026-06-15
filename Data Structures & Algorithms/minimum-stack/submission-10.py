class MinStack:

    def __init__(self):
        self.minStack = []
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minStack:
            self.minStack.append(val)
        else:
            if self.minStack[-1] >= val:
                self.minStack.append(val)

    def pop(self) -> None:
        if self.stack[-1] == self.minStack[-1]:
            self.stack.pop()
            self.minStack.pop()
        else:
            self.stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        return 0
    def getMin(self) -> int:
        if self.minStack:
            return self.minStack[-1]
        return 0
