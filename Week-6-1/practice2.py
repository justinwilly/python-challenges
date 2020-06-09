"""
from code challenge session 06-04-2020 taught by Kapil Sharma
​
Given a node, delete it from its singly-linked list.
No head is given.
Assume that the node is not the tail.
Return True if successful removal. False if not.
​
Example: if nodes are
1 -> 2 -> 3 -> 4
After deleting node2, nodes are :
1 -> 3 -> 4
​
Kapil showed us that we can replace the value of the node to be the node.next's value. 
Then get rid of the duplicate (by pointing node.next to be node.next.next).
1 -> 3 -> 3 -> 4
becomes
1 -> 3 -> 4
"""
​
​
class ListNode:
    def __init__(self, val):
        self.value = val
        self.next = None
​
​
def delete_node(my_node):
    if type(my_node) != ListNode or my_node == None or my_node.next == None:
        return False
​
    # Copy val from my_node.next and set my_node to have that value.
    # Set my_node.next to be my_node.next.next to jump over the old my_node.next (which isn't needed anymore)
    # Then return True
​
    my_node.value = my_node.next.value
    my_node.next = my_node.next.next
    return True
​
​
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
​
node1.next = node2
node2.next = node3
node3.next = node4
​
print(delete_node(node2))
​
# Head's next should now be node3 instead of node2
print(node1.next.value)
​
print(delete_node(3))