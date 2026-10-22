class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        self.result = []
        self.n = n
        self.current = []
        self.dfs(0,0)
        return self.result
    def dfs(self, opens: int, closes: int):
        if closes > opens or opens > self.n:
            return
        if opens == closes == self.n:
            self.result.append("".join(self.current))
            return
        self.current.append("(")
        self.dfs(opens+1, closes)
        self.current.pop()

        self.current.append(")")
        self.dfs(opens, closes+1)
        self.current.pop()