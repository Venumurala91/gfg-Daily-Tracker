
class Solution:
    def encode(self, s : str) -> str:
        # code here
        
        
        c=1
        combined_string=" "
        for i in range(len(s)-1):
            if s[i]==s[i+1]:
                c+=1
                
            else:
                combined_string+=s[i]
                combined_string+=str(c)
                c=1
                
                
        
        
        
        if c!=1:
            combined_string+=s[i]
            combined_string+=str(c)
        else:
            if i<len(s):
                combined_string+=s[i+1]
                combined_string+=str(c)
            
        
        
        return combined_string
        



#{ 
 # Driver Code Starts

if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        s = (input())
        
        obj = Solution()
        res = obj.encode(s)
        
        print(res)
        

        print("~")
# } Driver Code Ends