#User function Template for python3
class Solution:
    def getSecondLargest(self, arr):
        
        arr.sort()
        m=0
        for i in range(len(arr)):
            m=max(arr[i],m)
        
        min=0
        for i in range(len(arr)):
            if arr[i]<m:
                min=arr[i]
        
        if not min:
            return "-1"
        else:
            return min
            


#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.getSecondLargest(arr)
        print(ans)

# } Driver Code Ends