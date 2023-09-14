class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # path will always start from JFK
        # if multiple path - return lexically smallest one
        # Considering position as nodes, and paths as edges, graph ques, DFS? BFS?
        # Need to cover all the nodes, choose lexically, but the node should get covered
        # agar multiple paths hai to lexically travel kro, and if saari locations cover nahi hoti to explore other 

        #observation -> len(res) == numberOfCities + 1
        
        g = defaultdict()

        tickets.sort(key = lambda x:x[1])

        for i, j in tickets:
            if i in g:
                g[i].append(j)
            else:
                g[i] = [j]
        
        path = []
        stack = [("JFK")]
        while stack:
            if stack[-1] in g and len(g[stack[-1]]) > 0:
                stack.append(g[stack[-1]].pop(0))
            else:
                path.append(stack.pop())
        
        return path[::-1]
        