class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #Get count of fresh and rotten fruits
        q = collections.deque()
        minutes = 0
        fresh = 0  
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                #if 1 or 2 -> fresh or rotten
                if grid[r][c] == 1:
                    fresh+=1
                if grid[r][c] == 2:
                    q.append((r,c))
        #loop until we have something in the q and fresh >0
        #defining the 4 directions up,down,left,right
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        while q and fresh > 0:
            #loop over the length of our q.count
            for i in range(len(q)):
                #getting the position of our rotten fuit
                r,c = q.popleft()
                for rd,cd in directions:
                    #chech if its a valid move 1 - within range, 2 - the neighbour -> a fresh(1)
                    #manage fresh count and qeue items
                    row,col = rd+r,cd+c
                    if(row in range(len(grid)) and 
                        col in range(len(grid[0])) and
                        grid[row][col] == 1 ):
                        grid[row][col] = 2
                        fresh-=1
                        q.append((row,col))
                    
            minutes+=1
            #manage minute count
        return minutes if fresh == 0 else -1
        #return minute if fresh = 0 then return -1
        


