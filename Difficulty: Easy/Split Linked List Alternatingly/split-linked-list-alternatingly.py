class Solution:
    # Function to append a new node with newData at the end of a linked list
    def append(self, headRef, newData):
        new_node = Node(newData)
        last = headRef[0]

        if headRef[0] is None:
            headRef[0] = new_node
            return
        last = headRef[0]
        

        while last.next:
            last = last.next
        last.next = new_node

    # Function to split a linked list into two lists alternately
    def alternatingSplitList(self, head):
        a = [None]
        b = [None]
        current = head

        while current:
            self.append(a, current.data)
            current = current.next

            if current:
                self.append(b, current.data)
                current = current.next

        return [a[0], b[0]]



#{ 
 # Driver Code Starts
class Node:

    def __init__(self, x):
        self.data = x
        self.next = None


def printList(node):
    while node is not None:
        print(node.data, end=" ")
        node = node.next
    print()


if __name__ == "__main__":
    t = int(input().strip())

    for _ in range(t):
        arr = list(map(int, input().strip().split()))

        head = Node(arr[0])
        tail = head

        for i in range(1, len(arr)):
            tail.next = Node(arr[i])
            tail = tail.next

        ob = Solution()
        result = ob.alternatingSplitList(head)
        printList(result[0])
        printList(result[1])

# } Driver Code Ends