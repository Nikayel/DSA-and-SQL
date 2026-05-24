class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        minute = 0
        q = collections.deque()

        fresh_fruit = 0
        row,col = len(grid),len(grid[0])

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 2:
                    q.append((r,c))
                elif grid[r][c] == 1:
                    fresh_fruit+=1
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        while fresh_fruit > 0 and q:
            for _ in range(len(q)):
                r,c = q.popleft()
                for dr,dc in directions:
                    curr_r,curr_c = dr+r,dc+c
                    if(curr_r >= 0 and curr_r < row and
                        curr_c >= 0 and curr_c < col
                        and grid[curr_r][curr_c] == 1):
                        grid[curr_r][curr_c] = 2
                        q.append((curr_r,curr_c))
                        fresh_fruit-=1
            minute+=1      


        return minute if fresh_fruit == 0 else -1
            