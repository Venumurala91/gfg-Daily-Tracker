 #User function Template for python3
 
class Solution:
    
    # arr[] : the input array
    
    #Function to return length of longest subsequence of consecutive integers.
    def longestConsecutive(self,arr):
        #code here
        # Sort the array
        arr.sort()
    
        res = 1
        cnt = 1
    
        # Find the maximum length by traversing the array
        for i in range(1, len(arr)):
            
            # Skip duplicates
            if arr[i] == arr[i - 1]:
                continue
    
            # Check if the current element is equal
            # to previous element + 1
            if arr[i] == arr[i - 1] + 1:
                cnt += 1
            else:
                # Reset the count
                cnt = 1
    
            # Update the result
            res = max(res, cnt)
    
        return res

                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    t = int(input())
    for tt in range(t):
        a = list(map(int, input().strip().split()))
        print(Solution().longestConsecutive(a))
        print("~")
# } Driver Code Ends