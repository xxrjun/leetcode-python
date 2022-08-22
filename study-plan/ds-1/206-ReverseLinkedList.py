# 206. Reverse Linked List

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        front = None

        while head.next:
            cur = head
            head = head.next
            cur.next = front
            front = cur
        
        head.next = front

        return head