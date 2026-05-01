class MinStack:

    def __init__(self):
        self.regStack =[]
        self.minStack =[]

    def push(self, val: int) -> None:
        #min and regular
        #compare curr number with the highest number in the min stack
        #then add

        #step 1: add -> 1 minstack,regualrstack ->step 2: minstack [1,1]; regularstack[1,2]; 
        #step 3: add -> 0 minstack[1,1,0], regularStack [1,2,0]
        self.regStack.append(val)
        if not self.minStack or val < self.minStack[-1]:
            self.minStack.append(val)
        else:
            self.minStack.append(self.minStack[-1])
    def pop(self) -> None:
        if not self.minStack:
            raise IndexError("Cannot pop from empty stack")
        self.regStack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.regStack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
        #minStack
        #regular

        
