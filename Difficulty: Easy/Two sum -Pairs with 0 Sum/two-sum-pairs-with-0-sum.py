class Solution:

    def getPairs(self, arr):
        result = []
        n = len(arr)
        arr.sort()
        left = 0
        right = n - 1
        while left < right:
            sum = arr[left] + arr[right]
            if sum < 0:
                left += 1
            elif sum > 0:
                right -= 1
            else:
                triplet = [arr[left], arr[right]]
                result.append(triplet)
                left += 1
                right -= 1
                # Skip duplicates
                while left < right and arr[left] == arr[left - 1]:
                    left += 1
                while left < right and arr[right] == arr[right + 1]:
                    right -= 1

        return result

   




#{ 
 # Driver Code Starts
class IntArray:

    def __init__(self) -> None:
        pass

    def Input(self, n):
        arr = [int(i) for i in input().strip().split()]  # array input
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


class IntMatrix:

    def __init__(self) -> None:
        pass

    def Input(self, n, m):
        matrix = []
        # matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix

    def Print(self, arr):
        for i in arr:
            for j in i:
                print(j, end=" ")
            print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().strip().split()))

        obj = Solution()
        res = obj.getPairs(arr)
        if len(res) == 0:
            print()
        else:
            IntMatrix().Print(res)
        print("~")
# } Driver Code Ends