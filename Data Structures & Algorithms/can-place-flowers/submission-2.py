class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        res = 0
        for x in range(len(flowerbed)):
            if flowerbed[x] == 0:
                left = (x == 0 or flowerbed[x-1]==0)
                right = (x == len(flowerbed)-1 or flowerbed[x+1] == 0)

                if left and right:
                    flowerbed[x] = 1
                    res += 1
        return res >= n