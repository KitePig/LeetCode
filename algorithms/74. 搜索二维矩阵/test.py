import bisect
from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        M, N = len(matrix), len(matrix[0])
        t_list = [x[0] for x in matrix]
        target_row = bisect.bisect_right(t_list, target) - 1
        if target_row == 0:
            return False
        target_col = bisect.bisect_left(matrix[target_row], target)
        if target_col > N:
            return False
        if matrix[target_row][target_col] == target:
            return True
        return False

object = Solution()
print(object.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13))
