class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        fast=head
        slow=head

        for i in range(k-1):
            if fast is None:
                return head
            fast=fast.next

        first=fast
        fast=fast.next

        while fast is not None:
            slow=slow.next
            fast=fast.next

        first.val, slow.val = slow.val,first.val 
        return head