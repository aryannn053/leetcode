import sys
sys.set_int_max_str_digits(150000)

class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        cur = head

        length = 0

        while cur:
            stack.append(str(cur.val))
            cur = cur.next
            length += 1
        
        res = int(''.join(stack))*2
        res = [*str(res)]

        ptr = head
        i = 0

        while ptr:
            ptr.val = res[i]
            ptr = ptr.next
            i += 1
        
        if len(res) > length:
            new_node = ListNode(res[-1])
        
            last = head
        
            new_node.next = None
        
            while last.next is not None:
                last = last.next
        
            last.next = new_node

        return head