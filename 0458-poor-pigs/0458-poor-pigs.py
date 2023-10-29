class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        p = 0
        while (minutesToTest / minutesToDie + 1) ** p < buckets:
            p += 1
        
        return p

        