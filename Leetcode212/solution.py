#time complexity: O(M * 4 * 3^(L-1)) where M is the number of cells in the board and L is the maximum length of words.
"""
1. Building the trie: O(S)

Each character of each word is inserted once, with an O(1) dict operation per character. That’s W words × average length, which is exactly S.

2. The DFS: O(M · 4 · 3^(L-1))

This is the dominant part. Break it into three pieces:

Starting cells (M): You can start a search from any cell, so there are up to M searches.
Depth is at most L: The DFS only continues while the current path matches a trie prefix. No word is longer than L, so no path goes deeper than L cells.
Branching factor: From the starting cell you can go in up to 4 directions. After that, one neighbor is the cell you just came from. It’s marked '#', so you can’t revisit it, leaving at most 3 choices per step. Over L levels, that’s 4 · 3^(L-1) paths.

Multiplying: M starts × 4 · 3^(L-1) paths each. Dropping the constant 4/3 gives O(M · 3^L).

3. Why this is a worst case, not a typical case

Two things make real runtime much smaller than the bound:

The trie restricts branching. You only recurse into a neighbor if its letter is in node.children. If the current trie node has 1 child, you explore at most one neighbor, not 3. To really hit 3^L, the board and word list would need to be adversarial, such as a board full of 'a' and words like "aaaaaaaa".
Pruning shrinks the trie as you go. Once a word is found and its branch has no children left, you delete it. Later searches skip that region entirely. The bound ignores this, but it’s why the solution performs well in practice.

4. Comparison with the naive approach

Running a separate Word Search I for each word costs O(W · M · 3^L). The trie replaces the factor W with a shared traversal. Words with common prefixes are searched together instead of repeatedly, which is the whole point of using a trie.

5. Space complexity

Trie: O(S) in the worst case, when no words share prefixes.
Recursion stack: O(L), because depth is at most L.
Output: O(S) at most, since the result can’t hold more characters than the input words.
The visited tracking is O(1) extra space, because you modify the board in place.
"""
#space complexity: O(N) where N is the total number of letters in the words list.
class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        root = TrieNode()
        for w in words:
            node = root
            for ch in w:
                node = node.children.setdefault(ch, TrieNode())
            node.word = w
        result = []
        visited = []
        n = len(board)
        m = len(board[0])
        def dfs(r, c, parent):
            ch = board[r][c]
            node = parent.children[ch]

            if node.word:
                result.append(node.word)
                node.word = None         

            board[r][c] = '#'            
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < m and board[nr][nc] in node.children:
                    dfs(nr, nc, node)
            board[r][c] = ch             

            
            if not node.children and node.word is None:
                del parent.children[ch]
        for i in range(n):
            for j in range(m):
                if board[i][j] in root.children:
                    dfs(i, j, root)
        return result


class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None   # set only at the end of a word