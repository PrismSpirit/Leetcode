class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        output = list()
        freq_dict = dict()
        words.sort()
        
        for x in words:
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