class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res= cursum=0
        prefixsum = {0:1}

        for num in nums:
            cursum+=num
            diff=cursum-k

            if diff in prefixsum:
                res+=prefixsum[diff]
            prefixsum[cursum]=1+prefixsum.get(cursum,0)
        return res