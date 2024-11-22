class Solution:
    def maximumProfit(self, prices):
        # code here
        
        # m = 0
        # for i in range(len(prices) - 1):  
        #     if (abs(prices[i] - max(prices[i+1:])) > m )and (prices[i]<max(prices[i+1:])):  
        #         m = abs(prices[i] - max(prices[i+1:]))  

        
        # return m

        i = 0 
        mini = prices[0]
        s = 0 
        res = 0 
        for i in range(1,len(prices)):
            if prices[i-1] < prices[i]:
                s = (prices[i] - mini) 
            else:
                res = max(res,s)
                mini = min(mini,prices[i])
            
        res = max(res,s)
        return res


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())  # Read number of test cases
    for _ in range(t):
        # Read input and split it into a list of integers
        prices = list(map(int, input().split()))
        # Create a Solution object and calculate the result
        obj = Solution()
        result = obj.maximumProfit(prices)
        # Print the result
        print(result)

# } Driver Code Ends