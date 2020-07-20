class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        self_div_nums = list()
        
        while not left > right:
            isSDN = True
            for x in str(left):
                if int(x) == 0:
                    isSDN = False
                    break
                if left % int(x) != 0:
                    isSDN = False
                    break
            if isSDN == True:
                self_div_nums.append(left)
            left += 1
            
        return self_div_nums