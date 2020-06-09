"""
From Kapil Sharma's lecture 9 Jun 2020
​
Given the index of a node, and the head of linked list, delete the node at that index.
​
Singly-linked list
Return True if successful; False if not.
"""
​
​
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
​
​
def delete_node(index, head):
    if head == None:
        return False
​
    # Current node as we loop along the sll
    temp = head
​
    # Pointer to keep track of position as we loop along the sll
    track = 0
​
    # Loop until temp becomes None or track is one less than the desired index
    while temp != None and track < index - 1:
        temp = temp.next
        if temp == None or temp.next == None:
            return False
        track += 1
​
    # Now that we're out of the loop, temp.next should be the node at our desired index.
    # Skip the node at temp.next by assigning temp's next property to be the next.next instead.
    temp.next = temp.next.next
    return True
​
# Trying it out:
​
​
# Removing a middle node
# 1 -> 2 -> 3
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node1.next = node2
node2.next = node3
​
delete_node(1, node1)
print(node1.value)
print(node1.next.value)
try:
    print(node1.next.next.value)
except AttributeError:
    print("End of sll")
​
# Removing a tail
# 1 -> 3 -> 4
node4 = Node(4)
delete_node(2, node1)
print(node1.value)
print(node1.next.value)
try:
    print(node1.next.next.value)
except AttributeError:
    print("End of sll")
​
# Removing a head
# 1 -> 3
delete_node(0, node1)
try:
    print(node1.next.value)
except AttributeError:
    print("Old head is no longer connected to rest of sll")
​
# Edge cases
print(delete_node(0, None))  # when head is None
print(delete_node(3, node3))  # when index is out of range

"""
From Kapil Sharma's lecture 9 Jun 2020
​
Given 2 singly-linked lists.
Each list represents a positive integer.
Each node in the slls represents a digit in the integer.
5 -> 7 -> 9 represents the integer 975
7 -> 6 represents the integer 67
​
Return the sum of the two integers, in the form of a sll.
2 -> 4 -> 0 -> 1 represents 1042
"""
​
​
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
​
# The function has an additional parameter named carry, which holds the second digit that might result from
# adding 2 single-digit ints.
# 5
# + 7
# -------
# 12  so 1 will be carry in this example
​
​
def add_2_lls(l1, l2, carry=0):
    # base cases
    if l1 == None and l2 == None and carry == 0:
        return None
​
    # Create a variable to hold the sum. It is initialized at 0 the first time this function is called.
    # Later calls to the function will add carry to the total used during the call.
    total = carry
​
    # Add the value of l1 to total
    if l1 != None:
        total += l1.data
​
    # Add the value of l2 to total
    if l2 != None:
        total += l2.data
​
    # Create a new node to hold the ones digit of total. This will be part of the returned sll.
    result = Node(total % 10)
​
    # As long as there are still nodes in at least one of the slls, recursively call the function.
    # If the current node of a sll has a next, advance to the next node
    if l1 != None:
        l1 = l1.next
    if l2 != None:
        l2 = l2.next
​
    # Determine what carry should be
    if total >= 10:
        carry = 1
    else:
        carry = 0
​
    next_node_of_result = add_2_lls(l1, l2, carry)
​
    # attach next_node_of_result to the sll we will return
    result.next = next_node_of_result
​
    return result
​
​
# Testing this out
# 5 -> 7 -> 9 represents the integer 975
​
node1 = Node(5)
node2 = Node(7)
node3 = Node(9)
​
node1.next = node2
node2.next = node3
​
# 7 -> 6 represents the integer 67
​
node4 = Node(7)
node5 = Node(6)
​
node4.next = node5
​
test = add_2_lls(node1, node4)
curr = test
return_value = ''
while curr:
    return_value = str(curr.data) + return_value
    curr = curr.next
print(return_value)
​
​
def add_2_lls(l1, l2):
    # Initialize carry to be 0 to start with.
    return add_2_lls_inner(l1, l2, 0)
​
​
'''
Note: Kapil used an outer and inner function for his version:
def add_2_lls(l1, l2):
    # Initialize carry to be 0 to start with.
    return add_2_lls_inner(l1, l2, 0)
​
​
def add_2_lls_inner(l1, l2, carry):
    etc.
'''