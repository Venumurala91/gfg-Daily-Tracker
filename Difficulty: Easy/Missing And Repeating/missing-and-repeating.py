#User function Template for python3

class Solution:
    def findTwoElement( self,arr): 
        # code here
        
        n = len(arr)
        missing = (n * (n + 1)) // 2 
        
    
        for i in range(n):
            if arr[abs(arr[i]) - 1] > 0:
                arr[abs(arr[i]) - 1] = -arr[abs(arr[i]) - 1]
                missing -= abs(arr[i])  # subtract unique elements
            else:
                c=abs(arr[i])
    
        
        return [c,missing]
            

# 6 5 8 7 1 4 1 3 2
# 112345678

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findTwoElement(arr)
        print(str(ans[0]) + " " + str(ans[1]))
        tc = tc - 1
        print("~")

# } Driver Code Ends