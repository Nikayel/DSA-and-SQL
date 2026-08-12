class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        direction = [[1,0],[-1,0],[0,1],[0,-1]]
        num_islands = 0 
        ROW, COL = len(grid),len(grid[0])
        def dfs(r,c):
            grid[r][c] = "0"
            for rdir,cdir in direction:
                curr_row,curr_col = rdir+r, cdir+c
                if(curr_row < ROW and curr_row >= 0 and curr_col < COL and 
                curr_col >= 0 and grid[curr_row][curr_col] == "1"):
                    dfs(curr_row,curr_col)
        for row in range(ROW):
            for col in range(COL):
                if grid[row][col] == "1":
                    num_islands+=1
                    dfs(row,col)
        return num_islands