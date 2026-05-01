
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        left,right = 0, len(heights)-1
        while left < right:
            width = right-left
            height = min(heights[left],heights[right])
            current_area = width*height
            max_area = max(current_area,max_area)
            if heights[left] > heights[right]:
                right-=1
            else:
                left+=1

        return max_area
        