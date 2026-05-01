class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROW,COL = len(grid), len(grid[0])
        num_islands = 0
        def bfs(r,c):
            q = deque()
            q.append((r,c))
            grid[r][c] = "0"
            while(q):
                curr_r,curr_c = q.popleft()
                for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                    nr,nc = curr_r+dr, curr_c+dc
                    if (nr >= 0 and nc >= 0 and nr < ROW and nc < COL and grid[nr][nc] == "1"):
                        q.append((nr,nc))
                        grid[nr][nc] = "0"



        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == "1":
                    num_islands+=1
                    bfs(i,j)
        return num_islands
