from collections import deque
class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if len(arr) <= k:
            return max(arr)
        
        ct = 0
        for i in range(1, len(arr)):
            if arr[i] > arr[0]:
                arr[0],arr[i] = arr[i], arr[0]
                ct = 1
            else:
                ct += 1
            if ct == k:
                return arr[0]
        return arr[0]
    
        

        