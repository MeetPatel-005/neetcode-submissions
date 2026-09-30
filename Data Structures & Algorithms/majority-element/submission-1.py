class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        hash_map={}
        for x in nums:
            if x in hash_map:
                hash_map[x] += 1
                if hash_map[x] >= (len(nums)/2):
                    return x
            else:
                hash_map[x] = 1
