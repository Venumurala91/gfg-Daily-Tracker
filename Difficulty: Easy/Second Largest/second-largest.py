#User function Template for python3
class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        c=max(arr)
        m=-1
        for i in arr:
            if i!=c and i>m:
                m=i
        
        
        
        if m<0:
            return "-1"
        
        return m
            


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
        print("~")
# } Driver Code Ends