class Solution:
    def copyRandomList(self, head):
        m = {None: None}
        n = head
        while n:
            m[n] = Node(n.val)
            n = n.next
        n = head
        while n:
            m[n].next = m[n.next]
            m[n].random = m[n.random]
            n = n.next
        return m[head]
