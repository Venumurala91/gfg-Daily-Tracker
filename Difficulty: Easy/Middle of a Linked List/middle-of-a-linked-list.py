# your task is to complete this function

'''
class node:
    def __init__(data):
        self.data = data
        self.next = None
'''
class Solution:
    #  Should return data of middle node. If linked list is empty, then  -1
    def getMiddle(self, head):
        l=0
        n=head
        while n is not None:
            n=n.next
            l+=1
        
        
        # print(l)
        m=l//2
        n=head
        while m:
            n=n.next
            m-=1
        
        return n.data
            


#{ 
 # Driver Code Starts
# Initial Template for Python3


# Node Class
class node:

    def __init__(self):
        self.data = None
        self.next = None


# Linked List Class
class Linked_List:

    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, data):
        if self.head == None:
            self.head = node()
            self.tail = self.head
            self.head.data = data
        else:
            new_node = node()
            new_node.data = data
            new_node.next = None
            self.tail.next = new_node
            self.tail = self.tail.next


def printlist(head):
    temp = head
    while temp is not None:
        print(temp.data, end=" ")
        temp = temp.next
    print('')


# Driver Program
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        list1 = Linked_List()
        arr = list(map(int, input().strip().split()))
        for i in arr:
            list1.insert(i)
        ob = Solution()
        print(ob.getMiddle(list1.head))

# } Driver Code Ends