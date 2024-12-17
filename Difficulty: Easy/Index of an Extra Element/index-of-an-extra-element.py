class Solution:
    def findExtra(self,a,b):
        #add code here
        n=len(b)
        for i in range(0, n):
            if (arr1[i] != arr2[i]) :
                return i
     
        return n


#{ 
 # Driver Code Starts
if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        # Take the first array as input
        arr1 = list(map(int, input().strip().split()))

        # Take the second array as input
        arr2 = list(map(int, input().strip().split()))

        # Create an instance of Solution and call the function
        ob = Solution()
        result = ob.findExtra(arr1, arr2)

        # Print the result
        print(result)

        tc -= 1
        print("~")

# } Driver Code Ends