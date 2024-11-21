#User function Template for python3

class Solution:
    
    #Function to check if a string is Pangram or not.
    def checkPangram(self,s):
        
        alpha=set()
        c=0
        s.lower()
        
        for i in range(len(s)):
            
            if s[i].isalpha() and s[i] not in alpha:
                alpha.add(s[i].lower())
                c+=1
        
        # print(alpha)
        
        
        if len(alpha)>=26:
            return True
        
        return False
#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        s=str(input())
        obj = Solution()
        if(obj.checkPangram(s)):
            print(1)
        else:
            print(0)
        print("~")
# } Driver Code Ends