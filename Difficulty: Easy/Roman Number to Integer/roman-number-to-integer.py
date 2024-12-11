#User function Template for python3

class Solution:
    def romanToDecimal(self, s): 
        # code here
        
        r = {'I':1,'V':5, 'X':10, 'L':50, 'C':100,'D':500,'M':1000}
        integer = 0
        pre = s[-1]
        for i in range(len(s)-1,-1,-1):
            if r[s[i]] < r[pre]:
                integer -=r[s[i]]
            else:
                integer +=r[s[i]]
            pre = s[i]
        return integer


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        ob = Solution()
        S = input()
        print(ob.romanToDecimal(S))
        print("~")

# } Driver Code Ends