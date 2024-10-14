#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3


#Function to find a continuous sub-array which adds up to a given number.
class Solution:
    def subArraySum(self,arr, n, s): 
       #Write your code here
        # arr.sort()
        temp=arr[0]
        l=0
        r=-1
        ans=[]
        if(temp==s):
            ans.extend([l+1,r+2])
            return ans
        for i in range(1,n):
            temp+=arr[i]
            while temp>s and l<i:
                temp-=arr[l]
                l+=1
            if(temp==s):
                r=i
                break
        if r==-1:
            ans.append(-1)
            return ans
        ans.extend([l+1,r+1])
        return ans

            

             

#{ 
 # Driver Code Starts.
#Initial Template for Python 3

import math

def main():
        T=int(input())
        while(T>0):
            
            NS=input().strip().split()
            N=int(NS[0])
            S=int(NS[1])
            
            A=list(map(int,input().split()))
            ob=Solution()
            ans=ob.subArraySum(A, N, S)
            
            for i in ans:
                print(i, end=" ")
                
            print()
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends