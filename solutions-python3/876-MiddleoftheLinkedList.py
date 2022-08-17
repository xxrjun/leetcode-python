# 876. Middle of the Linked List

# Solution 1: Two Pointers (Faster)
# Solution 2: Mid of Array (Slow)

class Solution:
    # Solution 1: Two Pointers (Faster, O(n/2))
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head     # Initilize two pointers

        while fast != None:            
            fast = fast.next
            if fast != None:
                fast = fast.next
            elif fast == None:
                # fast hah reached the end of linked list
                # slow i on the middle point now    
                break
                
            slow = slow.next


        return slow

    # # Solution 2: Mid of Array (Slow, O(n))
    # def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     count = 0
    #     list = {}

    #     cur = head
    #     while cur != None:
    #         list[count] = cur
    #         count += 1
    #         cur = cur.next

    #     return list[len(list) // 2]
        