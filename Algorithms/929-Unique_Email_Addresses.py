class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        fin_lst = list()
        
        for x in range(0, len(emails)):
            l1 = emails[x].split("@")
            l2 = l1[0].split("+")[0].replace(".", "")
            l3 = l1[1]
            fin_str = l2 + "@" + l3
            
            if fin_lst.count(fin_str) == 0:
                fin_lst.append(fin_str)
                
        return len(fin_lst)