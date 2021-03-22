class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')

object = Solution()
re = object.hammingWeight(666)
print(re)
