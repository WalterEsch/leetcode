class Solution:
    def reorderList(self, head):
        nodes = []
        while head:
            nodes.append(head)
            head = head.next
        i, j = 0, len(nodes) - 1
        order = []
        while i <= j:
            order.append(nodes[i])
            if i != j:
                order.append(nodes[j])
            i += 1
            j -= 1
        for a, b in zip(order, order[1:]):
            a.next = b
        order[-1].next = None
