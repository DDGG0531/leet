import heapq


class Solution:
    def connectSticks(self, sticks: list[int]) -> int:
        # 合併兩個數字，ˊ直到只剩一個數字，找出最小的合併成本
        # 最後回傳，合併成本
        # PS: 找最小的兩個數字做累加可以得到最小的合併成本

        ans = 0
        heapq.heapify(sticks)

        while len(sticks) > 1:
            v1 = heapq.heappop(sticks)
            v2 = heapq.heappop(sticks)
            ans += v1 + v2
            heapq.heappush(sticks, v1 + v2)

        return ans


solution = Solution()
print(solution.connectSticks([2, 4, 3]))  # 14
print(solution.connectSticks([1, 8, 3, 5]))  # 30
print(solution.connectSticks([5]))  # 0
