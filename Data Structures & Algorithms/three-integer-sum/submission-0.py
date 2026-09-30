class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        for i,num in enumerate(nums):
            if num > 0:
                break

            if i > 0 and num == nums[i - 1]:
                continue
            check=-num
            j=i+1
            k=len(nums)-1
            while j<k:
                if nums[j] + nums[k] == check:
                    res.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1
                    while nums[j] == nums[j - 1] and j < k:
                        j += 1
                elif nums[j] + nums[k] > check:
                    k-=1
                elif nums[j] + nums[k] < check:
                    j+=1
        return res