class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        result = [[]]
        def backTrack(idx: int, currSet: list[int]):
            while idx < len(nums):
                currSet.append(nums[idx])
                result.append(currSet.copy())
                backTrack(idx+1, currSet)
                currSet.pop()
                idx+=1
        backTrack(0, [])
        return result
# Time Complexisty: O(n*2^n) where n is the length of nums. The number of subsets is 2^n and for each subset, we may take O(n) time to copy it to the result list.