from collections import Counter
import math
import heapq


class Solution:
    def minSetSize(self, arr: list[int]) -> int:
        # 可以一次拿掉所有相同的數字，希望用最少步驟，讓長度減到一半以下
        # 貪心法: 砍掉出現次數最多的數字，直到長度小於一半

        cut_at_least = math.ceil(len(arr) / 2)
        cuts = 0
        times = 0

        counter = Counter(arr)
        heap = []

        for value in counter.values():
            heapq.heappush(heap, -value)

        while cuts < cut_at_least:
            v = -heapq.heappop(heap)
            cuts += v
            times += 1

        return times


solution = Solution()

print(solution.minSetSize([3, 3, 3, 3, 5, 5, 5, 2, 2, 7]))  # 2
print(solution.minSetSize([7, 7, 7, 7, 7, 7]))  # 1
