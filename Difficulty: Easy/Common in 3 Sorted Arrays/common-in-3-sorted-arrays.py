#User function Template for python3

class Solution:
    def commonElements(self, arr1, arr2, arr3):
        #Code Here
        
        a=set(arr1)
        b=set(arr2)
        c=set(arr3)
        
        d=a.intersection(b)
        
        return sorted(d.intersection(c))


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        brr = list(map(int, input().split()))
        crr = list(map(int, input().split()))
        ob = Solution()
        res = ob.commonElements(arr, brr, crr)
        if len(res) == 0:
            print(-1)
        else:
            print(" ".join(map(str, res)))
        print("~")
# } Driver Code Ends