class Solution(object):
    def findNumbers(self, nums):
        count = 0

        for n in nums:
            digits = len(str(n))

            if digits % 2 == 0:
                count += 1
        return count