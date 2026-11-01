class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        inc = 1
        dec = 1
        prev = nums[0]
        for i in range(1,len(nums)):
            if prev < nums[i]:
                inc = 0
            elif prev > nums[i]:
                dec = 0
            prev = nums[i]
        return bool(inc or dec)