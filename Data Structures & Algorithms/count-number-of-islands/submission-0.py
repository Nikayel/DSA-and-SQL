class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        #Increase island count then Change the 1 to 0, 
        number_islands=0
        m,n = len(grid),len(grid[0])
        #create a recursive function
        def DFS(i,j):
            #base case - > make sure if its a 0 ignore
            if i >= m or j >= n or j < 0 or i < 0 or grid[i][j] == "0":
                return
            else:
                #its a 1 then -> got though all directions recusively
                grid[i][j] = "0"
                DFS(i,j+1)
                DFS(i,j-1)
                DFS(i-1,j)
                DFS(i+1,j)


        #Loop over each row in the matrix
        for i in range(m):
            #loop over each col in the matrix
            for j in range(n):
                #Increase count
                if grid[i][j] == "1":
                    number_islands+=1
                #Recursviely go over the current n X m.  T and S is O n x m 
                    DFS(i,j)
        return number_islands