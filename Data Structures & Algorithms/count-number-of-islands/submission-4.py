class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #numIsland
        numIslands = 0
        #Create a qeue
        ROW,COL = len(grid),len(grid[0]) 
        q = deque()
        #direction -> all 4 directions (be used for looping)
        directions = [(0,1),(-1,0),(1,0),(0,-1)]
        #BFS(n,m)
        def BFS(r,c):
            #q.append(n,m)
            q.append((r,c))
            grid[r][c] == "0"
            #while q:
            while(q):
                #pop first -> popleft
                row,col = q.popleft()
                #check the neighbours using the direction array that we create
                for dr,dc in directions:
                    nrow,ncol = row+dr,col+dc 
                    if(nrow < ROW and ncol < COL and
                      nrow >=0 and ncol >= 0 and
                    grid[nrow][ncol]== "1"):
                        q.append((nrow,ncol))
                        grid[nrow][ncol] = "0"


        
        #Loop over the grid(n,m)
        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == "1":
                    numIslands+=1
                    BFS(i,j)
                #numIsland+=1
                #BFS(n,m)
        return numIslands




        