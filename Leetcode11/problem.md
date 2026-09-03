https://leetcode.com/problems/container-with-most-water/
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container

Using 2 pointers
What is symbol here we could use the two pointer? The moving is not in same direction. We need to find the maximum area.
Why do we need to use 2 pointer? Because the largest area is l\*w. The maximum area is when l and w are max.

Starting point at both end we will have the largest l.

Why do we need to move? Because we need to check if we could find the largest w. The largest w is min between both y. If the y is greater than (r -l), then y could be new length and possibly the area could be larger.

Time complexity : O(n)
Space Complexity: O(1)
