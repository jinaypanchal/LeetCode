# from collections import deque
class SmallestInfiniteSet:
    # smallest = 1
    def __init__(self):
        self.smallest = 1
        self.nums = [True]*1001               

    def popSmallest(self) -> int:
        res = self.smallest
        self.nums[self.smallest] = False
        for j in range(self.smallest + 1, 1001):
            if self.nums[j] == True:
                self.smallest = j   
                break 
        return res    

    def addBack(self, num: int) -> None:
        self.nums[num] = True
        if num < self.smallest:
            self.smallest = num
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)