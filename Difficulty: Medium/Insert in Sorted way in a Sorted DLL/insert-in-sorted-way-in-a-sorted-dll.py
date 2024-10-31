#User function Template for python3
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
'''
class Solution:
    #Function to insert a node in a sorted doubly linked list.
    def sortedInsert(self, head, x):
        
        new_node = Node(x)

    # If the list is empty, return the new node
    # as the head
        if head is None:
            return new_node
    
        # If the new node needs to be inserted at
        # the beginning
        if x <= head.data:
            new_node.next = head
            head.prev = new_node
            return new_node
    
        # Traverse the list to find the correct
        # position to insert the new node
        curr = head
        while curr.next is not None and curr.next.data < x:
            curr = curr.next
    
        # Insert the new node in the correct position
        new_node.next = curr.next
        if curr.next is not None:
            curr.next.prev = new_node
        curr.next = new_node
        new_node.prev = curr
    
        return head
            
            
            
            
            
            
            
                
                
                
        
        
        
        
        
    #code here
    
    


#{ 
 # Driver Code Starts
class Node:

    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


def print_list(head):
    current = head
    while current:
        print(current.data, end=' ')
        current = current.next
    print()


if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        values = list(map(int, input().strip().split()))
        head = None
        tail = None

        for value in values:
            if head is None:
                head = Node(value)
                tail = head
            else:
                tail.next = Node(value)
                tail.next.prev = tail
                tail = tail.next

        value_to_insert = int(input().strip())
        solution = Solution()
        head = solution.sortedInsert(head, value_to_insert)
        print_list(head)

        print("~")

# } Driver Code Ends