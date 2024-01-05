class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        points.sort(key=lambda x: x[1])
        arrows = 1
        shot = points[0][1]

        for balloon in points[1:]:
            if shot < balloon[0]:
                arrows += 1
                shot = balloon[1]

        return arrows


if __name__ == '__main__':
    task = Solution()
    print(task.findMinArrowShots(points=[[10, 16], [2, 8], [1, 6], [7, 12]]))
