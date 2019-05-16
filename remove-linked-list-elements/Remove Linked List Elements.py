# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#设置虚拟变量 dummy head






class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        
        dummy_head = ListNode(-1)
        #设置一个虚拟节点 dummy_head,它的值为-1
        dummy_head.next = head
        #虚拟节点的指针指向head
        
        current_node = dummy_head
        while current_node.next != None:
        #当还没有到最后一个节点
            if current_node.next.val == val:
                current_node.next = current_node.next.next
            else:
                current_node = current_node.next
                
        return dummy_head.next
