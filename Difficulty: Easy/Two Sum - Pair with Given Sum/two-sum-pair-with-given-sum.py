#User function Template for python3
class Solution:
	def twoSum(self, arr, target):
		# code here
		arr.sort()

        left, right = 0, len(arr) - 1
    
        # Iterate while left pointer is less than right
        while left < right:
            sum = arr[left] + arr[right]
    
            # Check if the sum matches the target
            if sum == target:
                return True
            elif sum < target: 
                left += 1  # Move left pointer to the right
            else:
                right -= 1 # Move right pointer to the left
    
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