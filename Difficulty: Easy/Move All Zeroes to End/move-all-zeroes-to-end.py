#User function Template for python3

class Solution:
	def pushZerosToEnd(self,arr):
    	
    	count = 0  

        # If the element is non-zero, replace the element at
        # index 'count' with this element and increment count
        for i in range(len(arr)):
            if arr[i] != 0:
                arr[count] = arr[i]
                count += 1
    
        # Now all non-zero elements have been shifted to
        # the front. Make all elements 0 from count to end.
        while count < len(arr):
            arr[count] = 0
            count += 1
    	    
    	    
    	    

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.pushZerosToEnd(arr)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1
# } Driver Code Ends