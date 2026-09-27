class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s = {}
        count_t = {}

        for char in s:
            # what goes here?
            count_s[char] = count_s.get(char,0)+1

        for char in t:
            # what goes here?
            count_t[char] = count_t.get(char,0)+1

        # what single comparison answers the original question?

        return count_s == count_t