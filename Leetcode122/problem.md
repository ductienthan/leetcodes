122. Best Time to Buy and Sell Stock II

You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can sell and buy the stock multiple times on the same day, ensuring you never hold more than one share of the stock.

Find and return the maximum profit you can achieve.

Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.

analysis

this is accumulation problem where we will need to sum all of profit to get max profit

Questions:

1. When do we need to sell and buy? - Idealy, we alway buy at the mimum and sell at maximum. In example,
   if we buy at day 1, we pay 7, On the next day, if the price is decrease that mean, we should buy at that day instead of previous one. the buy now is 1,
   stock = 1
   day 3, the price is 5

if we sell it now, profit will be 4
buy_stock now is 5,
next day the price is 3, price down, we should not buy from previous, we should buy not the current sotck is 3
next dat price is 6, if we sell now, the profit will be 3 + 4
next dat price is 4, price down so we sell the previous one 2. How could we consider the profit is max or not? the profit is max when we buy and sell with sum which is max 3. how do we know when we actually sell? when
