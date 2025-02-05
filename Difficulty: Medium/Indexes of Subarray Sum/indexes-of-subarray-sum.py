#User function Template for python3
class Solution:
    def subarraySum(self, arr, target):
        # code here
        if arr[0] == target:
            return [1, 1]
        l = 0
        n = len(arr)
        s = arr[0]
        for r in range(1, n):
            s += arr[r]
            if s == target:
                return [l + 1, r + 1]
            elif s > target:
                while s > target:
                    s -= arr[l]
                    l += 1
                if s == target:
                    return [l + 1, r + 1]
        return [-1]





#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input().strip())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        d = int(input().strip())
        ob = Solution()
        result = ob.subarraySum(arr, d)
        print(" ".join(map(str, result)))
        tc -= 1
        print("~")

# } Driver Code Ends