# PROBLEM -> https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
# DIFFICULTY: EASY
# TYPE: STRINGS

class Solution:
    # noinspection PyMethodMayBeStatic
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)

    # wersja bez użycia wbudowanej funkcji .find
    # noinspection PyMethodMayBeStatic
    def strStr2(self, haystack: str, needle: str) -> int:
        haystack_len = len(haystack)
        needle_len = len(needle)
        if haystack_len < needle_len:
            return -1
        i = 0
        while i < haystack_len:
            l = i + needle_len
            if l > haystack_len:
                return -1
            if haystack[i:l] == needle:
                return i
            i += 1
        return -1








s = Solution()
print(s.strStr2("sadbutsad", "sad"))
print(s.strStr2("sadbutsad", "but"))
print(s.strStr2("sadbutsad", "sadbutsad"))
print(s.strStr2("aaa", "aaaaa"))
print(s.strStr2("mississippi", "issip"))