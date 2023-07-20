import heapq


class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        # 找出前K接近原點的點
        # 使用 minheap
        pointsWithValue = []
        for e in points:
            value = (e[0] ** 2 + e[1] ** 2) ** 0.5
            pointsWithValue.append((value, e))

        heapq.heapify(pointsWithValue)

        ans = []

        while k > 0:
            v, e = heapq.heappop(pointsWithValue)
            ans.append(e)
            k -= 1

        return ans


solution = Solution()
print(solution.kClosest([[1, 3], [-2, 2]], 1))  # [[-2,2]]
print(solution.kClosest([[3, 3], [5, -1], [-2, 4]], 2))  # [[3,3],[-2,4]]
