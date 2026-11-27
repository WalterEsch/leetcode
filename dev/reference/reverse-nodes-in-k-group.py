class Solution:
    def reverseKGroup(self, head, k):
        vals = linked_list_to_values(head)
        out = []
        for i in range(0, len(vals), k):
            chunk = vals[i:i + k]
            out.extend(chunk[::-1] if len(chunk) == k else chunk)
        return build_linked_list(out)
