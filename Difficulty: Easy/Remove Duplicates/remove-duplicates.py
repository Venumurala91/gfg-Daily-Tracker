#User function Template for python3
class Solution:
	def removeDups(self, str):
		
		c=""
		for i in str:
		    if i not in c:
		        c+=i
		
		return c
    

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        s = input()

        ob = Solution()
        answer = ob.removeDups(s)

        print(answer)

# } Driver Code Ends