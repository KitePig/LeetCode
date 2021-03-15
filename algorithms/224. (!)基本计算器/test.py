class Solution(object):
    def calculate(self, s):
        res, num, sign = 0, 0, 1
        stack = []
        for c in s:
            print(c)
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

            print(res, num, sign)
            print(stack)
            print("\n")
        res += sign * num
        return res

object = Solution()
result = object.calculate('(1+(4+5+2)-3)+(6+8)')
print(result)
