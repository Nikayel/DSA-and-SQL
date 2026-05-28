class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #declare all vars
        num_Of_Islands = 0
        row,col = len(grid), len(grid[0])
        direction = [(1,0),(0,1),(-1,0),(0,-1)]
        #DFS(r,c)
        def DFS(r,c):
            #Go through all 4 directions
            grid[r][c] = "0"
            for row_d,col_d in direction:
            #validity: curr_r,curr_c < row,col, curr_r,curr_c > 0 
                curr_r,curr_c = r+row_d,c+col_d
                if(curr_r >= 0 and curr_r < row
                   and curr_c >= 0 and curr_c < col
                   and grid[curr_r][curr_c] == "1"):
                   grid[curr_r][curr_c] = "0"
                   DFS(curr_r,curr_c)
            







        #loop over the grid
        for i in range(row):
            for j in range(col):
                #Everytime see a 1 run the dfs on it -> num_of_Island +=1
                if grid[i][j] == "1":   
                    DFS(i,j)
                    num_Of_Islands +=1
        return num_Of_Islands
