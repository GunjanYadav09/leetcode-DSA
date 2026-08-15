class Solution(object):
    def checkInclusion(self, s1, s2):
        if len(s1) > len(s2):
            return False

        freq1 = {}

        for ch in s1:
            if ch in freq1:
                freq1[ch] += 1
            else:
                freq1[ch] = 1
        window_freq = {}

        for right in range(len(s2)):
            window_freq[s2[right]] = window_freq.get(s2[right], 0) + 1

            if right >= len(s1):
                left_char = s2[right - len(s1)]
                window_freq[left_char] -= 1
                    
                if window_freq[left_char] == 0:
                    del window_freq[left_char]

            if window_freq == freq1:
                return True
        return False
        