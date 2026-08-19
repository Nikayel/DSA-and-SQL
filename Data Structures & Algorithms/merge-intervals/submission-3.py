class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        output = []
        intervals.sort()
        for interval in intervals:
            #if new stack or not overlapping
            if not output or interval[0] > output[-1][1]:
                output.append(interval)
            else:
                output[-1][1] = max(output[-1][1], interval[1])
        return output