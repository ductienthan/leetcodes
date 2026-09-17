153. Find Minimum in Rotated Sorted Array
     Hint
     Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:
     [4,5,6,7,0,1,2] if it was rotated 4 times.
     [0,1,2,4,5,6,7] if it was rotated 7 times.
     Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.

Input: nums = [5,6,7,1,2,3,4]
Output: 1

Hint 1 — What does binary search need?
Binary search needs a way to decide, from looking at nums[mid], whether the answer is in the left half or right half. Think about: how can you tell if the array segment nums[lo..hi] is "fully sorted" (no rotation point inside it) just by comparing nums[lo] and nums[hi]?

the half is sirted meaning that nums[lo] < nums[hi]

if nums[mid] > nums[lo], meaning that [nums[lo], nums[mid]] is sorted then hi = mid -1

else mean that the [nums[mid], nums[hi]] is sorted then hi = mid-1

Hint 2 — Comparing mid to an edge
Instead of comparing nums[lo] vs nums[hi] directly, compare nums[mid] vs nums[hi]:

If nums[mid] > nums[hi], what does that tell you about where the rotation point (and thus the minimum) is — left half or right half of mid? min in right part
If nums[mid] < nums[hi], what does that tell you instead? min is in the left half or mid

Work out both cases on paper with [4,5,6,7,0,1,2] — pick a mid and see which case you're in.

Hint 3 — Narrowing the search
Once you know which side the minimum is on:

If nums[mid] > nums[hi], the minimum can't be at mid or anything before it that's still "high" — the minimum must be to the right of mid, so lo = mid + 1.
If nums[mid] <= nums[hi], the minimum could be mid itself (don't rule it out) — so hi = mid, not mid - 1.
