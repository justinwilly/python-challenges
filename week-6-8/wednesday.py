def reverse_sublist(head, p, q):
	if p == q:
		return
	
	current, prev = head, None
	counter = 1
	
	while current and counter < p - 1:
		prev = current
		current = current.next
		counter += 1
	
	# keep track of p - 1 node 
	p_1 = prev
	# after reversing, current will be the new tail
	# so let's keep track of it 
	new_tail = current
	
	# do the reversal
	# stores the next node so we have access to it
	# outside of the while loop 
	next = None 
	counter = 0
	while current and counter < q - p + 1:
		next - current.next
		current.next = prev
		prev = current
		current = next
		counter += 1
	
	# connect with p - 1
	if p_1:
		p_1.next = prev
	else:
		head = prev
		
	# connect with q+1
	new_tail.next = current
	
	return head