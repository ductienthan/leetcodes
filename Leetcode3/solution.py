class Solution:
    from collections import defaultdict
    def lengthOfLongestSubstring(self, s: str) -> int:
        slow, fast = 0, 0
        occurances = {}
        maxLen = 0
        while fast < len(s):
            if s[fast] in occurances and occurances[s[fast]] >= slow:
                slow = occurances[s[fast]] + 1
            maxLen = max(maxLen, fast-slow+1)
            occurances[s[fast]] = fast
            fast += 1
        return maxLen
            