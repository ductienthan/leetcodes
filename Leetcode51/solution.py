class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        result = []
        queens = []
        cols = set()
        diag = set()
        anti_diag = set()
        def backTrack(r):
            if r == n:
                board = []
                for row in range(n):
                    line = ['.']*n
                    line[queens[row]] = 'Q'
                    board.append("".join(line))
                result.append(board.copy())
                return
            for c in range(n):
                if c in cols or (r-c) in diag or (r+c) in anti_diag:
                    continue
                queens.append(c)
                cols.add(c)
                diag.add(r-c)
                anti_diag.add(r+c)
                backTrack(r+1)

                queens.pop()
                cols.remove(c)
                diag.remove(r-c)
                anti_diag.remove(r+c)
        backTrack(0)
        return result