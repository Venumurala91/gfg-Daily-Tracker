#User function Template for python3
class Solution:
	def printString(self, a, ch, count):
		c=0
		s=""
		
		if ch not in a:
		    return ""
		    
		for i in a:
		    if c==count:
		        s+=i
		 
		    else:
		        if i==ch:
		            c+=1
		    
# 		print(c)
		return s


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        s = input()
        ch = input()[0]
        count = int(input())
        ob = Solution()
        answer = ob.printString(s, ch, count)

        print(answer)
        print("~")

# } Driver Code Ends