class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        seen = set()
        hashmap = {}

        for x,y in zip(s,t):
            if x in hashmap:
                if hashmap[x] != y:
                    return False
            elif y not in seen:
                hashmap[x] = y
                seen.add(y)
            else:
                return False
        
        return True