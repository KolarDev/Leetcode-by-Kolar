class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        first = float('inf')
        second = float('inf')
        
        for n in nums:
            if n <= first:
                # We found a new smallest number
                first = n
            elif n <= second:
                # We found something bigger than 'first' 
                # but smaller than our previous 'second'
                second = n
            else:
                # If we find something bigger than 'second', 
                # we have found our triplet! (first < second < n)
                return True
                
        return False