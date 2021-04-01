class Solution:
    def clumsy(self, N: int) -> int:
        stack = [N]
        op = 0
        for i in range(N-1, 0, -1):
            if op == 0:
                stack.append(stack.pop() * i)
            elif op == 1:
                stack.append(int(stack.pop() / float(i)))
            elif op == 2:
                stack.append(i)
            else:
                stack.append(-i)

            op = (op+1) % 4

        return sum(stack)
