class Solution(object):
    def calculate(self, s):
        res, num, sign = 0, 0, 1
        # res 表示左边表达式除去栈内保存元素的计算结果；
        # sign 表示运算符；
        # num 表示当前遇到的数字，会更新到 res 中；
        # 用栈保存遇到左括号时前面计算好了的结果和运算符
        stack = []
        for c in s:
            if c.isdigit():
                num = 10 * num + int(c)
            elif c == "+" or c == "-":
                res += sign * num
                num = 0
                sign = 1 if c == "+" else -1
            elif c == "(":
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            elif c == ")":
                res += sign * num
                num = 0
                res *= stack.pop()
                res += stack.pop()
        res += sign * num
        return res

object = Solution()
result = object.calculate('(1+(4+5+2)-3)+(6+8)')
print(result)
