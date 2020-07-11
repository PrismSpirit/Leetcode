import operator

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = {}
        
        for x in nums:
            if(str(x) in dic):
                tmp = dic.get(str(x))
                tmp += 1
                dic[str(x)] = tmp
            else:
                dic[str(x)] = 1
        
        print(dic.items())
        print(max(dic.items(), key=operator.itemgetter(1)))
        
        return max(dic.items(), key=operator.itemgetter(1))[0]