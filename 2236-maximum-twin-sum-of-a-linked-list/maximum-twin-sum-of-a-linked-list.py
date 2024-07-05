# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        stack = []

        cur = head

        while cur:
            stack.append(cur.val)
            cur = cur.next
        
        maximum = 0
        n = len(stack)

        for i in range(len(stack)):
            twin = 0

            if i <= (n//2) - 1:
                twin = stack[n-1-i]
            
            if twin != 0:
                maximum = max(maximum, stack[i]+twin)
        
        return maximum