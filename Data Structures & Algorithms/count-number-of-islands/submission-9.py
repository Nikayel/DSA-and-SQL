class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        rows,cols = len(grid),len(grid[0])
        island_count = 0
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        def BFS(r,c):
            q = collections.deque()
            q.append((r,c))
            grid[r][c] = "0"
            while q:
                row,col = q.popleft()
                for r_dir, c_dir in directions:
                    curr_r,curr_c = row + r_dir, col + c_dir
                    if (curr_r >= 0 and curr_c >= 0
                    and curr_r < rows and curr_c < cols
                    and grid[curr_r][curr_c] == "1"):
                        q.append((curr_r,curr_c))
                        grid[curr_r][curr_c] = "0"
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    island_count +=1
                    BFS(i,j)
        return island_count
