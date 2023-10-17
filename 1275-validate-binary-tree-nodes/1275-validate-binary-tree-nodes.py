class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        p2c = defaultdict(list)
        c2p = {}
        for i in range(n):
            node = i
            leftchild = leftChild[node]
            rightchild = rightChild[node]

            if leftchild != -1:
                p2c[node].append(leftchild)

                if leftchild in c2p:
                    return False  
                else:
                    c2p[leftchild] = node
            
            if rightchild != -1:
                p2c[node].append(rightchild) 
                if rightchild in c2p:
                    return False
                else:
                    c2p[rightchild] = node

        root = -1
        for i in range(n):
            if i not in c2p:
                if root != -1:
                    return False
                else:
                    root = i

        if root == -1:
            return False
        
        vis = [False] * n
        queue = deque()
        count = 1
        queue.append(root)
        vis[root] = True

        while queue:
            node = queue.popleft()

            for ch in p2c[node]:
                if not vis[ch]:
                    vis[ch] = True
                    count += 1
                    queue.append(ch)

        return count == n
               