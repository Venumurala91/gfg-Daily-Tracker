#User function template for Python

class Solution:
    def binarysearch(self, arr, k):
        
        l=0
        m=len(arr)-1
        mid=0
        
        if k not in arr:
            return "-1"
        while l<=m:
            mid=(l+m)//2
            
            if arr[mid]>k:
                m=mid-1
            
            elif arr[mid]<k:
                l = mid+1
            else:
                return mid
                
        return "-1"
                



#{ 
 # Driver Code Starts
#Initial template for Python

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        k = int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.binarysearch(arr, k)
        print(res)
        print("~")

# } Driver Code Ends