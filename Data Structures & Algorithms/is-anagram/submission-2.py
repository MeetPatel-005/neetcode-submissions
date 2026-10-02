class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        freq={}
        freq2={}
        for ch in s:
            freq[ch] = freq.get(ch,0) + 1
        for ch in t:
            freq2[ch] = freq2.get(ch,0) + 1
        
        return freq == freq2