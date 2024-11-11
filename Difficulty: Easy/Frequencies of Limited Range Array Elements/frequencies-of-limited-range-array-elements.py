class Solution:
    #Function to count the frequency of all elements from 1 to N in the array.
    def frequencyCount(self, arr, N, P):
        #  do modify in the given array
        
        from collections import Counter
        c=Counter(arr)
        
        for i in range(1,len(arr)+1):
            if i in c:
                arr[i-1]=c[i]
            
            else:
                arr[i-1]=0
        




#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
if __name__ == "__main__":
    T = int(input())
    while (T > 0):
        N = int(input())
        arr = [int(x) for x in input().strip().split()]
        P = int(input())
        ob = Solution()
        ob.frequencyCount(arr, N, P)
        for i in arr:
            print(i, end=" ")
        print()
        T -= 1

# } Driver Code Ends