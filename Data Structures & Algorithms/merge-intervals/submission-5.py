class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        output = []
        for interval in intervals:
            if not output or interval[0] > output[-1][1]:
                output.append(interval)
            else:
                output[-1][1] = max(interval[1], output[-1][1])
        return output
                