class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        ROW, COL = len(grid),len(grid[0])

        #return the size of the current island
        def dfs(r,c):
            grid[r][c] = 0
            curr_area = 1
            for row_dir, col_dir in directions:
                curr_row, curr_col = r+row_dir, c+col_dir
                if(curr_row >= 0 and curr_row < ROW and 
                    curr_col >= 0 and curr_col < COL and 
                    grid[curr_row][curr_col] == 1
                    ):
                    curr_area += dfs(curr_row, curr_col)
            return curr_area
                    

        
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    #compare the size of current dfs with our max_area
                    curr_area = dfs(r,c)
                    max_area = max(max_area, curr_area)
        return max_area
