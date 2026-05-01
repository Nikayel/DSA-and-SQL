class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        max_length = 0
        visited = {}
        for right,character in enumerate(s):
            if character in visited and visited[character] >=left:
                left = visited[character] +1
            visited[character] = right 
            max_length = max(max_length, right-left+1)
        return max_length

        