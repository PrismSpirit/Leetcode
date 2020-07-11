class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic1 = {}
        dic2 = {}
        
        for x in s:
            if(str(x) in dic1):
                tmp = dic1.get(str(x))
                tmp += 1
                dic1[str(x)] = tmp
            else:
                dic1[str(x)] = 1
        for x in t:
            if(str(x) in dic2):
                tmp = dic2.get(str(x))
                tmp += 1
                dic2[str(x)] = tmp
            else:
                dic2[str(x)] = 1
        
        if dic1 == dic2:
            return True
        else:
            return False