# 2. Add Two Numbers

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize return list
        cur = head = ListNode(0)

        carry = 0
        while carry > 0 or l1 or l2:
            # Get value of list1 and list2
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            sum = val1 + val2 + carry

            # 將個位數部分作為此 node 的值
            pop = sum % 10
            cur.next = ListNode(pop)

            # 將十位數部分作為下此進位的值
            carry = sum // 10
            sum //= 10

            # Iterate returnList, list1 and list2
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return head.next
