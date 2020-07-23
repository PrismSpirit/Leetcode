class Solution:
    def frequencySort(self, s: str) -> str:
        freq_dict = dict()
        output = ""
        
        for x in s:
            if x in freq_dict:
                freq_dict[x] += 1
            else:
                freq_dict[x] = 1

        refined_freq = sorted(freq_dict.items(), key=operator.itemgetter(1), reverse=True)
        for x in refined_freq:
            output += x[0] * x[1]

        return output