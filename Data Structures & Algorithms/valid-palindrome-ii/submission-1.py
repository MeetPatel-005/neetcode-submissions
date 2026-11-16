class Solution:
    def isPalindrome(self, s:str):
        start = 0
        end = len(s) - 1

        while start < end:
            if s[start] != s[end]:
                return False

            start += 1
            end -= 1

        return True


    def validPalindrome(self, s: str) -> bool:
        if self.isPalindrome(s): return True
        
        for i in range(len(s)):
            if self.isPalindrome(s[0:i] + s[i+1:len(s)]):
                return True
        return False