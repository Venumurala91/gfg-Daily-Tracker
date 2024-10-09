
from typing import List


class Solution:
    def duplicates(self, n : int, arr : List[int]) -> List[int]:
        d={}
        c=[]
        for i in range(n):
            if arr[i] in d:
                d[arr[i]]+=1
            else:
                d[arr[i]]=1
                
                
        for i,v in d.items():
            if v>1:
                c.append(i)
        
        if len(c)==0:
            return [-1] 

        
        return sorted(c)
                
        
        



#{ 
 # Driver Code Starts
class IntArray:

    def __init__(self) -> None:
        pass

    def Input(self, n):
        arr = [int(i) for i in input().strip().split()]  #array input
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        n = int(input())

        arr = IntArray().Input(n)

        obj = Solution()
        res = obj.duplicates(n, arr)

        IntArray().Print(res)

# } Driver Code Ends