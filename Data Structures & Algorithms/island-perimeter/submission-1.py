class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        #Perim
        perimeter = 0
        #directions
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        #ROW,COL
        row,col = len(grid),len(grid[0])
        #loop over the row
        for r in range(row):
            #loop over column
            for c in range(col):
            #If land:
                if grid[r][c] == 1:
                 #loop in all 4 directions
                 for dir_r,dir_c in directions:
                    curr_r, curr_c = r+dir_r, c+dir_c
                 #take care of perim count here
                    if(curr_r < 0 or curr_c < 0
                        or curr_r >= row or curr_c >= col
                        or grid[curr_r][curr_c] == 0
                        ):
                        perimeter +=1
        return perimeter

