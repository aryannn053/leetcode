class Solution:
    def insertGreatestCommonDivisors(self, head: ListNode) -> ListNode:

        node = head
        
        while node.next:
           node.next, node = ListNode(gcd(node.val, node.next.val), node.next), node.next
        return head