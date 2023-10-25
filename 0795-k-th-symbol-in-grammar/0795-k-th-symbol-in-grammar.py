class Solution:
    def kthGrammar(self, n: int, k: int) -> int:

        if n == 1 and k == 1:
            return 0

        final_length = 2**(n-1)
        mid = final_length/2
        if k <= mid:
            return self.kthGrammar(n-1, k)

        return 1 - self.kthGrammar(n-1, k - mid)


        

        