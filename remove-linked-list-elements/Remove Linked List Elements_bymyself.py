class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeElements(self, head, val):
    	dummy_head=ListNode(-1)
    	dummy_head.next=head

    	current_node=dummy_head
    	while current_node.next!=None:
    		if current_node.next.val==val:
    			current_node.next=current_node.next.next
    		else:
    			current_node=current_node.next
    	return dummy_head.next