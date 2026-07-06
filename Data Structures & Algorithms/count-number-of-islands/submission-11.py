class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        numIslands = 0
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        row,col = len(grid),len(grid[0])
        def DFS(i,j):
            grid[i][j] = "0"
            for r,c in directions:
                curr_row,curr_col = r+i,c+j
                if (curr_row >= 0 and curr_col >= 0 and curr_row < row and
                    curr_col < col and grid[curr_row][curr_col] == "1"):
                        DFS(curr_row,curr_col)



        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1":
                    numIslands +=1
                    DFS(i,j)
        return numIslands