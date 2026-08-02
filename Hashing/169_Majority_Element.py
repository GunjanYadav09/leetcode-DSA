class Solution(object):
    def majorityElement(self, nums):
        freq = {}
        m = len(nums)
        
        for n in nums:
            if n in freq:
                freq[n] += 1
            else:
                freq[n] = 1

        for n in nums:
            if freq[n] > m/2:
                return n
        