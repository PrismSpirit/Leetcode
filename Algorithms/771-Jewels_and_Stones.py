class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        j_list = list(J)
        count = 0
        
        for x in S:
            if x in j_list:
                count += 1
                
        return count