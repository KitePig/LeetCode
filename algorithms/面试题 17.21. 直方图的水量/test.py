from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        # 第一格，最后一个无法盛水
        for i in range(1, len(height)-1):
            # 当前格子左右最高，用低的减去当前高度，等于可以盛水的高度
            left_height = max(height[:i])
            right_height = max(height[i+1:])
            h = min(left_height, right_height) - height[i]
            if h > 0:
                res += h

        return res

obj = Solution()
re = obj.trap([0,1,0,2,1,0,1,3,2,1,2,1])
print(re)
