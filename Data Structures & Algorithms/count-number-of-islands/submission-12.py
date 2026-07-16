class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #directions 
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        #ROW,COl 
        ROW,COL = len(grid),len(grid[0])
        #Num_Of_Islands
        num_Of_Islands =0

        #DFS
        def DFS(r,c):
            #Mark as seen(make it a 0)
            grid[r][c] = "0"
            for rd,cd in directions:
                curr_dirR,curr_dirC = r+rd,c+cd
                #Boundry Check -> IF valid 
                if (curr_dirR < ROW and curr_dirR >= 0 and curr_dirC < COL and curr_dirC >= 0
                    and grid[curr_dirR][curr_dirC] == "1"
                ):
                #recursively Call DFS
                    DFS(curr_dirR,curr_dirC)




        #Loop over the grid 
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == "1":
                    num_Of_Islands +=1
                    DFS(r,c)
            #if a land(1) Then DFS -> Num_Of_Islands+=1
        return num_Of_Islands