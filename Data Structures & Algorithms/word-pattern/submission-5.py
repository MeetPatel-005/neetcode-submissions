class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s= s.split(" ")
        if len(s) != len(pattern):
            return False

        hashmap = {}
        seen = set()
        for x in range(len(pattern)):
            if pattern[x] in hashmap:
                if hashmap[pattern[x]] != s[x]:
                    return False
            elif s[x] not in seen:
                hashmap[pattern[x]] = s[x]
                seen.add(s[x])
            else:
                return False
        return True
        