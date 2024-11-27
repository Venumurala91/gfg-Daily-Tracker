from typing import List


class Solution:
    def convertToWave(self, arr : List[int]) -> None:
        # code here
        
        for i in range(0,len(arr)-1,2):
            arr[i],arr[i+1]=arr[i+1],arr[i]
            


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

        arr = list(map(int, input().strip().split()))

        obj = Solution()
        obj.convertToWave(arr)
        IntArray().Print(arr)
        print("~")

# } Driver Code Ends