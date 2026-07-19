class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        #Perimeter 
        param = 0
        ROW,COL = len(grid),len(grid[0])
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
    #Nested for loop
        for row in range(ROW):
            for col in range(COL):
                if grid[row][col] == 1:
                    for rdir,cdir in directions:
                        currR,currC = row+rdir,col+cdir
                        if (currR < 0 or currC < 0 or currR >=ROW or currC >= COL or
                            grid[currR][currC] == 0
                        ):      
                            param +=1
        return param