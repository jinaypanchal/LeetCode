class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        mini_time = max(abs(sx-fx), abs(sy-fy))
        if abs(sx-fx) == 0 and abs(sy-fy) == 0 and t == 1:
            return False

        if t < mini_time:
            return False
        elif t >= mini_time:
            return True
        