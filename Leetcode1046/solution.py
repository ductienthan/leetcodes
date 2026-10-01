import heapq
class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        negStones = [-s for s in stones]
        heapq.heapify(negStones)
        while len(negStones) > 1:
            largest = -heapq.heappop(negStones)
            secondLargest = -heapq.heappop(negStones)
            if largest != secondLargest:
                heapq.heappush(negStones, -(largest-secondLargest))
        return -heapq.heappop(negStones) if len(negStones) > 0 else 0
        