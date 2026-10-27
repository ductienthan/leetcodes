# Time Complexity: O(2^n), n is the number of rows in the chessboard. In the worst case, we have to explore all possible placements of queens on the board, which can be represented as a binary tree with 2^n nodes.
# Space Complexity: O(n), where n is the number of rows in the chessboard. The space complexity is determined by the maximum depth of the recursion stack, which can go up to n in the worst case.
class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        result = []
        def backTrack(left, target, current, numUsed):
            if left == 0:
                if  target == 0:
                    result.append(current.copy())
                return
            for i in range(numUsed, 10 - left +1):
                if i > target:
                    break
                current.append(i)
                backTrack(left -1, target - i, current, i+1)
                current.pop()
        backTrack(k, n, [], 1)
        return result
            