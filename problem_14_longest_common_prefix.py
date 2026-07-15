from typing import List


class Solution:

    def find_longest_substring(self, word1: str, word2: str):
        count = 0
        for index in range(min([len(word1), len(word2)])):
            if word1[index] != word2[index]:
                break
            count += 1

        return count

    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""

        if len(strs) == 1:
            return strs[0]

        first_word = strs[0]
        substring_count = []
        # skip over the first word
        for word in strs[1:]:
            substring_count.append(self.find_longest_substring(first_word, word))

        if substring_count:
            max_substring = min(substring_count)
            return first_word[:max_substring]
        return ""
