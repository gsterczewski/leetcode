# PROBLEM URL -> https://leetcode.com/problems/minimum-time-to-revert-word-to-initial-state-i
# DIFFICULTY: Medium

def minimum_time_to_initial_state(word: str, k: int) -> int:
    left = word
    right = word
    res = 0
    while left != right or res == 0:
        left = left[k:]
        right = right[0:-k]
        res += 1
    return res


print(minimum_time_to_initial_state("abacaba", 4))
print(minimum_time_to_initial_state("abcbabcd", 2))
print(minimum_time_to_initial_state("abacaba", 3))
