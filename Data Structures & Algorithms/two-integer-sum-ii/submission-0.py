class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        visited={}

        for i,num in enumerate(numbers):
            diff=target-num
            if diff in visited:
                return [visited[diff],i+1]
            else:
                visited[num]=i+1