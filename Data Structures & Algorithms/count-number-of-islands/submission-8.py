class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island_counts = 0

        #4 directions
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        #ROW, COL
        row,col = len(grid),len(grid[0])
        def DFS(r,c):
            grid[r][c] = "0"
            for dr,dc in directions:
                curr_r,curr_c = r+dr,c+dc
                if(curr_r < row and curr_c < col and
                   curr_r >= 0 and curr_c >= 0 and 
                   grid[curr_r][curr_c] == "1"):
                   grid[curr_r][curr_c] = "0"
                   DFS(curr_r,curr_c)


        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1":
                    DFS(i,j)
                    island_counts+=1
        return island_counts
        
