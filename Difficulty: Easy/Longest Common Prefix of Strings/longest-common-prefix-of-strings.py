#User function Template for python3

class Solution:
    def longestCommonPrefix(self, arr):
        # code here
        l=len(arr[0])
        lenght=0
        if len(arr)==1:
            return arr[0]
        for i in range(1,len(arr)):
            length=min(l,len(arr[i]))
            while length>0 and arr[0][0:length]!=arr[i][0:length]:
                length-=1
                if length==0:
                    return -1
        
        return arr[0][0:length]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        arr = [x for x in input().strip().split(" ")]

        ob = Solution()
        print(ob.longestCommonPrefix(arr))

# } Driver Code Ends