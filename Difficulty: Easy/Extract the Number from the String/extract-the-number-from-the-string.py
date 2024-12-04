class Solution:
    def ExtractNumber(self,sentence):
        #code here
        words = sentence.split()
    
        # Extract numbers that do not contain the digit '9'
        valid_numbers = [int(word) for word in words if word.isdigit() and '9' not in word]
        
        # Return the largest valid number or -1 if no such number exists
        return max(valid_numbers) if valid_numbers else -1

#{ 
 # Driver Code Starts
t = int(input())
for _ in range(t):
    S = input()
    ob = Solution()
    ans = ob.ExtractNumber(S)
    print(ans)
    print("~")

# } Driver Code Ends