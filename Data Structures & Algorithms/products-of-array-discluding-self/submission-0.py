class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[0]*len(nums)
        prefixsum=[0]*len(nums)
        suffixsum=[0]*len(nums)

        prefixsum[0] = suffixsum[-1] = 1

        for i in range(1,len(nums)):
            prefixsum[i] = prefixsum[i-1]*nums[i-1]
        for i in range(len(nums)-2,-1,-1):
            suffixsum[i]= suffixsum[i+1]*nums[i+1]
        for i in range(len(nums)):
            res[i]=prefixsum[i]*suffixsum[i]
        return res