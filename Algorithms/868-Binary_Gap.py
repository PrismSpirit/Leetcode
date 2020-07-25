class Solution:
    def binaryGap(self, N: int) -> int:
        bin_str = str(bin(N))[2:]
        output = list()

        tmp_index = 0
        for index in range(0, len(bin_str)):
            if bin_str[index] == "1":
                output.append(index - tmp_index)
                tmp_index = index

        return max(output)