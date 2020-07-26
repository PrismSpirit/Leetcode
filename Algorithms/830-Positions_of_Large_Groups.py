class Solution:
    def largeGroupPositions(self, S: str) -> List[List[int]]:
        output = list()
        prev_s = S[0]
        size = 1

        for x in range(1, len(S)):
            if prev_s != S[x]:
                if size > 2:
                    output.append([x - size, x - 1])
                size = 1
            if prev_s == S[x]:
                size += 1
            if x == len(S) - 1 and size > 2:
                output.append([x - size + 1, x])
            prev_s = S[x]

        return output