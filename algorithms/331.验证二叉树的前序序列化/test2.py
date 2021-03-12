class Solution(object):
    def isValidSerialization(self, preorder):
        # 核心：二叉树入度和出度是相等的。
        nodes = preorder.split(',')
        diff = 1

        for node in nodes:
            diff -= 1
            if diff < 0:
                return False
            if node != '#':
                diff += 2
        return diff == 0

object = Solution()
result = object.isValidSerialization('9,3,4,#,#,1,#,#,2,#,6,#,#')
print(result)

'''
1

2
4
3
2
'''
