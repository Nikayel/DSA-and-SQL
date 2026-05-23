class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        #stack
        stack = []
        #looping over asteroid
        for i in range(len(asteroids)):
            alive = True
            #check the stack and campare top of stack with current
            while alive and stack and stack[-1] > 0 and asteroids[i] < 0:
                #if same remove both by popping the stack
                if stack[-1] == abs(asteroids[i]):
                    #remove both
                    stack.pop()
                    alive = False
                #elif abs(topOfStack) > abs(curent)
                elif stack[-1] > abs(asteroids[i]):
                    #remove current
                    alive = False
                #else
                else:
                    #remove old
                    stack.pop()
            if alive:
                stack.append(asteroids[i])
        #return stack
        return stack

        #edge case:
        #zero -ok
        #comaprin goingleft And right