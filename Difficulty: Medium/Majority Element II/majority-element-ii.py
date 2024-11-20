class Solution:
    # Function to find the majority elements in the array
    def findMajority(self, arr):
        #Your Code goes here.
        
        d={}
        ans=[]
        n=len(arr)//3
        for i in range(len(arr)):
            d[arr[i]]=d.get(arr[i],0)+1
        
       
        

        for i in d:
            if d[i]>=0 and d[i]>n:
                ans.append(i)
        
        
        if ans:
            return sorted(ans)
            
        
        



# 3 2 1 1 2 3 4 1 4 4 4 1 3 1 2 1
# Your Code's output is: 
# 1 2 3 4
# It's Correct output is: 
# 1

#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    t = int(input().strip())
    for _ in range(t):
        s = input().strip()
        nums = list(map(int, s.split()))
        ob = Solution()
        ans = ob.findMajority(nums)
        if not ans:
            print("[]")
        else:
            print(" ".join(map(str, ans)))


if __name__ == "__main__":
    main()

# } Driver Code Ends