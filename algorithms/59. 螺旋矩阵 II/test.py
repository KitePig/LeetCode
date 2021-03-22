from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        number = pow(n, 2)
        numbers = [item for item in range(1, number+1)]
        height, width, point = n, n, 0
        top, down, left, right = 0, height-1, 0, width-1
        direction = ((1, 0), (0, 1), (-1, 0), (0, -1)) # 右 下 左 上
        list = [[0 for _ in range(n)] for _ in range(n)]
        row, column = 0, 0
        numbers.reverse()

        item = numbers.pop()
        while item is not None:
            list[row][column] = item
            if len(numbers) == 0:
                break

            #调整方向
            if point == 0 and column == right: # 向右到达最后一个元素，方向修正为下，max top +1
                point += 1
                top += 1
            elif point == 1 and row == down: # 向下到达最后一个元素，方向修正为左。max right -1
                point += 1
                right -= 1
            elif point == 2 and column == left: # 向左最后一件元素。方向修正为上。max down -1
                point += 1
                down -= 1
            elif point == 3 and row == top: # 向上最后一个元素，方向修正为右，max left +1
                point += 1
                left += 1
            point %= 4 # 方向取模运算

            column += direction[point][0]
            row += direction[point][1]
            item = numbers.pop()

        return list

object = Solution()
re = object.generateMatrix(1)
print(re)
