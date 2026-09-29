23. Merge k Sorted Lists

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
1->4->5,
1->3->4,
2->6
]
merging them into one sorted linked list:
1->1->2->3->4->4->5->6

easiest way is merge 2 linked list at once

merge 2 lists
for each node in list
time: O(n\*m); n is length of list, m is number of nodes

space: O(1)
