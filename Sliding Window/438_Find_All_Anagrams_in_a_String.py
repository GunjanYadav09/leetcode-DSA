class Solution(object):
    def findAnagrams(self, s, p):
        
        if len(p) > len(s):
            return []
        freq_p = {}
        for ch in p:
            freq_p[ch] = freq_p.get(ch, 0) + 1
        window_freq = {}
        result = []
        for right in range(len(s)):
            window_freq[s[right]] = window_freq.get(s[right], 0) + 1
            
            if right >= len(p):
                left_char = s[right - len(p)]
                window_freq[left_char] -= 1

                if window_freq[left_char]==0:
                    del window_freq[left_char]

            if window_freq==freq_p:
                left = right - len(p) + 1
                result.append(left)
        return result