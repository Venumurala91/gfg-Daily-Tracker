class Solution:

    def maxDistance(self, arr):
        n = len(arr)
        mp = {}
        max_dist = 0
        for i in range(n):
            if arr[i] not in mp:
                mp[arr[i]] = i
            else:
                max_dist = max(max_dist, i - mp[arr[i]])
        return max_dist



#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        print(ob.maxDistance(arr))

# } Driver Code Ends