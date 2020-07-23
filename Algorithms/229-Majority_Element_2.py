class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq_dict = dict()
        output = list()
        for x in nums:
            if x in freq_dict:
                freq_dict[x] += 1
            else:
                freq_dict[x] = 1
        
        refined_freq = sorted(freq_dict.items(), key=itemgetter(1), reverse=True)
        
        for x in refined_freq:
            if x[1] > len(nums) / 3:
                output.append(x[0])
            else:
                break
        
        return output