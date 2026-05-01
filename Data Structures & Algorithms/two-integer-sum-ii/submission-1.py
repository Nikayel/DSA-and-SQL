class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # two pointers, left and right
        left,right = 0, len(numbers)-1
        #left starts from 1st itme and right from last itme
        while left < right:
            result = numbers[left] + numbers[right] 
            if result == target:
                return [left+1,right+1]
            elif result < target:
                left +=1
            else:
                right -=1

        
        