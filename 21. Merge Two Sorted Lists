 Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 or not l2:
            return l1 if not l2 else l2
        cur = sorted_list = ListNode(-1)
        while l1 or l2:
            if l1 and l2:
                if l1.val < l2.val:
                    sorted_list.next = l1
                    l1 = l1.next
                    sorted_list = sorted_list.next
                else:
                    sorted_list.next = l2
                    l2 = l2.next
                    sorted_list = sorted_list.next
            else:
                sorted_list.next = l1 if l1 else l2
                break
        return cur.next
