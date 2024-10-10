class Solution:
    # Your task is to Complete this function
    # functtion should return an integer
    def maxDistance(self, arr):
        
                
                
        c={}
        m=0
        for i in range(len(arr)):
            c[arr[i]]=i
            m=max(c[arr[i]],m)
        
        ma=0
        for i in range(len(arr)):
            ma=max(abs(c[arr[i]])-i,ma)
        
        return ma
            
                
            
        
        
        
        

#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        print(ob.maxDistance(arr))

# } Driver Code Ends