class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        alice = 0
        bob = 0
        n = len(colors)
        for i in range(1,n-1):
            if colors[i-1] == 'A' and colors[i] == 'A' and colors[i+1] == 'A':
                alice += 1
            elif colors[i-1] == 'B' and colors[i] == 'B' and colors[i+1] == 'B':
                bob += 1
 
        
        return alice > bob
        