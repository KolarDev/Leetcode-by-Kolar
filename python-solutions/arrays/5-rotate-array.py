class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # Slower way
        # while k > 0:
        #     nums.insert(0, nums.pop())
        #     k -= 1

        # This does the same thing instantly
        k = k % len(nums) # Handle cases where k is larger than the list
        nums[:] = nums[-k:] + nums[:-k]
                    
                