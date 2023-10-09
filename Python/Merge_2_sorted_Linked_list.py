"""
Idea:
Adjusting the pointers to the next greater element considering both LL, and returning the node with the lowest value

"""


# User function Template for python3


# Function to merge two sorted linked list.
def sortedMerge(head1, head2):
    # code here
    t1 = head1
    t2 = head2

    # Determine the head of the merged list
    if t1.data < t2.data:
        ans = head1
        t1 = t1.next
    else:
        ans = head2
        t2 = t2.next

    ptr = ans
    # Merge the two lists
    while t1 is not None and t2 is not None:
        if t1.data < t2.data:
            ptr.next = t1
            t1 = t1.next
        else:
            ptr.next = t2
            t2 = t2.next

        ptr = ptr.next

    # Append any remaining nodes from both lists (if any)
    if t1:
        ptr.next = t1
    elif t2:
        ptr.next = t2

    return ans


# {
# Driver Code Starts
# Initial Template for Python 3
# Node Class
class Node:
    def __init__(self, data):  # data -> value stored in node
        self.data = data
        self.next = None


# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node


# prints the elements of linked list
def printList(n):
    while n is not None:
        print(n.data, end=' ')
        n = n.next
    print()


if __name__ == '__main__':
    for _ in range(int(input())):
        n, m = map(int, input().strip().split())

        a = LinkedList()  # create a new linked list 'a'.
        b = LinkedList()  # create a new linked list 'b'.

        nodes_a = list(map(int, input().strip().split()))
        nodes_b = list(map(int, input().strip().split()))

        for x in nodes_a:
            a.append(x)

        for x in nodes_b:
            b.append(x)

        printList(sortedMerge(a.head, b.head))

# } Driver Code Ends
