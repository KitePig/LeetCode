class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        stack = []
        for x in preorder.split(','):
            stack.append(x)
            while len(stack) >= 3 and stack[-1] == '#' and stack[-2] == '#' and stack[-3] != '#':
                # 主要逻辑在这里，合并有效叶子节点 为节点。如果是二叉树，合并到最后一定只有一个节点
                stack.pop(), stack.pop(), stack.pop()
                stack.append('#')

        return len(stack) == 1 and stack.pop() == '#'

object = Solution()
result = object.isValidSerialization('9,3,4,#,#,1,#,#,2,#,6,#,#')
print(result)
