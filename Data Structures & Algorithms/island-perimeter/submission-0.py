class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        #Perimeter
        Perimeter = 0
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        #row,col
        row,col = len(grid),len(grid[0])
        #looping on row
        for r in range(row):
            #looping over col
            for c in range(col):
                #check if 1:
                if grid[r][c] == 1:
                    #Go through all 4 neighbours
                    for dir_R,dir_C in directions:
                        current_R,current_C = r + dir_R, c + dir_C
                        if (current_R < 0 or current_C < 0 or current_R >= row or current_C >= col):
                            Perimeter +=1
                        elif grid[current_R][current_C] == 0:
                            Perimeter += 1
        return Perimeter




        