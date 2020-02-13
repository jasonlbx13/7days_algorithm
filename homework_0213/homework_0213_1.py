class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1==None or l2==None:
            return l1 or l2
        tmp = ListNode(0)
        res = tmp
        while l1 and l2:
            if l1.val<=l2.val:
                tmp.next = l1
                l1 = l1.next
            else:
                tmp.next = l2
                l2 = l2.next
            tmp = tmp.next
        if l1==None:
            tmp.next = l2
        else:
            tmp.next = l1
        return res.next