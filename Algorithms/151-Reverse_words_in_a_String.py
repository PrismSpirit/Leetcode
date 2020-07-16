class Solution:
    def reverseWords(self, s: str) -> str:
        tmp_list = s.split(" ")
        tmp_list.reverse()
        
        while tmp_list.count(""):
            tmp_list.remove("")
        
        return " ".join(tmp_list)