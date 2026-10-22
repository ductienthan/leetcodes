# Time complexity: O(N * 3^L) where N is the number of cells in the board and L is the length of the word. In the worst case, we may have to explore all possible paths in the board for each cell.
# Space complexity: O(L) where L is the length of the word. In the worst case, we may have to store the entire word in the visited list.
class Solution:
    def backtrack(self, board: list[list[str]], row: int, col: int, word: str, visited: list[tuple[int, int]]) -> bool:
        if len(word) == 0:
            return True
        rows = len(board)
        cols = len(board[0])
        for i, j in [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]:
            if 0 <= i < rows and 0 <= j < cols and (i, j) not in visited and board[i][j] == word[0]:
                visited.append((i,j))
                if self.backtrack(board, i, j, word[1:], visited):
                    return True
                visited.pop()
        return False
        
        
    def exist(self, board: list[list[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        board_count = Counter(c for row in board for c in row)
        word_count = Counter(word)
        if any(board_count[c] < n for c, n in word_count.items()):
            return False
        if board_count[word[0]] > board_count[word[-1]]:
            word = word[::-1]
        visited = []
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    visited.append((i,j))
                    if self.backtrack(board, i, j, word[1:], visited):
                        return True
                    visited.pop()
        return False
        