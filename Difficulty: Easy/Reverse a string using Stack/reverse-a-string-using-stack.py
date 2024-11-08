#{ 
 # Driver Code Starts

# } Driver Code Ends
def reverse(S):
    
    stack=[]
    S=list(S)
    for i in range(len(S)):
        c=S.pop(-1)
        stack.append(c)
        
    
    return ''.join(stack)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    #Add code here

#{ 
 # Driver Code Starts.
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        str1=input()
        print(reverse(str1))
        print("~")
# } Driver Code Ends