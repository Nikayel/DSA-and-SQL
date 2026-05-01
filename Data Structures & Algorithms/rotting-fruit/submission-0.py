class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #variables
        fresh = 0
        minute = 0
        q = collections.deque()
        #Get the position/s of rotten fruit and Fresh Count
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh+=1
                if grid[r][c] == 2:
                    q.append((r,c))
        #fresh - 5
        #[2,2]
        direction = [[0,1],[0,-1],[1,0],[-1,0]]
        while q and fresh > 0:
            for i in range(len(q)):
                r,c = q.popleft()
        #Go in both directions and see if Fresh -> Append qeue
                for rd,cd in direction:
                    row,col = r+rd,c+cd
                    if(row in range(len(grid)) and
                    col in range(len(grid[0]))
                    and grid[row][col] == 1):
                        grid[row][col] = 2
                        q.append((row,col))
                        fresh-=1
            minute+=1 
        return minute if fresh == 0 else -1


        
      






        #return minute if fresh == 0 else return -1




