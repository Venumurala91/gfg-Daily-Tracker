#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def modifyAndRearrangeArr (self, arr) : 
        #Complete the function
        
        a=[0]*len(arr)
        j=0
        for i in range(len(arr)-1):
            if arr[i]==arr[i+1]:
                arr[i]=arr[i]+arr[i]
                arr[i+1]=0
        
        for i in range(len(arr)):
            if arr[i]!=0:
                a[j]=arr[i]
                j+=1
        
       
        return a


#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.modifyAndRearrangeArr(arr)
        print(*ans)
        t -= 1


# } Driver Code Ends