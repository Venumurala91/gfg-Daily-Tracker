#{ 
 # Driver Code Starts

# } Driver Code Ends
class Solution:
    def rearrange(self, arr):
        #Code here
        
        c=0
        for i in range(len(arr)):
            if arr[i]!=-1:
                arr[arr[i]],arr[i]=arr[i],arr[arr[i]]
          
                
        for i in range(len(arr)):
            if arr[i]==-1:
                c+=1
        
        
        if 0 not in arr and c==1:
            return sorted(arr)
        
        return arr
                
                
                

#{ 
 # Driver Code Starts.
def main():
    t = int(input())
    for _ in range(t):
        input_str = input()
        arr = list(map(int, input_str.split()))
        solution = Solution()
        ans = solution.rearrange(arr)
        print(" ".join(map(str, ans)))

if __name__ == "__main__":
    main()
# } Driver Code Ends