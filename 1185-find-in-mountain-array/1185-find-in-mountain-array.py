# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        n = mountain_arr.length()
        def peakIndexinMountArray(arr):
            l = 0 
            r = arr.length() - 1

            while(l < r):
                mid = (l+r)//2
                if arr.get(mid) >= arr.get(mid+1):
                    r = mid
                else:
                    l = mid+1
            
            # if l == r:
            return l
        
        def binarySearch(arr, l ,r , target):
            while l <= r:
                mid = l + (r-l)//2
                
                if arr.get(mid) == target:
                    return mid
                elif arr.get(mid) > target:
                    r = mid - 1                
                else:
                    l = mid + 1
            return -1

        def reverseBinarySearch(arr, l ,r , target):
            while l <= r:
                mid = l + (r-l)//2
                
                if arr.get(mid) == target:
                    return mid
                elif arr.get(mid) > target:
                    l = mid + 1                
                else:
                    r = mid - 1
            return -1
        
        idx = peakIndexinMountArray(mountain_arr)

        res = binarySearch(mountain_arr, 0, idx, target)
        if res != -1:
            return res
        
        res = reverseBinarySearch(mountain_arr, idx +1, n - 1, target)

        return res
        