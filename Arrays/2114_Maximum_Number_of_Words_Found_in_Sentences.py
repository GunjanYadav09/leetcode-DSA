class Solution(object):
    def mostWordsFound(self, sentences):
        max_words = 0

        for words in sentences:
            s_words = words.split()
            total_words = len(s_words)

            if total_words > max_words:
                max_words = total_words

        return max_words