#User function Template for python3

class Solution:
    #Function to return the position of the first repeating element.
    def firstRepeated(self,arr):
        
        #arr : given array
        #n : size of the array
        
        d={}
        m=100000
        c=False
        for i in range(len(arr)):
            if arr[i] not in d:
                d[arr[i]]=i
                
            else:
                if d[arr[i]]<m:
                    c=True
                    m=d[arr[i]]
        
        if c:
            return m+1
        
        return '-1'
        
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):

        arr = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.firstRepeated(arr))
        print("~")

# } Driver Code Ends