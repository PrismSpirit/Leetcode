class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        result = ""
        
        for x in s.split(" "):
            if x == "":
                continue
            else:
                result = x
                
        return len(result)