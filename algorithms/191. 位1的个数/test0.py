class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            count += 1
            print(n)
            n &= n - 1
            print(n, '\n')
        return count

object = Solution()
re = object.hammingWeight(666)
print(re)
