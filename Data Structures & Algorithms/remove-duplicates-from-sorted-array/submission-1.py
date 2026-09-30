class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l=1
        for x in range(1,len(nums)):
            if nums[x] !=nums[x-1]:
                nums[l] = nums[x]
                l+=1
        return l