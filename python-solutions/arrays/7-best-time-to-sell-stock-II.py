class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_p = 0
    
        for i in range(1, len(prices)):
            # If the price increased from yesterday, take the profit
            if prices[i] > prices[i-1]:
                max_p += prices[i] - prices[i-1]
                
        return max_p