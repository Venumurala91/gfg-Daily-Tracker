class Solution:
    def transitionPoint(self, arr): 
        c=False
        
        arr.sort()
        for i in range(len(arr)-1):
            if arr[i]==0 and arr[i+1]==1:
                c=True
                break
                
        
        
        if c:
            return i+1
        
        elif int(1) not in arr:
            return "-1"
        else:
            return "0"
            
                
        


#{ 
 # Driver Code Starts
#driver code
if __name__ == '__main__':
    t = int(input())
    for i in range(t):

        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.transitionPoint(arr))

        print("~")

# } Driver Code Ends