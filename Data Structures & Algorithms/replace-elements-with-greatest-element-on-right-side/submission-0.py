class Solution:
    def replaceElements(self, nums: List[int]) -> List[int]:
        for x in range(len(nums)):
            max_i = 0
            for y in range(x+1,len(nums)):
                max_i = max(max_i,nums[y])
                nums[x] = max_i
        nums[-1] = -1
        return nums