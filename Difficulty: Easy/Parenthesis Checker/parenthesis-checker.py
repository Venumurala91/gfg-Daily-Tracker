# #User function Template for python3
# ]]}(([}){{]
# ()([]     
               
                
# # ([)]    
# (){}
# {)]}
class Solution:
    
    #Function to check if brackets are balanced or not.
    def ispar(self,x):
        
        
        if len(x)==1:
            return False
        
        stack=[]
        
        for i in x:
            if i in "{([":
                stack.append(i)
            
            elif stack:
                if stack[-1]=="{" and i=="}":
                    stack.pop()
                elif stack[-1]=="[" and i=="]":
                    stack.pop()
                    
                elif stack[-1]=="(" and i==")":
                    stack.pop()
                
                else:
                    stack.append(i)
                
            else:
                return False
        
        # print(stack)
        if not stack:
            return True
        
        else:
            return False
        
        # c=0
        # stack=[]
        # d=[]
        # if len(x)==1:
        #     return False
        
        # for i in x:
        #     if i in "({[":
        #         stack.append(i)
        #         c+=1
            
            
        #     elif i=="}" and stack:
        #         if stack.pop(-1)=="{":
        #             c-=1
            
        #     elif i==")" and stack:
        #         if stack.pop(-1)=="(":
        #             c-=1
            
        #     elif i=="]" and stack:
        #         if stack.pop(-1)=="[":
        #             c-=1
            
        #     else:
        #         d.append(i)
                
            
        
        # if not c and not stack :
        #     return True
        
        
        # return False
            
            
            
            
        
        
        
        
        
        
        




#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

#Contributed by : Nagendra Jha

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        #n = int(input())
        #n,k = map(int,imput().strip().split())
        #a = list(map(int,input().strip().split()))
        s = str(input())
        obj = Solution()
        if obj.ispar(s):
            print("true")
        else:
            print("false")

# } Driver Code Ends