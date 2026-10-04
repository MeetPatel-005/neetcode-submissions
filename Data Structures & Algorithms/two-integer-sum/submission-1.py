class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_ = {}
        for x in range(len(nums)):
            diff = target - nums[x]
            print(diff)
            if diff in hash_:
                return [hash_[diff], x]
            hash_[nums[x]] = x
            