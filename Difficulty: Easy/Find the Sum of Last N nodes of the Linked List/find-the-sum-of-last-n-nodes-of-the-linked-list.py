#User function Template for python3

'''
# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''
class Solution:
    def sumOfLastN_Nodes(self, head, k):
        #function should return sum of last n nodes
        
        c=[]
        n=head
        while n:
            c.append(n.data)
            n=n.next
        
        
        c=c[::-1]
        # print(c)
        s=0
        for i in range(k):
            s+=c[i]
        
        return s
        
        # l=0
        # n=head
        # while n:
        #     n=n.next
        #     l+=1
        
        # print(l)
        # c=0
        # if l==k:
        #     n=head
        #     while n:
        #         c+=n.data
        #         n=n.next
        # else:
        #     d=1
        #     p=0
        #     n=head
        #     while n:
        #         d+=1
        #         n=n.next
        #         # print(n.next.data)
        #         if d-l==k:
        #             p=n.next
        #             print(p.data)
        #             break
            
        #     while p:
        #         c+=p.data
        #         p=p.next
        
        # return c
            
            
            
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split('\n')

    t = int(data[0])
    for i in range(1, t + 1):
        arr = list(map(int, data[2 * i - 1].split()))
        n = int(data[2 * i])
        head = Node(arr[0])
        tail = head
        for value in arr[1:]:
            tail.next = Node(value)
            tail = tail.next
        ob = Solution()
        print(ob.sumOfLastN_Nodes(head, n))

# } Driver Code Ends