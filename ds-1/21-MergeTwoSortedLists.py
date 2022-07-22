class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode],
                      list2: Optional[ListNode]) -> Optional[ListNode]:
        head1, head2 = list1, list2
        cur1, cur2 = head1, head2

        # Check empty list
        if list1 == None and list2 == None:
            return None
        elif list1 == None and list2:
            return list2
        elif list1 and list2 == None:
            return list1

        # list1 and list2 are not empty lists
        returnHead = ListNode(0)
        cur = returnHead
        while cur1 and cur2:
            if cur1.val <= cur2.val:
                cur.next = cur1
                cur = cur.next
                cur1 = cur1.next
            elif cur1.val > cur2.val:
                cur.next = cur2
                cur = cur.next
                cur2 = cur2.next

        if cur1:
            cur.next = cur1
        if cur2:
            cur.next = cur2

        return returnHead.next
