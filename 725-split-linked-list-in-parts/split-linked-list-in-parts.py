# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:

        size  = 0 
        current = head 
        while current:
            size+=1
            current = current.next
        extra  = size%k
        tot  = size//k
        result = []

        for i in range(k):
            current_node = ListNode()
            curr = current_node
            current_size = tot+(1 if i < extra else 0)
            for _ in range(current_size):
                curr.next = ListNode(head.val)
                curr = curr.next
                head = head.next
            result.append(current_node.next)

        return result