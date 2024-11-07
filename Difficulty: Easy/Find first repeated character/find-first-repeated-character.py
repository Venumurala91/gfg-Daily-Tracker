#User function Template for python3

class Solution:

    def firstRepChar(self, s):
        
        c=""
        d=False
        for i in s:
            if i not in c:
                c+=i
            else:
                d=True
                break
        
        if d:
            return i
        
        return "-1"
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s = input()

        solObj = Solution()

        print(solObj.firstRepChar(s))
# } Driver Code Ends