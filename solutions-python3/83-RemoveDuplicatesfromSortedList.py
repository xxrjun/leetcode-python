# 83. Remove Duplicates from Sorted List

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head == None:    return

        cur = head
        next = cur.next

        while next:
            if next.val == cur.val:
                while next and next.val == cur.val:
                    next = next.next

                cur.next = next

                if next == None: return head

            cur = cur.next
            next = next.next


        return head 