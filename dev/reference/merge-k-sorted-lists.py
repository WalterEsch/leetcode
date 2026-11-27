class Solution:
    def mergeKLists(self, lists):
        vals = []
        for node in lists:
            while node:
                vals.append(node.val)
                node = node.next
        return build_linked_list(sorted(vals))
