# Brute force solution: merge two lists at a time
# Time complexity: O(NK) where N is the total number of nodes in all lists and K is the number of lists. In the worst case, we have to merge K lists, and each merge operation takes O(N) time.
# Space complexity: O(1) since we are merging the lists in place without using any additional data structures.
#  Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        if not lists:
            return None
        head1 = lists[0]
        for i in range(1, len(lists)):
            head2 = lists[i]
            head1 = self.merge2Lists(head1, head2)
        return head1
    def merge2Lists(self, head1: ListNode, head2: ListNode) -> ListNode:
        dummy = ListNode()
        tail = dummy
        while head1 and head2:
            if head1.val < head2.val:
                tail.next = head1
                tail = tail.next
                head1 = head1.next
            else:
                tail.next = head2
                tail = tail.next
                head2 = head2.next
        if head1:
            tail.next = head1
        elif head2:
            tail.next = head2
        return dummy.next

# Divide and Conquer solution: merge lists in pairs

class Solution1:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        if not lists:
            return None
        step = 1
        while step < len(lists):
            for i in range(0, len(lists) - step, step * 2):
                lists[i] = self.merge2Lists(lists[i], lists[i + step])
            step *= 2
        return lists[0]
    def merge2Lists(self, head1: ListNode, head2: ListNode) -> ListNode:
        dummy = ListNode()
        tail = dummy
        while head1 and head2:
            if head1.val < head2.val:
                tail.next = head1
                tail = tail.next
                head1 = head1.next
            else:
                tail.next = head2
                tail = tail.next
                head2 = head2.next
        if head1:
            tail.next = head1
        elif head2:
            tail.next = head2
        return dummy.next

# heap solution: using min heap to store the smallest element of each list
import heapq
class Solution3:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        if not lists:
            return None
        heap = []
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))
        dummy = ListNode()
        tail = dummy
        while heap:
            _, node, i = heapq.heappop(heap)
            tail.next = node
            tail = tail.next
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next ))
        return dummy.next