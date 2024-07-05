# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if not head or not head.next or not head.next.next:
            return [-1, -1]
        
        f_crit = -1
        l_crit = -1
        min_distance = float('inf')

        prev = head
        cur = head.next
        idx = 2

        while cur.next:
            if (cur.val > prev.val and cur.val > cur.next.val) or (cur.val < prev.val and cur.val < cur.next.val):
                if f_crit == -1:
                    f_crit = idx
                else:
                    min_distance = min(min_distance, idx-l_crit)
                l_crit = idx
            prev = cur
            cur = cur.next
            idx += 1
        
        if f_crit == -1 or f_crit == l_crit:
            return [-1,-1]
        
        max_distance = l_crit - f_crit
        return [min_distance, max_distance]