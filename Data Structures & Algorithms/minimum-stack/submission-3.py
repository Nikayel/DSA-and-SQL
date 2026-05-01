class MinStack:

    def __init__(self):
        self.regStack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.regStack.append(val)
        if not self.minStack or val < self.minStack[-1]:
            self.minStack.append(val)
        else:
            self.minStack.append(self.minStack[-1])

    def pop(self) -> None:
        self.regStack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.regStack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
        
