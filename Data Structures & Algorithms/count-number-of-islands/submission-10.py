class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROW,COL = len(grid),len(grid[0])
        island = 0
        
        def DFS(r,c):
            grid[r][c] = "0"
            directions = [[1,0],[0,1],[-1,0],[0,-1]]
            for row,col in directions:
                curr_row,curr_col = r+row,c+col
                if( curr_row >= 0 and curr_row < ROW and curr_col >= 0 
                and curr_col < COL
                and grid[curr_row][curr_col] == "1"
                ):
                    DFS(curr_row,curr_col)



        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == "1":
                    island+=1
                    DFS(r,c)
        return island
