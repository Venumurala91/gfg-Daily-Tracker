# your task is to complete this function
# function should return new head pointer

'''
class node:
    def __init__(self):
        self.data = None
        self.next = None
'''

def deleteNode(head, x):
    # Code here
    
    # Base case if linked list is empty
    if not head:  # If the list is empty
        return None
    
    # If the first node is to be deleted
    if x == 1:
        return head.next  # New head is the second node

    # Traverse to the (x-1)-th node
    current = head
    for i in range(x - 2):
        if not current.next:  # If x is out of bounds
            return head
        current = current.next
    
    # If x-th node exists, adjust pointers to skip it
    if current.next:
        current.next = current.next.next

    return head


   
    
    
            


#{ 
 # Driver Code Starts
# Node Class
class Node:

    def __init__(self, data=None):
        self.data = data
        self.next = None


# Linked List Class
class LinkedList:

    def __init__(self):
        self.head = None
        self.last = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.last = self.head
        else:
            self.last.next = new_node
            self.last = new_node


def print_list(head):
    temp = head
    while temp:
        print(temp.data, end=" ")
        temp = temp.next
    print('')


# Driver Program
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        list1 = LinkedList()
        values = list(map(int, input().strip().split()))
        for value in values:
            list1.insert(value)
        k = int(input())
        new_head = deleteNode(list1.head, k)
        print_list(new_head)
        print("~")
# } Driver Code Ends