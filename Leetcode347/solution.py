import heapq
from collections import Counter
#using heapq with frequence time - O(nlogk) and space - O(n)

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        result = []
        frequence = Counter(nums)
        frequence = list(frequence.items())
        result = heapq.nlargest(k, frequence, key=lambda s: s[1])
        result = [r[0] for r in result]
        return result
    
#using Bucket counter - O(n) time and space - O(n)

class Solution2:
    def topKFrequent(self, nums: list[int], k : int) -> list[int]:
        result = []
        frequence = Counter(nums)
        bucket = [[] for _ in range(len(nums) + 1)]
        for key, value in frequence.items():
            bucket[value].append(key)
        for i in range(len(bucket) - 1, -1, -1):
            if bucket[i]:
                result.extend(bucket[i])
            if len(result) >= k:
                break
        return result[:k]
