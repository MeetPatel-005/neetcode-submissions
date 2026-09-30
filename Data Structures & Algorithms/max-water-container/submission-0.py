class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r= 0, len(heights)-1
        maxArea=0
        curArea=0
        while l<r:
            breadth=r-l
            curArea= min(heights[l],heights[r]) * breadth
            maxArea=max(maxArea,curArea)

            if heights[l]>heights[r]:
                r-=1
            else: l+=1
        return maxArea
