class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        M, N = len(matrix), len(matrix[0])
        for i in range(M):
            for j in range(N):
                if matrix[i][j] == target:
                    return True

        return False
