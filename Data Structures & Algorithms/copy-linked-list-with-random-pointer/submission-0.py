
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if not head: return None
        h_map = {}
        curr = head

        while curr:
            node = Node(curr.val)
            h_map[curr] = node
            curr = curr.next

        new_h = h_map[head]
        node = head
        while node:
            h_map[node].next = h_map[node.next] if node.next else None
            h_map[node].random = h_map[node.random] if node.random else None
            node = node.next

        return new_h    