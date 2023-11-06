import heapq
class SeatManager:

    def __init__(self, n: int):
        self.pq = list(range(1,n+1))
        # self.ls = [-1] * (n+1)
        # for i in range(1,n+1):
        #     ls.append(i)
        

    def reserve(self) -> int:
        seat = heapq.heappop(self.pq)
        return seat
        # for i in range(1, len(self.ls) + 1):
        #     if self.ls[i] == -1:
        #         self.ls[i] = 1
        #         return i   

        # return -1  

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.pq,seatNumber)
        # self.ls[seatNumber] = -1
        


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)