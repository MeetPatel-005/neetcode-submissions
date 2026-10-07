class Solution:
    def maxScore(self, s: str) -> int:
        l_sum = 0
        r_sum = s.count('1')
        max_i = -1
        for i in range(1,len(s)):
            if s[i-1] == '0':
                l_sum += 1
            else:
                r_sum -= 1
            max_i = max(l_sum + r_sum , max_i)
        return max_i