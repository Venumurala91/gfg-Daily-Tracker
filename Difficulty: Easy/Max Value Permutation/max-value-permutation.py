#User function Template for python3

class Solution:
    def maxValue(self, arr): 
        # Complete the function
        
        arr.sort()
        c=1
        summ=0
        for i in range(len(arr)):
            c=arr[i]*i
            summ+=c
        
        
        return summ%1000000007
            
      



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        A = list(map(int, input().strip().split()))
        # k = int(input())
        ob = Solution()
        print(ob.maxValue(A))
        print("~")

# } Driver Code Ends