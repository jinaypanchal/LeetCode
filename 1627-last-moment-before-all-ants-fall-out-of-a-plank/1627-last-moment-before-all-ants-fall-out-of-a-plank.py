class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        lt = [l for l in left]
        rt = [n-r for r in right]
        return max(lt + rt)

        