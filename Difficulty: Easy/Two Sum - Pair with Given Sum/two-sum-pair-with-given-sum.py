#User function Template for python3
class Solution:
	def twoSum(self,arr, target):
		# code here
		
		s = set()

    # Iterate through each element in the array
        for num in arr:
          
            # Calculate the complement that added to
            # num, equals the target
            complement = target - num
    
            # Check if the complement exists in the set
            if complement in s:
                return True
    
            # Add the current element to the set
            s.add(num)
    
        # If no pair is found
        return False
		    
		    
		    

#{ 
 # Driver Code Starts
#Initial Template for Python 3

#Initial Template for Python 3


def main():
    T = int(input())
    while T > 0:
        x = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.twoSum(arr, x)
        if ans:
            print("true")
        else:
            print("false")
        T -= 1
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends