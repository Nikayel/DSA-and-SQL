class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #create a pair of p, s 
        pair = [[p,s] for p,s in zip(position, speed)]
        stack = []
        #sort closest item first
        pair.sort(reverse=True) 
        #loop over get position and check top of stack  
        for p, s in pair:
            arrival_time = (target - p) / s
            if stack and stack[-1] >= arrival_time:
                continue
            else:
                stack.append(arrival_time)
        return len(stack) 
        #10:2,8:4,5:1,3:3,0:1