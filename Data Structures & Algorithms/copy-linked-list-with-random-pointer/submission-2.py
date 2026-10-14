class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if not head: return None
        seen = {}

        # make and add all nodes for O(1) acess
        curr = head
        while curr:
            node = Node(x = curr.val)
            seen[curr] = node
            curr = curr.next
        
        # connect .next and .random
        curr = head
        while curr:
            seen[curr].next = seen[curr.next] if curr.next else None
            seen[curr].random = seen[curr.random] if curr.random else None
            curr = curr.next
        
        return seen[head]