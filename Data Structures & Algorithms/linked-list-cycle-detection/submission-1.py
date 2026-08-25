#   Slo fast pointer

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        slo = fast = head

        while fast and fast.next:
            slo = slo.next
            fast = fast.next.next
            if slo == fast: return True
        
        return False   