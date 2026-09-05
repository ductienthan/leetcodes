Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Example:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Analysis:
Just one loop, and each iteration does this in order:
Compare height[left] vs height[right] → decide which side to work on.
On that side only, compare the current bar to that side's running max → decide if it's a new wall or if it traps water.
Move that pointer.

That's it. There is no separate step where you compare leftMax to rightMax directly — comparing height[left] to height[right] in step 1 already tells you the same thing (whichever is smaller has the smaller max behind it too, since you always update the max as you go).

Let's trace it on real numbers

height = [0,1,0,2,1,0,1,3,2,1,2,1]

Start: left = 0, right = 11, leftMax = 0, rightMax = 0, water = 0

Step 1:
height[left]=0 vs height[right]=1 → left is smaller → work on left.
Is height[left]=0 a new max? Compare to leftMax=0 → yes, 0 >= 0 → update leftMax = 0. No water. Move left to 1.

Step 2:
height[left]=1 vs height[right]=1 → equal → work on left (pick either, doesn't matter).
Is height[left]=1 a new max? Compare to leftMax=0 → yes, 1 >= 0 → update leftMax = 1. No water. Move left to 2.

Step 3:
height[left]=0 vs height[right]=1 → left smaller → work on left.
Is height[left]=0 a new max? Compare to leftMax=1 → no, 0 < 1 → water trapped! water += 1 - 0 = 1. Move left to 3.

Step 4:
height[left]=2 vs height[right]=1 → right is now smaller → work on right this time.
Is height[right]=1 a new max? Compare to rightMax=0 → yes → update rightMax = 1. No water. Move right to 10.

...and so on.

The two comparisons, plainly
"Which side do I work on?" → compare height[left] to height[right]. Do this every single iteration, first.
"Does water get trapped here?" → compare the bar you just picked to that side's own max (leftMax if you picked left, rightMax if you picked right). Do this second, only for the side you picked.

You never compare leftMax to rightMax directly — comparing height[left] to height[right] does that job for you automatically.

Why do we need 2 pointer? we need both side wall to make sure we could contain the water
how the water is trapped? we should have some space between 2 walls
when do we need to move pointer? move the shorter one, so we could check how much we could store for that space. if the current validting point has same height then we do not have any space to contain water

Question 1: In Container With Most Water, you compute one area using only the two pointer positions.
In this problem — how many "containers" of water are there? what is containers meaning here. Container is the gap between left max, left, right, and right max.
Is it one final answer computed from left and right directly, or something computed at every bar along the way? Need to compare the bar with previous maximum left and right height

Question 2: Water trapped at a specific bar — what actually determines how much water sits there? Need a gap between current bar and the left and right bar
Is it the distance between your current left and right pointers, or is it something about the walls to that bar's left and right specifically? the water is the subtraction of current bar with min of left and right bar

Question 3: Consider the bar at index 5 (height 0) in the example. What's the tallest wall to its left? What's the tallest wall to its right? Now — is the water above index 5 limited by the shorter wall or the taller wall of those two? Why? same as above

Question 4: Look at index 3 (height 2) and index 7 (height 3) in the example — they're not equal, so let's instead ask: what happens when height[left] == height[right]? Does that mean zero water can be trapped anywhere, or does it just tell you something about which pointer is safe to move next? the water should be stored by the index 3, and we should be index 7 because the water is always trapped in smaller one. If heights are same, then check the next one which is taller then move that.

Question 5: As your pointers move inward, do you need to know the height of a wall you've already passed?
For example, once you've moved past the bar of height 2 at index 3, do you still need that information later, or can you forget it? Yes we need to keep the max index of 2. so we could know if there is the higher one, to see how much we could store water from current point to previous max

Q6: If leftMax < rightMax, can you say for certain what the water level is at the current left pointer's position, even without knowing the exact tallest wall on the right eventually? Why or why not? we should move the leftmax, because if there is higher left, then we could not sure we could store water between current left position to the previous left max
Q7 (rephrase): Given that, when do you "resolve"/finalize the water at the current left pointer vs. current right pointer? What's the rule — and does it match a rule you already used in Container With Most Water? Comparing the leftMax and rightMax, to see which is smaller then finalize the water with that pointer. If leftmax < rightmax, then water increase by subtraction of the leftmax and left pointer and move left pointer

Question 4 was specifically about height[left] == height[right] — what does that specific case tell you? it does not matter, we need to validate by the leftmax and rightmax
