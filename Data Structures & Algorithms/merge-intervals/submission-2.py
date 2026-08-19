class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        output = []
        stack = []
        intervals.sort()
        for interval in intervals:
            #if new stack or not overlapping
            if not stack or interval[0] > stack[-1][1]:
                output.append(interval)
                stack.append(interval)
            else:
                output[-1][1] = max(stack[-1][1], interval[1])
        return output