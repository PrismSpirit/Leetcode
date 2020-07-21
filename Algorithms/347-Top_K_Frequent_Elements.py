class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        output = list()
        freq_dict = dict()
        
        for x in nums:
            if x in freq_dict:
                freq_dict[x] += 1
            else:
                freq_dict[x] = 1
        
        _ = 1
        for x in sorted(freq_dict.items(), key=itemgetter(1), reverse=True):
            output.append(x[0])
            if _ == k:
                break
            _ += 1

        return output