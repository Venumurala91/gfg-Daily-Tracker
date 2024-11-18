#User function Template for python3

class Solution:
    #Function to rotate an array by d elements in counter-clockwise direction. 
    def rotateArr(self, arr, d):
        #Your code here
        
        
        n = len(arr)

        # Handle case when d > n
        d %= n
        
        # Storing rotated version of array
        temp = [0] * n
    
        # Copy last n - d elements to the front of temp
        for i in range(n - d):
            temp[i] = arr[d + i]
    
        # Copy the first d elements to the back of temp
        for i in range(d):
            temp[n - d + i] = arr[i]
    
        # Copying the elements of temp in arr
        # to get the final rotated array
        for i in range(n):
            arr[i] = temp[i]
                















#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    T = int(input())

    while (T > 0):
        A = [int(x) for x in input().strip().split()]
        nd = [int(x) for x in input().strip().split()]
        D = nd[0]
        ob = Solution()
        ob.rotateArr(A, D)

        for i in A:
            print(i, end=" ")

        print()

        T -= 1

        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends