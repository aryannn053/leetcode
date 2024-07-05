class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        start, end = list1, list1
        for _ in range(a-1):
            start = start.next

        for _ in range(b+1):
            end = end.next

        start.next = list2
        while start.next:
            start = start.next
        start.next = end
        return list1