#User function template for Python 3

class Solution:
    def majorityElement(self, arr):
        #Your code here
        
        
        
        from collections import Counter
        
        c=Counter(arr)
        
        for key,value in c.items():
            if value > len(arr)//2:
                return key
                
        
        return "-1"


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

from sys import stdin


def main():
    T = int(input())
    while (T > 0):

        A = [int(x) for x in input().strip().split()]

        obj = Solution()
        print(obj.majorityElement(A))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends