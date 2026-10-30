class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero = one = 0
        for two in range(len(nums)):
            i = nums[two]
            nums[two] = 2
            if i < 2:
                nums[one] = 1
                one += 1
            if i < 1:
                nums[zero] = 0
                zero += 1