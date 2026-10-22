# Time complexity: O(N * 2^N) where N is the length of the string. In the worst case, we may have to explore all possible partitions of the string.
# Space complexity: O(N) where N is the length of the string. In the worst case, we may have to store the entire string in the path list.
class Solution:
    def partition(self, s: str) -> list[list[str]]:
        result = []
        path = []


        def dfs(start):
            if start == len(s):
                result.append(path.copy())
                return
            for end in range(start, len(s)):
                piece = s[start:end+1]
                if self.isPal(piece):
                    path.append(piece)
                    dfs(end+1)
                    path.pop()
        dfs(0)
        return result

    def isPal(self, t: str) -> bool:
        l = 0
        r = len(t) -1
        while l <= r:
            if t[l] != t[r]:
                return False
            l += 1
            r-=1
        return True
    
#time complexity: O(N * 2^N) where N is the length of the string. In the worst case, we may have to explore all possible partitions of the string.
#space complexity: O(N^2) where N is the length of the string. In the worst case, we may have to store the entire string in the path list and the isPal table.
class OptimizationSolution:
    def partition(self, s: str) -> list[list[str]]:
        n = len(s)
        result = []
        path = []
        isPal =  [[False] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i < 2 or isPal[i + 1][j - 1]):
                    isPal[i][j] = True
        def dfs(start):
            if start == len(s):
                result.append(path.copy())
                return
            for end in range(start, len(s)):
                piece = s[start:end+1]
                if isPal[start][end]:
                    path.append(piece)
                    dfs(end+1)
                    path.pop()
        dfs(0)
        return result