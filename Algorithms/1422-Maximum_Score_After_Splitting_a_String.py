class Solution:
    def maxScore(self, s: str) -> int:
        max_score = 0
        left = s[:1].count("0")
        right = s[1:].count("1")
        
        max_score += left + right
        
        for x in range(1, len(s) - 1):
            if s[x] == "0":
                left += 1
            else:
                right -= 1
            if left + right > max_score:
                max_score = left + right
        
        return max_score