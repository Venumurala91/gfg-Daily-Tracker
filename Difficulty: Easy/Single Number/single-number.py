#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    
    
    def getSingle(self,arr):
        from collections import Counter
        c=Counter(arr)
        
        for key,value in c.items():
            if value % 2 !=0:
                return key
                
                
        
        

#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        # k= int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.getSingle(arr)
        print(res)
        t -= 1


# } Driver Code Ends