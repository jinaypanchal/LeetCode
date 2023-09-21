class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1 = len(nums1)
        n2 = len(nums2)
        res = []
        i = 0
        j = 0
        while i<n1 and j<n2:
            if nums1[i] < nums2[j]:
                res.append(nums1[i])
                i+=1
            else:
                res.append(nums2[j])
                j+=1
        
        while i < n1:
            res.append(nums1[i])
            i+=1
        while j < n2:
            res.append(nums2[j])
            j+=1
        
        n = len(res)

        if n%2 == 1:
            return res[n//2]
        
        return (res[n//2] + res[n//2 - 1])/2.0
        