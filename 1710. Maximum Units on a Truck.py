import heapq


class Solution:
    def maximumUnits(self, boxTypes: list[list[int]], truckSize: int) -> int:
        # 限制箱子數量，要搬最重
        # 所以先搬最重的箱子上車，依此類推
        # index0: 箱子數量
        # index1: 箱子重量
        boxTypes = [(-weight, amount) for amount, weight in boxTypes]
        heapq.heapify(boxTypes)
        ans = 0

        for _ in range(truckSize):
            if not boxTypes:
                break
            weight, amount = heapq.heappop(boxTypes)
            ans += -weight
            amount -= 1
            if amount > 0:
                heapq.heappush(boxTypes, (weight, amount))

        return ans


solution = Solution()

print(solution.maximumUnits([[1, 3], [2, 2], [3, 1]], 4))  # 8
print(solution.maximumUnits([[5, 10], [2, 5], [4, 7], [3, 9]], 10))  # 91
print(
    solution.maximumUnits(
        [
            [1, 3],
            [5, 5],
            [2, 5],
            [4, 2],
            [4, 1],
            [3, 1],
            [2, 2],
            [1, 3],
            [2, 5],
            [3, 2],
        ],
        35,
    )
)
