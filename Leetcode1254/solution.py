#Time Complexity: O(m*n) where m is the number of rows and n is the number of columns in the grid. We visit each cell once.
#Space Complexity: O(m*n) in the worst case where all cells are land. The recursion stack can go as deep as the number of cells in the grid.
class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        count = 0
        def dfs(queue):
            result = True
            while queue:
                position = queue.pop()
                i, j = position[0], position[1]
                for r, c in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                    if r < 0 or r >= m or c < 0 or c >= n:
                        result = False
                        continue
                    if grid[r][c] == 0:
                        grid[r][c] = 1
                        queue.append((r,c))
            return result

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    grid[i][j] = 1
                    queue = [(i,j)]
                    if dfs(queue):
                        count+=1
        return count


#time complexity: O(m*n) where m is the number of rows and n is the number of columns in the grid. We visit each cell once.
#space complexity: O(m*n) in the worst case where all cells are land. The recursion stack can go as deep as the number of cells in the grid.
class Solution2:
    def closedIsland(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def fill(i, j):
            if grid[i][j] != 0:
                return
            grid[i][j] = 1
            stack = [(i, j)]
            while stack:
                x, y = stack.pop()
                for r, c in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                    if 0 <= r < m and 0 <= c < n and grid[r][c] == 0:
                        grid[r][c] = 1
                        stack.append((r, c))

        # Pass 1: sink every island that touches the border
        for i in range(m):
            fill(i, 0)
            fill(i, n - 1)
        for j in range(n):
            fill(0, j)
            fill(m - 1, j)

        # Pass 2: every remaining island is closed
        count = 0
        for i in range(1, m - 1):
            for j in range(1, n - 1):
                if grid[i][j] == 0:
                    count += 1
                    fill(i, j)
        return count