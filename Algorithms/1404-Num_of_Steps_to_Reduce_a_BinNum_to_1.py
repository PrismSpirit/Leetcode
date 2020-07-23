class Solution:
    def numSteps(self, s: str) -> int:
        integer = int(s, 2)
        steps = 0
        
        while integer != 1:
            steps += 1
            if integer % 2 != 0:
                integer += 1
            else:
                integer //= 2
        
        return steps