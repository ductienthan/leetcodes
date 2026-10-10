from typing import List
# DFS
class DFSSolution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])

        def dfs(r: int, c: int) -> None:
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != '1':
                return
            grid[r][c] = '0'  # mark visited by sinking the land
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    count += 1
                    dfs(r, c)
        return count
    
class BFSSolution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        count = 0

        def bfs(r: int, c: int) -> None:
            queue = [(r, c)]
            grid[r][c] = '0'  # mark visited by sinking the land
            while queue:
                row, col = queue.pop(0)
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    newRow, newCol = row + dr, col + dc
                    if 0 <= newRow < rows and 0 <= newCol < cols and grid[newRow][newCol] == '1':
                        grid[newRow][newCol] = '0'  
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    count += 1
                    bfs(r, c)
        return count