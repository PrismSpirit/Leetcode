class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        x_index = set()
        y_index = set()
        
        for x in range(0, len(matrix)):
            for y in range(0, len(matrix[x])):
                if matrix[x][y] == 0:
                    x_index.add(x)
                    y_index.add(y)
        
        for x in x_index:
            matrix[x] = [0] * len(matrix[x])
        for y in y_index:
            for i in range(0, len(matrix)):
                matrix[i][y] = 0