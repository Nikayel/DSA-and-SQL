class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #left and right pointer
        left = 0
        row = len(matrix)
        col = len(matrix[0])
        right = row*col - 1
        while left <= right:
            #find the middle
            middle = (left+right)//2 
            #convert middle to 2d matrix
            i = middle // col
            j = middle % col
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                right = middle-1
            else:
                left = middle+1
        return False
            #compare the 2d with our target
        #find the length of the matrix(row and col)

        