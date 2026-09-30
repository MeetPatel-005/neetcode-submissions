class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curMax=curMin=0
        globalMax=globalMin=nums[0]
        total=0
        for num in nums:
            curMax=max(curMax,0) + num
            curMin=min(curMin,0) + num
            total+=num
            globalMax= max(globalMax,curMax)
            globalMin= min(globalMin,curMin)
        
        return max(total-globalMin,globalMax) if globalMax>0 else globalMax