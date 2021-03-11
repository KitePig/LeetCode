class Solution:
    def calculate(self, s):
        stack = [] #栈
        pre_op = '+' #默认加法 return有 sum()
        num = 0

        for i, x in enumerate(s):
            if x.isdigit():
                # 多位数字合并int 为了后面做运算
                num = num * 10 + int(x)

            if x in '+-*/' or i == len(s)-1:
                # 为 加减乘除 和 最后一位数做运算
                if pre_op == '+':
                    stack.append(num)
                elif pre_op == '-':
                    stack.append(-num)
                elif pre_op == '*':
                    stack.append(stack.pop() * num)
                elif pre_op == '/':
                    top = stack.pop()
                    # 除数和被除数必须大于0
                    if top > 0 and num > 0:
                        stack.append(top // num)
                    else:
                        stack.append(int(top / num))

                # 运算符
                pre_op = x
                # 运算后清除运算数字
                num = 0

        # stack 求和即可
        return sum(stack)

object = Solution()
result = object.calculate('14-3/2')
print(result)
