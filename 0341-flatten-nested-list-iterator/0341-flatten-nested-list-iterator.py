# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = []
        n = len(nestedList)
        for i in range(n-1, -1, -1):
            self.stack.append(nestedList[i])        
    
    def next(self) -> int:
        #Idhr check krna padega ki integer hi hai ya fir koi list nikal k aa rhi h
        # Aur agr list aaegi to usko unpack karke stack me daalunga
        while not self.stack[-1].isInteger():
            curr = self.stack.pop()
            nested_l = curr.getList()
            for i in range(len(nested_l)-1, -1, -1):
                self.stack.append(nested_l[i])
        
        return self.stack.pop().getInteger()      
    
    def hasNext(self) -> bool:
        while self.stack:
            curr = self.stack[-1]
            if curr.isInteger():
                return True
            self.stack.pop()
            nested_list = curr.getList()
            for i in range(len(nested_list) - 1, -1, -1):
                self.stack.append(nested_list[i])
        return False

         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())