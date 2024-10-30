#User function Template for python3
class Solution:
	def countPairsWithDiffK(self,arr, k):
	    
	    
	    counts = {}
        for number in arr:
            if number in counts:
                counts[number] += 1
            else:
                counts[number] = 1
            
    # Step 2: Count pairs with the specified difference k
        pair_count = 0
        for number in counts:
            # Check if (number + k) exists in the counts
            if (number + k) in counts:
                pair_count += counts[number] * counts[number + k]
        
        return pair_count
    	            
	    
	    
	    
    	        
    	
    	




#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        k = int(input().strip())
        ob = Solution()
        ans = ob.countPairsWithDiffK(arr, k)
        print(ans)
        print("~")
        tc -= 1

# } Driver Code Ends