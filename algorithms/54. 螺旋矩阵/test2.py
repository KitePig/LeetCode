class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or not matrix[0]: return []
        height, width = len(matrix), len(matrix[0])
        top, down, left, right = 0, height-1, 0, width-1
        direction = ((1, 0), (0, 1), (-1, 0), (0, -1)) # 右 下 左 上
        column, row, point = 0, 0, 0
        order = []
        while len(order) != (height * width):
            # 添加元素
            order.append(matrix[row][column])
            print(row, column, '---', matrix[row][column])
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
            # 调整 row 与 column 寻找元素
            column += direction[point][0]
            row += direction[point][1]
        return order

object = Solution()
re = object.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(re)
