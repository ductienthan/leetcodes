class KthLargest:

  def __init__(self, k: int, nums: list[int]):
    self.minHeap = []
    self.k = k
    for num in nums:
      self.add(num)

  def add(self, val: int) -> int:
    if self.k > len(self.minHeap) or self.minHeap[0] < val:
      heapq.heappush(self.minHeap, val)
      if self.k < len(self.minHeap):
        heapq.heappop(self.minHeap)
    return self.minHeap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
