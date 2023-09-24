class Solution:
    def checkStraightLine(self, coordinates: list[list[int]]) -> bool:
        try:
            equation = self.give_equation(coordinates[0], coordinates[1])
        except ValueError:
            return False
        for point in coordinates[2:]:
            if not equation(point):
                return False
        return True

    @staticmethod
    def give_equation(a: tuple, b: tuple):
        x0, y0 = a
        x1, y1 = b
        if x0 == x1 or y0 == y1:
            raise ValueError
        return lambda point: (point[0] - x0) / (x1 - x0) == (point[1] - y0) / (y1 - y0)


coordinates = [[1, 1], [2, 2], [3, 4], [4, 5], [5, 6], [7, 7]]

if __name__ == '__main__':
    task = Solution()
    print(task.checkStraightLine(coordinates))
