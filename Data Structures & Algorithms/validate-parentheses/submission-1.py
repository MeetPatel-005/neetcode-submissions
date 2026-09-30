class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        closepair={')':'(','}':'{',']':'['}
        for ch in s:
            if ch in closepair:
                if stack and stack[-1]==closepair[ch]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)
        return True if not stack else False
