#User function Template for python3

class Solution:
    def increment(self, arr, N):
        # code here
        import sys

        # Increase the limit on string digits for integer conversion
        sys.set_int_max_str_digits(100000)
        
        
        num_str = ''.join(map(str, arr))
        
        # Increment the number
        num = int(num_str) + 1
        
        # Convert back to an array of digits
        return [int(digit) for digit in str(num)]

                    
                

        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        arr=list(map(int,input().split()))
        
        ob = Solution()
        ptr = ob.increment(arr,N)
        for i in ptr:
            print(i,end=" ")
        print()
        print("~")
# } Driver Code Ends