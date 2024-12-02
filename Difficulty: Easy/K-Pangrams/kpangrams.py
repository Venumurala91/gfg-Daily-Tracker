#User function Template for python3
class Solution:
    def kPangram(self,s, k):
        
        characts= [c for c in s if c.isalpha()]  
        return 26-len(set(characts))<=k and len(characts)>=26
        
        
        
   
    
    
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())

    for tcs in range(T):
        string = input()
        K = int(input())
        ob = Solution()
        a = ob.kPangram(string, K)
        if a:
            print("true")
        else:
            print("false")
        print("~")
# } Driver Code Ends