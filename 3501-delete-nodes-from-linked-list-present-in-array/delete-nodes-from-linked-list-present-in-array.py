class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        excluded_vals = set(nums)
        dummy_head = ListNode(0)
        tail = dummy_head
        
        while head:
            if head.val not in excluded_vals:
                tail.next = ListNode(head.val)
                tail = tail.next
            head = head.next
        
        return dummy_head.next