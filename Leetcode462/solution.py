#Time Complexity: O(NlogN) where N is the number of elements in the array. We sort the array which takes O(NlogN) time and then we iterate through the array to calculate the sum of absolute differences which takes O(N) time.
#Space Complexity: O(1) as we are using constant space.
class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        median = nums[len(nums) //2]
        return sum(abs(x-median) for x in nums)