class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        for x in range(len(nums)-1):
            if (nums[x] - nums[x+1]) % 2 == 0:
                return False 
        return True