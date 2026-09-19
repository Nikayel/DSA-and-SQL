class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_island = 0
        ROW,COL = len(grid),len(grid[0])
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        def dfs(r,c):
            grid[r][c] = 0 
            curr_size = 1
            for row, col in directions:
                row_dir,col_dir = row+r,col+c
                if (row_dir >= 0 and row_dir < ROW and col_dir >=0 
                and col_dir < COL and 
                    grid[row_dir][col_dir]==1):
                    curr_size += dfs(row_dir,col_dir)
            return curr_size
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c]:
                    current = dfs(r,c)
                    max_island = max(max_island, current)
        return max_island