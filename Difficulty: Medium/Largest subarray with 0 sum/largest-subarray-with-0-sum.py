#Your task is to complete this function
 
class Solution:
    def maxLen(self, arr):
        # code here
        
        presum = {}

        sum = 0
        max_len = 0
    
        # Traverse through the given array
        for i in range(len(arr)):
          
            # Add current element to sum
            sum += arr[i]
    
            # If the sum is 0, update max_len
            if sum == 0:
                max_len = i + 1
    
            # Check if this sum is seen before
            if sum in presum:
                # If this sum is seen before, update max_len
                max_len = max(max_len, i - presum[sum])
            else:
              
                # If this sum is not seen before, add it to the map
                presum[sum] = i
    
        return max_len
            
#{ 
 # Driver Code Starts
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.maxLen(arr))
        print("~")

# } Driver Code Ends