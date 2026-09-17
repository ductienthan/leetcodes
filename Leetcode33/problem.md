33. Search in Rotated Sorted Array
    There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly left rotated at an unknown index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be left rotated by 3 indices and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Why need to use binary search? Because arrays is sorted but just rotated.

Because the array is rotated, the array will be like the upside down parabola.

For normal binary search, if the target is smaller than middle one, we will move the r to the left. Otherwise, move to the right.

But for the rotated, we dont know which one is the largest value.

Characteristic,
If I take the middle one, how many cases could happen for this value
Hint 1: The array isn't fully sorted, but it's made of two sorted halves. If you pick any midpoint, at least one of the two halves (left of mid, or right of mid) must be sorted normally. Can you figure out how to tell which side is sorted just by comparing nums[left], nums[mid], and nums[right]?

Hint 2: Once you know which half is sorted, you can easily check whether the target lies within that sorted half's range (nums[left] <= target < nums[mid], for example). If it does, search there — otherwise, search the other half.

Hint 3: This is still a binary search — you're just adding a decision step at each iteration to figure out which half to recurse/iterate into, instead of the usual "target > mid go right" logic.

if mid < left:
then right half is sorted because the right part will alway less than left helf in the origin rotating
if the target in the range from mid to right: then left = mid+1, right = right
else:
right -= 1 because target is out of range from mid to right

else: the left part is sorted

if target in range from left to mid, left = left, right = mid -1

else
left += 1 becuase the target
