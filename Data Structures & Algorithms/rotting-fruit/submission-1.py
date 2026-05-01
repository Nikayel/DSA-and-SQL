class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        minute = 0
        q = collections.deque()
        #get count of all rotten and fresh fruits
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh+=1
                if grid[i][j] == 2:
                    q.append((i,j))
        

        #get position of the rotten fruit and start rottin gfruits around it 
        directions = [[-1,0],[1,0],[0,1],[0,-1]]
        #increase the minute after each cycle
        while q and fresh > 0:
            for i in range(len(q)):
                r,c = q.popleft()
                for rd,cd in directions:
                    row,col = r+rd,c+cd
                    if(row in range(len(grid)) and col in range(len(grid[0]))
                    and grid[row][col] == 1 
                    ):
                        fresh-=1
                        grid[row][col] = 2
                        q.append((row,col))
            minute+=1
                
        return minute if fresh == 0 else -1
            
            

