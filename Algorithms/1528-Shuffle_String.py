class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        pair_list = []
        output = ""
        
        for x in range(0, len(s)):
            pair_list.append([s[x], indices[x]])
        
        for x in sorted(pair_list, key=lambda x: x[1]):
            output += x[0]
        
        return output