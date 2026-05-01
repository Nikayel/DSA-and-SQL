class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r = len(matrix)
        c = len(matrix[0])
        total = r * c
        left_pointer = 0
        right_pointer = total - 1
        while left_pointer <= right_pointer:
            middle = (right_pointer + left_pointer)//2
            i = middle // c
            j = middle % c
            if target == matrix[i][j]:
                return True
            elif target < matrix[i][j]:
                right_pointer = middle - 1
            else:
                left_pointer = middle + 1
        return False

        return False