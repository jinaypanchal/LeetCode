class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.buck = [[] for _ in range(1000)]        

    def put(self, key: int, value: int) -> None:
        buck_num = key % self.size
        chain = self.buck[buck_num]
        n = len(chain)
        for i in range(n):
            if chain[i][0] == key:
                chain[i] = (key, value)   
                return
        chain.append((key, value))     

    def get(self, key: int) -> int:
        buck_num = key%self.size
        chain = self.buck[buck_num]
        if not chain:
            return -1
        
        for k, v in chain:
            if k == key:
                return v        
        return - 1        

    def remove(self, key: int) -> None:
        buck_num = key%self.size
        chain = self.buck[buck_num]
        n = len(chain)
        for i in range(n):
            if chain[i][0] == key:
                chain.pop(i)
                return
        
# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)