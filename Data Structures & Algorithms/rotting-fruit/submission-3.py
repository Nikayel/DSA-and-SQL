class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

    #Take count of each fresh and rotten
        minutes = 0
        fresh = 0
        q = collections.deque()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh+=1
                elif grid[r][c] == 2:
                    q.append((r,c))

    #loop over the rotten qeue length
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        while q and fresh > 0:
            # Go through all the 4 directions (iF in bound and valid)
            for i in range(len(q)):
                row,col = q.popleft()
                for rd,cd in directions:
                    r,c = row+rd,col+cd
                    if (r in range(len(grid)) and 
                        c in range(len(grid[0])) and
                        grid[r][c] == 1):
                        grid[r][c] = 2
                        fresh-=1
                        q.append((r,c))
            minutes+=1
        return minutes if fresh == 0 else -1
            

                



        #If FreshFruit and valid then 1 - > 2 and add to qeue


    #increase the minute (timer)

