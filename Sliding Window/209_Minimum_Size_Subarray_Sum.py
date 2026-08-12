class Solution(object):
    def minSubArrayLen(self, target, nums):
       left = 0
       window_sum = 0
       min_len = float('inf')

       for right in range(len(nums)):
        window_sum += nums[right]
        while window_sum >= target:
            current_len = right - left + 1

            if current_len < min_len:
                min_len = current_len
            window_sum -= nums[left]
            left += 1
       if min_len == float('inf'):
        return 0
       return min_len

        
        