class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        k=0
        maxk=0
        check=-1

        for i in range(0,len(arr)-1):
            if (arr[i]==arr[i+1]):
                k=0
                check=-1
            
            elif (arr[i]>arr[i+1]): 
                if check == 0:
                    k=1
                else:
                    check=0
                    k+=1
            
            elif (arr[i]<arr[i+1]):
                if check == 1:
                    k=1
                else:
                    check=1
                    k+=1
            
            maxk=max(maxk,k)
        return maxk+1
            
