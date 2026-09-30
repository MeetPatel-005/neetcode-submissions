class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 0:
            return 0
        
        leftMax = [0]*len(height)
        rightMax = [0]*len(height) 
        
        leftMax[0]=height[0] 
        rightMax[len(height) - 1]= height[len(height) - 1]

        for x in range(1, len(height)):
            leftMax[x]= max(leftMax[x - 1], height[x])
        
        for x in range(len(height)-2,-1,-1):
            rightMax[x]= max(rightMax[x + 1], height[x])
        
        res=0
        for x in range(len(height)):
            res+=min(leftMax[x], rightMax[x]) - height[x]
        
        return res