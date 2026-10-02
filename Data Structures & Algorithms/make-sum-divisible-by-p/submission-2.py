class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        remain = sum(nums) % p
        if remain == 0: return 0
        
        res = len(nums)
        cur_rem = 0
        remain_to_id = {0:-1}

        for i,n in enumerate(nums):
            cur_rem = (cur_rem + n) % p
            prefix= (cur_rem - remain + p) % p
            if prefix in remain_to_id:
                length = i - remain_to_id[prefix]
                res = min(res,length)
            remain_to_id[cur_rem] = i

        return -1 if res == len(nums) else res