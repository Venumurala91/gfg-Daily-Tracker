#User function Template for python3


class Solution:
    
    #Function is to check whether two strings are anagram of each other or not.
    def isAnagram(self, s1, s2):
        
        if sorted(s1)==sorted(s2):
            return True
        
        
        return False


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        a = input().strip()
        b = input().strip()
        if (Solution().isAnagram(a, b)):
            print("true")
        else:
            print("false")

# } Driver Code Ends