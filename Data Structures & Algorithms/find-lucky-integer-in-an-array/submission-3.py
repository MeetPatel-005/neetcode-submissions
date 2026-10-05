class Solution:
    def findLucky(self, arr: List[int]) -> int:
        cnt = Counter(arr)
        res = -1
        for i,x in cnt.items():
            if i == x and res < x:
                res = i
        return res