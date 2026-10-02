class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        if len(words) != len(pattern): return False
        seen = set()
        hashmap = {}

        for ch,word in zip(pattern,words):
            if ch in hashmap:
                if hashmap[ch] != word:
                    return False
            
            elif word not in seen:
                hashmap[ch] = word
                seen.add(word)
            else:
                return False
        
        return True