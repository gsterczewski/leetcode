# PROBLEM URL: https://leetcode.com/problems/merge-strings-alternately
# DIFFICULTY: EASY
# COLLECTION: LeetCode75

class Solution:
    # noinspection PyMethodMayBeStatic
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len1 = len(word1)
        len2 = len(word2)
        i1 = 0
        i2 = 0
        result = ""
        while i1 < len1:
            if i2 < len2:
                result += word1[i1]
                result += word2[i2]
            else:
                result += word1[i1:len1]
                return result
            i1 += 1
            i2 += 1
        if i2 < len2:
            result += word2[i2:len2]
        return result

s = Solution()
print(s.mergeAlternately("abc","pqr"))
print(s.mergeAlternately("ab","pqrs"))
print(s.mergeAlternately("abcd","pq"))
print(s.mergeAlternately("a","b"))