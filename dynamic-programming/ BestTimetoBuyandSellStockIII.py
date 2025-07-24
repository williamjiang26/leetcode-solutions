class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # set buys to negative infinity to always buy the first stock no matter how large
        b1 = b2 = float(-inf)

        # set sells to zero to have the option of not taking profit or not buying
        # if its only one stock
        s1 = s2 = 0

        # for each price take the max of buying and selling on first and second transactions
        for p in prices:
            b1 = max(b1, -p)
            s1 = max(s1, b1 + p)
            b2 = max(b2, s1 - p)
            s2 = max(s2, b2 + p)
        

        # return the max of selling at the second transaction. 
        return s2