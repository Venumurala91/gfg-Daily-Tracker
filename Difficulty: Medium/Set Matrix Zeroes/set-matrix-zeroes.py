#User function Template for python3
class Solution:
    def setMatrixZeroes(self, mat):
        n = len(mat)
        m = len(mat[0])
    
        # To store which rows and columns are
        # supposed to mark with zeroes
        rows = [False] * n
        cols = [False] * m
    
        # Traverse the matrix to fill rows[] and cols[]
        for i in range(n):
            for j in range(m):
    
                # If the cell contains zero then mark
                # its row and column as zero
                if mat[i][j] == 0:
                    rows[i] = True
                    cols[j] = True
    
        # Set matrix elements to zero if they
        # belong to a marked row or column
        for i in range(n):
            for j in range(m):
    
                # Mark cell (i, j) with zero if either
                # of rows[i] or cols[j] is true
                if rows[i] or cols[j]:
                    mat[i][j] = 0
            
            


#{ 
 # Driver Code Starts
import sys

# Position this line where user code will be pasted.
if __name__ == "__main__":
    input = sys.stdin.read
    data = input().split()

    idx = 0
    t = int(data[idx])
    idx += 1
    results = []

    for _ in range(t):
        n, m = map(int, data[idx:idx + 2])
        idx += 2
        arr = []
        for i in range(n):
            arr.append(list(map(int, data[idx:idx + m])))
            idx += m

        sol = Solution()
        sol.setMatrixZeroes(arr)

        for row in arr:
            results.append(" ".join(map(str, row)))

        results.append("~")

    sys.stdout.write("\n".join(results) + "\n")

# } Driver Code Ends