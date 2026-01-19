class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        n = len(nums)
        res = [1] * n
        
        # Calculate the product of everything to the left of each index
        left_product = 1
        for i in range(n):
            res[i] = left_product
            left_product *= nums[i]
            
        # Calculate product of everything to the right and multiply it in
        right_product = 1
        for i in range(n - 1, -1, -1):
            res[i] *= right_product
            right_product *= nums[i]
            
        return res