class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        slow, fast = 0, 0
        profit = 0
        prev_profit = 0
        while fast < len(prices):
            if prices[slow] > prices[fast]:
                slow = fast
                fast += 1
                profit += prev_profit
                prev_profit = 0
            else:
                if prev_profit <= (prices[fast] - prices[slow]):
                    prev_profit = prices[fast] - prices[slow]
                    fast += 1
                else:
                    profit += prev_profit
                    prev_profit = 0
                    slow = fast
                    fast +=1
        return profit + prev_profit