class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:        

        def first_Occurence_BS(arr, ele, firstOccurence):
            low = 0
            high = len(arr)-1
            found = -1
            while(low<=high):
                mid = (low+high)//2

                if arr[mid] == ele:
                    found = mid
                    if firstOccurence:
                        high = mid - 1
                    else:
                        low = mid + 1
                    # high = mid-1                  
                
                elif arr[mid] > ele:
                    high = mid - 1
                else:
                    low = mid + 1
            return found
        

        
        first = first_Occurence_BS(nums, target, True)
        print(first)
        if first == -1:
            return [-1, -1]
        last  = first_Occurence_BS(nums, target, False)
        print(last)
        return [first, last]




     