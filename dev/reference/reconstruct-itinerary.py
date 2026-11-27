class Solution:
    def findItinerary(self, tickets):
        g = collections.defaultdict(list)
        for a, b in sorted(tickets, reverse=True):
            g[a].append(b)
        route = []
        def visit(a):
            while g[a]:
                visit(g[a].pop())
            route.append(a)
        visit("JFK")
        return route[::-1]
