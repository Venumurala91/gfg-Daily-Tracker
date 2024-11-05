#User function Template for python3

def rotate(arr): 
    #code here
    
    n = len(arr)  # Assuming a square matrix
    for i in range(n):
        for k in range(i, n):  # Iterate only over the upper triangle of the matrix
            arr[i][k], arr[k][i] = arr[k][i], arr[i][k]
    
    
    
    m=n//2
    
    for j in range(n):
        c=0
        for h in range(n-1,-1,-1):
            
            arr[j][c],arr[j][h] = arr[j][h],arr[j][c]
            
            c+=1
            
            if h==m :
                break
    
        
        
        
        
    
            
        
    
    
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        matrix = []
        for i in range(N):
            arr = [int(x) for x in input().strip().split()]
            matrix.append(arr)

        rotate(matrix)
        for i in range(N):
            for j in range(N):
                print(matrix[i][j], end=' ')
            print()
        print("~")

# } Driver Code Ends