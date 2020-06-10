class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next
​
​
def reverse_sublist(head, p, q):
    # analyzing the runtime 
    # two traversals through the sublist (q - p)
    # n = q - p 
    # m = p - head 
    # O(m + 2n)
    # "Do this in one traversal time"
​
    # analyzing the space complexity 
    # after the first traversal through the n linked list elements 
    # we have n elements in our stack 
    # on the second traversal we do pop them all off the stack 
    # O(n)
​
    # create a stack 
    # traverse the linked list
    # add the list elements to between p and q to our stack 
    # start another traversal at p
    # for each node, set its data as the result of popping from our stack 
    # until we get to q 
​
    # well, I've implemented an in-place linked list reversal method before
    # let's assume we have access to a reverse_linked_list_in_place() function 
    # we have to traverse to the p node 
    current = head
    # traverse to p 
    # hold on to the p - 1 node 
    # we'll also want a reference to q + 1
    counter = 1
​
    while current and counter < p - 1:
        current = current.next
        counter += 1
​
    # at this point, current is at p - 1
    # call our reverse helper with the node right after current 
    (new_head, new_tail, q_1) = reverse_linked_list_in_place(current.next, q - p + 1)
    current.next = new_head 
    new_tail.next = q_1
​
    return head
​
    # make use of our reverse_linked_list_in_place()
    # how does our helper method know when to stop reversing? 
    # pass in the number of nodes to reverse in our sublist 
    # we get back the head of the reversed list 
    # we need to rearrange the nodes directly surrounding the sublist 
    # can we alter our helper method to return both the new head and the new tail 
​
# return both the new head and the new tail of the reversed list 
# also returns the node right after the sublist 
def reverse_linked_list_in_place(head, range):
    prev = head 
    current = head.next 
​
    counter = 1
​
    # also change head's next reference 
    head.next = None 
​
    while current and counter < range:
        next = current.next 
        current.next = prev
        prev = current 
        current = next 
        counter += 1