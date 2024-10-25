class Solution:
    def alternateSort(self,arr):
        # Your code goes here
        # 1,2,3,4,5,6,7
        
        # 1,2,3,4,6,7,8,9
        
        arr.sort()
        # print(arr)
        a=[]
        i=0
        j=len(arr)-1
        while i<j :
            a.append(arr[j])
            a.append(arr[i])
            i+=1
            j-=1
        
        if len(arr) % 2 !=0:
            a.append(arr[j])
            
        
        return a

#{ 
 # Driver Code Starts
#Initial Template for Python 3
#Position this line where user code will be pasted.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.alternateSort(arr)
        print(*ans)
        print("~")
        t -= 1

# } Driver Code Ends