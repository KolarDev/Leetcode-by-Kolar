class Solution(object):
    def zeroFilledSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        streak_count = 0
        total_count = 0
        for i in nums:
            if i == 0:
                streak_count += 1
                total_count += streak_count
            else:
                streak_count = 0
        return total_count

        