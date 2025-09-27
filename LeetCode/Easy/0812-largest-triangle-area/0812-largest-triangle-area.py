class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        output = 0

        for p1, p2, p3 in combinations(points, 3):
            output = max(output, abs(
                p1[0] * (p2[1] - p3[1]) +
                p2[0] * (p3[1] - p1[1]) + 
                p3[0] * (p1[1] - p2[1])
            ))

        return output / 2