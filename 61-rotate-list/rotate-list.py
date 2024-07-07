class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        length = 0
        cur = head
        tail = None
        while cur:
            length += 1
            tail = cur
            cur = cur.next
        k = k % length
        if k == 0:
            return head
        k = length - k
        cur = head
        for i in range(k - 1):
            cur = cur.next
        new_head = cur.next
        tail.next = head
        cur.next = None
        return new_head